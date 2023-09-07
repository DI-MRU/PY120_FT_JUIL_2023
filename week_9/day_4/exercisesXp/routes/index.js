const express = require("express");
const router = express.Router();

// router.get('/', (req,res) => {
//     res.send('Homepage');
// });

// router.get('/about', (req,res) => {
//     res.send('About Us Page');
// });

const todos = [];

// Get all to-do-items
router.get("/", (req, res) => {
  res.json(todos);
});

router.post("/", (req, res) => {
  const { task, completed } = req.body;
  if (!task) {
    return res.status(404).json({ error: "Task is required" });
  }

  const newTask = {
    id: todos.length + 1,
    task,
    completed: completed || false,
  };
  todos.push(newTask);
  res.status(201).json(newTask);
});

// Update 
router.put("/:id", (req,res)=> {
    const { id } = req.params;
    const { task, completed } = req.body;

    const todo = todos.find((t) => t.id === parseInt(id));
    if (!todo){
        return  res.status(404).json({error : "The To-Do took an L"});
    };
    if (task !== undefined){
        todo.task = task;
    };
    if (completed !== undefined){
        todo.completed = completed;
    };
    res.json({ message: 'To-do item updated successfully', data: todo})
});

// Delete
router.delete("/:id", (req, res) => {
  const { id } = req.params;

  const index = todos.findIndex((t) => t.id === parseInt(id));
  if (index === -1) {
    return res.status(404).json({ error: "To-do not found" });
  }

  todos.splice(index, 1);
  res.status(204).json({ message: "To-do item deleted successfully" });
});


module.exports = router;
