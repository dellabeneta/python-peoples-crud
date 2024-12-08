import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  TextField,
  Button,
  Typography,
  FormControlLabel,
  Switch,
  Paper,
} from '@mui/material';
import { Save as SaveIcon, ArrowBack as ArrowBackIcon } from '@mui/icons-material';
import api from '../services/api';

function CadastrarPessoa() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    telefone: '',
    cpf: '',
    data_nascimento: '',
    ativo: true,
  });

  const handleChange = (e) => {
    const { name, value, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: name === 'ativo' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/pessoas/', formData);
      navigate('/');
    } catch (error) {
      console.error('Erro ao cadastrar pessoa:', error);
      alert('Erro ao cadastrar pessoa. Verifique os dados e tente novamente.');
    }
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Box sx={{ mb: 4, display: 'flex', alignItems: 'center', gap: 2 }}>
        <Button
          variant="outlined"
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate('/')}
        >
          Voltar
        </Button>
        <Typography variant="h4" component="h1">
          Cadastrar Nova Pessoa
        </Typography>
      </Box>

      <Paper sx={{ p: 4 }}>
        <Box component="form" onSubmit={handleSubmit} sx={{ display: 'flex', flexDirection: 'column', gap: 2 }} autoComplete="off">
          <TextField
            required
            label="Nome"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            placeholder="Ex: João Silva"
            autoComplete="off"
            fullWidth
          />
          
          <TextField
            required
            label="Email"
            name="email"
            type="email"
            value={formData.email}
            onChange={handleChange}
            placeholder="Ex: joao.silva@email.com"
            autoComplete="off"
            fullWidth
          />
          
          <TextField
            required
            label="Telefone"
            name="telefone"
            type="text"
            value={formData.telefone}
            onChange={(e) => {
              let value = e.target.value;
              // Remove tudo que não for número
              value = value.replace(/\D/g, '');
              
              // Formata o número conforme a quantidade de dígitos
              if (value.length <= 2) {
                // Apenas DDD
                if (value.length === 2) {
                  value = `(${value})`;
                } else if (value.length === 1) {
                  value = `(${value}`;
                }
              } else {
                // DDD + restante do número
                let ddd = value.slice(0, 2);
                let nono = value.slice(2, 3);
                let parte1 = value.slice(3, 7);
                let parte2 = value.slice(7, 11);
                
                value = `(${ddd}) ${nono}`;
                if (parte1) value += `-${parte1}`;
                if (parte2) value += `-${parte2}`;
              }
              
              // Atualiza o estado com o telefone formatado
              handleChange({
                target: {
                  name: 'telefone',
                  value: value
                }
              });
            }}
            placeholder="Ex: (21) 9-5678-2334"
            autoComplete="off"
            fullWidth
          />
          
          <TextField
            required
            label="CPF"
            name="cpf"
            type="text"
            value={formData.cpf}
            onChange={(e) => {
              let value = e.target.value;
              // Remove tudo que não for número
              value = value.replace(/\D/g, '');
              
              // Formata o CPF
              if (value.length <= 3) {
                // Primeiros 3 dígitos
                value = value;
              } else if (value.length <= 6) {
                // Adiciona o primeiro ponto
                value = `${value.slice(0, 3)}.${value.slice(3)}`;
              } else if (value.length <= 9) {
                // Adiciona o segundo ponto
                value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6)}`;
              } else {
                // Adiciona o hífen
                value = `${value.slice(0, 3)}.${value.slice(3, 6)}.${value.slice(6, 9)}-${value.slice(9, 11)}`;
              }
              
              handleChange({
                target: {
                  name: 'cpf',
                  value: value
                }
              });
            }}
            placeholder="Ex: 123.456.789-09"
            autoComplete="off"
            fullWidth
          />
          
          <TextField
            required
            label="Data de Nascimento"
            name="data_nascimento"
            type="text"
            inputProps={{
              placeholder: "Ex: 28/02/1994"
            }}
            value={formData.data_nascimento}
            onChange={(e) => {
              let value = e.target.value;
              // Permite apenas números
              value = value.replace(/\D/g, '');
              
              // Adiciona as barras automaticamente
              if (value.length >= 2) value = value.slice(0, 2) + '/' + value.slice(2);
              if (value.length >= 5) value = value.slice(0, 5) + '/' + value.slice(5);
              if (value.length > 10) value = value.slice(0, 10);
              
              // Atualiza o estado com a data formatada
              handleChange({
                target: {
                  name: 'data_nascimento',
                  value: value
                }
              });
            }}
            autoComplete="off"
            fullWidth
          />
          
          <FormControlLabel
            control={
              <Switch
                checked={formData.ativo}
                onChange={handleChange}
                name="ativo"
                color="primary"
              />
            }
            label="Ativo"
          />
          
          <Button
            type="submit"
            variant="contained"
            color="primary"
            startIcon={<SaveIcon />}
            sx={{ mt: 2 }}
          >
            Salvar
          </Button>
        </Box>
      </Paper>
    </Box>
  );
}

export default CadastrarPessoa;
