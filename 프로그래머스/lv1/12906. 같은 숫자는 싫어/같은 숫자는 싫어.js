function solution(arr) {
  const result = [];
  
  arr.forEach((num, index) => {
    if (index === 0 || num !== arr[index - 1]) {
      result.push(num);
    }
  });
  
  return result;
}
