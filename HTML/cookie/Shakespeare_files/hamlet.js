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
  var rollOne = Math.round(Math.random()*6)+1;
  var rollTwo = Math.round(Math.random()*6)+1;

  console.log(rollOne + " " + rollTwo);
}
