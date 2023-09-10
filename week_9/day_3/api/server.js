const express = require('express');
var bodyParser = require('body-parser'); 

function fmt(data){
    return {response: data};
}

const app = express()

var products={
    milk: 200.00,
    rice: 350.00,
    sugar: 90.00
}

app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(bodyParser());

app.get('/', (req, res) => {
    response={
        message: 'Api works'
    }

    res.json(response); 
});

app.get('/products', (req, res) => {
    res.json(products);
});

app.get('/products/:name', (req, res) => {
    product_price=products[req.params.name];
    res.json({price: product_price});
});

app.delete('/products/:name', (req, res) => {
    delete products[req.params.name];
    res.json({response: 'deleted'});
});

app.post('/products/:name', (req, res) => {
    name=req.params.name;
    price=req.body.price;
    products[name]=price;
    res.json({response:'success'});
});

app.post('/products/:name/add', (req, res) => {
    name=req.params.name;
    price=req.body.price;
    products[name]=price;
    res.json({response:'success'});
});


port=3000;
app.listen(port,'localhost', () => {
    console.log(`server is listening on port ${port}`)
});