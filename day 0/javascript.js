// Day 0: Hello, World!

/**
 * REVIEW chung:
 * - Sửa thành file ".js" thay vì ".txt"
 * - Kí tự lùi đầu dòng em đang để là tab, nên sửa thành space
 * - Có nhiều khoảng trắng thừa (VD: dấu cách ở cuối dòng, dấu lùi dòng ở những dòng trống).
 * Cần xóa các khoảng trắng thừa (Tip: trên Vscode dùng tổ hợp phím Ctrl + K + X để tự động xóa khoảng trắng thừa)
 * - Em chỉ cần viết bài làm vào đây, không cần copy cả đoạn khởi tạo "process.stdin.resume() v.v."
 * Trừ khi muốn gõ lại cho quen tay thì cũng được :)
 */

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
	// REVIEW: ví dụ dòng này có khoảng trắng thừa
	main();
});

function readLine() {
	return inputString[currentLine++];
}

var parameterVariable = "Welcome to 10 Days of JavaScript!"


function greeting(parameterVariable) {
	console.log('Hello, World!');
	console.log(parameterVariable);
}



// Day 0: Data Types
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

function performOperation(secondInteger, secondDecimal, secondString) {
	const firstInteger = 4;

	const firstDecimal = 4.0;

	const firstString = 'HackerRank ';

	// REVIEW: giữa 2 đầu dấu "+" thêm 1 dấu cách. VD: `firstInteger + parseInt(...)`
	console.log(firstInteger + parseInt(secondInteger))
	console.log(firstDecimal + parseFloat(secondDecimal))
	console.log(firstString + secondString)
}

