import api from "../api";

import handleAuthorisationErrors from "./handleAuthorisationErrors";


export default async function runScript(id, setLoggedIn) {
    try {
        await api.post(`/run/${id}`)
    }
    catch (error) {
        handleAuthorisationErrors(error, setLoggedIn);
    };
}
