# Paint Calculator
This program calculates the number of paint cans required to paint a wall of given dimensions. The number of cans is calculated based on the height and width of the wall and the coverage provided by a single can of paint.

## Usage
Input the height of the wall: The user is prompted to enter the height of the wall in meters.
Input the width of the wall: The user is prompted to enter the width of the wall in meters.
Coverage per can: The program uses a fixed coverage rate (e.g., 5 square meters per can) to determine how much area one can of paint will cover.
Calculate the number of cans: The program calculates the total number of paint cans needed and rounds up to the nearest whole number to ensure full coverage of the wall.
Example
Height: 3 meters
Width: 4 meters
Coverage: 5 square meters per can
The program will calculate and print the following:

You'll need 3 cans of paint.
## Concepts Used
Input Function: The input() function is used to get user input for the height and width of the wall. These inputs are then converted to integers using the int() function.

Arithmetic Operations: Basic arithmetic operations are used to calculate the total area of the wall (height * width) and to determine the number of paint cans needed (total area / coverage).

Math Library: The math.ceil() function from the math library is used to round up the number of paint cans to the nearest whole number. This ensures that we always have enough paint to cover the entire wall.

Formatted String: The f-string (formatted string) is used to format the output message, making it clear and readable.

## License
This project is open-source and available under the MIT License.
