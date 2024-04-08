# Bird Eats Bugs Game

This is a simple game where a bird eats bugs using hand tracking controls. The game is built with Phaser, a JavaScript game framework, and uses TensorFlow.js and Handpose for hand tracking.

## Try it Out

You can play the game online by visiting the following link:

[Bird Eats Bugs Game](https://brdi-fight-hand-control.vercel.app)

## Running the Game Locally

If you prefer to run the game locally, follow these steps:

### Prerequisites

Before running the game, ensure you have the following installed:

- Python (version 2.x or 3.x)
- A modern web browser (e.g., Chrome, Firefox, Safari)
- A webcam connected to your computer

### Getting Started

1. Download the game files from the repository or obtain them from the provided source.

2. Open a terminal or command prompt and navigate to the directory where your game files are located.

3. Start a local web server by running one of the following commands:
   - For Python 3.x: `python -m http.server`
   - For Python 2.x: `python -m SimpleHTTPServer`

4. Open a web browser and visit `http://localhost:8000` (or the appropriate URL and port number displayed in the terminal).

5. Allow the browser to access your webcam when prompted.

6. Wait for the hand pose model to load. You will see an alert when it's ready.

7. Place your hand in front of the webcam. The bird will follow the movement of your index finger.

8. Guide the bird to eat the bugs that appear on the screen.

## Game Controls

- Move your index finger to control the bird's position.
- The bird will automatically eat the bugs when it collides with them.

## Customization

If you want to customize the game, you can modify the following files:

- `index.html`: Update the game layout, add new elements, or modify the existing ones.
- `main.js` (or the script section in `index.html`): Modify the game logic, add new features, or change the game mechanics.
- Replace the game assets (images) with your own by updating the file names in the `preload` function of the `MainScene` class.

## Troubleshooting

- If the game doesn't start, ensure that you have a stable internet connection, as the game relies on loading external libraries (Phaser and TensorFlow.js).
- If the hand tracking doesn't work, make sure your webcam is properly connected and you have granted permission for the browser to access it.
- If you encounter any other issues, please refer to the browser console for error messages and seek further assistance.

## Acknowledgments

- This game is built using the Phaser game framework: [https://phaser.io/](https://phaser.io/)
- Hand tracking is implemented using TensorFlow.js and Handpose: [https://github.com/tensorflow/tfjs-models/tree/master/handpose](https://github.com/tensorflow/tfjs-models/tree/master/handpose)

Enjoy playing the Bird Eats Bugs game!