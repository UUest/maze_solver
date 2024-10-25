from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, width=width, height=height, bg="white")
        self._canvas.pack(fill=BOTH, expand=True)
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
            time.sleep(0.1) # 100ms delay

    def draw_line(self, line, fill_color="black"):
        line.draw(self._canvas, fill_color)

    def close(self):
        self._running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, Canvas, fill_color="black"):
      Canvas.create_line(
                self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
      )

