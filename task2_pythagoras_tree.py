import turtle
import math

def draw_tree(t, branch_len, level):
    if level == 0:
        return
    t.forward(branch_len)
    t.left(45)
    draw_tree(t, branch_len * math.sqrt(2)/2, level - 1)
    t.right(90)
    draw_tree(t, branch_len * math.sqrt(2)/2, level - 1)
    t.left(45)
    t.backward(branch_len)

if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.left(90)
    draw_tree(t, 100, level)
    screen.mainloop()
