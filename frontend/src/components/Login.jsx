import "./Login.css"


export default function LoginTab() {
    return (
        <div className="login-tab">
            <h1>
                Log in
            </h1>
            <input className="login-button" type="text" id="username" placeholder="Username" />
            <input className="login-button" type="password" id="password" placeholder="Password" />
            <button className="login-button" id="login-button">Log in</button>
        </div>
    );
}