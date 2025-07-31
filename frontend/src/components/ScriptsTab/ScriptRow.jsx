import "./ScriptRow.css"

import LoadingButton from "../general/LoadingButton/LoadingButton";


export default function ScriptRow() {
    return (
        <div className="script-row">
            <div className="script-content">
                <img src="/defaultScriptIcon.svg" className="script-icon" />
                <h2>Halo</h2>
            </div>
            <LoadingButton className="script-execute-button">Execute</LoadingButton>
        </div>
    );
}