import React from "react";
import { useState, useEffect } from "react";
import "tachyons";
// class HandlerFunction extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       number: 0,
//     };
//   }

//   handlePloosh = () => {
//     this.setState({ number: this.state.number + 1 });
//   };
//   render() {
//     return (
//       <>
//         <h1>Number = {this.state.number}</h1>
//         <button onClick={this.handlePloosh}>Ploosh</button>
//       </>
//     );
//   }
// }
// export default HandlerFunction;

// function HandlerFunction() {
//   const [number, Setnumber] = useState(0);
//   const handlePloosh = () => {
//     Setnumber(number +1)
//   }
//   return (
//     <>
//       <h1>Number = {number}</h1>
//       <button onClick={handlePloosh}>Ploosh</button>
//     </>
//   );
// }
// export default HandlerFunction;

// function HandlerFunction(){
//     const [hasError,sethasError] = useState(false);
//     const throwError = () => {
//         try{
//             throw new Error("something went wrong")
//         }catch(error){
//             sethasError(true)
//         }
//     }
//     if (hasError){
//         return <div className="red">404</div>
//     }
//     return(<>
//     <button onClick={throwError}>Error</button></>)
// }
// export default HandlerFunction;

// class HandlerFunction extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { hasError: false };
//   }
//   throwError = () => {
//     try {
//       throw new Error("Something went wrong");
//     } catch (error) {
//       this.setState({ hasError: true });
//     }
//   };
//   static getDerivedStateFromError(error) {
//     // Update state so the next render will show the fallback UI.
//     return { hasError: true };
//   }
//   componentDidCatch(error, errorInfo) {
//     // You can also log the error to an error reporting service
//     console.error(error, errorInfo);
//   }
//   render() {
//     if (this.state.hasError) {
//       return <div className="red">404</div>;
//     }
//     return <button onClick={this.throwError}>Error</button>;
//   }
// }
// export default HandlerFunction;

// const HandlerFunction = (props) => {
//   let { handleSubmit } = props;
//   return (
//     <>
//       <form onSubmit={handleSubmit}>
//         {/* <label htmlFor="name">Name</label>
//                 <input
//                     id="name"
//                     type="text"
//                 />
//                 <label htmlFor="age">Age</label>
//                 <input
//                     id="age"
//                     type="number"
//                 />
//                 <label htmlFor="email">Email</label>
//                 <input
//                     id="email"
//                     type="email"
//                 />
//                 <button type="submit">Submit</button>
//             </form>
//         </>

//     )
// } */}
//         <InputWithLabel id="name" label="Name" type="text" />
//         <InputWithLabel id="age" label="Age" type="number" />
//         <InputWithLabel id="email" label="Email" type="email" />
//         <button type="submit">Submit</button>
//       </form>
//     </>
//   );
// };

// const InputWithLabel = (props) => {
//   let { id, label, type } = props;
//   return (
//     <>
//       <label htmlFor={id}>{label}</label>
//       <input id={id} type={type} />
//     </>
//   );
// };

// export default HandlerFunction;

// class Sunrise extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             country: "Israel",
//             city: "Tel Aviv",
//         };
//     }

//     componentDidMount() {
//         fetch("https://api.sunrise-sunset.org/json?lat=32.0853&lng=34.7818")
//             .then((resp) => resp.json()) //return a promise
//             .then((resp) =>
//                 this.setState({ hourSunrise: resp.results.sunrise }) //add a new attribute to the state
//             )
//             .catch(function (error) {
//                 console.log(`We got the error ${error}`)
//             });
//     }

//     render() {
//         let { country, city, hourSunrise } = this.state
//         return (
//             <div>
//                 <h1>In {country}</h1>
//                 <p>
//                     The hour of the sunrise in {city} is {hourSunrise}
//                 </p>
//             </div>
//         );
//     }
// }

// export default Sunrise;

const Sunrise = () => {
  const [sunrise, Setsunrise] = useState({
    country: "Israel",
    city: "Tel Aviv",
    hourSunrise: "",
  });

  useEffect(() => {
    fetch("https://api.sunrise-sunset.org/json?lat=32.0853&lng=34.7818")
      .then((resp) => resp.json())
      .then((resp) =>
        Setsunrise((sunrise) => ({
          ...sunrise,
          hourSunrise: resp.results.sunrise,
        }))
      )
      .catch(function (error) {
        console.log(`We got the error ${error}`);
      });
  }, []);
  const { country, city, hourSunrise } = sunrise;
  return (
    <div>
      <h1>In {country}</h1>
      <p>
        The hour of the sunrise in {city} is {hourSunrise}
      </p>
    </div>
  );
};
export default Sunrise;
