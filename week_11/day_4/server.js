const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
// const { Pool } = require("pg");
const dotenv = require("dotenv");
const mongoose = require("mongoose");
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");

dotenv.config();
const app = express();

// const pool = new Pool({
//   user: "postgres",
//   host: "localhost",
//   database: "postgres",
//   password: "8462",
//   port: 5432,
// });
const url = process.env.URL;
mongoose.connect(url, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const registerSchema = new mongoose.Schema({
  username: String,
  password: String,
});
const db = mongoose.connection;
db.on("error", console.error.bind(console, "MongoDB connection Failed"));
db.once("open", () => {
  console.log("connected to MongoDB");
});

registerSchema.pre("save", async function (next) {
  try {
    if (!this.isModified("password")) {
      return next();
    }
    const hash = await bcrypt.hash(this.password, 10);
    this.password = hash;
    next();
  } catch (err) {
    next(err);
  }
});
const register = mongoose.model("register", registerSchema);
app.use(bodyParser.json());
app.use(cors());

app.post("/register", async (req, res) => {
  const { username, password } = req.body;
  try {
    // const query = "INSERT INTO register (username,password) VALUES ($1,$2)";
    // const hashPassword = await bcrypt.hash(password, 10);
    // await pool.query(query, [username, hashPassword]);
    const newRegister = new register({ username, password });
    await newRegister.save();
    res.status(200).json({ message: "User registered successfully" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "User register Failed" });
  }
});

app.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    // const result = await pool.query(
    //   "SELECT * FROM register WHERE username = $1",
    //   [username]
    // );
    // if (result.rowCount === 0) {
    //   res.status(400).json({ message: "User not found" });
    //   return;
    // }
    // const table = result.rows[0];
    // const passwordCompared = await bcrypt.compare(password, table.password);

    // if (!passwordCompared) {
    //   res.status(400).json({ message: "Password incorrect" });
    //   return;
    // }
    const user = await register.findOne({ username });
    if (!user) {
      res.status(400).json({ message: "User not found" });
      return;
    }
    const passwordCompared = await bcrypt.compare(password, user.password);

    if (!passwordCompared) {
      res.status(400).json({ message: "Password incorrect" });
      return;
    }
     const token = jwt.sign({ username: user.username }, process.env.JWT_TOKEN);
    // const token = jwt.sign({ username: table.username }, process.env.JWT_TOKEN);
    res.json({ token });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Internal error" });
  }
});

app.listen(5000, () => {
  console.log("The server is running catch it!");
});
