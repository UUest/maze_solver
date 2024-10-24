from visuals import Window, Point, Line, Cell 

def main():
    win = Window(800, 600)
    point1 = Point(100,100)
    point2 = Point(200,200)
    point3 = Point(300,300)
    point4 = Point(400,400)
    point5 = Point(500,500)
    point6 = Point(600,600)
    point7 = Point(700,700)
    point8 = Point(800,800)
    cell1 = Cell(win, point1, point2)
    cell2 = Cell(win, point2, point3)
    cell3 = Cell(win, point3, point4)
    cell3.has_top_wall = False
    cell3.has_bottom_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
