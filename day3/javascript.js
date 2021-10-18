// Day 3: Arrays

/**
 * REVIEW 1: tên biến trong JS em nên dùng camelCase thay vì snake_case.
 *
 * REVIEW 2:
 * Trong doc của MDN, anh đọc có đoạn này:
 * "Note: When the first argument is undefined or null a similar outcome can be achieved using the array spread syntax."
 * (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
 * => "Math.max.apply(null, nums)" em có thể viết thành "Math.max(...nums)"
 *
 * Ý nghĩa của "spread operator" (dấu 3 chấm):
 * - Với array: trải 1 array ra thành các biến để truyền vào hàm
 VD:
 1) Math.max(...[1, 2, 3]) tương đương Math.max(1, 2, 3)
 2) const l1 = [1, 2, 3]; const l2 = [...l1, 4, 5] => l2 = [1, 2, 3, 4, 5]
 * - Với object: trải 1 object ra thành nhiều cặp key-value
 VD:
 const obj1 = { a: 1, b: 2 };
 const obj2 = { ...obj1, c: 3 } => obj2 = { a: 1, b: 2, c: 3 }
 *
 * Tương đương trong python:
 * Dấu "*": trải 1 list
 * Dấu "**": trải 1 dict
 VD:
 l = [1, 2, 3]
 my_func(*l) => tương đương my_func(1, 2, 3)
 d = {'a': 1, 'b': 2}
 my_func(**d) => tương đương my_func(a=1, b=2)
 */
function getSecondLargest(nums) {
    const new_arr = nums.filter(item => item !== Math.max.apply(null, nums));
    return Math.max.apply(null, new_arr);
}


// Day 3: Try, Catch, and Finally

function reverseString(s) {
    try {
        s = s.split('').reverse().join('');
    } catch (e) {
        console.log(e.message);
    } finally {
        console.log(s);
    }
}


// Day 3: Throw

function isPositive(a) {
    if (a > 0) {
        return 'YES'; // REVIEW: ở đây chỉ cần "return 'YES';"
    }
    else if (a === 0) {  // REVIEW: nên dùng so sánh chặt (3 dấu "="), thay vì 2 dấu "=". Lý do: tránh bug ẩn
        throw Error('Zero Error');
    }
    else {
        throw Error('Negative Error');
    }
}
