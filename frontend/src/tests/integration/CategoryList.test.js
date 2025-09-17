import React from 'react';
import { render, screen } from '@testing-library/react';
import CategoryList from '../../components/CategoryList';
import { fetchCategories } from '../../services/api';

// Mock the API module
jest.mock('../../services/api');

test('fetches and displays categories', async () => {
  const mockCategories = [
    { id: 'project-structure', name: 'Project Structure', description: '...' },
    { id: 'advanced-patterns', name: 'Advanced Patterns', description: '...' },
  ];
  fetchCategories.mockResolvedValue(mockCategories);

  render(<CategoryList />);
  
  // This test will fail because the placeholder component does not render the categories.
  expect(await screen.findByText(/Project Structure/i)).toBeInTheDocument();
  expect(await screen.findByText(/Advanced Patterns/i)).toBeInTheDocument();
});