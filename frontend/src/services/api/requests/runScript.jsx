import api from "../api";


export default async function runScript(id, setLoggedIn) {
    try {
        await api.post(`/run/${id}`)
    }
    catch (error) {
        handleError(error, setLoggedIn);
    };
}


function handleError(error, setLoggedIn) {
    if (error.response && error.response.status === 401) {
        console.error("User unauthorised.")
        setLoggedIn(false);
    }
    else if (error.response && error.response.status === 405) {
        console.warn("Token expired, moving back to log in page.")
        setLoggedIn(false);
    }
    else {
        throw error;
    }
}