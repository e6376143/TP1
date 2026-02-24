def tokenize(expression: str) -> list[str]:
    tokens = []
    current_token = ""
    for t in expression:
        if t == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif t in "+-*/()":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(t)
        else:
            current_token += t
    if current_token:
        tokens.append(current_token)
    return tokens


print(tokenize("3 + 4 * (2 - 1)"))