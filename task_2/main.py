import sys
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_koch_curve(order, size=400):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()
    try:
        draw_snowflake(t, order, size)
    except Exception as _:
        print("Stop drawing")

    window.mainloop()

def main():
    if len(sys.argv) == 2:
        level = int(sys.argv[1])
        draw_koch_curve(level)
        
    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()