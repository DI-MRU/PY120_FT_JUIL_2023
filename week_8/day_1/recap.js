// let onyekaFavNum = 10;

// const changeNum = (favNum) => {
//   favNum = 200;
//   console.log(`New: ${favNum}`);
// };

// // Deep copy - Complete new clone
// changeNum(onyekaFavNum);

// console.log(`Original: ${onyekaFavNum}`);

let onyekaFavNumList = [10, 200];

const changeNumList = (favNumList) => {
  favNumList[0] = 200;
  favNumList[1] = 500;
  console.log(`New: ${favNumList}`);
};

// Shallow copy - By reference
changeNumList(onyekaFavNumList);

console.log(`Original: ${onyekaFavNumList}`);

let a = 10;
let b = 20;
let rest = [30, 40, 50];

const iterable = [a, b, ...rest];
console.log(iterable);
// expected output: [10, 20, [30, 40, 50]] with [a, b, rest];
// expected output: [10, 20, 30, 40, 50] with [a, b, ...rest];
