let letters = document.getElementById('letters')
letters.addEventListener('input',function(){
    const check = letters.value.replace(/[^a-zA-z]/g,"");
    letters.value = check;
})

function hello(){
    console.log('hello');
}

const hello = () =>{
    console.log('hello');
}
