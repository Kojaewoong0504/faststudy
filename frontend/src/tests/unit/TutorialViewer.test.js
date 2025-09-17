import React from 'react';
import { render, screen } from '@testing-library/react';
import TutorialViewer from '../../components/TutorialViewer';
import { fetchTutorialById } from '../../services/api';

// Mock the API module
jest.mock('../../services/api');

// Mock react-markdown and react-syntax-highlighter without jest.requireActual
jest.mock('react-markdown', () => ({ children }) => <div>{children}</div>);
jest.mock('react-syntax-highlighter', () => ({
  Prism: ({ children }) => <code>{children}</code>,
  atomOneDark: {},
  // Mock other named exports if they are used directly
  // SyntaxHighlighter: ({ children }) => <code>{children}</code>, // If SyntaxHighlighter is imported directly
}));

describe('TutorialViewer', () => {
  beforeEach(() => {
    fetchTutorialById.mockClear();
  });

  test('renders loading state initially', () => {
    fetchTutorialById.mockReturnValueOnce(new Promise(() => {})); // Never resolve
    render(<TutorialViewer tutorialId="test-id" />);
    expect(screen.getByText(/Loading tutorial.../i)).toBeInTheDocument();
  });

  test('renders tutorial content after fetching', async () => {
    const mockTutorial = {
      id: 'test-id',
      title: 'Test Tutorial Title',
      content: '# Heading\n\nThis is **markdown** content.\n\n```python\nprint("Hello, World!")\n```',
    };
    fetchTutorialById.mockResolvedValue(mockTutorial);

    render(<TutorialViewer tutorialId="test-id" />);

    expect(await screen.findByText(/Test Tutorial Title/i)).toBeInTheDocument();
    // Match the plain text content, as markdown is mocked to render children directly
    expect(screen.getByText(/This is markdown content./i)).toBeInTheDocument();
    // Check for the mocked code block content
    expect(screen.getByText(/print("Hello, World!")/i)).toBeInTheDocument();
    expect(fetchTutorialById).toHaveBeenCalledTimes(1);
    expect(fetchTutorialById).toHaveBeenCalledWith('test-id');
  });

  test('renders error message on fetch failure', async () => {
    fetchTutorialById.mockRejectedValueOnce(new Error('Network error'));
    render(<TutorialViewer tutorialId="test-id" />);
    expect(await screen.findByText(/Failed to fetch tutorial./i)).toBeInTheDocument();
  });

  test('renders message when no tutorial is found', async () => {
    fetchTutorialById.mockResolvedValueOnce(null);
    render(<TutorialViewer tutorialId="non-existent" />);
    expect(await screen.findByText(/Select a tutorial to start./i)).toBeInTheDocument();
  });
});