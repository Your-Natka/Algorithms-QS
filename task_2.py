# def hanoi(n, source, target, auxiliary, pegs):
#     if n == 1:
#         # переміщення диска
#         disk = pegs[source].pop()
#         pegs[target].append(disk)
#         print(f"Перемістити диск з {source} на {target}: {disk}")
#         print(f"Проміжний стан: {pegs}")
#         return

#     # перемістити n-1 диск з source на auxiliary
#     hanoi(n - 1, source, auxiliary, target, pegs)
    
#     # перемістити останній диск з source на target
#     hanoi(1, source, target, auxiliary, pegs)
    
#     # перемістити n-1 диск з auxiliary на target
#     hanoi(n - 1, auxiliary, target, source, pegs)


# if __name__ == "__main__":
#     n = 3  # кількість дисків
#     pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}  # початковий стан
#     print(f"Початковий стан: {pegs}")
#     hanoi(n, 'A', 'C', 'B', pegs)
#     print(f"Кінцевий стан: {pegs}")
    
    
def move_tower(height, from_pole, to_pole, with_pole, towers):
    if height >= 1:
        # Переміщуємо стек дисків висотою height-1 на допоміжний стрижень
        move_tower(height - 1, from_pole, with_pole, to_pole, towers)
        # Переміщуємо диск на цільовий стрижень
        move_disk(from_pole, to_pole, towers)
        # Переміщуємо стек дисків висотою height-1 з допоміжного стрижня на цільовий
        move_tower(height - 1, with_pole, to_pole, from_pole, towers)


def move_disk(fp, tp, towers):
    disk = towers[fp].pop()  # Вилучаємо диск з вершини стрижня fp
    towers[tp].append(disk)  # Додаємо диск на вершину стрижня tp
    print(f"Перемістити диск з {fp} на {tp}: {disk}")
    print("Проміжний стан:", towers)


if __name__ == "__main__":
    n = 3  # кількість дисків
    # Ініціалізація стержнів
    towers = {"A": list(range(n, 0, -1)), "B": [], "C": []}
    print("Початковий стан:", towers)
    move_tower(n, "A", "C", "B", towers)
    print("Кінцевий стан:", towers)
