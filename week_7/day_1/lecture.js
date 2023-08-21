/**
 * Greet a person.
 * @param {String} firstName The first name of the person.
 * @param {String} lastName The last name of the person.
 * @param {Number} age The age of the person.
 * @return {Number} The age of the person.
 */
function greeting(firstName = "Vincent", lastName, age = 18) {
  // console.log("Welcome back " + firstName + " " + lastName + "!"); // This is the old way
  // console.log("Welcome back ${firstName}!"); // This will not work
  console.log(`Welcome back ${firstName} ${lastName}!`); // This is the modern way
  console.log("Good morning everyone");
  return age;
}

totalAge = 0;
totalAge += greeting("Anas", "Rasmally", 30);
totalAge += greeting("Laeticia", "Wong Sin Hing", 10);
totalAge += greeting("Onyeka", "Okpalaugo", 5);
totalAge += greeting("Jeremy", "Guyonne", 90);
totalAge += greeting(
  (lastName = "Leung Yin Ko"),
  (firstName = "Vincent"),
  1000
); // Leung Yin Ko

greeting; // This will not call the function

console.warn(`The total age is: ${totalAge}`);
// console.log("Welcome back Borel");
// console.log("Good morning everyone");

// console.log("Welcome back Borel");
// console.log("Good morning everyone");

// console.warn("Where is Parvesh?");
// console.error("Borel is missing?!");

// Global variables
var goodbye = "Cheers";
var firstName = "Joe";

function sayGoodbye() {
  let goodbye = "Have a good night,";
  // let firstName = "Himanish";
  var testValue = "Anas";
  firstName = "Laeticia";
  console.log(`${goodbye} ${firstName}`);
}

sayGoodbye();
console.log(`${goodbye} ${firstName}`);
// console.log(testValue);

// function exercise1(myAge) {
//   let momAge = myAge * 2;
//   let dadAge = momAge * 1.2;

//   console.log(`Mom: ${momAge} | Dad: ${dadAge}`);
//   // Mom: 200 | Dad: 240
// }

// exercise1(100);

function exercise1Extra(myAge, momModifier, dadModifier) {
  let momAge = myAge * momModifier;
  let dadAge = myAge * dadModifier;

  console.log(`Mom: ${momAge} | Dad: ${dadAge}`);
  // Mom: 500 | Dad: 240
  // If my mom is older than my dad, "Mom is older"
  // Else if my dad is odler than my mom, "Dad is older"
  if (momAge > dadAge) {
    console.log("Mom is older");
  } else if (momAge < dadAge) {
    console.log("Dad is older");
  } else {
    console.log("Mom and dad are of the same age.");
  }

  // momAge is a Number
  // "55" is a String
  // 55 is a Number
  if (momAge === 55) {
    console.log("Yay, it's a double number.");
  }
}

exercise1Extra(100, 0.6, 6);

// = Assignment
// == Compare value
// === Compare value and type
// > Greater than
// < Less than
// >= Greater than or equal to
// <= Less than or equal to
// != Not equal to
