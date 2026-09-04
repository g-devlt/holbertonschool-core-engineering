#!/usr/bin/env python3

def best_score(a_dictionary: dict):
    return sorted(
        a_dictionary.items(),
        key=lambda item: item[1],
        reverse=True
    )[0][0] if a_dictionary is not None and len(a_dictionary) > 0 else None


if __name__ == "__main__":
    print(best_score({
        "Gabriel": 2,
        "Mattéo": 100,
        "Matt": 4,
        "Leïla": 99
    }))

    print(best_score({
        "Gabriel": 99,
        "Mattéo": 99,
        "Matt": 89,
        "Leïla": 99
    }))

    print(best_score({
        "Gabriel": 0,
        "Mattéo": 0,
        "Matt": 0,
        "Leïla": 0
    }))

    print(best_score({}))
    print(best_score(None))
