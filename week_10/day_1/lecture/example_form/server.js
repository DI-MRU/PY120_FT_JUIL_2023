// Server init
const express = require("express");
const bp = require("body-parser");
const path = require("path");

const app = express();
app.use(bp.urlencoded({ extended: false }));
app.use(bp.json());

app.use(express.static("public"));
app.use("/static", express.static(path.join(__dirname, "public")));
app.listen(
  5000,
  console.log("Just the app is listening on http://127.0.0.1:5000")
);

const knex = require("knex")({
  client: "pg",
  version: "7.2",
  connection: {
    host: "127.0.0.1",
    user: "postgres",
    password: "postgres",
    database: "wk10db",
    port: 5432,
  },
});

// Routing
app.get("/", (req, res) => {
  res.sendFile(express.static(path.join(__dirname, "./public", "index.html")));
});

app.post("/", (req, res) => {
  console.log(req.body.tamagotchi_name);
  knex("tamagotchis")
    .insert({
      name: req.body.tamagotchi_name,
      age: 0,
    })
    .then((tamatgotchi) =>
      res.sendFile("public/index.html", { root: __dirname })
    );
});

app.get("/init-db", (req, res) => {
  knex.schema
    .createTable("tamagotchis", function (table) {
      table.increments();
      table.timestamps();
      table.string("name");
      table.integer("age");
    })
    .then(() => console.log("Table created"));
  res.sendStatus(200);
});

app.get("/api/v1/tamagotchis", (req, res) => {
  knex("tamagotchis")
    .select()
    .then((tamagotchis) => res.status(200).json(tamagotchis));
});
