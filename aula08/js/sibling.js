// Select the starting point and find its siblings.
var startItem = document.getElementById('three');
var prevItem = startItem.previousSibling;
var nextItem = startItem.nextSibling;
// Change the values of the siblings' class attributes.
prevItem.className = 'complete';
nextItem.className = 'cool';
