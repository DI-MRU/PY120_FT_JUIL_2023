const express = require('express');
var bodyParser = require('body-parser'); 

function fmt(data){
    return {response: data};
}

const app = express()

app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(bodyParser());

app.get('/', (req, res) => {
    response={
        message: 'Hello World'
    }

    res.json(response); 
});

//body parameter
app.post('/login', (req, res) => {
    username=req.body.username;
    password=req.body.password;
    console.log(username,password);
    
    res.send(fmt('Login Successful'));
});

app.get('/contact', (req, res) => {
    res.send('Phone: 12345');
});

//request parameter
app.get('/products/:id', (req, res) => {
    
    res.json(fmt(req.params.id));
});


//query parameter
app.get('/products', (req, res) => {
    response={
        name: req.query.name,
        price: req.query.price
    }
    res.json(response);
});


port=3000;
app.listen(port,'localhost', () => {
    console.log(`server is listening on port ${port}`)
});