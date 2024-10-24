from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
            time.sleep(0.1) # 100ms delay

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

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

class Cell:
    def __init__(self, win, p1, p2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.__win = win
        
    def draw(self):
        if self.has_left_wall:
            point1 = Point(self.__x1, self.__y1)
            point2 = Point(self.__x1, self.__y2)
            wall = Line(point1, point2)
            win = self.__win
            win.draw_line(wall)
        if self.has_right_wall:
            point1 = Point(self.__x2, self.__y1)
            point2 = Point(self.__x2, self.__y2)
            wall = Line(point1, point2)
            win = self.__win
            win.draw_line(wall)
        if self.has_top_wall:
            point1 = Point(self.__x1, self.__y1)
            point2 = Point(self.__x2, self.__y1)
            wall = Line(point1, point2)
            win = self.__win
            win.draw_line(wall)
        if self.has_bottom_wall:
            point1 = Point(self.__x1, self.__y2)
            point2 = Point(self.__x2, self.__y2)
            wall = Line(point1, point2)
            win = self.__win
            win.draw_line(wall)


