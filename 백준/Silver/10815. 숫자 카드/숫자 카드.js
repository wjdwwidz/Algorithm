const fs = require('fs');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let myCard = new Set(input[1].split(" ").map(Number));
let cardToCheck = input[3].split(" ").map(Number);

let answerArr = cardToCheck.map(item => myCard.has(item));


// answerArr = answerArr.map(item=>(Number(item)));

console.log(answerArr.map(Number).join(" "));