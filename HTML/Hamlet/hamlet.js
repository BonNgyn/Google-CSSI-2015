var isRobAwesome = "YES";
var colorOfRobShirt = "yellow";

console.log("Hello World!");
console.log("And all our yesterdays are lighted fools");
console.log("The way to dusty death");
console.log("Out, out brief candle " + isRobAwesome);

function checkout(item1, item2, coupon) {
  var subtotal = item1 + item2;
  subtotal = subtotal * (1-coupon);
  var total = subtotal * 1.06;

  return total;
}

function goToLunch(name) {
  alert("Lunch Time!");
  alert("Close your computer, " + name);
  console.log("Let's eat food");
}

function newCheckout(item1, item2) {
  var total = item1 + item2;
  total = total * 1.095;
  total = Math.round(total*100)/100

  alert("Your Total Is: " + total);
  return total;
}

function roll() {
  var roll = Math.round(Math.random()*6)+1;
  return roll;
}

function rollTwo() {
  var rollOne = roll();
  var rollTwo = roll();

  console.log(rollOne + " " + rollTwo);
}

function howAmIDoing(gpa, isFootballPlayer, needToGetIntoGradSchool) {
  if(gpa >= 4.0) {
    alert("I am so awesome");
  } else if(gpa >=3.0 || !needToGetIntoGradSchool || isFootballPlayer) {
    console.log("Better get a job");
  } else if (gpa >=3.0) {
    alert("Not too shabby");
  } else if (isFootballPlayer == true){
    alert("I'm happy either way");
  } else {
    alert("I need to study");
  }
}


var numbers = [2, 3, 5, 7, 11, 13, 17, 23];
var i = 0;
while(i < numbers.length) {
  numbers[i] = numbers[i] + 1;
  i++;
}

//write a function that takes an array "arr" as an argument, and multiplie each element in the array by 2

function multByTwo(arr) {
  var i = 0;
  while(i < arr.length) {
    arr[i] = arr[i] * 2;
    i++;
  }
  return arr;
}
function multByFortyTwo(arr) {
  for(var i=0; i<arr.length; i++) {
    arr[i] = arr[i] * 42;
    return arr;
  }
}
