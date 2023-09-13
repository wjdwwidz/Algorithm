const fs = require('fs');
let arr = fs.readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(Number);

let sum = 0;
let newArr = [];

for (const item of arr) {
    sum += item;
}

let diff = sum - 100;

for (var i = 0; i < arr.length; i++) {
    let firstNum = arr[i];
    let secondNum = diff - firstNum;

    if (arr.includes(firstNum) && arr.includes(secondNum) && i !== arr.indexOf(secondNum)) {
        arr.forEach(item => {
            if (item !== firstNum && item !== secondNum) {
                newArr.push(item);
            }
        });
        
        break;
    }
}

console.log(newArr.join("\n"));
