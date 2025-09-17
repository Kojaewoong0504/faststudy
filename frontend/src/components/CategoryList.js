import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { fetchCategories } from '../services/api';

const listStyle = {
  listStyle: 'none',
  padding: 0,
};

const listItemStyle = {
  marginBottom: '10px',
  border: '1px solid #ddd',
  padding: '15px',
  borderRadius: '5px',
  transition: 'background-color 0.2s',
};

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

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Topics</h2>
      <ul style={listStyle}>
        {categories.map(category => (
          <li key={category.id} style={listItemStyle}>
            <Link to={`/tutorials/${category.id}`}>
              <h3>{category.name}</h3>
              <p>{category.description}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoryList;