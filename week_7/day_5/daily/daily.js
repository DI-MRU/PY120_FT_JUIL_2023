function anagram(word1, word2) {
  let split = word1.replace(/\s+/g, "").toLowerCase();
  let split2 = word2.replace(/\s+/g, "").toLowerCase();

  if (split.length !== split2.length) {
    return false;
  }
  split = split.split("").sort().join("");
  split2 = split2.split("").sort().join("");

  return split === split2;
}

console.log(anagram("w     d", "wd"));

let anagram2 = (word1, word2) => {
  let split = word1.replace(/\s+/g, "").toLowerCase();
  let split2 = word2.replace(/\s+/g, "").toLowerCase();

  if (split.length !== split2.length) {
    return false;
  }

  let str = {};
  let str2 = {};

  for (letter of split) {
    str[letter] = (str[letter] || 0) + 1;
    console.log(str);
  }

  split2.split("").forEach((letter) => {
    str2[letter] = (str2[letter] || 0) + 1;
  });

  for (key in str) {
    if (str[key] !== str2[key]) {
      return false;
    }
  }
  return true;
};

console.log(anagram2("hello", "ehllo"));
