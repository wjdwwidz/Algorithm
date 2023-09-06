const fs = require("fs");
const input = fs.readFileSync("dev/stdin").toString().trim().split("\n");

const t = input.shift();
const dp = new Array(10).fill(0);

dp[1] = 1; 
dp[2] = 2; 
dp[3] = 4; 

// dp[n] = dp[n-1]+dp[n-2]+dp[n-3];
for (let i = 4; i <= 11; i++) {
  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
}

const log = [];
input.forEach((v) => {
  log.push(dp[parseInt(v)]);
});
console.log(log.join("\n"))