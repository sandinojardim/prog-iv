var message = "in global";
console.log("global: message = " + message);

var a = function () {
  var message = "inside a";
  console.log("a: message = " + message);

  function b () {
    message = "inside b";
    console.log("b: message = " + message);
  }

  b();
  console.log("a: message2 = " + message);
}

a();
console.log("global: message2 = " + message);
