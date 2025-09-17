import React from 'react';

const layoutStyle = {
  display: 'flex',
  flexDirection: 'column',
  minHeight: '100vh',
};

const headerStyle = {
  backgroundColor: '#282c34',
  padding: '20px',
  color: 'white',
  textAlign: 'center',
  fontSize: '1.5em'
};

const mainStyle = {
  flex: 1,
  padding: '20px',
  maxWidth: '960px',
  margin: '0 auto',
  width: '100%'
};

const Layout = ({ children }) => {
  return (
    <div style={layoutStyle}>
      <header style={headerStyle}>
        <h1>FastAPI Learning Hub</h1>
      </header>
      <main style={mainStyle}>
        {children}
      </main>
    </div>
  );
};

export default Layout;
