import { useState } from "react";
import React from "react";
import 'bootstrap/dist/css/bootstrap.css';

function Dropdown(props) {
    const [isActive, setActive] = useState("false");

    const handleToggle = () => {
        setActive(!isActive);
    }

    return (
        <>
        <div class="accordion" id="accordionDropdown">
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                    <button onClick={handleToggle} class="accordion-button bg-info" type="button" data-bs-toggle={isActive ? "collapse" : "show"} data-bs-target="#collapseOne" aria-expanded={isActive ? "true" : "false"} aria-controls="collapseOne">
                        {props.title}
                    </button>
                </h2>
                <div id="collapseOne" class={isActive ? "accordion-collapse collapse" : "accordion-collapse show"} aria-labelledby="headingOne" data-bs-parent="#accordionDropdown">
                    <div class="accordion-body">
                        {props.items}
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export default Dropdown;