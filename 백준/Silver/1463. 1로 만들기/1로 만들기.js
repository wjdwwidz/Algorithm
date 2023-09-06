const fs = require('fs');
const x = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

let dp = new Array(x+1).fill(0);

dp[2] = 1; //숫자 2와 3을 만드는 데 필요한 최소 연산의 횟수를 정의하는 것 
dp[3] = 1; //2와 3은 각각 1을 빼는 연산 한 번으로 1을 만들 수 있으므로 초기값으로 1을 설정



dp.forEach((value,index)=>{
   
    if(index>3){
        let temp = [dp[index-1]];
        index%2 === 0?temp.push(dp[index/2]):0;
        index%3 === 0?temp.push(dp[index/3]):0;
        dp[index] = Math.min(...temp)+1; 
        //temp에는 index에 도달하기까지의 가능한 모든 연산의 결과가 담겨있다 
        //ex) index = 9 일때 : 9%3 , 9-1 가능 => dp[9/3] 와 dp[9-1]의 value를 temp에 담아두고, (현재 index까지 오는 횟수) +1 을 한 뒤, 더 작은 값을 dp[9]에 담는다     
    }
})
console.log(dp[x])
