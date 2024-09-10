// src/api/api.js

const API_URL = 'http://localhost:8000'; // URL da API Django

export const getCliente = async (cpf) => {
    try {
        const response = await fetch(`${API_URL}/retira-dados/${cpf}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Erro na requisição: ${response.statusText}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Erro ao buscar cliente:', error);
        throw error;
    }
};
