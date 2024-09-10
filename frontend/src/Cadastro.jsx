// src/Cadastro.jsx
import React from 'react';
import { Form, Input, Button, Layout } from 'antd';
import { Link } from 'react-router-dom';

const { Header, Content } = Layout;

const Cadastro = () => {
  const onFinish = (values) => {
    console.log('Dados enviados:', values);
    // Lógica de envio de dados para a API
  };

  return (
    <Layout>
      <Header>
        <Link to="/resgate">Resgatar Dados</Link>
      </Header>
      <Content style={{ padding: '50px' }}>
        <Form name="basic" onFinish={onFinish} style={{ maxWidth: '600px', margin: '0 auto' }}>
          <Form.Item
            label="Nome"
            name="nome"
            rules={[{ required: true, message: 'Por favor, insira o seu nome!' }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="CPF"
            name="cpf"
            rules={[{ required: true, message: 'Por favor, insira o seu CPF!' }]}
          >
            <Input />
          </Form.Item>
          {/* Outros campos do formulário */}
          <Form.Item>
            <Button type="primary" htmlType="submit">
              Cadastrar
            </Button>
          </Form.Item>
        </Form>
      </Content>
    </Layout>
  );
};

export default Cadastro;
