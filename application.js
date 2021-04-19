var canvas = document.querySelector('canvas');

canvas.width = window.innerWidth - 150;
canvas.height = 500;


var c = canvas.getContext('2d');

c.fillRect(100, 100, 100, 100);
console.log(canvas);