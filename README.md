# Pseudo-Network Pipeline

This project computes gene regulatory networks using mutual information and visualizes the top-ranked edges.

---

## Requirements

- Python 3.10+
- Git
- WSL / Linux / macOS (recommended)

---

## Setup Instructions

Clone the repository:

git clone https://github.com/daniel-315/Pseudo-network-work.git
cd Pseudo-network-work

Create a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Run the Pipeline

Create output folder:

mkdir -p output

Run the main script:

python main.py \
  --data_file input/ExpressionData.csv \
  --time_file input/PseudoTime.csv \
  --save_dir output

---

## Generate Graph

python graph_output.py

---

## Output

- output/rankedEdges.csv → ranked gene interactions  
- output/network_top20.png → network visualization  

---

## Notes

- Make sure your virtual environment is activated (.venv)
- If you get errors, reinstall dependencies:

pip install -r requirements.txt
