function maxCombine(xs) {
 return parseInt(
 xs
 .map(String)
 .sort((a, b) => (b + a).localeCompare(a + b))
 .join(''),
 10
 );
}
