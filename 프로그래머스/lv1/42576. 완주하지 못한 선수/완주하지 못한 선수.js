function solution(participant, completion) {
  const hashTable = {};

  // completion을 해시테이블에 추가
  for (const element of completion) {
    if (hashTable[element]) {
      hashTable[element]++;
    } else {
      hashTable[element] = 1;
    }
  }

  // participant를 해시테이블에서 빼면서 완주하지 못한 사람 찾기
  for (const element of participant) {
    if (!hashTable[element]) { //해시테이블에 원소의 값이 없으면
      return element; // 완주하지 못한 사람 반환
    }
    hashTable[element]--;
  }
}
