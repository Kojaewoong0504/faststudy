import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchCategories } from '../services/api';

const CategoryList = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getCategories = async () => {
      try {
        const data = await fetchCategories();
        setCategories(data);
      } catch (err) {
        setError('Failed to fetch categories.');
      }
      setLoading(false);
    };

    getCategories();
  }, []);

  if (loading) return <div className="text-center py-4">Loading...</div>;
  if (error) return <div className="text-center py-4 text-red-500">{error}</div>;

  return (
    <div className="container mx-auto p-4">
      <h2 className="text-3xl font-bold mb-6 text-center">Topics</h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {categories.map(category => (
          <li key={category.id} className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300">
            <Link to={`/categories/${category.id}/tutorials`} className="block p-6">
              <h3 className="text-xl font-semibold mb-2 text-gray-800">{category.name}</h3>
              <p className="text-gray-600 text-sm">{category.description}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryList;
