const fs = require('fs');
let [N,money,...wons] = fs.readFileSync('dev/stdin').toString().trim().split(/\s+/).map(Number);
let maxIndex, cnt=0


wons.sort(function(a,b){return b-a});

wons.forEach((item)=>{
  cnt += parseInt(money/item);
  money%= item;
})

console.log(cnt);