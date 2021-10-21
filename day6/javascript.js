// Day 7: Regular Expressions I
/**
 * REVIEW:
 * - Nên dùng const thay vì let
 * - Một số lỗi format
 */

function regexVar() {
    let re = /^([aeiou]).+\1$/;
    return re;
}




// Day 7: Regular Expressions II

function regexVar() {
    let re = /^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$/
    return re;
}




// Day 7: Regular Expressions III

function regexVar() {
    let re= /[0-9]+/g
    return re;
}