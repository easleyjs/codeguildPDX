function customCoin (coinName, coinAmount, coins) {
	coins[coinName] = coinAmount
	return coins
}

function makeChange(totalAmount, coins) {
	remainderAmt = totalAmount
	coinObjArr = []

	valueList = Object.values(coins).sort((a,b) => {return b - a}) // Creates a descending array of coin values
	valueList.forEach(elem => {
		amtInt = Math.floor(remainderAmt / elem)
		remainderAmt -= amtInt * elem

		Object.keys(coins).forEach(coin => {
			if (coins[coin] === elem) {
				coinObjArr.push({ name:coin, amount:amtInt }) //need to do change computation above
			}
		})
	})
	return coinObjArr
}

const coins = {
	quarters:25,
	dimes:10,
	nickels:5,
	pennies: 1
}

//Display results/change to output div
document.addEventListener("keyup", (evt) => {
	outputDiv = document.querySelector("#output_div")
	outputDiv.innerHTML = ""
	amtInput = document.querySelector("#cash_amt").value
	changeObjs = makeChange(amtInput, coins)
	changeObjs.forEach(elem => {
		outputDiv.innerHTML += '<p class="results">' + elem.amount + " " + elem.name + "</p>"
	})

})
