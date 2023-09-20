const fs = require('fs');
let [num,link,...input] = fs.readFileSync('dev/stdin').toString().trim().split(/\n/);

num = Number(num);
link = Number(link);
//console.log(typeof(num),link,arr);

let graph = [...new Array(num+1)].map(()=>[]); 
let visited = [...new Array(num + 1)].fill(false);
let answer =0;


// console.log(input)
for (let i=0; i<link; i++){
    let [from,to] = input[i].split(' ').map(Number);
    graph[from].push(to);
    graph[to].push(from);
}

function dfs(from){
    visited[from] = true;
    for (let to of graph[from]){
        if (!visited[to]){
            visited[to] =1;
            answer ++;
            dfs(to);
        }
    }
}
dfs(1);
console.log(answer);