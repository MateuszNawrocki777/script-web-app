import { useState } from "react";

import logInRequest from "../services/api/requests/login";

import "./Login.css"


export default function LoginTab() {
    const [errorMessage, setErrorMessage] = useState("");

    let login = "", password = "";

    function handleLogin() {
        logInRequest(login, password, setErrorMessage, true);
    }

    return (
        <div className="login-tab">
            <h1>
                Log in
            </h1>
            <input className="login-button" type="text" id="username" placeholder="Username"
             onChange={(e) => {login = e.target.value}} />
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
