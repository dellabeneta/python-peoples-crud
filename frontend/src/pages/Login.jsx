import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Button,
  TextField,
  Typography,
  Container,
  Paper,
  Alert,
  Input,
} from '@mui/material';
import { useAuth } from '../contexts/AuthContext';
import { login as apiLogin } from '../services/api';

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const data = await apiLogin(formData.username, formData.password);
      login(data.access_token);
      navigate('/');
    } catch (err) {
      setError('Credenciais inválidas');
      console.error('Erro ao fazer login:', err);
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Paper sx={{ p: 4 }}>
          <Typography component="h1" variant="h5" align="center" gutterBottom>
            Login
          </Typography>
          <Box 
            component="form" 
            onSubmit={handleSubmit} 
            sx={{ display: 'flex', flexDirection: 'column', gap: 2 }} 
            autoComplete="off"
            spellCheck="false"
          >
            {error && (
              <Alert severity="error" sx={{ mb: 2 }}>
                {error}
              </Alert>
            )}
            <TextField
              required
              label="Usuário"
              name="username"
              type="text"
              autoFocus
              inputProps={{
                autoComplete: "off",
                form: {
                  autoComplete: "off",
                },
              }}
              value={formData.username}
              onChange={handleChange}
              fullWidth
            />
            
            {/* Campo oculto para enganar o preenchimento automático */}
            <input type="password" style={{ display: 'none' }} />
            
            <TextField
              required
              label="Senha"
              name="password"
              // Mudando para text e usando CSS para ocultar
              type="text"
              sx={{
                '& input': {
                  '-webkit-text-security': 'disc',
                  'text-security': 'disc'
                }
              }}
              inputProps={{
                autoComplete: "off",
                autoCorrect: "off",
                autoCapitalize: "off",
                spellCheck: "false",
                "data-form-type": "other",
              }}
              value={formData.password}
              onChange={handleChange}
              fullWidth
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  e.preventDefault();
                  handleSubmit(e);
                }
              }}
            />
            
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 2 }}
            >
              Entrar
            </Button>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Login;
