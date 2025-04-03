// Game state variables
let score = 0;
let lives = 3;
let currentRgb = null;
let correctOptionIndex = null;

// DOM elements
const rgbValueDisplay = document.getElementById('rgb-value');
const livesDisplay = document.querySelector('#lives span');
const scoreDisplay = document.querySelector('#score span');
const colorOptions = document.querySelectorAll('.color-option');
const feedbackEl = document.getElementById('feedback');
const resetBtn = document.getElementById('reset-btn');
const gameOverModal = document.getElementById('game-over-modal');
const finalScoreDisplay = document.getElementById('final-score');
const playAgainBtn = document.getElementById('play-again-btn');

/**
 * Generates a random RGB color value
 * @returns {Object} Object containing r, g, b values
 */
function generateRandomColor() {
    return {
        r: Math.floor(Math.random() * 256),
        g: Math.floor(Math.random() * 256),
        b: Math.floor(Math.random() * 256)
    };
}

/**
 * Converts RGB object to CSS rgb string
 * @param {Object} rgb RGB object with r, g, b properties
 * @returns {String} CSS rgb string
 */
function rgbToString(rgb) {
    return `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
}

/**
 * Generates similar (but different) RGB color to the given one
 * @param {Object} sourceRgb Original RGB color
 * @returns {Object} New similar RGB color
 */
function generateSimilarColor(sourceRgb) {
    // Create variations within a reasonable range (±40)
    const variation = 40;
    
    // Create a new RGB color with constrained variations
    const newRgb = {
        r: Math.min(255, Math.max(0, sourceRgb.r + Math.floor(Math.random() * variation * 2) - variation)),
        g: Math.min(255, Math.max(0, sourceRgb.g + Math.floor(Math.random() * variation * 2) - variation)),
        b: Math.min(255, Math.max(0, sourceRgb.b + Math.floor(Math.random() * variation * 2) - variation))
    };
    
    // Ensure the new color is different from the source
    if (newRgb.r === sourceRgb.r && newRgb.g === sourceRgb.g && newRgb.b === sourceRgb.b) {
        // Force at least one component to be different
        const component = ['r', 'g', 'b'][Math.floor(Math.random() * 3)];
        newRgb[component] = (newRgb[component] + 30) % 256;
    }
    
    return newRgb;
}

/**
 * Sets up a new round with new colors
 */
function setupRound() {
    // Clear any previous feedback
    feedbackEl.textContent = '';
    feedbackEl.className = '';
    
    // Generate the target RGB color
    currentRgb = generateRandomColor();
    rgbValueDisplay.textContent = `RGB(${currentRgb.r}, ${currentRgb.g}, ${currentRgb.b})`;
    
    // Randomly choose which option will be correct
    correctOptionIndex = Math.floor(Math.random() * colorOptions.length);
    
    // Assign colors to all options
    colorOptions.forEach((option, index) => {
        // Set correct color for the chosen option, similar colors for others
        if (index === correctOptionIndex) {
            option.style.backgroundColor = rgbToString(currentRgb);
        } else {
            option.style.backgroundColor = rgbToString(generateSimilarColor(currentRgb));
        }
        
        // Reset any previous styles and enable clicking
        option.style.opacity = '1';
        option.style.cursor = 'pointer';
    });
}

/**
 * Handles user selection of a color option
 * @param {Number} index Index of the selected option
 */
function handleSelection(index) {
    // Check if the selection is correct
    const isCorrect = index === correctOptionIndex;
    
    // Update score and feedback
    if (isCorrect) {
        score++;
        scoreDisplay.textContent = score;
        feedbackEl.textContent = 'Correct!';
        feedbackEl.className = 'correct';
        
        // Highlight the correct answer
        colorOptions.forEach((option, i) => {
            if (i !== correctOptionIndex) {
                option.style.opacity = '0.5';
                option.style.cursor = 'default';
            }
        });
        
        // Short delay before next round
        setTimeout(setupRound, 1500);
    } else {
        lives--;
        livesDisplay.textContent = lives;
        feedbackEl.textContent = 'Incorrect! Try again.';
        feedbackEl.className = 'incorrect';
        
        // Disable the selected wrong option
        colorOptions[index].style.opacity = '0.5';
        colorOptions[index].style.cursor = 'default';
        
        // Check if game over
        if (lives <= 0) {
            endGame();
        }
    }
}

/**
 * Ends the current game and shows game over screen
 */
function endGame() {
    // Display final score
    finalScoreDisplay.textContent = score;
    
    // Show the game over modal
    gameOverModal.style.display = 'flex';
}

/**
 * Starts a new game with reset score and lives
 */
function startNewGame() {
    // Reset game state
    score = 0;
    lives = 3;
    scoreDisplay.textContent = score;
    livesDisplay.textContent = lives;
    
    // Hide game over modal if visible
    gameOverModal.style.display = 'none';
    
    // Set up first round
    setupRound();
}

// Add click event listeners to color options
colorOptions.forEach((option, index) => {
    option.addEventListener('click', function() {
        // Only allow click if option is not disabled
        if (this.style.opacity !== '0.5') {
            handleSelection(index);
        }
    });
});

// Add event listeners for buttons
resetBtn.addEventListener('click', startNewGame);
playAgainBtn.addEventListener('click', startNewGame);

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', startNewGame);