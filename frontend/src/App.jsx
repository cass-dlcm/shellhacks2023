import 'bootstrap/dist/css/bootstrap.css';
import './App.css'
import Navbar from './components/Navbar/Navbar.jsx'
import './components/Navbar/Navbar.css'
import Recipe from './components/Recipe/Recipe.jsx'
import './components/Recipe/Recipe.css'
import Ingredients from './components/Ingredients';

function App() {

  return (
    <>
      <Navbar />
      <div className='recipeContainer'>
        <div className='recipeItem'>
          <Recipe name= "Carrot Cake" description="cool recipe!" image="./img/CarrotCake.jpeg"/>
          <ul>
            <Ingredients name = "carrot" num = "2"/>
          </ul>
        </div>
        <div className='recipeItem'>
          <Recipe name= "Carrot Cake 2" description="cool recipe!" image="./img/CarrotCake.jpeg"/>
          <ul>
            <Ingredients name = "carrot" num = "2"/>
          </ul>
        </div>
      </div>
    </>
  )
}

export default App;
