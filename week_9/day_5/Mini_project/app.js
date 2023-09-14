const express = require("express");
const fs = require("fs");
const bodyPaser = require("body-parser");

const app = express();
const Router = require("./routes/routes")


app.use(bodyPaser.json());
app.use("/tasks",Router)
app.listen(3000,() => {
    console.log("server is running")
})