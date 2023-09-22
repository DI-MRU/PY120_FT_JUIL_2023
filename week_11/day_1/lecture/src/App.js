// import logo from './logo.svg';
import './App.css';
import {Route,Routes,Link} from 'react-router-dom'
import Home from './home';
import About from './about';

function App() {
  return (
    <div className="App">
      <Link to={"/"}>Home</Link>
      <Link to={"/about"}>About</Link>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
      </Routes>

    </div>
  );
}

export default App;
