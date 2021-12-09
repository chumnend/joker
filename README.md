# Joker API
Joker is an api used for getting and retrieving jokes

## Getting Started

### Prerequistes
- Python 3.8
- virtualenv

### Installation
1) Create new virtual environment, if not created yet.
  ```
    python -m venv venv
  ```

2) Activate the newly created virtualenv
  ```
    source venv/bin/activate
  ```

3) Install python dependecies.
  ```
    make install-deps
  ```

4) Start the server.
  ```
    make start
  ```

## API Documentation

### GET `/v1/joke`

Response:
```
{
  "joke": "What's the best thing about Switzerland?",
  "answer": "I don't know, but the flag is a big plus."
}
```



## Contact
Nicholas Chumney - [nicholas.chumney@outlook.com](nicholas.chumney@outlook.com) 

## Acknowledgments
- [Pyramid Tutorials](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html)
