Vue.component('clock-face', {
  props: ['time'],
  data: function(){
    return{
      rawHour:"",
      rawMinutes:"",
      rawSeconds:"",
      minutes:"",
      hours:"",
      seconds:"",
      ampm:"",
    };
  },
  template: `<div id="clock">
              <span class="lcd number">{{ hours }}</span>
              <span class="lcd colon">:</span>
              <span class="lcd number">{{ minutes }}</span>
              <span class="lcd colon">:</span>
              <span class="lcd number">{{ seconds }}</span>
              <span id="ampm" class="lcd">{{ ampm }}</span>
            </div>
            `,
mounted(){
  this.clockUpdate();
  this.interval = setInterval(() => {
      this.clockUpdate();
  }, 1000);
  this.colonInterval = setInterval(() => {
    this.colonBlink();
  }, 900);
},
methods: {
    clockUpdate: function() {
      let now = new Date()
      //console.log(now.getHours())

      this.rawHour = parseInt(now.getHours())
      this.rawMinutes = now.getMinutes()
      this.rawSeconds = now.getSeconds()
      //console.log("0" + this.rawHour)

      this.hours = this.rawHour > 9 ? this.rawHour : "0" + this.rawHour
      this.minutes = this.rawMinutes > 9 ? this.rawMinutes : "0" + this.rawMinutes
      this.seconds = this.rawSeconds > 9 ? this.rawSeconds : "0" + this.rawSeconds
      this.ampm = this.rawHour > 12 ? "PM" : "AM"

    },
    colonBlink: function() {
      this.clockColons = document.querySelectorAll(".colon")
      //console.log(clockColons[0])
      this.clockColons.forEach((colon) => {
        //console.log(colon)
        if (colon.style.opacity === "0") {
          colon.style.opacity = "1"
        } else {
          colon.style.opacity = "0"
        }
      })
    }
}
});

var clockApp = new Vue({
  el: '#clock-app',
  data: {}
})
