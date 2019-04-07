/*
Ported from Python Lab 18 - Peaks and Valleys

"""
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
"""

def peaks(data):
    """
    >>> print(peaks(data))
    [6, 14]
    """
    return [i for i in range(1, len(data)-1) if (data[i] > data[i-1]) & (data[i] > data[i+1])]


def valleys(data):
    """
    >>> print(valleys(data))
    [9, 17]
    """
    return [i for i in range(1, len(data)-1) if (data[i] < data[i-1]) & (data[i] < data[i+1])]

*/
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] // peak(7) and peak(15)

function peaks(data) {
  // will replace this with a filter method..
  peaksArr = []
  for (let i=1;i<data.length-1;i++) {
    if (data[i] > data[i-1] && data[i] > data[i+1]) {
      peaksArr.push({x:i, y:data[i]-1})
    }
  }
  return peaksArr
}

function drawElements(inputArr, type) {
  for (let i=0;i<inputArr.length;i++) {
    //get CSS classes of block at the coords, if type is peak or valley, remove fill class.
    
    setGridElement(inputArr[i].x, inputArr[i].y, type)
  }
}
///// to do..
function valleys(data) {
  //return [i for i in range(1, len(data)-1) if (data[i] < data[i-1]) & (data[i] < data[i+1])]
  //to be replaced w/ filter
  // will replace this with a filter method..
  valleyArr = []
  for (let i=1;i<data.length-1;i++) {
    if (data[i] < data[i-1] && data[i] < data[i+1]) {
      valleyArr.push({x:i, y:data[i]-1})
    }
  }
  return valleyArr
}

function setGridElement (gridX, gridY, elemType) {
  gridElementDiv = document.querySelector("#row" + gridY + "col" + gridX)
  gridElementDiv.classList.add(elemType)
}

const outputDiv = document.querySelector("#output_div")
for (let i=8;i>=0;i--){
  outputDiv.innerHTML += '<div id="row' + i + '" class="row"></div>'
  let outputRowDiv = document.querySelector("#row"+i)
  for (let x = 0; x < 20; x++) {
     outputRowDiv.innerHTML += '<div id="row' + i + 'col' + x + '" class="col"></div>'
  }
}

//setGridElement(1,0,"fill");
//setGridElement(1,1,"water");
drawElements(peaks(data), "peak")
drawElements(valleys(data), "valley")
