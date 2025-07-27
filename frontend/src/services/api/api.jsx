import axios from "axios";


const api = axios.create({
    baseURL: "http://localhost:8000" // Replace with your server URL
});

export default api;


export function setTokenInterceptor(token) {
    api.interceptors.request.use((config) => {
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        else {
            delete config.headers.Authorization;
        }
        return config;
    });
}
