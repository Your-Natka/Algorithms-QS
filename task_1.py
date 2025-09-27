# def check_brackets(expression: str) -> str:
#     stack = []
#     # словник відповідностей
#     pairs = {')': '(', ']': '[', '}': '{'}

#     for char in expression:
#         # якщо символ – відкрита дужка → кладемо в стек
#         if char in '([{':
#             stack.append(char)
#         # якщо закрита дужка
#         elif char in ')]}':
#             if not stack or stack[-1] != pairs[char]:
#                 return "Несиметрично"
#             stack.pop()

#     # якщо після проходження стек пустий → симетрично
#     return "Симетрично" if not stack else "Несиметрично"


# # Приклади
# print("( ){[ 1 ]( 1 + 3 )( ){ }}")  # Симетрично
# print("( 23 ( 2 - 3);")             # Несиметрично
# print("( 11 }")                     # Несиметрично

def are_brackets_balanced(s):
    # Стек для зберігання дужок, що відкривають
    stack = []
    # Словник для відповідності дужок, що відкривають і закривають
    brackets = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        # Якщо символ - дужка, що відкриває, додаємо її в стек
        if char in brackets:
            stack.append(char)
        # Якщо символ - закриваюча дужка
        elif char in brackets.values():
            # Якщо стек порожній або дужка, що закриває, не відповідає останній дужці, що відкриває, повертаємо False
            if not stack or brackets[stack.pop()] != char:
                return False
    # Якщо стек порожній, усі дужки збалансовані
    return not stack


if __name__ == "__main__":
    examples = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]
    for example in examples:
        print(
            f"{example}: {'Симетрично' if are_brackets_balanced(example) else 'Несиметрично'}"
        )
