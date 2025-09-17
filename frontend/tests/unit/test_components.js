import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import CategoryList from '../../src/components/CategoryList';
import TutorialList from '../../src/components/TutorialList';
import TutorialViewer from '../../src/components/TutorialViewer';
import * as api from '../../src/services/api';

// Mock API calls
jest.mock('../../src/services/api');

describe('CategoryList', () => {
  test('renders categories after fetching', async () => {
    api.fetchCategories.mockResolvedValueOnce([
      { id: '1', name: 'Category 1', description: 'Desc 1' },
      { id: '2', name: 'Category 2', description: 'Desc 2' },
    ]);

    render(
      <MemoryRouter>
        <CategoryList />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/Category 1/i)).toBeInTheDocument());
    expect(screen.getByText(/Category 2/i)).toBeInTheDocument();
  });

  test('renders error message on fetch failure', async () => {
    api.fetchCategories.mockRejectedValueOnce(new Error('Failed to fetch'));

    render(
      <MemoryRouter>
        <CategoryList />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/Failed to fetch categories./i)).toBeInTheDocument());
  });
});

describe('TutorialList', () => {
  test('renders tutorials for a category', async () => {
    api.fetchTutorialsByCategory.mockResolvedValueOnce([
      { id: 't1', title: 'Tutorial 1', order: 1 },
      { id: 't2', title: 'Tutorial 2', order: 2 },
    ]);

    render(
      <MemoryRouter initialEntries={['/categories/cat1/tutorials']}>
        <TutorialList />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/Tutorial 1/i)).toBeInTheDocument());
    expect(screen.getByText(/Tutorial 2/i)).toBeInTheDocument();
  });

  test('renders no tutorials message if empty', async () => {
    api.fetchTutorialsByCategory.mockResolvedValueOnce([]);

    render(
      <MemoryRouter initialEntries={['/categories/cat1/tutorials']}>
        <TutorialList />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/No tutorials found in this category./i)).toBeInTheDocument());
  });

  test('renders error message on fetch failure', async () => {
    api.fetchTutorialsByCategory.mockRejectedValueOnce(new Error('Failed to fetch'));

    render(
      <MemoryRouter initialEntries={['/categories/cat1/tutorials']}>
        <TutorialList />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/Failed to fetch tutorials./i)).toBeInTheDocument());
  });
});

describe('TutorialViewer', () => {
  test('renders tutorial content', async () => {
    api.fetchTutorialById.mockResolvedValueOnce({
      id: 'tut1',
      title: 'My Tutorial',
      content: '# Hello World',
      category_id: 'cat1',
      order: 1,
      created_at: '2023-01-01T00:00:00Z',
      updated_at: '2023-01-01T00:00:00Z',
    });

    render(
      <MemoryRouter initialEntries={['/tutorials/tut1']}>
        <TutorialViewer />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading tutorial.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/My Tutorial/i)).toBeInTheDocument());
    expect(screen.getByText(/Hello World/i)).toBeInTheDocument();
  });

  test('renders error message on fetch failure', async () => {
    api.fetchTutorialById.mockRejectedValueOnce(new Error('Failed to fetch'));

    render(
      <MemoryRouter initialEntries={['/tutorials/tut1']}>
        <TutorialViewer />
      </MemoryRouter>
    );

    expect(screen.getByText(/Loading tutorial.../i)).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText(/Failed to fetch tutorial./i)).toBeInTheDocument());
  });
});
