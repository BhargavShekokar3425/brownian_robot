Brownian Robot Motion Simulator
================================

A Python package to simulate Brownian motion behavior in a robotic system within a bounded arena. This package provides tools to visualize random motion patterns and test collision dynamics using Python and Pygame.

Features
--------
- Simulates Brownian motion of a robot in a square arena.
- Handles boundary collisions with random rotations.
- Visualizes robot motion using Pygame.
- Provides a modular Python library for integration into other projects.
- Includes a command-line demo for quick testing.

Prerequisites
-------------
Before using this package, ensure you have the following installed:
- Python 3.8 or higher
- `numpy` library (version >= 1.21)
- `pygame` library (version >= 2.1)

Installation
------------
Install the package via pip:

    pip install brownian_robot

Alternatively, install directly from the source:

    git clone https://github.com/yourusername/brownian_robot.git
    cd brownian_robot
    pip install .

Usage
-----
### As a Library
Import the package in your Python code:

    from brownian_robot import BrownianRobot

    robot = BrownianRobot(arena_size=500)
    robot.run()

### Command-Line Demo
Run the included demo application:

    brownian-demo

This will launch a Pygame window showing the robot's random motion.

Examples
--------
### Running the Demo Script
You can find an example script in the `examples/demo.py` file:

    python examples/demo.py

This demonstrates how to use the `BrownianRobot` class to simulate motion in an 800x800 arena.

Testing
-------
To run tests, use `pytest`:

    pytest tests/

Ensure all dependencies are installed before running tests.

Contributing
------------
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Create a pull request.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.


Acknowledgments
---------------
Inspired by concepts of Brownian motion and its applications in robotics, physics, and mathematics.



About Brownian Motion
---------------------
Brownian motion refers to the random movement of particles due to collisions with surrounding molecules. This concept has applications in physics, robotics, biology, and more. Learn more about Brownian motion here: https://thoughtco.com/introduction-to-brownian-motion.
