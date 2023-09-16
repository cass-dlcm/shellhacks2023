import React from "react";

const Recipe = (props) => {
    return (
        <>
        <img className="recipeImg" src={props.image}></img>
        <h2>{props.name}</h2>
        <p>{props.description}</p>
        <h5>Ingredients & Supplies:</h5>
        </>
    )
}

export default Recipe;