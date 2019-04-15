function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
}

const urls = []
urls.push("http://www.burningman.com")
urls.push("http://www.wizardsofthecoast.com")
urls.push("http://www.slashdot.org")
urls.push("http://www.etsy.com")

statusMsgSpan = document.querySelector("#status-message")
let counter = 5

//Version 2: Countdown from five, then redirect to a random page in the array.
let countdownToWindowRedirect = () => {
  if (counter === 0) {
    statusMsgSpan.innerText = "Redirecting..."
    window.location = urls[getRandomIntInclusive(0,urls.length-1)]
    console.log("Done.")
  } else {
    console.log(counter)
    statusMsgSpan.innerText = "You will be redirected to the random page in " + counter + " seconds.."
    counter--
    setTimeout(countdown, 1000)
  }
}

//countdownToWindowRedirect();

//Version 3: iframe StumbleUpon clone.
//https://cors-anywhere.herokuapp.com/http://example.com

const myFrame = document.querySelector("iframe")

const responseToJSON = async (url) => {
    try {
        const res = await fetch(url)
        const json = await res.json()
        console.log(json)
        //myFrame.inner
        //factElem.innerText = json.text
        //sourceElem.innerText = json.source
        //sourceElem.href = json.source_url
    } catch (err) {
        console.log(err)
    }
}

responseToJSON("https://cors-anywhere.herokuapp.com/https://www.google.com");
