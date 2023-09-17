import 'bootstrap/dist/css/bootstrap.css';
import './App.css'
import Navbar from './components/Navbar/Navbar.jsx'
import './components/Navbar/Navbar.css'
import Recipe from './components/Recipe/Recipe.jsx'
import './components/Recipe/Recipe.css'
import Ingredients from './components/Ingredients';
import Supplies from './components/Supplies';
import Directions from './components/Directions';
import Card from './components/Card.jsx';
import Dropdown from './components/Dropdown/Dropdown.jsx';
import './components/Dropdown/Dropdown.css';

function App() {

  return (
    <>
      <Navbar />
      <div className='recipeContainer'>
        <div className='recipeItem'>
          <Recipe name= "Carrot Cake" description="This is the best carrot cake recipe I have ever made!" image="./img/CarrotCake.jpeg"/>
          <Card prepTime="20 mins" cookTime="45 mins" totalTime="1 hr 10 mins" servings="10"/>
          <Dropdown title="Ingredients & Supplies" items={[
            <ul>
              <Ingredients name = "cup unsalted butter" num = "3/4"/>
              <Ingredients name = "cup brown sugar" num = "2/3"/>
              <Ingredients name = "large egg yolk" num = "1"/>
              <Supplies name = "mixing bowl" num ="1"/>
              <li>...</li>
            </ul>
          ]}/>

          <Dropdown title="Directions" items={[
            <ol>
              <Directions direction="Prepare ingredients & supplies"/>
              <li>...</li>
            </ol>
          ]}/>
          
          
        </div>
      </div>
    </>
  )
}

export default App;
