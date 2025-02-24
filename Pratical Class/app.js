// Calculator functionality
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.buttons button');

let currentInput = '';
let operator = null;
let firstOperand = null;
let waitingForSecondOperand = false;

// Add event listeners to all buttons
buttons.forEach(button => {
    button.addEventListener('click', () => handleButtonClick(button.textContent));
});

function handleButtonClick(value) {
    if (isNumber(value)) {
        handleNumber(value);
    } else if (isOperator(value)) {
        handleOperator(value);
    } else if (value === '=') {
        handleEquals();
    } else if (value === 'C') {
        handleClear();
    } else if (value === '.') {
        handleDecimal();
    }
    updateDisplay();
}

function isNumber(value) {
    return !isNaN(value) || value === '.';
}

function isOperator(value) {
    return ['+', '-', '*', '/'].includes(value);
}

function handleNumber(number) {
    if (waitingForSecondOperand) {
        currentInput = number;
        waitingForSecondOperand = false;
    } else {
        currentInput = currentInput === '0' ? number : currentInput + number;
    }
}

function handleOperator(nextOperator) {
    const inputValue = parseFloat(currentInput);
    
    if (operator && !waitingForSecondOperand) {
        const result = calculate(firstOperand, inputValue, operator);
        display.value = result;
        firstOperand = result;
        currentInput = result.toString();
    } else {
        firstOperand = inputValue;
    }
    
    waitingForSecondOperand = true;
    operator = nextOperator;
}

function handleEquals() {
    if (operator && !waitingForSecondOperand) {
        const inputValue = parseFloat(currentInput);
        const result = calculate(firstOperand, inputValue, operator);
        display.value = result;
        currentInput = result.toString();
        firstOperand = null;
        operator = null;
        waitingForSecondOperand = false;
    }
}

function handleClear() {
    resetCalculator();
    display.value = '0';
}

function handleDecimal() {
    if (!currentInput.includes('.')) {
        currentInput += '.';
    }
}

function calculate(firstOperand, secondOperand, operator) {
    switch (operator) {
        case '+':
            return firstOperand + secondOperand;
        case '-':
            return firstOperand - secondOperand;
        case '*':
            return firstOperand * secondOperand;
        case '/':
            return firstOperand / secondOperand;
        default:
            return secondOperand;
    }
}

function resetCalculator() {
    currentInput = '';
    operator = null;
    firstOperand = null;
    waitingForSecondOperand = false;
}

function updateDisplay() {
    display.value = currentInput || '0';
}
