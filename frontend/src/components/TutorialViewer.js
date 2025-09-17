import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { fetchTutorialById } from '../services/api';

const TutorialViewer = () => {
  const { tutorialId } = useParams();
  const [tutorial, setTutorial] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!tutorialId) return;

    const getTutorial = async () => {
      setLoading(true);
      try {
        const data = await fetchTutorialById(tutorialId);
        setTutorial(data);
      } catch (err) {
        setError('Failed to fetch tutorial.');
      }
      setLoading(false);
    };

    getTutorial();
  }, [tutorialId]);

  if (loading) return <div className="text-center py-4">Loading tutorial...</div>;
  if (error) return <div className="text-center py-4 text-red-500">{error}</div>;
  if (!tutorial) return <div className="text-center py-4 text-gray-600">Select a tutorial to start or tutorial not found.</div>;

  return (
    <div className="container mx-auto p-4 bg-white shadow-lg rounded-lg">
      <h2 className="text-3xl font-bold mb-4 text-gray-800">{tutorial.title}</h2>
      <div classNameName="prose max-w-none">
        <ReactMarkdown
          components={{
            code({ node, inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || '');
              return !inline && match ? (
                <SyntaxHighlighter
                  style={oneDark}
                  language={match[1]}
                  PreTag="div"
                  {...props}
                >
                  {String(children).replace(/\n$/, '')}
                </SyntaxHighlighter>
              ) : (
                <code className={className} {...props}>
                  {children}
                </code>
              );
            },
          }}
        >
          {tutorial.content}
        </ReactMarkdown>
      </div>
    </div>
  );
};

export default TutorialViewer;
