const object1 = {
  a: "somestring",
  b: 42,
  c: false,
  Anas: 12384632978759,
};

// Get all the keys (i.e. the left side of `:`s)
console.log(Object.keys(object1));

// Get all the values (i.e. the right side of `:`s)
console.log(Object.values(object1));

// Get all the keys & values (i.e. both sides of `:`s)
console.log(Object.entries(object1));

for (let [key, value] of Object.entries(object1)) {
  console.log(`${key}: ${value}`);
}

const shopping = [
  ["apple", "$2"],
  ["pear", "$1"],
  ["banana", "$0.77"],
];

const shoppingObject = Object.fromEntries(shopping);
console.log(shoppingObject);

const address = {
  street: "Evergreen Terrace",
  number: "742",
  city: "Springfield",
  state: "NT",
  zip: "49007",
};

const { street: street, city: hometown, number, zip: postcode } = address;
console.log({ street, hometown, number, postcode });

const student = {
  name: "John Doe",
  age: 16,
  scores: {
    maths: 74,
    english: 63,
  },
};
const { name: studentName } = student;
const {
  scores: { maths: algebra = 50, chemistry = 100 },
} = student;
console.log(studentName, algebra, chemistry);

// const student = {
//   name: "John Doe",
//   age: 16,
//   scores: {
//     maths: 74,
//     english: 63,
//     science: 85,
//   },
// };

// Without Destructuring
function displaySummary(student) {
  console.log("Hello, " + student.name);
  console.log("Your Maths score is " + (student.scores.maths || 0));
  console.log("Your English score is " + (student.scores.english || 0));
  console.log("Your Science score is " + (student.scores.science || 0));
}

// With Destructuring
function displaySummary({
  name,
  scores: { maths = 0, english = 0, science = 0 },
}) {
  console.log("Hello, " + name);
  console.log("Your Maths score is " + maths);
  console.log("Your English score is " + english);
  console.log("Your Science score is " + science);
}

displaySummary(student);

// let obj = { foo: 1, bar: 2 };
// let newObj = { ...obj, baz: 3 };
// console.log(newObj); // Expected output is { { foo: 1, bar: 2 }, baz: 3 } with { obj, baz: 3 }
// console.log(newObj); // Expected output is { foo: 1, bar: 2, baz: 3 } with { ...obj, baz: 3 }

// If property keys clash, the property that is mentioned last “wins”:
let obj = { foo: 1, bar: 2, baz: 3 };
// let newObj = { ...obj, foo: true };
// console.log(newObj); //{ foo: true, bar: 2, baz: 3 }

let newObj = { foo: true, ...obj };
console.log(newObj); //{ foo: 1, bar: 2, baz: 3 }

let myCar = {
  color: "blue",
  details: {
    plateNumber: 123,
    name: "Ford",
  },
};

let myNewCar = { ...myCar };
console.log("myNewCar : ", myNewCar);
// myNewCar :
// {
//      color: 'blue',
//      details: { plateNumber: 123, name: 'Ford' }
// }

// DEEP COPYING
myCar.color = "red";
console.log("myNewCar.color :", myNewCar.color);
// myNewCar.color : blue -- UNCHANGED
console.log("myCar.color :", myCar.color);
// myCar.color : red -- CHANGED

// SHALLOW COPYING
myCar.details.plateNumber = 345;
console.log("myNewCar.details.plateNumber :", myNewCar.details.plateNumber);
// myNewCar.details.plateNumber : 345 -- CHANGED
console.log("myCar.details.plateNumber :", myCar.details.plateNumber);
// myCar.details.plateNumber : 345 : red -- CHANGED
