# Joker API
Joker is an API used for getting and retrieving jokes

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

### GET `/v1/surprise` (Get a random joke)

Response:
```
{
  "joke": "What's the best thing about Switzerland?",
  "answer": "I don't know, but the flag is a big plus."
}
```

### GET `/v1/jokes` (Get list of all jokes)

Response:
```
{
  "jokes": [
    {
      "joke": "What's the best thing about Switzerland?",
      "answer": "I don't know, but the flag is a big plus."
    },
    {
      "joke": "I invented a new word!",
      "answer": "Plagiarism!"
    },
    {
      "joke": "Did you hear about the mathematician who's afraid of negative numbers?",
      "answer": "He'll stop at nothing to avoid them!"
    },
    {
      "joke": "Why do we tell actors to 'break a leg'?",
      "answer": "Because ebery play has a cast!"
    },
    {
      "joke": "Helvetica and Times New Roman walk into a bar.",
      "answer": "'Get out of here!' shouts the bartender. 'We don’t serve your type.'"
    }
  ]
}
```

## Contact
Nicholas Chumney - [nicholas.chumney@outlook.com](nicholas.chumney@outlook.com) 

## Acknowledgments
- [Pyramid Tutorials](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html)
