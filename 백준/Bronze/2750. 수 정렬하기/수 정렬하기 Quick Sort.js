const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[0];
  const left = [];
  const right = [];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else {
      right.push(arr[i]);
    }
  }

  const sortedLeft = quickSort(left);
  const sortedRight = quickSort(right);

  return [...sortedLeft, pivot, ...sortedRight];
}



const numbers = input.slice(1).map(Number); //첫 번째 수 제외

const sortedNumbers = quickSort(numbers);

console.log(sortedNumbers.join('\n'));
