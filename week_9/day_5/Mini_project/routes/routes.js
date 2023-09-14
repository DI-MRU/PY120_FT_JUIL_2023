const express = require("express");
const router = express.Router();
const fs = require("fs");

const path = "./task.json"

router.get("/", (req,res) => {
    fs.readFile(path,"utf-8",(err,data) => {
        if (err){
            return res.status(404).json({error : "Error not found"})
        }
        const tasks = JSON.parse(data);
        res.json(tasks);
    })
})

router.post("/", (req,res) => {
    const newTask = req.body;
    
    if(!newTask.task || !newTask.description){
        return res.status(400).json({ error : "li Pas exister"})
    }
    fs.readFile(path,"utf-8",(err,data) => {
        if (err){
            return res.status(404).json({error : "Error not found"})
        }
        const tasks = JSON.parse(data);

        const maxId = tasks.reduce(
            (max, task) => (parseInt(task.id) > max ? parseInt(task.id) : max),
            0
          );
          newTask.id = (maxId + 1).toString();
      
          tasks.push(newTask);
      
          fs.writeFile(path, JSON.stringify(tasks), (err) => {
            if (err) {
              return res.status(500).json({ error: err.message });
            }
            res.status(201).json(newTask);
          });
        });
      });


module.exports = router;