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
  }
  removeTask = (idx) => {
    const elem = document.querySelector("li#"+idx)
    elem.parentNode.removeChild(elem)
    this.todos.splice(idx,1)
  }
  displayTasks = (displayList) => {
    displayList.innerHTML = ''
    this.todos.forEach((todo, idx) => {
      let taskItem = document.createElement("li")
      taskItem.innerHTML = todo.name
      taskItem.setAttribute("idx", idx)  // need to look at how to get array index #
      const deleteElement = document.createElement("a")
      const toggleElement = document.createElement("a")
      deleteBtn.innerHTML = '<i class="fas fa-times"></i>'
      deleteBtn.setAttribute('class', 'delete')
      toggleBtn.innerHTML = '<i class="fas fa-check"></i>'
      toggleBtn.setAttribute('class', 'toggle')
      
      displayList.insertBefore( taskItem, displayList.childNodes[0] );
      //might need parentNode later.
    })
  }
}

const myToDos = new ToDoList()
const inputField = document.querySelector("#to_do")
const displayList = document.querySelector("#task_list")

inputField.addEventListener("keyup", (evt) => {
  //console.log(evt.code)
  if (evt.code === "Enter") {
    myToDos.addTask(inputField.value);
    myToDos.displayTasks(displayList);
  }
})
