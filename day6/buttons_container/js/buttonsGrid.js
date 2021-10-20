function btn5click() {
    let temp = document.getElementById('btn1').innerText;
    document.getElementById('btn1').innerText = document.getElementById('btn4').innerText;
    document.getElementById('btn4').innerText = document.getElementById('btn7').innerText;
    document.getElementById('btn7').innerText = document.getElementById('btn8').innerText;
    document.getElementById('btn8').innerText = document.getElementById('btn9').innerText;
    document.getElementById('btn9').innerText = document.getElementById('btn6').innerText;
    document.getElementById('btn6').innerText = document.getElementById('btn3').innerText;
    document.getElementById('btn3').innerText = document.getElementById('btn2').innerText;
    document.getElementById('btn2').innerText = temp;
}