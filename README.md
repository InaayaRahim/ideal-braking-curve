# ideal-braking-curve
## Description
This program uses Python to calculate and plot the ideal braking curve for a Formula Student vehicle. It calculates the braking forces at the front and rear axles, and considers how weight shifts towards the front of the vehicle during braking.
## Requirements
- Python 3
- NumPy
- Matplotlib
## Installation
Clone the repository and navigate to the project folder:
```
git clone https://github.com/InaayaRahim/ideal-braking-curve
cd ideal-braking-curve
```
Create and activate a virtual environment.
### macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
### Windows (Command Prompt):
```
py -m venv .venv
.venv\Scripts\activate.bat
```
Install the required libraries:
```
python -m pip install -r requirements.txt
```
## How to Run
With the virtual environment activated, run:
```
python main.py
```
The program prints the braking force results in the terminal, displays the ideal braking curve and saves the graph to `plots/ideal_braking_curve.png`.
## Project Structure
```text
ideal-braking-curve/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── report.docx
├── report.pdf
└── plots/
    └── ideal_braking_curve.png
```