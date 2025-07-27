import { useState } from 'react'
import './App.css'

import LoginTab from './components/LoginTab/LoginTab'


function App() {
    const [loggedIn, setLoggedIn] = useState(false);

    return (
        <>
            {!loggedIn && <LoginTab setLoggedIn={setLoggedIn} />}
        </>
    )
}

export default App
