def tokenize(expression: str) -> list[str]:
    tokens = []
    current_token = ""
    
    for t in expression:
        if t == ' ':
            if current_token:
                if current_token.count('.') > 1:
                    raise Exception(f"Nombre mal formé : {current_token}")
                tokens.append(current_token)
                current_token = ""
        
        elif t == '-' and not current_token and (not tokens or tokens[-1] in "+-*/("):
            current_token += t
            
        elif t in "+*/()":
            if current_token:
                if current_token.count('.') > 1:
                    raise Exception(f"Nombre mal formé : {current_token}")
                tokens.append(current_token)
                current_token = ""
            tokens.append(t)
            
        elif t not in "0123456789.+-*/() ":
            raise Exception(f"Opérateur inconnu : {t}")
            
        else:
            if t == '-' and current_token:
                if current_token.count('.') > 1:
                    raise Exception(f"Nombre mal formé : {current_token}")
                tokens.append(current_token)
                tokens.append(t)
                current_token = ""
            else:
                current_token += t

    if current_token:
        if current_token.count('.') > 1:
            raise Exception(f"Nombre mal formé : {current_token}")
        tokens.append(current_token)
        
    return tokens

def infix_to_postfix(tokens: list[str]) -> list[str]:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []
    dernier_token = None

    for token in tokens:

        if token == '(':
            operator_stack.append(token)

        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())

            if not operator_stack:
                raise Exception("Parenthèses non appariées : ) en trop")

            operator_stack.pop()

        elif token in precedence:

            if dernier_token is None or dernier_token in "+-*/(":
                raise Exception("Expression invalide")

            while (operator_stack and operator_stack[-1] != '(' and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output.append(operator_stack.pop())

            operator_stack.append(token)

        else:
            output.append(token)

        dernier_token = token

    if dernier_token in "+-*/":
        raise Exception("Expression invalide")

    while operator_stack:
        op = operator_stack.pop()
        if op == '(':
            raise Exception("Parenthèses non appariées : ( non fermée")
        output.append(op)

    return output


def evaluate_postfix(tokens: list[str]) -> float:
    stack = []

    for token in tokens:

        if token in "+-*/":

            if len(stack) < 2:
                raise Exception("Expression invalide")

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

            elif token == '/':
                if b == 0:
                    raise Exception("Division par zéro")
                stack.append(a / b)

        else:
            try:
                stack.append(float(token))
            except:
                raise Exception(f"Nombre mal formé : {token}")

    if len(stack) != 1:
        raise Exception("Expression invalide")

    return stack[0]