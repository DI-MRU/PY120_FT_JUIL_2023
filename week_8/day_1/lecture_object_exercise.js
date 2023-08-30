let myObj = {
  name: "John",
  lastName: "Doe",
  age: 25,
  friends: ["Mark", "Lucie", "Ana"],
};

const keySize = Object.keys(myObj).length;
const valueSize = Object.values(myObj).length;

// console.log(`The ${keySize} key is: --- The ${valueSize} value is: ---`);

// // Method 1
// for (let key = 0; key < keySize; key++) {
//   const keyName = Object.keys(myObj)[key];
//   const value = Object.values(myObj)[key];
//   const position = key + 1;
//   console.log(
//     `The ${position}# key is: ${keyName}\nThe ${position}# value is: ${value}`
//   );

//   console.log({
//     key: `The ${position}# key is: ${keyName}`,
//     value: `The ${position}# value is: ${value}`,
//   });
// }

// // Method 2
// let position = 0;
// for ([key, value] of Object.entries(myObj)) {
//   position++;
//   console.log(
//     `The ${position}# key is: ${key}\nThe ${position}# value is: ${value}`
//   );
// }

const user = { name: "Lydia", age: 21 };
const admin = { admin: true, ...user };
console.log(admin);
