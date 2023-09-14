import React from "react";
// import HandlerFunction from "./handlerFunction";
import Sunrise from "./handlerFunction";



// class App extends React.Component {
    
//   handleSubmit = event => {
//     event.preventDefault();
//     let inputs = event.target.getElementsByTagName('input')
//     for (const item of inputs) {
//       console.log(item.value)
//     }
//   }

//   render() {
//     return <><HandlerFunction handleSubmit={this.handleSubmit}/></>
//   }
// }
// export default App;
const App = () => {

    return (
      <div className="box">
        <h1>In the App.js</h1>
        <Sunrise />
      </div>
    )
  }
  
  export default App;
