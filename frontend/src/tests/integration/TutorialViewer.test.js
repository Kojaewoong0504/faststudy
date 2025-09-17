import React from 'react';
import { render, screen } from '@testing-library/react';
import TutorialViewer from '../../components/TutorialViewer';
import { fetchTutorialById } from '../../services/api';

// Mock the API module
jest.mock('../../services/api');

test('fetches and displays a specific tutorial', async () => {
  const mockTutorial = {
    id: 'class-based-services',
    title: 'Implementing Class-Based Services',
    content: 'This is the content for class-based services.',
  };
  fetchTutorialById.mockResolvedValue(mockTutorial);

  render(<TutorialViewer tutorialId="class-based-services" />);
  
  // This test will fail because the placeholder component does not render the tutorial.
  expect(await screen.findByText(/Implementing Class-Based Services/i)).toBeInTheDocument();
  expect(await screen.findByText(/This is the content for class-based services./i)).toBeInTheDocument();
});