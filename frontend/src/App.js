import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import CategoryList from './components/CategoryList';
import TutorialList from './components/TutorialList';
import TutorialViewer from './components/TutorialViewer';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<CategoryList />} />
        <Route path="/categories/:categoryId/tutorials" element={<TutorialList />} />
        <Route path="/tutorials/:tutorialId" element={<TutorialViewer />} />
      </Routes>
    </Layout>
  );
}

export default App;
