import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt

BLOCK = '#'
EMPTY = ' '
TRACE = '.'
TERMINAL = 'E'
DIR_UP = '↑'
DIR_DOWN = '↓'
DIR_LEFT = '←'
DIR_RIGHT = '→'
DIRS = [DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT]

# 迷宫地图
maze = [
    "#############",
    "#↑ #        #",
    "#  #  ####  #",
    "#  ## #  #  #",
    "#  #E #     #",
    "#  ####  #  #",
    "#  #     #  #",
    "#     #  #  #",
    "#############",
]

# n = int(input())
# maze = []
# for i in range(n):
#     maze.append(list(map(int, input().split())))
# maze[0][0] = DIR_DOWN
# maze[n-1][n-1] = TERMINAL

len_x = len(maze[0])
len_y = len(maze)

class MazeGame(QWidget):
    def __init__(self, maze):
        super().__init__()

        self.setWindowTitle('Maze Game')
        self.setGeometry(600, 600, len_x * 80, len_y * 80)

        self.maze = [list(row) for row in maze]
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.move_history = []

        self.draw_maze()

    def draw_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                label = QLabel()
                if self.maze[i][j] == BLOCK:
                    label.setStyleSheet(
                        "background-color: black; border: 1px solid black;")
                elif self.maze[i][j] == TRACE:
                    label.setStyleSheet(
                        "background-color: gray; border: 1px solid black;")
                else:  # EMPTY, TERMINAL, DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT
                    label.setStyleSheet(
                        "background-color: white; border: 1px solid black;")
                if self.maze[i][j] in DIRS:
                    label.setText(self.maze[i][j])
                elif self.maze[i][j] == TERMINAL:
                    label.setText(TERMINAL)
                self.grid_layout.addWidget(label, i, j)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.move_player(0, -1, DIR_UP)
        elif event.key() == Qt.Key_S:
            self.move_player(0, 1, DIR_DOWN)
        elif event.key() == Qt.Key_A:
            self.move_player(-1, 0, DIR_LEFT)
        elif event.key() == Qt.Key_D:
            self.move_player(1, 0, DIR_RIGHT)
        elif event.key() == Qt.Key_Z:
            self.undo_move()

    def move_player(self, dx, dy, direction):
        x, y = self.find_player()
        new_x, new_y = x + dx, y + dy
        if self.check_move(new_x, new_y):
            prev_direction = self.maze[y][x]
            self.move_history.append((x, y, prev_direction))
            get_to_end = False
            if self.maze[new_y][new_x] == TERMINAL:
                get_to_end = True
            if self.maze[y][x] != TERMINAL:
                self.maze[y][x] = TRACE
            self.maze[new_y][new_x] = direction
            self.draw_maze()
            if get_to_end:
                self.solve_success()

    def check_move(self, x, y):
        if x < 0 or x >= len(self.maze[0]) or y < 0 or y >= len(self.maze) or self.maze[y][x] == BLOCK or self.maze[y][x] == TRACE:
            return False
        return True

    def undo_move(self):
        if not self.move_history:
            return

        x, y, direction = self.move_history.pop()
        prev_x, prev_y = self.find_player()
        self.maze[prev_y][prev_x] = EMPTY
        self.maze[y][x] = direction
        self.draw_maze()

    def find_player(self):
        for y, row in enumerate(self.maze):
            for x, char in enumerate(row):
                if char in DIRS:
                    return x, y

    def solve_success(self):
        QMessageBox.information(self, 'Success', 'You have solved the maze!')
        self.close()


def main():
    app = QApplication(sys.argv)
    game = MazeGame(maze)
    game.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
