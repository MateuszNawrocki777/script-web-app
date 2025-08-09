import axios from "axios";


const api = axios.create({
    baseURL: "http://localhost:8000" // Replace with your server URL
});

export default api;


let tokenInterceptorId = null;


export function setTokenInterceptor(token) {
    console.log("Setting token: " + token);
    if (tokenInterceptorId !== null) {
        api.interceptors.request.eject(tokenInterceptorId);
    }

    tokenInterceptorId = api.interceptors.request.use((config) => {
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        else {
            delete config.headers.Authorization;
        }
        return config;
    });
}
