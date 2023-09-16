import React from "react";
import 'bootstrap/dist/css/bootstrap.css';

const Navbar = () => {
    return (
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Personal Cookbook</a>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Add Recipe</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Edit Recipe</a>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Navbar;