import { useState, useRef } from "react";

import logInRequest from "../../services/api/requests/login";

import "./LoginTab.css"

import LoadingButton from "../general/LoadingButton/LoadingButton";

let username = "", password = "";

export default function LoginTab({ setLoggedIn }) {
    const [errorMessage, setErrorMessage] = useState("");
    const buttonRef = useRef(null);

    async function handleLogin() {
        await logInRequest(username, password, setErrorMessage, setLoggedIn);
    }

    function handleEnter(event) {
        if (event.key === "Enter") {
            buttonRef.current?.click();
        }
    }

    return (
        <div className="login-tab">
            <h1>
                Log in
            </h1>
            <input className="login-button" type="text" id="username" placeholder="Username"
             onChange={(e) => {username = e.target.value}}
             onKeyDown={handleEnter} />
            <input className="login-button" type="password" id="password" placeholder="Password"
             onChange={(e) => {password = e.target.value}}
             onKeyDown={handleEnter} />
            <LoadingButton className="login-button" id="login-button"
             onClick={handleLogin} ref={buttonRef}>
                Log in
            </LoadingButton>
            <p className="login-error-message">{errorMessage}</p>
        </div>
    );
}
