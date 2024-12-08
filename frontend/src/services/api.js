import axios from 'axios';

const api = axios.create({
    baseURL: window.location.hostname === 'localhost' 
        ? 'http://localhost:8000'
        : `http://${window.location.hostname}:8000`,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Função específica para login que usa x-www-form-urlencoded
export const login = async (username, password) => {
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    const response = await api.post('/auth/token', formData, {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    });
    return response.data;
};

// Intercepta todas as requisições
api.interceptors.request.use(config => {
    // Obtém o token do sessionStorage
    const token = sessionStorage.getItem('token');
    
    // Se houver um token, adiciona ele no header
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    
    return config;
}, error => {
    return Promise.reject(error);
});

// Intercepta todas as respostas
api.interceptors.response.use(response => {
    return response;
}, error => {
    if (error.response?.status === 401) {
        // Se receber um 401 (não autorizado), remove o token
        sessionStorage.removeItem('token');
        window.location.href = '/login';
    }
    return Promise.reject(error);
});

export default api;
