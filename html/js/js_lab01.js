/*
shouldStop = False

while shouldStop not true:
    importantName = input('Name of an important person: ')
    adjectives = input('Three Gross Adjectives (comma separated): ').split(',')
    place = input('Place on Earth: ')

    print("We're looking for a few " + adjectives[0] + ", " + adjectives[1] + ", " + adjectives[2] + " " + importantName + "s " + "to join us in taking over " + place + " this winter!!")
    playAgain = input('Would you like to play again? (yes/no): ')
    if playAgain === 'yes':
        shouldStop = True

*/

document.addEventListener("keyup", function(){
  const mad_lib_arr = []
  mad_lib_arr.push(document.getElementById('name').value)
  mad_lib_arr.push(...document.getElementById('gross_acros').value.split(','))
  mad_lib_arr.push(document.getElementById('place').value)
  document.getElementById("output").innerHTML = `We're looking for a few ${mad_lib_arr[1]}, ${mad_lib_arr[2]}, ${mad_lib_arr[3]} ${mad_lib_arr[0]}s to join us in taking over ${mad_lib_arr[4]} this winter!`
});
