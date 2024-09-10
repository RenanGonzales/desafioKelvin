// src/Resgate.jsx
import React, { useState } from 'react';
import { Input, Button, Layout, List, message } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content } = Layout;

const Resgate = () => {
  const [cpf, setCpf] = useState('');
  const [dados, setDados] = useState(null);

  const handleFetchData = async () => {
    try {
      const response = await fetch(`http://localhost:8000/retira-dados/${cpf}`);
      if (response.ok) {
        const data = await response.json();
        setDados(data);
      } else {
        message.error('Cliente não encontrado ou erro na busca.');
        setDados(null);
      }
    } catch (error) {
      message.error('Erro ao conectar à API.');
    }
  };

  return (
    <Layout>
      <Header>
        <Link to="/">Página de Cadastro</Link>
      </Header>
      <Content style={{ padding: '50px' }}>
        <Input
          placeholder="Digite o CPF"
          value={cpf}
          onChange={(e) => setCpf(e.target.value)}
          style={{ maxWidth: '300px', marginBottom: '20px' }}
        />
        <Button type="primary" onClick={handleFetchData}>
          Resgatar Dados
        </Button>
        {dados && (
          <List
            header={<div>Dados Resgatados</div>}
            bordered
            dataSource={Object.entries(dados)}
            renderItem={([key, value]) => (
              <List.Item>
                <strong>{key}:</strong> {value}
              </List.Item>
            )}
          />
        )}
      </Content>
    </Layout>
  );
};

export default Resgate;
