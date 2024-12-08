import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import { useState, useMemo, useEffect } from 'react';

// Componentes
import Header from './components/Header';
import PrivateRoute from './components/PrivateRoute';

// Páginas
import ListaPessoas from './pages/ListaPessoas';
import CadastrarPessoa from './pages/CadastrarPessoa';
import EditarPessoa from './pages/EditarPessoa';
import Login from './pages/Login';

// Contexto
import { AuthProvider } from './contexts/AuthContext';

function App() {
  // Inicializa o tema com o valor do localStorage ou 'light' como padrão
  const [mode, setMode] = useState(() => {
    const savedMode = localStorage.getItem('themeMode');
    return savedMode || 'light';
  });

  // Salva o tema no localStorage sempre que ele mudar
  useEffect(() => {
    localStorage.setItem('themeMode', mode);
  }, [mode]);

  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode,
          primary: {
            main: '#1976d2',
          },
          secondary: {
            main: '#dc004e',
          },
          background: {
            default: mode === 'light' ? '#ffffff' : '#121212',
            paper: mode === 'light' ? '#ffffff' : '#1e1e1e',
          },
        },
      }),
    [mode]
  );

  const toggleTheme = () => {
    setMode((prevMode) => (prevMode === 'light' ? 'dark' : 'light'));
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <AuthProvider>
          <Header toggleTheme={toggleTheme} mode={mode} />
          <Container>
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route
                path="/"
                element={
                  <PrivateRoute>
                    <ListaPessoas />
                  </PrivateRoute>
                }
              />
              <Route
                path="/cadastrar"
                element={
                  <PrivateRoute>
                    <CadastrarPessoa />
                  </PrivateRoute>
                }
              />
              <Route
                path="/editar/:id"
                element={
                  <PrivateRoute>
                    <EditarPessoa />
                  </PrivateRoute>
                }
              />
            </Routes>
          </Container>
        </AuthProvider>
      </Router>
    </ThemeProvider>
  );
}

export default App;
