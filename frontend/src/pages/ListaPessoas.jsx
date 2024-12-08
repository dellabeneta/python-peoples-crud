import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TablePagination,
  Paper,
  Button,
  Typography,
  Box,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  DialogContentText,
  TextField,
  InputAdornment,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon, Search as SearchIcon } from '@mui/icons-material';
import api from '../services/api';

function ListaPessoas() {
  const [pessoas, setPessoas] = useState([]);
  const [deleteDialog, setDeleteDialog] = useState(false);
  const [pessoaParaDeletar, setPessoaParaDeletar] = useState(null);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [total, setTotal] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    carregarPessoas();
  }, [page, rowsPerPage, searchTerm]);

  const carregarPessoas = async () => {
    try {
      const response = await api.get('/pessoas/', {
        params: {
          page: page + 1, // API começa em 1, MUI começa em 0
          per_page: rowsPerPage,
          search: searchTerm || undefined
        }
      });
      setPessoas(response.data.items);
      setTotal(response.data.total);
    } catch (error) {
      console.error('Erro ao carregar pessoas:', error);
    }
  };

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const handleEditar = (id) => {
    navigate(`/editar/${id}`);
  };

  const handleAbrirDeleteDialog = (pessoa) => {
    setPessoaParaDeletar(pessoa);
    setDeleteDialog(true);
  };

  const handleFecharDeleteDialog = () => {
    setPessoaParaDeletar(null);
    setDeleteDialog(false);
  };

  const handleConfirmarDelete = async () => {
    if (pessoaParaDeletar) {
      try {
        await api.delete(`/pessoas/${pessoaParaDeletar.id}`);
        handleFecharDeleteDialog();
        carregarPessoas();
      } catch (error) {
        console.error('Erro ao deletar pessoa:', error);
      }
    }
  };

  const formatarData = (data) => {
    if (!data) return '';
    const [ano, mes, dia] = data.split('-');
    return `${dia}/${mes}/${ano}`;
  };

  return (
    <Box sx={{ width: '100%', p: 3 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4" component="h1">
          Pessoas Cadastradas
        </Typography>
        <Button
          variant="contained"
          color="primary"
          startIcon={<AddIcon />}
          onClick={() => navigate('/cadastrar')}
        >
          Cadastrar Pessoa
        </Button>
      </Box>

      <TextField
        fullWidth
        variant="outlined"
        placeholder="Pesquisar por nome, email ou CPF..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        sx={{ mb: 3 }}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
      />

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Nome</TableCell>
              <TableCell>Email</TableCell>
              <TableCell>CPF</TableCell>
              <TableCell>Telefone</TableCell>
              <TableCell>Data de Nascimento</TableCell>
              <TableCell>Status</TableCell>
              <TableCell align="center">Ações</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {pessoas.map((pessoa) => (
              <TableRow key={pessoa.id}>
                <TableCell>{pessoa.nome}</TableCell>
                <TableCell>{pessoa.email}</TableCell>
                <TableCell>{pessoa.cpf}</TableCell>
                <TableCell>{pessoa.telefone}</TableCell>
                <TableCell>{formatarData(pessoa.data_nascimento)}</TableCell>
                <TableCell>{pessoa.ativo ? 'Ativo' : 'Inativo'}</TableCell>
                <TableCell align="center">
                  <IconButton
                    color="primary"
                    onClick={() => handleEditar(pessoa.id)}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    color="error"
                    onClick={() => handleAbrirDeleteDialog(pessoa)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <TablePagination
          component="div"
          count={total}
          page={page}
          onPageChange={handleChangePage}
          rowsPerPage={rowsPerPage}
          onRowsPerPageChange={handleChangeRowsPerPage}
          rowsPerPageOptions={[5, 10, 25, 50]}
          labelRowsPerPage="Itens por página:"
          labelDisplayedRows={({ from, to, count }) => 
            `${from}-${to} de ${count !== -1 ? count : `mais de ${to}`}`
          }
        />
      </TableContainer>

      <Dialog
        open={deleteDialog}
        onClose={handleFecharDeleteDialog}
      >
        <DialogTitle>Confirmar Exclusão</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Tem certeza que deseja excluir {pessoaParaDeletar?.nome}?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleFecharDeleteDialog}>Cancelar</Button>
          <Button onClick={handleConfirmarDelete} color="error">
            Excluir
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default ListaPessoas;
