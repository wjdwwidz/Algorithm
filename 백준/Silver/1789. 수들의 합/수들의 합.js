const fs = require('fs');
let input = fs.readFileSync("/dev/stdin").toString();

let sum =0;
let currentNum=1;

while(sum<=input){
   sum+=currentNum;
   if(sum > input){break;}
   currentNum ++;
};

console.log(currentNum-1);