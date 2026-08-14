function maxCombine(xs: number[]): number {
  if (!Array.isArray(xs) || xs.length === 0) return 0;
  const nums = xs.filter((x): x is number => Number.isInteger(x) && x >= 0);
  if (nums.length === 0) return 0;
  const sorted = nums.map(String).sort((a, b) => (b + a).localeCompare(a + b));
  const joined = sorted.join('');
  return joined[0] === '0' ? 0 : Number(joined);
}

const testCases: [number[], number][] = [
  [[1, 3, 3, 4, 55], 554331],
  [[71, 45, 23, 4, 5], 71545423],
  [[14, 43, 53, 114, 55], 55534314114],
  [[1, 34, 3, 98, 9, 76, 45, 4], 998764543431],
  [[54, 546, 548, 60], 6054854654],
];

for (const [numbers, expected] of testCases) {
  const result = maxCombine(numbers);
  const status = result === expected ? 'PASS' : 'FAIL';
  console.log(`${status}: [${numbers.join(', ')}] -> ${result} (expected ${expected})`);
}

export { maxCombine };
