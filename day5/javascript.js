// Day 5: Inheritance

Rectangle.prototype.area = function () {
    return (this.w * this.h);
};

class Square extends Rectangle {
    constructor(side) {
        super(side, side)
    }
}


// Day 5: Template Literals


function sides(literals, ...expressions) {
    let a = expressions[0];
    let p = expressions[1];
    var result = [];
    result[0] = (p - Math.sqrt(p ** 2 - (16 * a))) / 4;
    result[1] = (p + Math.sqrt(p ** 2 - (16 * a))) / 4;
    return result.sort()
}




// Day 5: Arrow Functions


function modifyArray(nums) {
    return nums.map(num => num % 2 === 0 ? num * 2 : num * 3)
}


// Day 6: JavaScript Dates


function getDayName(dateString) {
    let dayName;
    dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return dayName[new Date(dateString).getDay()];
}




// Day 6: Bitwise Operators


function getMaxLessThanK(n, k) {
    let max = 0;
    for (let i =1; i < n; i++) {
        for (let j = i + 1; j <= n; j++) {
            if ((i & j) < k && (i & j) > max) {
                max = i & j;
            }
        }
    }
    return max;
}