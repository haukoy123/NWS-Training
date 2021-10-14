// Day 2: Conditional Statements: If-Else

function getGrade(score) {
    let grade;
    if(score <= 5){
        grade = 'F';
    }
    else if(score <= 10){
        grade = 'E';
    }
    else if(score <= 15){
        grade = 'D';
    }
    else if(score <= 20){
        grade = 'C';
    }
    else if(score <= 25){
        grade = 'B';
    }
    else
        grade = 'A';

    return grade;
}


// Day 2: Conditional Statements: Switch

function getLetter(s) {
    let letter;
    const fc = s[0];
    switch(true) {
        case 'aeiou'.includes(fc) :
            letter = 'A'
            break;
        case 'bcdfg'.includes(fc):
            letter = 'B'
            break;
        case 'hjklm'.includes(fc):
            letter = 'C';
            break;
        case 'npqrstvwxyz'.includes(fc):
            letter = 'D';
            break;
    }

    return letter;
}




// Day 2: Loops


function vowelsAndConsonants(s) {
    const vowel = 'aeiou'
    for (let i of s){
        if (vowel.includes(i)){
            console.log(i);
        }
    }
    for (let i of s){
        if (!vowel.includes(i)){
            console.log(i);
        }
    }
}
