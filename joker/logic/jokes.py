import random


joke_tuples = [
    (
        "What's the best thing about Switzerland?",
        "I don't know, but the flag is a big plus.",
    ),
    ("I invented a new word!", "Plagiarism!"),
    (
        "Did you hear about the mathematician who's afraid of negative numbers?",
        "He'll stop at nothing to avoid them!",
    ),
    ("Why do we tell actors to 'break a leg'?", "Because ebery play has a cast!"),
    (
        "Helvetica and Times New Roman walk into a bar.",
        "'Get out of here!' shouts the bartender. 'We don’t serve your type.'",
    ),
]


def get_random_joke():
    joke_idx = random.randint(0, len(joke_tuples) - 1)
    return joke_tuples[joke_idx]


def get_all_jokes():
    jokes = []
    for (joke, answer) in joke_tuples:
        jokes.append({"joke": joke, "answer": answer})
    return jokes
