// Function used to handle authorisation errors
// for api calls for logged in users

export default function handleAuthorisationErrors(error, setLoggedIn) {
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