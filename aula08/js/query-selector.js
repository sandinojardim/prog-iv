// querySelector only returns the first match.

el.className = 'cool';
// querySelectorAll returns a NodeList.
// The third li element is then selected and changed.
var els = document.querySelectorAll('li.hot');
els[2].className = 'cool';