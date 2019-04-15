let now = new Date();
const clockColons = document.querySelectorAll(".colon")
const clockHours = document.querySelector("#clock-hours")
const clockAmpm = document.querySelector("#clock-ampm")
const clockMinutes = document.querySelector("#clock-minutes")
const clockSeconds = document.querySelector("#clock-seconds")
let ctr = 1;

function clockUpdate() {
    clockColons.forEach((colon) => {
      if (colon.style.opacity === "0") {
        colon.style.opacity = "1"
      } else {
        colon.style.opacity = "0"
      }
    })
    /*
    if (ctr === 0) {
      now.setSeconds(now.getSeconds() +1)
      setCurrentTime();
      ctr += 1
    } else {
      ctr--
    }
    */
    setTimeout(clockUpdate,500)
}

function setCurrentTime() {
  let now = new Date();
  let currentHour = now.getHours()
  let currentMinutes = now.getMinutes()
  let currentSeconds = now.getSeconds()

  if (currentHour > 12) {
    currentHour -= 12
    clockAmpm.innerText = "PM"
  } else {
    clockAmpm.innerText = "AM"
  }
  currentHour = currentHour >= 10 ? currentHour : 0 + currentHour
  clockHours.innerText = currentHour
  clockMinutes.innerText = currentMinutes >= 10 ? currentMinutes : "0"+currentMinutes
  clockSeconds.innerText = currentSeconds >= 10 ? currentSeconds : "0"+currentSeconds

}
setInterval(setCurrentTime,1000);
