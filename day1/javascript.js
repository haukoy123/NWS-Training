// REVIEW chung:
/**
 * Vẫn còn nhiều khoảng trắng thừa
 * Với các toán tử (+, -, *, /, v.v.), giữa 2 đầu vẫn chưa có dấu cách
 */

// Day 1: Arithmetic Operators

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
	inputString += inputStdin;
});

process.stdin.on('end', _ => {
	inputString = inputString.trim().split('\n').map(string => {
	return string.trim();
	});

	main();
});

function readLine() {
	return inputString[currentLine++];
}

function getArea(length, width) {
	let area;
	area = length * width
	return area;
}

function getPerimeter(length, width) {
	let perimeter;
	perimeter = (length + width) * 2
	return perimeter;
}





// Day 1: Functions

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
	inputString += inputStdin;
});

process.stdin.on('end', _ => {
	inputString = inputString.trim().split('\n').map(string => {
	return string.trim();
	});

	main();
});

function readLine() {
	return inputString[currentLine++];
}

function factorial(n){
	var result = 1;
	for (var i = n; i > 0; i--){  // REVIEW: xóa dấu cách trước kí tự ";"
	result *= i;
	}
	return result;
}

function main() {
	const n = +(readLine());

	console.log(factorial(n));
}




// Day 1: Let and Const

'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
	inputString += inputStdin;
});

process.stdin.on('end', _ => {
	inputString = inputString.trim().split('\n').map(string => {
	return string.trim();
	});

	main();
});

function readLine() {
	return inputString[currentLine++];
}

function main() {
	const PI = Math.PI;
	let r = readLine();
	console.log(PI * (Math.pow(r, 2))) // REVIEW: giữa 2 đầu toán tử phải có dấu cách, thừa dấu cách sau số "2"
	console.log(2 * PI * r)
	try {
	// REVIEW: code trong 1 block phải lùi vào 1 level, tương tự với block "catch"
		PI = 0;
		console.log(PI);
	} catch(error) {
		console.error("You correctly declared 'PI' as a constant.");
	}
}
