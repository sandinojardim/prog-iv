// Arrays
// var array = new Array();
// array[0] = "Tiago";
// array[1] = 2;
// array[2] = function (name) {
//   console.log("Hello " + name);
// };
// array[3] = {course: " HTML, CSS & JS"};
//
// console.log(array);
// array[2](array[0]);
// console.log(array[3].course);


// Short hand array creation
var names = ["Tiago", "João", "José"];
console.log(names);

for (var i = 0; i < names.length; i++) {
  console.log("Hello " + names[i]);
}

names[100] = "Jim";
for (var i = 0; i < names.length; i++) {
  console.log("Hello " + names[i]);
}
