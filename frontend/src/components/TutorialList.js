import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { fetchTutorialsByCategory } from '../services/api';

const TutorialList = () => {
  const { categoryId } = useParams();
  const [tutorials, setTutorials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getTutorials = async () => {
      try {
        const data = await fetchTutorialsByCategory(categoryId);
        setTutorials(data);
      } catch (err) {
        setError('Failed to fetch tutorials.');
      }
      setLoading(false);
    };

    if (categoryId) {
      getTutorials();
    }
  }, [categoryId]);

  if (loading) return <div className="text-center py-4">Loading...</div>;
  if (error) return <div className="text-center py-4 text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-3xl font-bold mb-6 text-center">Tutorials in Category: {categoryId}</h2>
      {tutorials.length === 0 ? (
        <p className="text-center text-gray-600">No tutorials found in this category.</p>
      ) : (
        <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {tutorials.map(tutorial => (
            <li key={tutorial.id} className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
              <Link to={`/tutorials/${tutorial.id}`} className="block p-6">
                <h3 className="text-xl font-semibold mb-2 text-gray-800">{tutorial.title}</h3>
                <p className="text-gray-600 text-sm">Order: {tutorial.order}</p>
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TutorialList;