# Random sampling tool

A CLI tool for random sampling from a list of number given discrete probabilities 
- Install poetry
```
python3 -m pip install poetry
```
- Install all dependencies 
```
poetry install
```
- Run the tool the the desired input, e.g.:
```
poetry run python main.py -n -1 0 1 2 3 -p 0.01 0.3 0.58 0.1 0.01 -r 100
```

Additionally you can:

- Run unit tests
```
poetry run pytest
```
- Run type checking
```
poetry run mypy .
```
- Run black
```
poetry run black .
```