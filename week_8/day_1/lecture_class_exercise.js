class People {
  constructor(firstName, lastName, favoriteFood) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.favoriteFood = favoriteFood;
  }

  displayFavoriteFood() {
    const resultString = `${this.firstName} ${this.lastName} likes ${this.favoriteFood}`;
    console.log(resultString);
    return resultString;
  }

  displayHometown() {
    const resultString = `Not defined`;
    console.log(resultString);
    return resultString;
  }
}

class Mauritian extends People {
  constructor(firstName, lastName, favoriteFood, hometown) {
    super(firstName, lastName, favoriteFood);
    this.hometown = hometown;
  }

  displayHometown() {
    const resultString = `${this.firstName} ${this.lastName} comes from ${this.hometown}`;
    console.log(resultString);
    return resultString;
  }
}

class Nigerian extends People {
  constructor(firstName, lastName, favoriteFood, hometown) {
    super(firstName, lastName, favoriteFood);
    this.hometown = hometown;
  }

  displayHometown() {
    const resultString = `${this.firstName} ${this.lastName} comes from ${this.hometown}`;
    console.log(resultString);
    return resultString;
  }
}

let peopleVincent = new Mauritian("Vincent", "Leung", "Burger", "QB");
let peopleAnas = new Mauritian("Anas", "Rasmally", "Burger", "Triolet");
let peopleLaeticia = new Mauritian("Laeticia", "Wong", "Dumplings", "PL");
let peopleOnyeka = new Nigerian("Onyeka", "Okpalaugo", "Rice", "Lagos");

const vincentString = peopleVincent.displayFavoriteFood();
peopleAnas.displayFavoriteFood();
peopleLaeticia.displayFavoriteFood();
peopleOnyeka.displayFavoriteFood();

peopleVincent.displayHometown();
peopleAnas.displayHometown();
peopleLaeticia.displayHometown();
peopleOnyeka.displayHometown();
