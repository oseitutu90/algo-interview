// find balance of a string with parenthesis
// ex: "((()))" => 0
// ex: "(()))" => 1
// ex: "(()))(" => 2
function balance(str) {
  let balance = 1;
  let max = 1;
  for (let i = 0; i < str.length; i++) {
    if (str[i] === "(") {
      balance++;
    } else if (str[i] === ")") {
      balance--;
    }
  }
  return balance;
}


console.log(balance("((())")); // 2
console.log(balance("(()))")); 