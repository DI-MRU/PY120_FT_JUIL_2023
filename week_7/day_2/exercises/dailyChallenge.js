const bygetting = document.getElementById("libform");
const myStory = document.getElementById("story");
const shuffle = document.getElementById("shuffle");

bygetting.addEventListener("submit", function (event) {
  const noun = document.getElementById("noun").value;
  const adjective = document.getElementById("adjective").value;
  const verb = document.getElementById("verb").value;
  const place = document.getElementById("place").value;
  const person = document.getElementById("person").value;

  event.preventDefault();
  if (noun && adjective && verb && place && person) {
    story = `${person}, a skilled ${adjective} ${noun}, ${verb} through the enchanting ${place}. Amidst ancient trees and tranquil streams, ${person} embarked on a quest to uncover hidden mysteries.

    Guided by whispers of legends, ${person} discovered a hidden path leading to an ancient ruin. Within its walls, they found intricate carvings depicting forgotten tales of bravery and love.
    
    As night descended, stars adorned the sky like diamonds. With a heart full of determination, ${person} deciphered the carvings, revealing the secrets of the ruin. The wisdom gained would forever shape their destiny.
    
    With newfound purpose, ${person} returned to their village, sharing the ancient lore with their people. The village flourished with renewed unity, as ${person}'s journey had inspired hope and courage.
    
    And so, ${person}'s legacy lives on, a testament to the power of ${noun}${adjective} hearts and the magic that thrives within every corner of ${place}.`;

    myStory.textContent = story;
  } else {
    myStory.textContent = "fill in the form";
  }})

shuffle.addEventListener("click", () => {
    const noun = document.getElementById("noun").value;
    const adjective = document.getElementById("adjective").value;
    const verb = document.getElementById("verb").value;
    const place = document.getElementById("place").value;
    const person = document.getElementById("person").value;

    if (
      noun === "" || adjective === "" || verb === "" || place === "" || person === "") {
      myStory.textContent = "fill in the form";
    } else {
      const stories = [
        "Once upon a time, a {{adjective}} {{noun}} met {{person}} at {{place}}. They decided to {{verb}} together.",
        "{{person}} found a {{adjective}} {{noun}} in {{place}} and couldn't resist {{verb}}ing it.",
        "In {{place}}, {{person}} encountered a {{adjective}} {{noun}}. {{person}} bravely {{verb}}ed it.",
        "There was a {{noun}} that belonged to {{person}}. One day, it {{verb}}ed so {{adjective}} in {{place}}.",
      ];
    
    let rand = stories[Math.floor(Math.random(stories) * stories.length)];

    const holder = {
      "{{adjective}}": adjective,
      "{{noun}}": noun,
      "{{person}}": person,
      "{{verb}}": verb,
      "{{place}}": place,
    };
    function placeholder(text) {
      return holder[text];
    }
    const randomShuffle = rand.replace(/{{adjective}}|{{noun}}|{{person}}|{{verb}}|{{place}}/g, placeholder)

    myStory.textContent = randomShuffle
  }});

