import "./ScriptsTab.css"

import ScriptRow from "./ScriptRow";


export default function ScriptsTab() {
    return (
        <div className="scripts-tab">
            <ScriptRow />
            <ScriptRow />
            <ScriptRow />
        </div>
    );
}