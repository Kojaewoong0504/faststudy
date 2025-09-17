import React from 'react';
import { Routes, Route, useParams } from 'react-router-dom';
import Layout from './components/Layout';
import CategoryList from './components/CategoryList';
import TutorialList from './components/TutorialList';
import TutorialViewer from './components/TutorialViewer';

// Helper component to extract params for TutorialViewer
const TutorialViewerWrapper = () => {
  const { tutorialId } = useParams();
  return <TutorialViewer tutorialId={tutorialId} />;
};

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<CategoryList />} />
        <Route path="/tutorials/:categoryId" element={<TutorialList />} />
        <Route path="/tutorial/:tutorialId" element={<TutorialViewerWrapper />} />
      </Routes>
    </Layout>
  );
}

export default App;