import { useState, useEffect } from "react";

import "./ScriptsTab.css"

import ScriptRow from "./ScriptRow";

import getScripts from "../../services/api/requests/getScripts";


export default function ScriptsTab({ setLoggedIn }) {
    const [scripts, setScripts] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        setIsLoading(true);
        getScripts(setLoggedIn).then((response) => {
            setScripts(response);
            setIsLoading(false);
        });
    }, []);

    return (
        <div className="scripts-tab">
            {scripts.map((script) => (
                <ScriptRow
                    id={script.id}
                    name={script.name}
                    icon={script.icon}
                    setLoggedIn={setLoggedIn}
                    key={script.id} />
                ))}
            {isLoading &&
                <h3 className="scripts-tab-loading">
                    Loading scripts...
                </h3>
            }
            {!isLoading && scripts.length === 0 &&
                <h3 className="scripts-tab-loading">
                    No scripts to display
                </h3>
            }
        </div>
    );
}