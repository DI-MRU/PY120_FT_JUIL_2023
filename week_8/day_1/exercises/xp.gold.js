// function printFullName({first , last}){
//     return `Your full name is ${first} ${last}`
// }
// console.log(printFullName({first: 'Elie', last:'Schoppik'}))


// function displayStudentInfo(objUser){
//     //destructuring
//     const {first, last} = objUser
//     console.log(`your full name is ${first} ${last}`)
// }
// displayStudentInfo({first: 'Elie', last:'Schoppik'});


function kandV(obj){
    const keys = Object.keys(obj).sort()
    // const values = keys.map(key =>obj[key])
    const values =[];
    keys.forEach(key => {
        values.push(obj[key])
    })
    return [keys, values]
}

console.log(kandV({ a: "Apple", b: "Microsoft", c: "Google" }))