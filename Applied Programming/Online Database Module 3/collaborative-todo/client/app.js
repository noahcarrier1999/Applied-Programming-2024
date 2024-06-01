const socket = io('http://localhost:3000');

socket.on('todoCreated', (todo) => {
  addTodoToList(todo);
});

socket.on('todoUpdated', (updatedTodo) => {
  updateTodoInList(updatedTodo);
});

socket.on('todoDeleted', (id) => {
  removeTodoFromList(id);
});

function addTodo() {
  const newTodoInput = document.getElementById('new-todo');
  const title = newTodoInput.value;

  fetch('http://localhost:3000/todos', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ title })
  }).then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(todo => {
    newTodoInput.value = '';  // Clear the input after adding
    // The new to-do will be added by the 'todoCreated' event listener
  })
  .catch(error => console.error('Error:', error));
}

function addTodoToList(todo) {
  const todoList = document.getElementById('todo-list');
  const listItem = document.createElement('li');
  listItem.id = todo._id;
  listItem.innerHTML = `
    <input type="checkbox" ${todo.completed ? 'checked' : ''} onclick="toggleComplete('${todo._id}', this.checked)">
    ${todo.title}
    <button onclick="deleteTodo('${todo._id}')">X</button>
  `;
  todoList.appendChild(listItem);
}

function updateTodoInList(updatedTodo) {
  const listItem = document.getElementById(updatedTodo._id);
  if (listItem) {
    listItem.innerHTML = `
      <input type="checkbox" ${updatedTodo.completed ? 'checked' : ''} onclick="toggleComplete('${updatedTodo._id}', this.checked)">
      ${updatedTodo.title}
      <button onclick="deleteTodo('${updatedTodo._id}')">X</button>
    `;
  }
}

function removeTodoFromList(id) {
  const listItem = document.getElementById(id);
  if (listItem) {
    listItem.remove();
  }
}

function toggleComplete(id, completed) {
  fetch(`http://localhost:3000/todos/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ completed })
  }).then(response => response.json())
    .then(updatedTodo => {
      const listItem = document.getElementById(updatedTodo._id);
      if (listItem) {
        listItem.style.textDecoration = updatedTodo.completed ? 'line-through' : 'none';
      }
    });
}

function deleteTodo(id) {
  fetch(`http://localhost:3000/todos/${id}`, {
    method: 'DELETE'
  }).then(() => {
    removeTodoFromList(id);
  });
}
