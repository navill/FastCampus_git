from lstack import LStack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        return False

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next


class Position:
    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir


class MazeSolver:
    direction = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

    def __init__(self, maze):  # maze : doubled_list
        self.maze = maze
        # EXIT_ROW, EXIT_COL : 출구 행과 열을 나타냄
        self.EXIT_ROW = len(self.maze)
        self.EXIT_COL = len(self.maze[0])

        for row in maze:
            row.insert(0, 1)
            row.append(1)

        added_row = [1 for _ in range(self.EXIT_COL + 2)]
        maze.insert(0, added_row)
        maze.append(added_row)

        self.path = LinkedList()

    def get_path(self):
        stack = LStack()
        # mark : 0으로된 미로 크기의 이중 리스트
        mark = []

        row = None  # 현재 위치
        col = None
        dir = None
        next_row = None  # 이동 가능 여부 확인
        next_col = None
        found = False  # 찾았을 때, True

        # 미로의 시작점
        mark[1][1] = 1
        # 첫 시작 위치 스택에 push
        stack.push(Position(1, 1, 2))

        # stack is empty -> not found final destination
        while not stack.empty() and not found:
            # 경로를 찾기 전, pop에 의해 모든 스택이 비어있을 경우 갈곳이 있는지 검사
            #
            # stack pop -> row, col, dir : current path update
            pos = stack.pop()
            row = pos.row
            col = pos.col
            dir = pos.dir
            # if search the every direction and not found, while is terminated
            while dir < 8 and not found:
                next_row = row + self.direction[dir][0]
                next_col = col + self.direction[dir][1]
                if next_row == self.EXIT_ROW and next_col == self.EXIT_COL:
                    found = True
                    stack.push(Position(row, col, dir))
                    stack.push(Position(next_row, next_col, 0))

                elif self.maze[next_row][next_col] == 0 and mark[next_row][next_col] == 0:
                    mark[next_row][next_col] = 1
                    stack.push(Position(row, col, dir))
                    row = next_row
                    col = next_col
                    dir = 0
                else:
                    dir += 1
        if found:
            while not stack.empty():  # final destination
                self.path.add(stack.pop())
        else:
            print('There is no path in this maze!')

    def print_path(self):
        g = self.path.traverse()
        for node in g:
            print("({}, {})".format(node.data.row, node.data.col))

    def show_maze(self):
        print('   ', end='')
        for i in range(self.EXIT_ROW + 2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW + 2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL + 2):
                if self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()

    def show_path(self):
        path_set = set()
        g = self.path.traverse()
        for node in g:
            path_set.add((node.data.row, node.data.col))

        print('   ', end='')
        for i in range(self.EXIT_ROW + 2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW + 2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL + 2):
                if (i, j) in path_set:
                    print(' P ', end='')
                elif self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()


if __name__ == "__main__":
    maze = [
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0],
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.show_maze()
    maze_solver.get_path()
    maze_solver.print_path()
    maze_solver.show_path()

print('git test')
