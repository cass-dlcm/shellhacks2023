import React from "react";
import 'bootstrap/dist/css/bootstrap.css';

const Card = (props) => {
    return (
    <>
    <div class="card bg-info mb-3">
        <div class="card-header">
            Recipe Info
        </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item">Prep time: {props.prepTime}</li>
            <li class="list-group-item">Cook time: {props.cookTime}</li>
            <li class="list-group-item">Total time: {props.totalTime}</li>
            <li class="list-group-item">Servings: {props.servings}</li>
        </ul>
    </div>
    </>
    )
}

export default Card;