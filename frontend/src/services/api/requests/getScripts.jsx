import api from "../api";

import handleAuthorisationErrors from "./handleAuthorisationErrors";


export default async function getScripts(setLoggedIn) {
    return api.get("/scripts")
    .then(
        (response) => {
            return response.data;
        }
    )
    .catch((error) => {
        handleAuthorisationErrors(error, setLoggedIn);
    });
}
