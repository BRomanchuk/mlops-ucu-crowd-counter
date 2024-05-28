# mlops-ucu-crowd-counter
UCU MLOps course project


## Installation

## Docker image
1. Pull Docker image
```bash
docker pull bromanchuk/crowd-counter
```
2. Run container
```bash
docker run -p 5555:5555 bromanchuk/crowd-counter
```

### Python app
1. Clone repo
```bash
git clone https://github.com/BRomanchuk/mlops-ucu-crowd-counter.git
```
2. Create and activate virtual environment
```bash
python3.10 -m venv ~/.crowd-counter
source ~/.crowd-counter/bin/activate
```
3. Install requiremets
```bash
pip install -r requirements.txt
```
4. Run application
```bash
python app.py
```