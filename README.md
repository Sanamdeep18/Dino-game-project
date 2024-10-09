# Dino-Game-Automation

This Python script automates the famous offline Chrome Dino game by using `PyAutoGUI` for keyboard control and `Pillow` for real-time screen capture. The script detects obstacles in the game like cacti and birds, helping the dino survive longer by automatically jumping or ducking at the right moment.

## Features:
- Automatically jumps over cacti
- Ducks to avoid birds
- Real-time image capture and obstacle detection
- Supports 100% zoom level on Chrome

## Installation:
1. Install the required libraries:
    ```bash
    pip install pyautogui pillow
    ```

2. Run the script:
    ```bash
    python dino_game.py
    ```

## How It Works:
1. The script continuously captures screenshots of the game using `ImageGrab` from `Pillow`.
2. The images are processed in grayscale, and specific screen areas are scanned for obstacles.
3. When an obstacle is detected within the defined regions:
    - The dino jumps (`up`) if a cactus is detected.
    - The dino ducks (`down`) if a bird is detected.
   
4. The script uses simple conditional checks to identify pixel colors corresponding to obstacles.

## Troubleshooting:
- Ensure that Chrome is set to **100% zoom** (`Ctrl + 0` to reset).
- The obstacle detection coordinates may need adjustments based on screen resolution. Fine-tune the coordinates in the `isCollide()` function to match your setup.
- You can add a visual debugging mode by uncommenting the `image.show()` section to see where obstacles are being detected.

## Tips:
- **Customizing Coordinates**: Depending on your screen resolution and zoom settings, you might need to modify the Y-axis and X-axis ranges in the `isCollide()` function to correctly detect obstacles.
- **Testing**: Before starting the game, run the script for a few seconds and print the captured data or visualize the detection regions to ensure the detection is accurate.
- **Game Speed**: As the game speeds up, consider adjusting the X-axis detection range for faster reactions.

## Contributing:
Feel free to submit pull requests to improve the detection mechanism or extend functionality.

## License:
This project is licensed under the MIT License.
