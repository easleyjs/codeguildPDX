document.addEventListener("keyup", function(){
  const mad_lib_arr = []
  mad_lib_arr.push(document.getElementById('name').value)
  mad_lib_arr.push(...document.getElementById('gross_acros').value.split(','))
  mad_lib_arr.push(document.getElementById('place').value)
  document.getElementById("output").innerHTML = `We're looking for a few ${mad_lib_arr[1]}, ${mad_lib_arr[2]}, ${mad_lib_arr[3]} ${mad_lib_arr[0]}s to join us in taking over ${mad_lib_arr[4]} this winter!`
});
