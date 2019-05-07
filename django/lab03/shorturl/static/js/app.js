const urlInput = document.querySelector("#long-url")
urlInput.onfocus = () => {
  urlInput.value = ''
  urlInput.style.color = "black"
  urlInput.style.background = "lightyellow"
}
urlInput.onblur = () => {
  urlInput.value = 'Enter a URL ..'
  urlInput.style.color = "lightgrey"
  urlInput.style.background = "white";
}

const shortUrlContainer = document.querySelector("#content")
function writeShortUrlToLink (container, shortUrl) {
  //console.log("short url: " + shortUrl)
  shortUrlLink = "http://localhost:8000/" + shortUrl + "/"
  container.innerHTML = ''
  container.innerHTML = "<p>Your short URL is: </p>"
  let urlLink = document.createElement("a")
  urlLink.href = shortUrlLink
  urlLink.value = shortUrlLink
  urlLink.innerHTML = shortUrlLink
  container.appendChild(urlLink)
}

//Post needs to send "longUrl"
longUrlInput = document.querySelector("#long-url")

longUrlInput.addEventListener("keyup", (evt) => {
  //do an ajax call and pass todoInput.value
  if (evt.keyCode == 13) {
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: '/',
      data: {
        longUrl: longUrlInput.value,
        csrfmiddlewaretoken: csrftoken,
      },
      success: function(response){
        writeShortUrlToLink (shortUrlContainer, response.short_url)
      },
    });

    urlInput.value = "Enter a URL.."
    urlInput.style.color = "lightgrey"
    urlInput.style.background = "white"

  }
})
