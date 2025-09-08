import "./ScriptsTab.css"

import ScriptRow from "./ScriptRow";


export default function ScriptsTab({ setLoggedIn }) {

    return (
        <div className="scripts-tab">
            <ScriptRow id={1} name={"HALO"} icon={"/defaultScriptIcon.svg"} setLoggedIn={setLoggedIn} />
            <ScriptRow />
            <ScriptRow />
        </div>
    );
}