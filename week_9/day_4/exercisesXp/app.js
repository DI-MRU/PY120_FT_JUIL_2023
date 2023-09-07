const express = require('express');
const app = express();
const port = 1999;
const router = require('./routes/index');

app.use(express.json())
app.use('/todos',router);
app.listen(port,()=>{
    console.log(`server is running on http://localhost:${port}/`)
})