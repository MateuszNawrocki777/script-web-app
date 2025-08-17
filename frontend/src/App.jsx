import { useState } from 'react'
import './App.css'

import LoginTab from './components/LoginTab/LoginTab'
import ScriptsTab from './components/ScriptsTab/ScriptsTab';


function App() {
    const [loggedIn, setLoggedIn] = useState(false);

    return (
        <>
            {loggedIn ?
            <ScriptsTab setLoggedIn={setLoggedIn} />
            : <LoginTab setLoggedIn={setLoggedIn} />}
        </>
    )
}

export default App
