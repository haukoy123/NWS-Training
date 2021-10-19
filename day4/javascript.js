// Day 4: Create a Rectangle Object

function Rectangle(a, b) {
    return {
        length: a,
        width: b,
        perimeter: 2 * (a + b), // REVIEW: thêm dấu cách ở 2 đầu dấu "+"
        area: a * b
    }
}



// Day 4: Count Objects

function getCount(objects) {
    let count = 0;
    for (let item of objects) {
        if (item.x === item.y) {
            count++;
        }
    }
    return count
}



// Day 4: Classes

class Polygon {
    constructor(sides) {
        this.sides = sides
    }

    perimeter() {  // REVIEW: thêm dấu cách giữa ")" và "{" => "perimeter() {"
        let sum = 0;
        for (let i of this.sides) {
            sum += i;
        }
        return sum
    }
}
