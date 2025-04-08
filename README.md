# Brownian Robot Motion Simulator

A Python package that simulates Brownian motion in a robotic system using `pygame`. The robot moves randomly in a 2D square arena, changing direction on collision with boundaries. This package is perfect for visualizing random motion patterns and experimenting with simple robotic behavior models.

---

## 🔧 Features
- Brownian motion simulation in a bounded arena.
- Randomized motion with boundary collision logic.
- Visualization using `pygame`.
- Modular and reusable Python class.
- CLI demo launcher: `brownian-demo`

---

## 📦 Installation

### Install via pip
```bash
pip install brownian_robot
```

### Install from source
```bash
git clone https://github.com/yourusername/brownian_robot.git
cd brownian_robot
pip install .
```

---

## 🚀 Usage

### As a Library
```python
from brownian_robot import BrownianRobot

robot = BrownianRobot(arena_size=500)
robot.run()
```

### Command Line Demo
```bash
brownian-demo
```

### Example Script
```bash
python examples/demo.py
```
Runs the simulation in an 800x800 arena.

---

## 🧪 Testing
Use `pytest` to run unit tests:
```bash
pytest tests/
```

---

## 📁 Project Structure
```
brownian_robot/
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.py
├── src/
│   └── brownian_robot/
│       ├── __init__.py
│       └── brownian.py
├── examples/
│   └── demo.py
└── tests/
    └── test_motion.py
```

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature-xyz`
3. Make your changes and commit: `git commit -m "Add feature xyz"`
4. Push to your fork: `git push origin feature-xyz`
5. Submit a pull request

---

## 🧾 License
This project is licensed under the MIT License.

---

## 📚 Acknowledgments
Inspired by physical Brownian motion and its implications in robotics and autonomous systems.

Learn more: [Introduction to Brownian Motion](https://thoughtco.com/introduction-to-brownian-motion)
