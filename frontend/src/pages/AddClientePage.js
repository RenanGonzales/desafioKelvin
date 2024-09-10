import React, { useState } from 'react';
import axios from 'axios';

const AddClientePage = () => {
  const [nome, setNome] = useState('');
  const [cpf, setCpf] = useState('');
  const [dataNascimento, setDataNascimento] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const clienteData = {
      nome: nome,
      cpf: cpf,
      data_nascimento: dataNascimento
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/cliente/', clienteData);
      console.log("Cliente adicionado com sucesso:", response.data);
      alert('Cliente adicionado com sucesso!');
    } catch (error) {
      console.error("Erro ao adicionar cliente:", error);
      alert('Erro ao adicionar cliente. Verifique o console para mais detalhes.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <input
        type="text"
        placeholder="CPF"
        value={cpf}
        onChange={(e) => setCpf(e.target.value)}
      />
      <input
        type="date"
        placeholder="Data de Nascimento"
        value={dataNascimento}
        onChange={(e) => setDataNascimento(e.target.value)}
      />
      <button type="submit">Adicionar Cliente</button>
    </form>
  );
};

export default AddClientePage;
