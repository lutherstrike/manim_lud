from manim import *

class RectTxt(VGroup):
    def __init__(self, txt, h=0.8, w=1.8, txt_offset=(0,0,1)):
        super().__init__()
        self.txtidx = 0
        self.txt = Text(txt)
        self.txt_offset = txt_offset
        self.rect = Rectangle(height=h, width=w)
        self.txt.move_to(self.rect.get_center() + self.txt_offset)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center() + self.txt_offset))
        self.add(self.rect, self.txt)
        self.set_color(BLACK, 1)

    def change_content(self, txt):
        self.remove(self.txt)
        self.txt = Text(txt)
        self.txt.add_updater(lambda m : m.move_to(self.rect.get_center() + self.txt_offset))
        self.add(self.txt)

    def get_rect(self):
        return self.rect

    def get_center(self):
        return self.rect.get_center()

    def change_color(self, color, opacity):
        self.rect.set_fill(color, opacity=opacity)
        self.txt.set_fill(BLACK, opacity=1)

    def change_fill(self, color, opacity):
        self.rect.set_fill(color, opacity=opacity)



### REFERENCE: https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html, search for "CircleWithContent"
class CircTxt(VGroup):
    def __init__(self, txt, radius=0.4):
        super().__init__()
        self.txt = Text(txt)
        self.circle = Circle(radius=radius)
        #self.txt.add_updater(lambda m : m.move_to(self.circle.get_center()))
        self.add(self.circle, self.txt)

    def outline_color(self, color, width=1):
        self.circle.set_stroke(color, width=width)

    def move_to(self, coords):
        self.circle.move_to(coords)
        self.txt.move_to( (coords[0], coords[1], coords[2]+1) )

    def txtcolor(self, txtcolor, txtopacity):
        self.txt.set_fill(color=txtcolor, opacity=txtopacity)


class MatrixBasic(VGroup):
    def __init__(self, matrix_size):
        super().__init__()
        self.head_coords = (-2,2,0)
        self.matrix = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        self.anim_step = 0

        for i in range(matrix_size):
            for j in range(matrix_size):
                element = RectTxt(txt=f"" ,h=1.0,w=1.0)
                self.matrix[i][j] = element

        # self.matrix[0][0].move_to(self.head_coords)
        # for i in range(0, matrix_size - 1):
        #     for j in range(0, matrix_size - 1):
        #         self.matrix[i][j].next_to(self.matrix[i][j+1], RIGHT, buff=0)
        #     self.matrix[i][matrix_size-1].next_to(self.matrix[i+1][0], DOWN, buff=0)
        for i in range(matrix_size):
            for j in range(matrix_size):
                self.matrix[i][j].move_to(self.head_coords + np.array([j,-i,0]))
                self.matrix[i][j].set_color(BLACK, 1)

        for i in range(matrix_size):
            for j in range(matrix_size):
                self.add(self.matrix[i][j])

    def set_color(self, color, opacity):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].set_color(color, opacity)

    def change_fill(self, color, opacity):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].change_fill(color, opacity)

    def change_fontsize(self, fontsize):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].txt.scale(fontsize)

    def animate_stepone(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i == self.anim_step and j == self.anim_step:
                    self.matrix[i][j].change_fill(RED_C, 1)
    
class MatrixLarge(VGroup):
    def __init__(self, matrix_size):
        super().__init__()
        self.head_coords = (-2,2,0)
        self.matrix = [[None for _ in range(matrix_size)] for _ in range(matrix_size)]
        self.anim_step = 0

        for i in range(matrix_size):
            for j in range(matrix_size):
                element = RectTxt(txt=f"" ,h= 4.0,w= 4.0)
                self.matrix[i][j] = element

        # self.matrix[0][0].move_to(self.head_coords)
        # for i in range(0, matrix_size - 1):
        #     for j in range(0, matrix_size - 1):
        #         self.matrix[i][j].next_to(self.matrix[i][j+1], RIGHT, buff=0)
        #     self.matrix[i][matrix_size-1].next_to(self.matrix[i+1][0], DOWN, buff=0)
        for i in range(matrix_size):
            for j in range(matrix_size):
                self.matrix[i][j].move_to(self.head_coords + np.array([4 * j,(-4) * i,0]))
                self.matrix[i][j].set_color(BLACK, 1)
                self.matrix[i][j].change_fill(WHITE, 1)

        for i in range(matrix_size):
            for j in range(matrix_size):
                self.add(self.matrix[i][j])

    def set_color(self, color, opacity):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].set_color(color, opacity)

    def change_fill(self, color, opacity):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].change_fill(color, opacity)

    def change_fontsize(self, fontsize):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].txt.scale(fontsize)

    def animate_stepone(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i == self.anim_step and j == self.anim_step:
                    self.matrix[i][j].change_fill(RED_C, 1)
    