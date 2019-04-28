// HTTP GET todo records from DB. Append to div container.
const todoContainer = document.querySelector("#todo-container")
function writeTodosToDiv (container, todosArr) {
  container.innerHTML = ""
  todosArr.forEach(function(todo) {
    let todoDiv = document.createElement("div")
    todoDiv.classList.add("todo-div")
    let todoText = document.createElement("span")
    let todoComplete = document.createElement("span")
    let todoDate = document.createElement("span")
    todoDate.classList.add("todo-date")
    let todoDelete = document.createElement("span")
    todoText.innerHTML = todo.text
    todoText.classList.add('todo-text')
    if (todo.completed) {
        todoComplete.innerHTML = '<i class="fas fa-undo"></i>'
        todoText.classList.toggle("completed")
    }else{
        todoComplete.innerHTML = '<i class="fas fa-check"></i>'
    }
    todoComplete.setAttribute('pk',todo.pk)
    todoComplete.classList.add('todo-complete')
    todoComplete.addEventListener("click", (e) => {
      const clickedNode = e.currentTarget
      //get pk from parentNode
      const pk = clickedNode.getAttribute("pk")
      //send to django toggle view
      const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
      $.ajax({
        type: "POST",
        url: 'toggle/'+pk+'/',
        data: {
          csrfmiddlewaretoken: csrftoken,
        },
        success: function(response){
          console.log(response)
          //update class based on current todo.completed
          // if task is complete, change "undo" to check.
          // if task is incomplete, change "check" to undo.
          clickedNode.firstChild.classList.toggle("fa-undo")
          clickedNode.firstChild.classList.toggle("fa-check")
          clickedNode.parentNode.childNodes[1].classList.toggle("completed")
        },
      });

    })
    todoDate.innerHTML = todo.created_date
    todoDelete.innerHTML = '<i class="fas fa-times"></i>'
    todoDelete.classList.add('todo-delete')
    todoDelete.setAttribute('pk',todo.pk)
    todoDelete.addEventListener("click",(e) => {
        const clickedNode = e.currentTarget
        //get pk
        const pk = clickedNode.getAttribute("pk")
        //send to django delete view
        const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
          type: "POST",
          url: 'delete/'+pk+'/',
          data: {
            csrfmiddlewaretoken: csrftoken,
          },
          success: function(response){
            console.log(response)
            //remove element from DOM
            const parentNodeElem = clickedNode.parentNode
            clickedNode.parentNode.removeChild(clickedNode)
            parentNodeElem.parentNode.removeChild(parentNodeElem)
          },
        });

    })
    todoDiv.appendChild(todoDate)
    todoDiv.appendChild(todoText)
    todoDiv.appendChild(todoComplete)
    todoDiv.appendChild(todoDelete)
    container.appendChild(todoDiv)
  });
}
function getTodoListFromApi () {
  let todoItemArr = ""
  $.ajax({
    type: 'GET',
    url: 'list/',
    success: (data) => {
      writeTodosToDiv (todoContainer, data.todos_list)
      console.log(data.todos_list)
      console.log("Successfully retrieved: " + data.todos_list.length + " records.")
    },
  });
}
const todoInput = document.querySelector("#todo-input")
todoInput.onfocus = () => {
  todoInput.value = ''
  todoInput.style.color = "black"
  todoInput.style.background = "lightyellow"
}
todoInput.onblur = () => {
  todoInput.value = 'Enter a new task..'
  todoInput.style.color = "lightgrey"
  todoInput.style.background = "white";
}
todoInput.addEventListener("keyup", (evt) => {
  //do an ajax call and pass todoInput.value
  if (evt.keyCode == 13) {
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: 'add/',
      data: {
        todoInput: todoInput.value,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function(response){
        console.log(response)
        getTodoListFromApi()
      },
    });
    todoInput.value = "Enter a new task.."
    todoInput.style.color = "lightgrey"
    todoInput.style.background = "white"
  }
})

document.onready = getTodoListFromApi()
