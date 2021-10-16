// Day 3: Arrays

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
        return ('YES');
    }
    else if (a == 0) {
        throw Error('Zero Error');
    }
    else {
        throw Error('Negative Error');
    }
}
