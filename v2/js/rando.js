function IsNumeric(n) {
    return !isNaN(n);
  }
  
  const generateButton = document.querySelector("#getit");
  const lowInput = document.querySelector("#lownumber");
  const highInput = document.querySelector("#highnumber");
  const randomNumberOutput = document.querySelector("#randomnumber");
  
  generateButton.addEventListener("click", () => {
    var numLow = lowInput.value;
    var numHigh = highInput.value;
  
    var adjustedHigh = parseFloat(numHigh) - parseFloat(numLow) + 1;
  
    var numRand = Math.floor(Math.random() * adjustedHigh) + parseFloat(numLow);
  
    if (
      IsNumeric(numLow) &&
      IsNumeric(numHigh) &&
      parseFloat(numLow) <= parseFloat(numHigh) &&
      numLow != "" &&
      numHigh != ""
    ) {
      randomNumberOutput.innerText = numRand;
    } else {
      randomNumberOutput.innerText = "Invalid High number";
    }
  
    return false;
  });