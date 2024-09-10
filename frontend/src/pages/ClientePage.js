import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getCliente } from '../api/api';

const ClientePage = () => {
    const { cpf } = useParams();
    const [cliente, setCliente] = useState(null);

    useEffect(() => {
        const fetchCliente = async () => {
            try {
                const data = await getCliente(cpf);
                setCliente(data);
            } catch (error) {
                console.error("Erro ao buscar cliente:", error);
            }
        };

        fetchCliente();
    }, [cpf]);

    if (!cliente) return <p>Carregando...</p>;

    return (
        <div>
            <h1>Cliente</h1>
            <p>Nome: {cliente.nome}</p>
            <p>CPF: {cliente.cpf}</p>
            <p>Data de Nascimento: {cliente['data de nascimento']}</p>
        </div>
    );
};

export default ClientePage;
