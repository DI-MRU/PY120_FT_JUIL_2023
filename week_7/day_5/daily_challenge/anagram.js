/**
 * Processes a raw string into a sanitized anagram string.
 * Removes whitespaces, removes non alphanumeric and sorts the string.
 * @param {*} rawString The raw string.
 * @returns The processed string.
 */
function processString(rawString) {
  return rawString
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "")
    .split("")
    .sort()
    .join("");
}

/**
 * Check if the two strings are anagrams of each other.
 * @param {*} rawString1 The first raw string.
 * @param {*} rawString2 The second raw string.
 * @returns true if anagrams. false otherwise.
 */
function checkAnagram(rawString1, rawString2) {
  let string1 = processString(rawString1);
  let string2 = processString(rawString2);

  if (string1 === string2) {
    return true;
  }
  return false;
}

resultList = [];

resultList.push(checkAnagram("Astronomer", "Moon starer"));
resultList.push(checkAnagram("School master", "The classroom"));
resultList.push(checkAnagram("The Morse Code", "Here come dots"));
resultList.push(checkAnagram("Cookie Monster", "King Julian"));

console.log(resultList);
