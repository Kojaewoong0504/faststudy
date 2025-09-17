import React from 'react';
import { Link, useParams } from 'react-router-dom';

// This is a placeholder. In a real app, you'd fetch tutorials for the category.
const tutorialsByCategory = {
  'advanced-patterns': [
    { id: 'class-based-services', title: 'Implementing Class-Based Services' },
  ],
};

const TutorialList = () => {
  const { categoryId } = useParams();
  const tutorials = tutorialsByCategory[categoryId] || [];

  return (
    <div>
      <h2>Tutorials in {categoryId}</h2>
      <ul>
        {tutorials.map(tutorial => (
          <li key={tutorial.id}>
            <Link to={`/tutorials/${tutorial.id}`}>{tutorial.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TutorialList;
