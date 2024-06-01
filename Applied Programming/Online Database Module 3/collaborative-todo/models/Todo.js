// Import Mongoose
const mongoose = require('mongoose');

const TodoSchema = new mongoose.Schema({
    title:{
        type: String,
        required: true,
    },
    completed: {
        type: Boolean,
        default: false,
    },
    createdAt:{
        type: Date,
        defautl: Date.now,
    }
});


// Create the To-Do Model
// A model is created from the schema. It will be used to create and read documents in the database.


// Export the model
// This makes the model available to other parts of our application.
module.exports = mongoose.model('Todo', TodoSchema);