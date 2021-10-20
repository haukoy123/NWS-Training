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

/**
 * REVIEW 1:
 * Em nên đặt tên biến đầy đủ: "area", "perimeter" thay vì "a", "p"
 * 
 * REVIEW 2:
 * Biến nào không thay đổi thì nên dùng `const`, nếu có thay đổi thì ưu tiên dùng `let` thay vì `var`:
 * const a = ...
 * const b = ...
 * const result = []
 * Lý do:
 *  - Dùng const để tránh vô tình thay đổi giá trị của biến ở đâu đó, dẫn đến bug rất khó tìm
 *  - Dùng let thì scope của biến là block, dễ kiểm soát hơn var
 */
function sides(literals, ...expressions) {
    const area = expressions[0];
    const perimeter = expressions[1];
    let result = [];
    result[0] = (perimeter - Math.sqrt(perimeter ** 2 - (16 * area))) / 4;
    result[1] = (perimeter + Math.sqrt(perimeter ** 2 - (16 * area))) / 4;
    return result.sort()
}




// Day 5: Arrow Functions


function modifyArray(nums) {
    return nums.map(num => num % 2 === 0 ? num * 2 : num * 3)
}


// Day 6: JavaScript Dates

/**
 * REVIEW: ở đây có thể khai báo và gán giá trị cho `dayName` cùng 1 lúc;
 * const dayName = ["Sunday", ...]
 */
function getDayName(dateString) {
    let dayName = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return dayName[new Date(dateString).getDay()];
}




// Day 6: Bitwise Operators


function getMaxLessThanK(n, k) {
    let max = 0;
    for (let i = 1; i < n; i++) {  // REVIEW: thiếu dấu cách chỗ "let i = 1"
        for (let j = i + 1; j <= n; j++) {
            if ((i & j) < k && (i & j) > max) {
                max = i & j;
            }
        }
    }
    return max;
}  // REVIEW: thiếu 1 dòng trắng cuối file
