import React from "react";
import Ingredients from "../Ingredients";

const Recipe = (props) => {
    return (
        <>
        <img className="recipeImg" src={props.image}></img>
        <h2>{props.name}</h2>
        <p>{props.description}</p>
        </>
    )
}

export default Recipe;