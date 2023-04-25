import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt

# 迷宫地图
maze = [
    "#############",
    "#↑ #        #",
    "#  #  ####  #",
    "#  #E #  #  #",
    "#  #  #     #",
    "#  ####  #  #",
    "#  #     #  #",
    "#     #  #  #",
    "#############",
]

class MazeGame(QWidget):
    def __init__(self, maze):
        super().__init__()

        self.setWindowTitle('Maze Game')
        self.setGeometry(300, 300, 400, 400)

        self.maze = [list(row) for row in maze]
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.move_history = []

        self.draw_maze()

    def draw_maze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                label = QLabel()
                if self.maze[i][j] == '#':
                    label.setStyleSheet("background-color: black; border: 1px solid black;")
                elif self.maze[i][j] == '.':
                    label.setStyleSheet("background-color: gray; border: 1px solid black;")
                else:
                    label.setStyleSheet("background-color: white; border: 1px solid black;")
                if self.maze[i][j] in '↑↓←→':
                    label.setText(self.maze[i][j])
                elif self.maze[i][j] == 'E':
                    label.setText('E')
                self.grid_layout.addWidget(label, i, j)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.move_player(0, -1, '↑')
        elif event.key() == Qt.Key_S:
            self.move_player(0, 1, '↓')
        elif event.key() == Qt.Key_A:
            self.move_player(-1, 0, '←')
        elif event.key() == Qt.Key_D:
            self.move_player(1, 0, '→')
        elif event.key() == Qt.Key_Z:
            self.undo_move()

    def move_player(self, dx, dy, direction):
        x, y = self.find_player()
        new_x, new_y = x + dx, y + dy

        if self.maze[new_y][new_x] != '#':
            prev_direction = self.maze[y][x]
            self.move_history.append((x, y, prev_direction))

            if self.maze[y][x] != 'E':
                self.maze[y][x] = '.'
            self.maze[new_y][new_x] = direction
            self.draw_maze()

            if self.maze[new_y][new_x] == 'E':
                self.close()

    def undo_move(self):
        if not self.move_history:
            return

        x, y, direction = self.move_history.pop()
        prev_x, prev_y = self.find_player()
        self.maze[prev_y][prev_x] = ' '
        self.maze[y][x] = direction
        self.draw_maze()

    def find_player(self):
        for y, row in enumerate(self.maze):
            for x, char in enumerate(row):
                if char in '↑↓←→':
                    return x, y

def main():
    app = QApplication(sys.argv)
    game = MazeGame(maze)
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
