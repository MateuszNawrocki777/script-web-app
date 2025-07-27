import api from "../api";
import { setTokenInterceptor } from "../api";
import qs from "qs";


export default function logInRequest(username, password, setErrorMessage, setLoggedIn) {
    if (checkIfLoginIsEmpty(username, password, setErrorMessage))
        return;

    sendLoginRequest(username, password)
    .then((response) => {
        handleCorrectLogIn(response, setLoggedIn);
    })
    .catch((error) => {
        handleIncorrectLogIn(error, setErrorMessage);
    });
}


function isLoginEmpty(username, password) {
    return username === "" || password.trim() === "";
}

function checkIfLoginIsEmpty(username, password, setErrorMessage) {
    if (isLoginEmpty(username, password)) {
        setErrorMessage("Username and password cannot be empty.");
        return true;
    }
    return false;
}

function sendLoginRequest(username, password) {
    const formData = qs.stringify({
        grant_type: "password",
        username: username,
        password: password
    })

    return api.post("/login", formData,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
    )
}

function handleCorrectLogIn(response, setLoggedIn) {
    if (response.status === 200) {
        setTokenInterceptor(response.data.access_token);
        setLoggedIn(true);
    } else {
        throw new Error("Unexpected response status: " + response.status);
    }
}

function handleIncorrectLogIn(error, setErrorMessage) {
    if (error.response && error.response.status === 403) {
        setErrorMessage("Invalid username or password.");
    }
    else {
        setErrorMessage("An error occurred while logging in. Please try again.");
    }
}
