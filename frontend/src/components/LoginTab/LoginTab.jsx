import { useState } from "react";

import logInRequest from "../../services/api/requests/login";

import "./LoginTab.css"

let username = "", password = "";

export default function LoginTab({ setLoggedIn }) {
    const [errorMessage, setErrorMessage] = useState("");

    function handleLogin() {
        logInRequest(username, password, setErrorMessage, setLoggedIn);
    }

    return (
        <div className="login-tab">
            <h1>
                Log in
            </h1>
            <input className="login-button" type="text" id="username" placeholder="Username"
             onChange={(e) => {username = e.target.value}} />
            <input className="login-button" type="password" id="password" placeholder="Password"
             onChange={(e) => {password = e.target.value}} />
            <button className="login-button" id="login-button"
             onClick={handleLogin}>
                Log in
            </button>
            {errorMessage !== "" && <p className="login-error-message">{errorMessage}</p>}
        </div>
    );
}
