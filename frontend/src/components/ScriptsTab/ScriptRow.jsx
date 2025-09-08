import "./ScriptRow.css"

import LoadingButton from "../general/LoadingButton/LoadingButton";

import runScript from "../../services/api/requests/runScript";


export default function ScriptRow({ id, name, icon, setLoggedIn }) {

    async function handleExecute() {
        await runScript(id, setLoggedIn);
    }

    return (
        <div className="script-row">
            <div className="script-content">
                <img src={icon} className="script-icon" />
                <h2>{name}</h2>
            </div>
            <LoadingButton className="script-execute-button"
            onClick={handleExecute}>Execute</LoadingButton>
        </div>
    );
}