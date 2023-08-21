let divElement = document.getElementsByTagName("div")[0];
console.log(divElement);
divElement.innerText = "This is modified text";

let anasDiv = document.getElementById("anas");
anasDiv.innerText = "Anas Div";

let laeticiaDiv = document.getElementsByClassName("laeticia")[0];
console.log(laeticiaDiv);
laeticiaDiv.innerText = "Laeticia Div";

let queryDiv = document.querySelectorAll("div");
console.log(queryDiv);
queryDiv[2].innerText = "Found ya";

document.body.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.innerText =
  "Text via siblings";

// alert("This is some alert");
// let userInput = prompt("Please enter your name");
// console.log(`The entered name is ${userInput}`);
// queryDiv[2].innerHTML =
//   "<h1>This is a random Header 1</h1><script>console.log('All your passwords')</script>";

let newHeader = document.createElement("h1");
newHeader.innerText = "This is a random Header 1";
queryDiv[2].appendChild(newHeader);
// queryDiv[2].removeChild(newHeader);
newHeader.style.background = "#FF0000";
newHeader.style.border = "5px solid";
newHeader.classList.add("h1_style_1"); // This affects only the h1_style_1 class of the element
newHeader.classList.add("h1_style_2");
newHeader.classList.add("h1_style_13");
newHeader.classList.add("h1_style_4");
newHeader.classList.toggle("h1_style_4");
newHeader.classList.toggle("h1_style_4");
newHeader.className = "h1_style_1"; // This affects all the classes of the element

document.getElementsByTagName("div");
document.getElementById("container");

document.querySelectorAll("ul");
document.getElementsByTagName("ul");
document.querySelectorAll(".list");

document.querySelectorAll("ul > li:first-child");

let ulList = document.getElementsByTagName("ul");
console.log(ulList);
let firstLiElements = [];
// Array.from(ulList).forEach((element) => {
//   firstLiElements.push(element)[0];
// });
for (let i = 0; i < ulList.length; i++) {
  firstLiElements.push(ulList[i].firstElementChild);
}
console.log(firstLiElements);

console.log(document.forms);

document.forms.first_form.innerText = "test";

// select.options[2].selected = true;
// select.selectedIndex = 2;
select.value = "pear";

let option = new Option("Borel", "100");
document.forms.fourth_form.querySelector("select").appendChild(option);
