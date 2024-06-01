const express = require("express");
const http = require("http");
const socketIo = require("socket.io");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
const server = http.createServer(app);
const io = socketIo(server,{
  cors:{
    origin:"http://127.0.0.1:5500",
    methods: ["GET","POST","PUT","DELETE"]
  }
});
const PORT = process.env.PORT || 3000;

// MongoDB connection
mongoose
  .connect("mongodb+srv://noahcarrier:Iaacog12@cluster0.711y1vu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get("/", (request, response) => {
  response.send("Hello World");
});

// Socket.io connection
io.on("connection", (socket) => {
  console.log("New client connected");

  socket.on("disconnect", () => {
    console.log("Client disconnected");
  });
});

const Todo = require('./models/Todo');

// Get all to-dos
app.get('/todos', async (req, res) => {
  try {
    const todos = await Todo.find();
    res.json(todos);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Create a new to-do
app.post('/todos', async (req, res) => {
  try {
    const newTodo = new Todo({
      title: req.body.title
    });
    const todo = await newTodo.save();
    io.emit("todoCreated", todo);
    res.status(201).json(todo);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a to-do
app.put("/todos/:id", async (req, res) => {
  try {
    const updatedTodo = await Todo.findByIdAndUpdate(
      req.params.id,
      { completed: req.body.completed },
      { new: true }
    );
    io.emit('todoUpdated', updatedTodo);
    res.json(updatedTodo);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete a to-do
app.delete("/todos/:id", async (req, res) => {
  try {
    await Todo.findByIdAndDelete(req.params.id);
    io.emit('todoDeleted', req.params.id);
    res.json({ message: "To-do deleted" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
