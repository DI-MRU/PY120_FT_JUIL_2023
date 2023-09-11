const express = require("express");
const app = express();

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

app.get("/", (req, res) => {
  res.send(404);
});

app.get("/select-all", (req, res) => {
  knex
    .select()
    .from("actors")
    .then((actors) => res.send(actors));
});

app.get("/select-full-name", (req, res) => {
  knex
    .select("first_name", "last_name")
    .from("actors")
    .then((actors) => res.send(actors));
});

app.get("/select-age", (req, res) => {
  knex
    .select("age")
    .from("actors")
    .then((actors) => res.send(actors));
});

app.get("/select-matt", (req, res) => {
  knex("actors")
    .where({ first_name: "Matt" })
    .then((actors) => res.send(actors));
});

app.get("/select-matt-damon", (req, res) => {
  knex("actors")
    .where({ first_name: "Matt", last_name: "Damon" })
    .then((actors) => res.send(actors));
});

app.get("/select-oscars", (req, res) => {
  knex("actors")
    .where("number_oscars", ">=", 2)
    .then((actors) => res.send(actors));
});

app.get("/select-matt-or-angelina", (req, res) => {
  knex("actors")
    .where({ first_name: "Matt" })
    .orWhere({ first_name: "Angelina" })
    .then((actors) => res.send(actors));
});

app.get("/select-aniston-or-oscar-1", (req, res) => {
  knex("actors")
    .where({ last_name: "Aniston" })
    .orWhere("number_oscars", "=", 1)
    .then((actors) => res.send(actors));
});

app.get("/insert-gadot-1", (req, res) => {
  knex("actors")
    .returning(["actor_id", "first_name", "last_name"])
    .insert({
      first_name: "Gal",
      last_name: "Gadot",
      age: "1985-04-30",
      number_oscars: 0,
    })
    .then((actors) => res.send(actors));
});

app.get("/insert-gadot-2", (req, res) => {
  knex("actors")
    .insert(
      {
        first_name: "Gal",
        last_name: "Gadot",
        age: "1985-04-30",
        number_oscars: 0,
      },
      ["actor_id", "first_name", "last_name"]
    )
    .then((actors) => res.send(actors));
});

app.get("/insert-gadot-3", (req, res) => {
  knex("actors")
    .insert(
      {
        first_name: "Gal",
        last_name: "Gadot",
        age: "1985-04-30",
        number_oscars: 0,
      },
      ["*"]
    )
    .then((actors) => res.send(actors));
});

app.get("/update-gadot", (req, res) => {
  knex("actors")
    .where("first_name", "Gal")
    .andWhere("last_name", "Gadot")
    .update(
      {
        number_oscars: 2,
        age: "1985-04-29",
      },
      ["actor_id", "number_oscars"]
    )
    .then((actors) => res.send(actors));
});

app.get("/delete-gadot", (req, res) => {
  knex("actors")
    .where("first_name", "Gal")
    .andWhere("last_name", "Gadot")
    .del(["actor_id", "first_name", "last_name"])
    .then((actors) => res.send(actors));
});

module.exports = app;
