/**
 * REVIEW: 
 * - Format chưa tốt :(
 * - "value += 1" em có thể thay bằng "value++"
 */

function button_click(value){
    value = parseInt(value);
    value +=1;
    document.getElementById('btn').innerText= value;
}