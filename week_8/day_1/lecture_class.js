// class Rectangle {
//   constructor(height, width) {
//     this.height = height;
//     this.width = width;
//   }

//   // Method
//   calcArea() {
//     return this.height * this.width;
//   }
// }

// const square = new Rectangle(10, 10);

// // calling the method
// console.log(square.calcArea()); // 100

// console.log(square);

class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says '${line}'`);
  }
}
let killerRabbit = new Rabbit("killer");
let blackRabbit = new Rabbit("black");

killerRabbit.speak("I want to eat your liver.");
blackRabbit.speak("I am sleepy");

class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.height * this.width;
  }

  // Setter
  set area(factor) {
    this.width = this.height * factor;
  }
}

const square = new Rectangle(10, 10);
square.area = 2;
square.area; //200
console.log(square.area);
console.log(square);

class Animal {
  constructor(name) {
    this.name = name;
  }
  speak() {
    console.log(`${this.name} makes a noise.`);
  }
}

class Dog extends Animal {
  constructor(name, noise) {
    super(name); // call the super class constructor and pass in the name parameter
    // Add a new property
    this.noise = noise;
  }

  speak() {
    console.log(`${this.name} barks.It says ${this.noise}`);
  }
}

let d = new Dog("Mitzie", "Wouaf");
console.log(d.name); // Mitzie
d.speak(); // Mitzie barks.It says Wouaf
console.log(d);
//Dog {name: "Mitzie", noise: "Wouaf"}
//__proto__: Animal
//  constructor: class Dog
//  speak: ƒ speak()
//__proto__: Object
