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
  addTask = (name, displayList) => {
    this.todos.push(new ToDoTask(name))
  }
  getTaskList = () => {
    return this.todos
  }
  createTaskElem (name, idx, displayList) {
    let taskItem = document.createElement("li")
    taskItem.innerHTML = name
    taskItem.setAttribute("idx", idx)  // need to look at how to get array index #
    const deleteBtn = document.createElement("a")
    const toggleBtn = document.createElement("a")
    deleteBtn.innerHTML = '<i class="fas fa-times"></i>'
    deleteBtn.setAttribute('class', 'delete')
    toggleBtn.innerHTML = '<i class="fas fa-check"></i>'
    toggleBtn.setAttribute('class', 'toggle')

    taskItem.appendChild(deleteBtn)
    taskItem.appendChild(toggleBtn)

    // btn event listeners
    deleteBtn.addEventListener('click', (evt) => {
      const li = evt.target.closest('li')
      const idx = parseInt(li.getAttribute('idx'))
      //todoList.deleteTodo(idx)
      myToDos.removeTask(idx)
      //update(todoList)
    })

    toggleBtn.addEventListener('click', (evt) => {
      const li = evt.target.closest('li')
      const idx = li.getAttribute('idx')
      this.toggleTask(idx)
    })
    return taskItem
    //displayList.insertBefore( taskItem, displayList.childNodes[0] );
  }

  toggleTask = (idx) => {
    const elem = document.querySelector("li[idx='"+idx+"']")
    elem.classList.toggle("completed")
    this.todos[idx].complete = !this.todos[idx].complete
  }

  removeTask = (idx) => {
    //document.QuerySelectorAll("*[data-sigil='some_thing']");
    const elem = document.querySelector("li[idx='"+idx+"']")
    elem.parentNode.removeChild(elem)
    this.todos.splice(idx,1)
  }

  displayTasks = (displayList) => {
    displayList.innerHTML = ''
    this.getTaskList().forEach((todo, idx) => {
      let taskItem = this.createTaskElem (todo.name, idx, displayList)
      displayList.insertBefore( taskItem, displayList.childNodes[0] );
    })
  }

}
      //might need parentNode later.

const myToDos = new ToDoList()
const inputField = document.querySelector("#to_do")
const displayList = document.querySelector("#task_list")

inputField.addEventListener("keyup", (evt) => {
  //console.log(evt.code)
  if (evt.code === "Enter") {
    myToDos.addTask(inputField.value, displayList);
    inputField.value = ''
    myToDos.displayTasks(displayList);
  }
})
