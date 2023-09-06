const fs = require('fs');
const x = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

let dp = new Array(x+1).fill(0);

dp[2] = 1;
dp[3] = 1; 

dp.forEach((value,index)=>{
   
    if(index>3){
        let temp = [dp[index-1]];
        index%2 === 0?temp.push(dp[index/2]):0;
        index%3 === 0?temp.push(dp[index/3]):0;
        dp[index] = Math.min(...temp)+1; 
    }
})
console.log(dp[x])
