const targetNumber = Math.floor(Math.random() * 100) + 1; // 生成 1 到 100 之间的随机整数
console.log(targetNumber);
let numGuesses = 0; // 记录猜测次数
let guessList = []; // 存储所有猜测的数字

function checkGuess() {
    const guess = parseInt(document.getElementById("guess").value);
    if (isNaN(guess) || guess < 1 || guess > 100) {
        document.getElementById("result").innerHTML = "请输入一个 1 到 100 之间的整数";
    } else {
        numGuesses++;
        guessList.push(guess);
        if (guess === targetNumber) {
            document.getElementById("result").innerHTML = `<div style="text-align: center;">恭喜你，猜对了！<br></br>共猜了 ${numGuesses} 次。</div>`;
            document.querySelector("button").disabled = true;
        } else if (guess < targetNumber) {
            document.getElementById("result").innerHTML = `<div style="text-align: center;">第 ${numGuesses} 次猜测：你猜的数字有点小，请再试一次。</div>`;
        } else {
            document.getElementById("result").innerHTML = `<div style="text-align: center;">第 ${numGuesses} 次猜测：你猜的数字有点大，请再试一次。</div>`;
        }
        document.getElementById("previousGuesses").innerHTML = `<div style="text-align: center;">之前的猜测：${guessList.join(', ')}</div>`;
    }
}