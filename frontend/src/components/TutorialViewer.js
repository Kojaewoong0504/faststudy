import React, { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { fetchTutorialById } from '../services/api';

const TutorialViewer = ({ tutorialId }) => {
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

  if (loading) return <div>Loading tutorial...</div>;
  if (error) return <div>{error}</div>;
  if (!tutorial) return <div>Select a tutorial to start.</div>;

  return (
    <div>
      <h2>{tutorial.title}</h2>
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
  );
};

export default TutorialViewer;