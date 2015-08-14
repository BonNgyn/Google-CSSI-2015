function takeANumber(line, name){
  line.push(name);
  console.log("You are number: " + line.length);
  return line.length;
}

function nowServing(line) {
  if(line.length == 0){
    console.log("There is no one waiting to be served!");
  } else {
    console.log("Now serving " + line.splice(0,1));
  }
}

function line(line) {
  console.log("The line is currently: ");
  for(var i=0; i<line.length; i++) {
    var name = ((i+1) + "." + " " + line[i]);
  }
}

function spot(line, name) {
  for(var i=0; i<line.length; i++) {
    if(line[i] == name){
      return (i+1);
    }
  }
  console.log("You are not in the line.");

}
