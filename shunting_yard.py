def tokenize(expression: str) -> list[str]:
    tokens = []
    current_token = ""
    
    for t in expression:
        if t == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ""
        
        elif t == '-' and not current_token and (not tokens or tokens[-1] == '('):
            current_token += t
            
        elif t in "+*/()":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(t)
            
        else:
            if t == '-' and current_token:
                tokens.append(current_token)
                tokens.append(t)
                current_token = ""
            else:
                current_token += t

    if current_token:
        tokens.append(current_token)
    return tokens

def infix_to_postfix(tokens: list[str]) -> list[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    for token in tokens:
        if token == '(':
            operator_stack.append(token)
            
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
            
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
            
        else:
            output.append(token)

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def evaluate_postfix(tokens: list[str]) -> float:
    stack = []
    
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
            
        else:
            stack.append(float(token))

    return stack[0]
