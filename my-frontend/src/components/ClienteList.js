import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const ClienteList = () => {
  const [clientes, setClientes] = useState([]);

  useEffect(() => {
    const fetchClientes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/clientes/');
        console.log(response.data);
        setClientes(response.data);
      } catch (error) {
        console.error('Erro ao buscar clientes:', error);
      }
    };

    fetchClientes();
  }, []);

  return (
    <div>
      <h1>Lista de Clientes</h1>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Nome (Cliente)</TableCell>
              <TableCell align="right">Email</TableCell>
              <TableCell align="right">CPF</TableCell>
              <TableCell align="right">Endereço</TableCell>
              <TableCell align="right">Cidade</TableCell>
              <TableCell align="right">CEP</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {clientes.map((cliente) => (
              <TableRow
                key={cliente.id}
                sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {cliente.nome}
                </TableCell>
                {/* Substitua as propriedades abaixo com as propriedades corretas do seu modelo de cliente */}
                <TableCell align="right">{cliente.email}</TableCell>
                <TableCell align="right">{cliente.cpf}</TableCell>
                <TableCell align="right">{cliente.endereco}</TableCell>
                <TableCell align="right">{cliente.cidade}</TableCell>
                <TableCell align="right">{cliente.cep}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  );
};

export default ClienteList;
