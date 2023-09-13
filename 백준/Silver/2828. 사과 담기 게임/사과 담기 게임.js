const fs = require('fs');
let [screen,box,howMany,...nums] = fs.readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(Number);
let nowApple = 0; // 초기 바구니 위치

let cnt = 0; // 바구니 이동 횟수

for (const item of nums) {
    if (item === nowApple) {
        // 사과가 현재 위치와 같다면 아무런 이동이 필요하지 않음
    } else if (item < nowApple) {
        // 사과가 현재 위치보다 왼쪽에 있다면 왼쪽으로 이동
        cnt += nowApple - item;
        nowApple = item;
    } else if (item > nowApple + box - 1) {
        // 사과가 현재 위치보다 오른쪽에 있다면 오른쪽으로 이동
        cnt += item - (nowApple + box - 1);
        nowApple = item - (box - 1);
    }
}

console.log(cnt-1);
