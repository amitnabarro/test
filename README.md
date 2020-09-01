### Coding Challenge

Developed by: Amit Nabarro - amit.nabarro@gmail.com

### Requirements

1. Python 3.6 or above

### Project Stack

This project was developed as a console application which prints the results in the console and exits.

### Running the code inside a virtual environment

1. CD into the project's root


    cd /path/to/project/root

2. Create a virtual environment with your local Python installation like so:

    which python3

    virtualenv -p path/to/python3 venv

3. Apply virtual environment:

    source venv/bin/activate

4. Install requirements

    pip install -r requirements.txt

5. Execute code

    python src/main.py

### Running the code in a dockerized environment

The project includes a docker file for running the code in a container

Building the docker container

    docker build -t code_challenge .

Running the docker container

    docker run --rm code_challenge:latest


