import React from 'react';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import CategoryList from '../../components/CategoryList';
import { fetchCategories } from '../../services/api';

// Mock the API module
jest.mock('../../services/api');

// Comprehensive mock for react-router-dom without jest.requireActual
jest.mock('react-router-dom', () => ({
  Link: ({ to, children }) => <a href={to}>{children}</a>,
  useParams: () => ({}), // Mock useParams if used
  useNavigate: () => jest.fn(), // Mock useNavigate if used
  // Add other exports if needed by the component under test
}));

describe('CategoryList', () => {
  beforeEach(() => {
    // Reset mocks before each test
    fetchCategories.mockClear();
  });

  test('renders loading state initially', () => {
    fetchCategories.mockReturnValueOnce(new Promise(() => {})); // Never resolve
    render(<MemoryRouter><CategoryList /></MemoryRouter>); // Wrap with MemoryRouter
    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
  });

  test('renders categories after fetching', async () => {
    const mockCategories = [
      { id: 'cat1', name: 'Category 1', description: 'Desc 1' },
      { id: 'cat2', name: 'Category 2', description: 'Desc 2' },
    ];
    fetchCategories.mockResolvedValue(mockCategories);

    render(<MemoryRouter><CategoryList /></MemoryRouter>); // Wrap with MemoryRouter

    expect(await screen.findByText(/Category 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Desc 1/i)).toBeInTheDocument();
    expect(screen.getByText(/Category 2/i)).toBeInTheDocument();
    expect(screen.getByText(/Desc 2/i)).toBeInTheDocument();
    expect(fetchCategories).toHaveBeenCalledTimes(1);
  });

  test('renders error message on fetch failure', async () => {
    fetchCategories.mockRejectedValueOnce(new Error('Network error'));
    render(<MemoryRouter><CategoryList /></MemoryRouter>); // Wrap with MemoryRouter
    expect(await screen.findByText(/Failed to fetch categories./i)).toBeInTheDocument();
  });
});