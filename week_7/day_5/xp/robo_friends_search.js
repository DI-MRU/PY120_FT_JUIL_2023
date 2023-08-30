const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

// Method 1: Keep an internal list
let cardList = []; // To keep track of card elements

// Add all robot cards to the DOM
for (let i = 0; i < robots.length; i++) {
  // Create card elements
  const newCard = document.createElement("div");
  const newCardImage = document.createElement("img");
  const newCardName = document.createElement("h2");
  const newCardEmail = document.createElement("p");

  // Keep track of card list
  //   cardList.push(newCard); // Method 1

  // Set card elements content
  newCard.className = "card";
  newCardImage.src = robots[i].image;
  newCardName.innerText = robots[i].name;
  newCardEmail.innerText = robots[i].email;

  // Append the card elements to the DOM
  newCard.appendChild(newCardImage);
  newCard.appendChild(newCardName);
  newCard.appendChild(newCardEmail);
  document.querySelector("#cards").appendChild(newCard);
}

/**
 * Show/Hide cards depending on if they contain the queried string in the name.
 * @param {*} inputEl The input element.
 */
function filterCards(inputEl) {
  // Method 2: Query directly from the DOM
  const cardList = document.querySelectorAll(".card");

  // Loop through all the cards
  cardList.forEach((card) => {
    // Check if the text includes the input query (case-insensitive)
    if (
      card.innerText.toLowerCase().includes(inputEl.target.value.toLowerCase())
    ) {
      card.removeAttribute("hidden");
      //   card.style.display = "block";
    } else {
      card.setAttribute("hidden", true);
      //   card.style.display = "none";
    }
  });
}

let inputEl = document.querySelector("#filter-input");
inputEl.addEventListener("input", filterCards);
