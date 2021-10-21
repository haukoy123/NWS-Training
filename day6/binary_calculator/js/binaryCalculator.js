/**
 * REVIEW:
 * - Tên hàm, biến trong JS nên để camelCase. VD: change_display -> changeDisplay
 * - Một số chỗ em vẫn quên dấu cách giữa ")" và "{"
 */

let operation = "";

function calculate() {
    const operands = operation.match(/[^\*\:\+\-]+/g);
    const operand1 = parseInt(operands[0], 2);
    const operand2 = parseInt(operands[1], 2);
    const operator = operation.match(/[\*\:\+\-]/g);
    if (operands.length === 2 && operator.length === 1) {
        if (operator[0] === "+") {
            operation = (operand1 + operand2).toString(2);
        } else if (operator[0] === "-") {
            operation = (operand1 - operand2).toString(2);
        } else if (operator[0] === "*") {
            operation = (operand1 * operand2).toString(2);
        } else {
            operation = (operand1 % operand2).toString(2);
        }
    }
    else {
        alert("enter as operand1 -> operator -> operand2");
    }
    change_display();
}

function cl(){
    operation = "";
    change_display();
}

function key(k) {
    operation += k;
    change_display();
}

function change_display(){
    document.getElementById("res").innerHTML = operation;
}
