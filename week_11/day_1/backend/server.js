const express = require("express");
const BodyParser = require("body-parser");
const cors = require("cors");
// const { Pool } = require("pg");
const dotenv = require('dotenv');
const mongoose = require('mongoose')

dotenv.config()

const app = express();

// env
const url = process.env.URL

// connection to mongodb
mongoose.connect(url, {
   useNewUrlParser: true,
   useUnifiedTopology: true
});

const studentSchema = {
    name : String,
    age : Number
}
const student = mongoose.model("Student", studentSchema);

// Connection to database
// const pool = new Pool({
//   user: "postgres",
//   host: "localhost",
//   database: "postgres",
//   password: "8462",
//   port: 5432,
// });

// Middleware
app.use(BodyParser.json());
app.use(cors());

app.post("/add-student", async (req, res) => {
  const { name, age } = req.body;
  try {
    // const query = "INSERT INTO student (name,age) VALUES($1,$2)";
    // await pool.query(query, [name, age]);
    const NewStudent = new student ({name,age});
    await NewStudent.save()
    res.status(200).json({ message: "successful" });
  } catch (err) {
    console.error(error);
    res.status(500).json({ message: "No connection" });
  }
});

app.listen(2000, () => {
  console.log("Ze p tender moii");
});
