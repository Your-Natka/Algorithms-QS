def check_brackets(expression: str) -> str:
    stack = []
    # словник відповідностей
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        # якщо символ – відкрита дужка → кладемо в стек
        if char in '([{':
            stack.append(char)
        # якщо закрита дужка
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()

    # якщо після проходження стек пустий → симетрично
    return "Симетрично" if not stack else "Несиметрично"


# Приклади
print("( ){[ 1 ]( 1 + 3 )( ){ }}")  # Симетрично
print("( 23 ( 2 - 3);")             # Несиметрично
print("( 11 }")                     # Несиметрично
