console.log("Lecture - Exceptions | START");
// hello;
// hello.testMethod();

function tryCatchError() {
  try {
    console.log("Hello");
    hello;
    hello.testMethod();
  } catch (someErrorName) {
    console.error("Some error occured");
    console.error(`${someErrorName}`);
    throw Error("Some error happened");
    return;
  } finally {
    console.log("The try-catch is finished");
  }

  console.log("The function is complete");
}

tryCatchError();

console.log("Lecture - Exceptions | END");
