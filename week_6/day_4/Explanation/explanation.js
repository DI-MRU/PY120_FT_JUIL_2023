// console.log("test")
// //variables
// let x = 3
// var y =4
// var y = 2
// const w = 2

// let names;
// names = "tushil"
// let surname = "Gunness"
// let full_name = names + " "+ surname
// console.log(full_name.length) 
// /*
// hello = "test"
// hello[0:1]
//  */
// let hello = "test"
// console.log(hello.substring(0,1))

// let words = "Hello Wnrd"
// let result = words.replace("Wnrd","World")
// console.log(result)

// // array = [1,2,3,4]
// // Array2 =[5,6,7,8]
// // total = array + Array2

// let array = [1,2,3]
// let array2 = [4,5,6]
// let total = array.concat(array2)
// console.log(total)

// let empty = "    hello world"
// let testing = empty.trim()
// console.log(testing)
// console.log(testing.charAt(0))
// let addressNUmber = "somewhere"
// let addressStreet = 23
// let country = "Mauritius"
// let globalAddress =addressNUmber + addressStreet + country +`${country}`
// console.log(globalAddress)


// console.log(1==='1')

// // alert("hello")
// // let age = prompt('How old are you?', 20);
// // alert(`You are ${age} years old!`); 

// // let isBoss = confirm("Are you the boss?");
// // alert(isBoss); // true if OK is pressed

// let person = {
//     firstName: "John",
//     lastName: "Doe",
//   };
// //   person1 = person["firstName"]

// let user = {
//     username :"Tushil",
//     password : "1234"
// }

// let database = [user]

// let newsfeed = [
//     {
//         username :"Tushil",
//         timeline : "2023"
//     },
//     {
//         username :"Tushil",
//         timeline : "2023"
//     }
// ]
// let age = 20

// if (age === 18) {
//     console.log("It's your birthday !!") 
// } else if (age > 18) {
//     console.log("We can go to a pub together !!")
// } else {
//     console.log("Sorry...You have to stay at home tonight")
// }

// let fruit = 'Oranges';

// switch (fruit) {
//   case 'Oranges':
//     console.log('Oranges are $0.59 a pound.');
//     break;
//   case 'Mangoes':
//   case 'Papayas':
//     console.log('Mangoes and papayas are $2.79 a pound.');
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log('Sorry, we are out of ' + fruit + '.');
// }

let names= ["john", "sarah", 23, "Rudolf",34]

for(let i = 0 ; i < names.length; i++){
    let item = names[i]
    if (typeof(item)!='string'){
    continue
    }
    if (item.charAt(0)!=item.charAt(0).toUpperCase()){
       item = names[i].charAt(0).toUpperCase() + item.slice(1)
       console.log(item)
    }
    console.log(item)
}
if (true){
    let x = 2 // block - scope
    const y = 5 // block - scope
    var num = 3 // global - scope
}
console.log(num)