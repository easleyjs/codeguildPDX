class ToDoTask {
  constructor (name) {
    this.name = name
    this.complete = false
  }
}
class ToDoList {
  constructor () {
    this.todos = []
  }
  addTask = (name) => {
    this.todos.push(new ToDoTask(name))
    let taskItem = document.createElement("li")
    taskItem.innerHTML = name
    taskItem.setAttribute("idx", XX)  // need to look at how to get array index #
    return taskItem
  }
  removeTask = (idx) => {
    const elem = document.querySelector("li#"+idx)
    elem.parentNode.removeChild(elem)
    this.todos.splice(idx,1)
  }
}

const myToDos = new ToDoList()
const inputField = document.querySelector("#to_do")

inputField.addEventListener("keyup", (evt) => {
  console.log(evt.code)
  if (evt.code === "Enter") {
    inputField.parentNode.insertBefore( myToDos.addTask(inputField.value), inputField.nextSibling );

  }
})
