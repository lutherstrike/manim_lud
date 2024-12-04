from manim import *
import basic_object as bo

class LUDBasic(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    def create_matrix(data):
      table = Table(
        [[str(item) for item in row] for row in data],
        include_outer_lines=True,
        element_to_mobject=lambda elem: Text(elem, color=BLACK)
      ).scale(0.8)

      table.get_horizontal_lines().set_color(BLACK).set_stroke(width=2)
      table.get_vertical_lines().set_color(BLACK).set_stroke(width=2)

      return table
    
    matrix_a = create_matrix(
      [[2, 3, 1],
       [4, 7, 2],
       [6, 18, 5]]
    )
    matrix_l = create_matrix(
      [[1, 0, 0],
       [2, 1, 0],
       [3, 6, 1]]
    )
    matrix_u = create_matrix(
      [[2, 3, 1],
       [0, 1, -0.5],
       [0, 0, 1]]
    )

    # a_group = VGroup(matrix_a)
    # l_group = VGroup(matrix_l).set_color(BLACK)
    # u_group = VGroup(matrix_u)

    # # a_group.to_edge(LEFT, buff=1)
    # # l_group.next_to(a_group, RIGHT, buff=1)
    # # u_group.next_to(l_group, RIGHT, buff=1)

    # a_group.move_to((-5, 0, 0))
    # l_group.move_to((0, 0, 0))
    # u_group.move_to((5, 0, 0))

    matrix_a.move_to((-5, 0, 0))
    matrix_l.move_to((0, 0, 0))
    matrix_u.move_to((5, 0, 0))

    equal = Text("=", font_size=36, color=BLACK)
    multiplication = Text("x", font_size=36, color=BLACK)

    equal.move_to((-2.5, 0, 0))
    multiplication.move_to((2.4, 0, 0))

    # equal_group = VGroup(equal)
    # multiplication_group = VGroup(multiplication)

    content_group = VGroup(matrix_a, matrix_l, matrix_u).set_color(BLACK)
    self.camera.frame.save_state()  # Save initial camera state
    self.play(
        self.camera.frame.animate.set(width=content_group.width + 1).move_to(content_group.get_center())
    )
    
    self.add(matrix_a)
    self.wait()

    self.add(equal, matrix_l) 
    self.wait(2)

    self.add(multiplication, matrix_u)
    self.wait(1)

class iterativeLUDFirst(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)
    basic_unit.move_to(ORIGIN)

    self.camera.frame.set_width(basic_unit.width * 2).move_to(basic_unit.get_center())
    self.add(basic_unit)
    self.wait(1)

    self.play(AnimationGroup(
      basic_unit.matrix[0][0].animate.change_fill(GREEN, 1),
      basic_unit.matrix[0][1].animate.change_fill(GREEN, 1),
      basic_unit.matrix[0][2].animate.change_fill(GREEN, 1),
      basic_unit.matrix[0][3].animate.change_fill(GREEN, 1),
    ))
    self.wait(1)

    row_group = VGroup(basic_unit.matrix[0][0], basic_unit.matrix[0][1], basic_unit.matrix[0][2], basic_unit.matrix[0][3]).copy()
    row_operation = Text("keep the same value", font_size=36, color=BLACK).move_to(row_group.get_center() + (4.5, 0, 0))

    all_objects = VGroup(basic_unit, row_group, row_operation)
    self.play(
      AnimationGroup(
      row_group.animate.move_to(row_group.get_center() + (4.5, 1, 0)),
      self.camera.frame.animate.set_width(all_objects.width * 1.2).move_to(all_objects.get_center() + 0.5 * UP)
      )
    )
    self.play(FadeIn(row_operation))
    self.wait(1)

    self.play(AnimationGroup(basic_unit.matrix[0][0].animate.change_fill(PURE_RED, 1)))
    self.wait(1)

    self.play(AnimationGroup(
      basic_unit.matrix[1][0].animate.change_fill(ORANGE, 1),
      basic_unit.matrix[2][0].animate.change_fill(ORANGE, 1),
      basic_unit.matrix[3][0].animate.change_fill(ORANGE, 1),
    ))

    column_group = VGroup(basic_unit.matrix[1][0], basic_unit.matrix[2][0], basic_unit.matrix[3][0])
    divisiion = Text("/=", font_size=36, color=BLACK).move_to(column_group.get_center() + (6, 0, 0))

    self.play(AnimationGroup(
      column_group.copy().animate.shift(RIGHT * 5),
      Create(divisiion),
      basic_unit.matrix[0][0].copy().animate.shift(RIGHT * 7 + DOWN * 2)
    ))

    all_objects = VGroup(basic_unit, row_group, row_operation, column_group, divisiion)
    # self.play(
    #   self.camera.frame.animate.set_width(all_objects.width * 1.3).move_to(all_objects.get_center() + 0.5 * RIGHT + 0.5 * UP)
    # )
  
    # self.play(AnimationGroup(test_unit.animate.animate_stepone()))
    # self.wait(1)
    
    # test_vect = test_unit.copy()
    # test_vect.move_to(test_vect.get_center() + np.array([2,0,0]))
    # test_vect.change_fill(ORANGE, 1)

    # self.add(test_vect)
    # self.wait(1)

class iterativeLUDSecond(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)
    
    basic_unit.matrix[0][1].change_fill(GREEN, 1)
    basic_unit.matrix[0][2].change_fill(GREEN, 1)
    basic_unit.matrix[0][3].change_fill(GREEN, 1)
    basic_unit.matrix[0][0].change_fill(PURE_RED, 1)
    basic_unit.matrix[1][0].change_fill(ORANGE, 1)
    basic_unit.matrix[2][0].change_fill(ORANGE, 1)
    basic_unit.matrix[3][0].change_fill(ORANGE, 1)

    # Resume the first step 
    

    row_elements = []
    col_elements = []
    for i in range(3):
      row_elements.append(bo.RectTxt(txt="", h=1.0, w=1.0))
      col_elements.append(bo.RectTxt(txt="", h=1.0, w=1.0))

    row_elements[0].move_to(basic_unit.matrix[0][1].get_center())
    row_elements[1].move_to(basic_unit.matrix[0][2].get_center())
    row_elements[2].move_to(basic_unit.matrix[0][3].get_center())
    col_elements[0].move_to(basic_unit.matrix[1][0].get_center())
    col_elements[1].move_to(basic_unit.matrix[2][0].get_center())
    col_elements[2].move_to(basic_unit.matrix[3][0].get_center())

    row_elements[0].change_fill(GREEN, 1)
    row_elements[1].change_fill(GREEN, 1)
    row_elements[2].change_fill(GREEN, 1)
    col_elements[0].change_fill(ORANGE, 1)
    col_elements[1].change_fill(ORANGE, 1)
    col_elements[2].change_fill(ORANGE, 1)

    row_vec = VGroup(row_elements[0], row_elements[1], row_elements[2])
    col_vec = VGroup(col_elements[0], col_elements[1], col_elements[2])

    # all_objects = VGroup(basic_unit, row_vec, col_vec)

    # all_objects.move_to(ORIGIN)  # Center the group
    # all_objects.scale_to_fit_width(self.camera.frame_width * 0.9)  # Fit width with a 10% margin
    # all_objects.scale_to_fit_height(self.camera.frame_height * 0.9) 

    # col_vec.shift(RIGHT * 5)
    # row_vec.shift(RIGHT * 6)
    # row_vec.shift(DOWN * 2)
    self.camera.frame.set_width(basic_unit.width * 2).move_to(basic_unit.get_center())

    self.add(basic_unit)
    self.wait(1)

    self.add(row_vec, col_vec)
    
    self.play(AnimationGroup(
      col_vec.animate.shift(RIGHT * 5),
      row_vec.animate.shift(RIGHT * 6 + DOWN * 2)
    ))

    all_objects = VGroup(basic_unit, row_vec, col_vec)
    equals = Text("-=", font_size=36, color=BLACK).move_to((2, 0, 0))
    multiplication_sign = Text("x", font_size=36, color=BLACK).move_to((4, 0, 0))

    self.play(
      AnimationGroup(
      self.camera.frame.animate.set_width(all_objects.width * 1.2).move_to(all_objects.get_center()),
      basic_unit.matrix[1][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[1][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[1][3].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][3].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][3].animate.change_fill(BLUE, 1),
      Create(equals),
      Create(multiplication_sign),
      basic_unit.matrix[0][0].animate.change_fill(WHITE, 1),
      basic_unit.matrix[0][1].animate.change_fill(WHITE, 1),
      basic_unit.matrix[0][2].animate.change_fill(WHITE, 1),
      basic_unit.matrix[0][3].animate.change_fill(WHITE, 1),
      basic_unit.matrix[1][0].animate.change_fill(WHITE, 1),
      basic_unit.matrix[2][0].animate.change_fill(WHITE, 1),
      basic_unit.matrix[3][0].animate.change_fill(WHITE, 1),
      )
    )

    self.wait(1)
       
class iterativeLUDThird(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(16)
    
    target_element = bo.RectTxt(txt="", h=1.0, w=1.0)
    target_element.move_to(basic_unit.matrix[12][14].get_center())

    row_elements = []
    col_elements = []

    for i in range(12):
      row_elements.append(bo.RectTxt(txt="", h=1.0, w=1.0))
      col_elements.append(bo.RectTxt(txt="", h=1.0, w=1.0))

    for i in range(12):
      row_elements[i].move_to(basic_unit.matrix[12][i].get_center())
      col_elements[i].move_to(basic_unit.matrix[i][14].get_center())

    row_vec = VGroup(row_elements[0], row_elements[1], row_elements[2], row_elements[3], row_elements[4], row_elements[5], row_elements[6], row_elements[7], row_elements[8], row_elements[9], row_elements[10], row_elements[11])
    col_vec = VGroup(col_elements[0], col_elements[1], col_elements[2], col_elements[3], col_elements[4], col_elements[5], col_elements[6], col_elements[7], col_elements[8], col_elements[9], col_elements[10], col_elements[11])

    self.camera.frame.set_width(basic_unit.width * 2).move_to(basic_unit.get_center())

    self.add(basic_unit)
    self.wait(0.5)

    self.play(AnimationGroup(
      target_element.animate.change_fill(BLUE, 1),
    ))
    self.wait(0.5)

    self.play(AnimationGroup(
      [col_elements[i].animate.change_fill(GREEN, 1) for i in range(12)],
      [row_elements[i].animate.change_fill(ORANGE, 1) for i in range(12)]
    ))
    self.wait(0.5)

    target_element_copy = target_element.copy()
    row_vec_copy = row_vec.copy()
    col_vec_copy = col_vec.copy()

    self.add(target_element_copy, row_vec_copy, col_vec_copy)
    
    self.play(AnimationGroup(
      target_element.animate.shift(RIGHT * 3 + UP * 5),
      row_vec.animate.shift(RIGHT * 20 + UP * 5),
      col_vec.animate.shift(RIGHT * 20 + DOWN * 2)
    ))

    all_objects = VGroup(basic_unit, row_vec, col_vec)
    equals = Text("-=", font_size=80, color=BLACK).move_to(target_element.get_center() + (1.5, 0, 0))
    multiplication_sign = Text("x", font_size=70, color=BLACK).move_to(target_element.get_center() + (15.5, 0, 0))

    self.play(
      AnimationGroup(
      self.camera.frame.animate.set_width(all_objects.width * 1.2).move_to(all_objects.get_center()),
      Create(equals),
      Create(multiplication_sign),
      )
    )
       

class blockLUD(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(16)
    large_unit = bo.MatrixLarge(4)

    large_unit.move_to(basic_unit.get_center())
    # large_unit.change_fill(WHITE, 1)

    self.camera.frame.set_height(basic_unit.height * 1.2).move_to(basic_unit.get_center())

    self.add(basic_unit)
    self.wait(1)

    self.play(FadeIn(large_unit))
    self.wait(1)

    self.play(
      AnimationGroup(
      large_unit.matrix[0][0].animate.change_fill(PURE_RED, 1),
      Transform(large_unit.matrix[0][0].txt, Text("C", font_size=200, color=BLACK, font="Helvetica").move_to(large_unit.matrix[0][0].get_center()))
      )
    )
    self.wait(1)

    self.play(
      AnimationGroup(
      large_unit.matrix[0][1].animate.change_fill(GREEN, 1),
      large_unit.matrix[0][2].animate.change_fill(GREEN, 1),
      large_unit.matrix[0][3].animate.change_fill(GREEN, 1),
      large_unit.matrix[1][0].animate.change_fill(ORANGE, 1),
      large_unit.matrix[2][0].animate.change_fill(ORANGE, 1),
      large_unit.matrix[3][0].animate.change_fill(ORANGE, 1),
      Transform(large_unit.matrix[0][2].txt, Text("U", font_size=200, color=BLACK, font="Helvetica").move_to(large_unit.matrix[0][2].get_center())),
      Transform(large_unit.matrix[2][0].txt, Text("L", font_size=200, color=BLACK, font="Helvetica").move_to(large_unit.matrix[2][0].get_center()))
      )
    )
    self.wait(1)

    self.play(
      AnimationGroup(
      large_unit.matrix[1][1].animate.change_fill(BLUE, 1),
      large_unit.matrix[1][2].animate.change_fill(BLUE, 1),
      large_unit.matrix[1][3].animate.change_fill(BLUE, 1),
      large_unit.matrix[2][1].animate.change_fill(BLUE, 1),
      large_unit.matrix[2][2].animate.change_fill(BLUE, 1),
      large_unit.matrix[2][3].animate.change_fill(BLUE, 1),
      large_unit.matrix[3][1].animate.change_fill(BLUE, 1),
      large_unit.matrix[3][2].animate.change_fill(BLUE, 1),
      large_unit.matrix[3][3].animate.change_fill(BLUE, 1),
      Transform(large_unit.matrix[2][2].txt, Text("T", font_size=200, color=BLACK, font="Helvetica").move_to(large_unit.matrix[2][2].get_center())),
      )
    )
    self.wait(1)

class blockLUDSecond(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)

    self.camera.frame.set_width(basic_unit.width * 2).move_to(basic_unit.get_center())

    self.add(basic_unit)
    self.play(AnimationGroup(
      basic_unit.matrix[0][0].animate.change_fill(PURE_RED, 1),
      Transform(basic_unit.matrix[0][0].txt, Text("C", font_size=50, color=BLACK, font="Helvetica").move_to(basic_unit.matrix[0][0].get_center()))
    ))

    self.wait(2)  
    self.play(AnimationGroup(
      basic_unit.matrix[0][1].animate.change_fill(GREEN, 1),
      basic_unit.matrix[0][2].animate.change_fill(GREEN, 1),
      basic_unit.matrix[0][3].animate.change_fill(GREEN, 1),
      basic_unit.matrix[1][0].animate.change_fill(ORANGE, 1),
      basic_unit.matrix[2][0].animate.change_fill(ORANGE, 1),
      basic_unit.matrix[3][0].animate.change_fill(ORANGE, 1),
      Transform(basic_unit.matrix[0][2].txt, Text("U", font_size=50, color=BLACK, font="Helvetica").move_to(basic_unit.matrix[0][2].get_center())),
      Transform(basic_unit.matrix[2][0].txt, Text("L", font_size=50, color=BLACK, font="Helvetica").move_to(basic_unit.matrix[2][0].get_center()))
    ))

    self.wait(2)
    self.play(AnimationGroup(
      basic_unit.matrix[1][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[1][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[1][3].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[2][3].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][1].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][2].animate.change_fill(BLUE, 1),
      basic_unit.matrix[3][3].animate.change_fill(BLUE, 1),
      Transform(basic_unit.matrix[2][2].txt, Text("T", font_size=50, color=BLACK, font="Helvetica").move_to(basic_unit.matrix[2][2].get_center()))
    ))

    upper_block = basic_unit.matrix[0][1].copy()
    lower_block = basic_unit.matrix[1][0].copy()
    trailing_block = basic_unit.matrix[1][1].copy()

    self.add(upper_block, lower_block, trailing_block)
    self.play(AnimationGroup(
      trailing_block.animate.shift(RIGHT * 4 + DOWN * 1),
      lower_block.animate.shift(RIGHT * 7 + DOWN * 1),
      upper_block.animate.shift(RIGHT * 8 + DOWN * 2),
    ))

    all_objects = VGroup(basic_unit, upper_block, lower_block, trailing_block)

    equals = Text("-= ", font_size=50, color=BLACK).move_to(trailing_block.get_center() + (1, 0, 0))
    multiplication_sign = Text("x", font_size=50, color=BLACK).move_to(lower_block.get_center() + (1, 0, 0))

    self.play(
      AnimationGroup(
      self.camera.frame.animate.set_width(all_objects.width * 1.2).move_to(all_objects.get_center()),
      Create(equals),
      Create(multiplication_sign),
      )
    )

    self.wait(1)


class blockLUDThird(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    #initilize block unit
    block_unit = bo.MatrixLarge(4)
    
    block_unit.move_to(ORIGIN)
    # block_unit.matrix[0][0].txt = Text("C", font_size=50, color=BLACK, font="Helvetica").move_to(block_unit.matrix[0][0].get_center())
    # block_unit.matrix[0][2].txt = Text("U", font_size=50, color=BLACK, font="Helvetica").move_to(block_unit.matrix[0][2].get_center())
    # block_unit.matrix[2][0].txt = Text("L", font_size=50, color=BLACK, font="Helvetica").move_to(block_unit.matrix[2][0].get_center())
    self.camera.frame.set_width(block_unit.width * 2).move_to(block_unit.get_center())
    
    self.play(
      AnimationGroup(
        FadeIn(block_unit),
        block_unit.matrix[0][0].animate.change_fill(PURE_RED, 1),
        block_unit.matrix[0][1].animate.change_fill(GREEN, 1),
        block_unit.matrix[0][2].animate.change_fill(GREEN, 1),
        block_unit.matrix[0][3].animate.change_fill(GREEN, 1),
        block_unit.matrix[1][0].animate.change_fill(ORANGE, 1),
        block_unit.matrix[2][0].animate.change_fill(ORANGE, 1),
        block_unit.matrix[3][0].animate.change_fill(ORANGE, 1),
        block_unit.matrix[1][1].animate.change_fill(BLUE, 1),
        block_unit.matrix[1][2].animate.change_fill(BLUE, 1),
        block_unit.matrix[1][3].animate.change_fill(BLUE, 1),
        block_unit.matrix[2][1].animate.change_fill(BLUE, 1),
        block_unit.matrix[2][2].animate.change_fill(BLUE, 1),
        block_unit.matrix[2][3].animate.change_fill(BLUE, 1),
        block_unit.matrix[3][1].animate.change_fill(BLUE, 1),
        block_unit.matrix[3][2].animate.change_fill(BLUE, 1),
        block_unit.matrix[3][3].animate.change_fill(BLUE, 1),
        Transform(block_unit.matrix[0][0].txt, Text("C", font_size=100, color=BLACK, font="Helvetica").move_to(block_unit.matrix[0][0].get_center())),
        Transform(block_unit.matrix[0][2].txt, Text("U", font_size=100, color=BLACK, font="Helvetica").move_to(block_unit.matrix[0][2].get_center())),
        Transform(block_unit.matrix[2][0].txt, Text("L", font_size=100, color=BLACK, font="Helvetica").move_to(block_unit.matrix[2][0].get_center())),
        Transform(block_unit.matrix[2][2].txt, Text("T", font_size=100, color=BLACK, font="Helvetica").move_to(block_unit.matrix[2][2].get_center())),
      )
    )
    self.wait(1)
    condition = lambda i, j: i == 0 and j == 0 or i == 2 and j == 0
    animation_group = [block_unit.matrix[i][j] for i in range(4) for j in range(4) if not condition(i, j)]
    self.play(
      AnimationGroup(
        FadeOut(*animation_group),
      )
    )
    self.wait(2)

    corner_unit = bo.MatrixBasic(4)
    lower_unit = bo.MatrixBasic(4)
    corner_unit.move_to(block_unit.matrix[0][0].get_center())
    lower_unit.move_to(block_unit.matrix[2][0].get_center())

    corner_label = Text("C", font_size=100, color=PURE_RED).move_to(corner_unit.get_center())
    lower_label = Text("L", font_size=100, color=ORANGE).move_to(lower_unit.get_center())

    self.play(
      AnimationGroup(
        FadeOut(block_unit.matrix[0][0]),
        FadeOut(block_unit.matrix[2][0]),
        FadeIn(corner_unit),
        FadeIn(lower_unit),
        corner_label.animate.move_to(corner_unit.get_center() + LEFT * 3),
        lower_label.animate.move_to(lower_unit.get_center() + LEFT * 3),
      )
    )

    self.wait(1)
    
    current_objects = VGroup(corner_unit, lower_unit, corner_label, lower_label)

    self.play(
      AnimationGroup(
        self.camera.frame.animate.set_height(current_objects.height * 1.1).move_to(current_objects.get_center() + UP * 2 + RIGHT * 5),
        lower_label.animate.shift(UP * 3),
        lower_unit.animate.shift(UP * 3),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        *[lower_unit.matrix[i][2].animate.change_fill(DARK_BROWN, 1) for i in range(4)],
      ) 
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        *[lower_unit.matrix[i][j].animate.change_fill(ORANGE, 1) for i in range(4) for j in range(2)],
        # lower_unit.matrix[2][0].animate.change_fill(ORANGE, 1),
        # lower_unit.matrix[2][1].animate.change_fill(ORANGE, 1),
        corner_unit.matrix[0][2].animate.change_fill(GREEN, 1),
        corner_unit.matrix[1][2].animate.change_fill(GREEN, 1),
        corner_unit.matrix[2][2].animate.change_fill(PURE_RED , 1),
      )
    )

    row_elements = []
    col_elements = [] 

    row_elements.append(lower_unit.matrix[2][0].copy())
    row_elements.append(lower_unit.matrix[2][1].copy())

    col_elements.append(corner_unit.matrix[0][2].copy())
    col_elements.append(corner_unit.matrix[1][2].copy())

    # row_vec = VGroup(row_elements[0], row_elements[1])
    row_elements = [lower_unit.matrix[i][j].copy() for i in range(4) for j in range(2)]
    row_vec = VGroup(*row_elements)
    col_vec = VGroup(col_elements[0], col_elements[1])

    # target_element = lower_unit.matrix[2][2].copy()
    target_elements = [lower_unit.matrix[i][2].copy() for i in range(4)]
    target_element = VGroup(*target_elements)

    divide = corner_unit.matrix[2][2].copy()

    self.wait(1)
    self.add(row_vec, col_vec, target_element, divide)
    self.play(
      AnimationGroup(
        row_vec.animate.shift(RIGHT * 10 + UP * 4.5),
        col_vec.animate.shift(RIGHT * 11 + DOWN * 2.5 + UP * 1),
        target_element.animate.shift(RIGHT * 6 + UP * 4.5),
        divide.animate.shift(RIGHT * 8.5 + DOWN * 3.5)
      )
    )

    all_objects = VGroup(corner_unit, lower_unit, corner_label, lower_label, row_vec, col_vec, target_element, divide)

    equals = Text("- ", font_size=50, color=BLACK).move_to(target_element.get_center() + (1, 0, 0))
    multiplication_sign = Text("x", font_size=50, color=BLACK).move_to(row_vec.get_center() + (1.5, 0, 0))
    horizontal_line = Line(start=[-3.5, 2, 0], end=[3.5, 2, 0], color=BLACK, stroke_width=4).move_to(divide.get_center() + 
    (0, 1, 0))
    results = target_element.copy().move_to(horizontal_line.get_center() + LEFT * 5)
    equal = Text("=", font_size=50, color=BLACK).move_to(results.get_center() + RIGHT)
    self.play(
      # self.camera.frame.animate.set_width(all_objects.width * 1.1).move_to(all_objects.get_center()),
      Create(equals),
      Create(multiplication_sign),
      Create(horizontal_line),
      Create(results),
      Create(equal)
    )

class systolicArrayStructure(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE
    basic_unit = bo.MatrixBasic(4)

    systolic_array = [[None for _ in range(4)] for _ in range(4)]

    for i in range(4):
      for j in range(4):
        element = bo.RectTxt(txt="PE", h=1.5, w=1.5)
        systolic_array[i][j] = element
        systolic_array[i][j].move_to(ORIGIN + np.array([2 * j, -2 * i, 0]))
        systolic_array[i][j].set_color(BLACK, 1)
    
    systolic_array_group = VGroup(*[systolic_array[i][j] for i in range(4) for j in range(4)])
    self.camera.frame.set_width(systolic_array_group.width * 2).move_to(systolic_array_group.get_center())

    horizontal_fifo_lines = []
    for i in range(4):
      for j in range(3):
        horizontal_fifo_lines.append(
          Line(start = systolic_array[i][j].get_right(),
               end = systolic_array[i][j+1].get_left(),
               color=BLACK, stroke_width=2).add_tip(tip_length=0.2, tip_width=0.1)
        )
    horizontal_fifo_lines_group = VGroup(*horizontal_fifo_lines)

    vertical_fifo_lines = []
    for i in range(3):
      for j in range(4):
        vertical_fifo_lines.append(
          Line(start = systolic_array[i][j].get_bottom(),
               end = systolic_array[i+1][j].get_top(),
               color=BLACK, stroke_width=2).add_tip(tip_length=0.2, tip_width=0.1)
        )
    vertical_fifo_lines_group = VGroup(*vertical_fifo_lines)

    self.add(systolic_array_group, horizontal_fifo_lines_group, vertical_fifo_lines_group)
    self.wait(1)

    self.play(
      AnimationGroup(
        *[systolic_array[i][j].animate.change_fill(BLUE, 1) for i in range(4) for j in range(4) if i != j],
      )
    )

    self.play(
      AnimationGroup(
        *[systolic_array[i][j].animate.change_fill(PURE_RED, 1) for i in range(4) for j in range(4) if i == j],
      )
    )
    self.wait(1)
    
    self.wait(1)
    
    selected_condition = lambda i, j: i == 1 and j == 1 or i == 0 and j == 1
    disappearing_elements = [systolic_array[i][j] for i in range(4) for j in range(4) if not selected_condition(i, j)]

    diagonal_label = Text("Diagonal \n   PE", font_size=36, color=BLACK).move_to(systolic_array[1][1].get_center() + LEFT * 3)
    non_diagonal_label = Text("Non-diagonal \n      PE", font_size=36, color=BLACK).move_to(systolic_array[0][1].get_center() + LEFT * 3)

    self.play(
      AnimationGroup(
        FadeOut(*disappearing_elements),
        FadeOut(horizontal_fifo_lines_group),
        FadeOut(vertical_fifo_lines_group),
        FadeIn(diagonal_label),
        FadeIn(non_diagonal_label)
      )
    )

    diagonalImage = ImageMobject("images/DiagonalPE.png")
    nonDiagonalImage = ImageMobject("images/NonDiagonalPE.png")

    diagonalImage.move_to(systolic_array[1][1].get_center() + RIGHT * 5 + DOWN * 1)
    nonDiagonalImage.move_to(systolic_array[0][1].get_center() + RIGHT * 5 + UP * 1)

    all_objects = Group(diagonal_label, non_diagonal_label, diagonalImage, nonDiagonalImage)
    self.play(
      AnimationGroup(
        self.camera.frame.animate.set_width(all_objects.width * 1.1).move_to(all_objects.get_center()),
      )
    )
    self.play(FadeIn(nonDiagonalImage))
    self.wait(2)  
    self.play(FadeIn(diagonalImage))
    self.wait(1)


class systolicArray(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)

    systolic_array = [[None for _ in range(4)] for _ in range(4)]

    for i in range(4):
      for j in range(4):
        element = bo.RectTxt(txt="PE", h=1.5, w=1.5)
        systolic_array[i][j] = element
        systolic_array[i][j].move_to(ORIGIN + np.array([2 * j, -2 * i, 0]))
        systolic_array[i][j].set_color(BLACK, 1)
    
    systolic_array_group = VGroup(*[systolic_array[i][j] for i in range(4) for j in range(4)])
    self.camera.frame.set_width(systolic_array_group.width * 2).move_to(systolic_array_group.get_center())

    horizontal_fifo_lines = []
    for i in range(4):
      for j in range(3):
        horizontal_fifo_lines.append(
          Line(start = systolic_array[i][j].get_right(),
               end = systolic_array[i][j+1].get_left(),
               color=BLACK, stroke_width=2).add_tip(tip_length=0.2, tip_width=0.1)
        )
    horizontal_fifo_lines_group = VGroup(*horizontal_fifo_lines)

    vertical_fifo_lines = []
    for i in range(3):
      for j in range(4):
        vertical_fifo_lines.append(
          Line(start = systolic_array[i][j].get_bottom(),
               end = systolic_array[i+1][j].get_top(),
               color=BLACK, stroke_width=2).add_tip(tip_length=0.2, tip_width=0.1)
        )
    vertical_fifo_lines_group = VGroup(*vertical_fifo_lines)

    self.add(systolic_array_group, horizontal_fifo_lines_group, vertical_fifo_lines_group)
    self.wait(1)

    basic_unit.move_to(systolic_array_group.get_center() + LEFT * 7)
    basic_unit.matrix[0][0].change_fill(PURE_RED, 1)
    basic_unit.matrix[0][1].change_fill(GREEN, 1)
    basic_unit.matrix[0][2].change_fill(GREEN, 1)
    basic_unit.matrix[0][3].change_fill(GREEN, 1)
    basic_unit.matrix[1][0].change_fill(ORANGE, 1)
    basic_unit.matrix[2][0].change_fill(ORANGE, 1)
    basic_unit.matrix[3][0].change_fill(ORANGE, 1)
    for i in range(1, 4):
      for j in range(1, 4):
        basic_unit.matrix[i][j].change_fill(BLUE, 1)

    all_objects = VGroup(systolic_array_group, horizontal_fifo_lines_group, vertical_fifo_lines_group, basic_unit)
    self.play(
      AnimationGroup(
        self.camera.frame.animate.set_width(all_objects.width * 1.2).move_to(all_objects.get_center()),
      )
    )
    self.add(basic_unit)
    self.wait(1)

    dummy_unit = basic_unit.copy()
    self.add(dummy_unit)

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(systolic_array[i][0].get_center()) for i in range(4)],
      )
    )
    self.wait(1)
    
    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(systolic_array[i][1].get_center()) for i in range(4)],
        [basic_unit.matrix[i][1].animate.move_to(systolic_array[i][0].get_center()) for i in range(4)],
      )
    )

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(systolic_array[i][2].get_center()) for i in range(4)],
        [basic_unit.matrix[i][1].animate.move_to(systolic_array[i][1].get_center()) for i in range(4)],
        [basic_unit.matrix[i][2].animate.move_to(systolic_array[i][0].get_center()) for i in range(4)],
      )
    )

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(systolic_array[i][3].get_center()) for i in range(4)],
        [basic_unit.matrix[i][1].animate.move_to(systolic_array[i][2].get_center()) for i in range(4)],
        [basic_unit.matrix[i][2].animate.move_to(systolic_array[i][1].get_center()) for i in range(4)],
        [basic_unit.matrix[i][3].animate.move_to(systolic_array[i][0].get_center()) for i in range(4)],
      )
    )

    self.play( 
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(systolic_array[i][3].get_center() + RIGHT * 3) for i in range(4)],
        [basic_unit.matrix[i][1].animate.move_to(systolic_array[i][3].get_center()) for i in range(4)],
        [basic_unit.matrix[i][2].animate.move_to(systolic_array[i][2].get_center()) for i in range(4)],
        [basic_unit.matrix[i][3].animate.move_to(systolic_array[i][1].get_center()) for i in range(4)],
      )
    )

    self.play(
      AnimationGroup( 
        [basic_unit.matrix[i][1].animate.move_to(systolic_array[i][3].get_center() + RIGHT * 4) for i in range(4)],
        [basic_unit.matrix[i][2].animate.move_to(systolic_array[i][3].get_center()) for i in range(4)],
        [basic_unit.matrix[i][3].animate.move_to(systolic_array[i][2].get_center()) for i in range(4)],
      )
    )

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][2].animate.move_to(systolic_array[i][3].get_center() + RIGHT * 5) for i in range(4)],
        [basic_unit.matrix[i][3].animate.move_to(systolic_array[i][3].get_center()) for i in range(4)],
      )
    )

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][3].animate.move_to(systolic_array[i][3].get_center() + RIGHT * 6) for i in range(4)],
      )
    )
    self.wait(2)

    self.play(
      self.camera.frame.animate.set_width(systolic_array_group.width * 3).move_to(systolic_array_group.get_center())
    )


    new_systolic_array = []
    for i in range(4):
      element = bo.RectTxt(txt="PEG", h=8, w=1.5)
      element.move_to(systolic_array_group.get_center() + LEFT * 3 + i * RIGHT * 2)
      element.set_color(BLACK, 1)
      new_systolic_array.append(element)

    self.play(
      AnimationGroup(
      [FadeIn(new_systolic_array[i]) for i in range(4)],
      FadeOut(systolic_array_group),
      FadeOut(vertical_fifo_lines_group)
      )
    )


class systolicArrayCorner(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    peg_array = []
    for i in range(4):
      element = bo.RectTxt(txt=f"PEG {i} \n {4 - i} x {4 - i}", h=6, w = 6, txt_offset=UP * 2)
      element.move_to(ORIGIN + i * RIGHT * 7)
      element.set_color(BLACK, 1)
      peg_array.append(element)

    fifo_lines = []
    for i in range(3):
      fifo_lines.append(
        Line(start = peg_array[i].get_right(),
             end = peg_array[i+1].get_left(),
             color=BLACK, stroke_width=8).add_tip()
      )

    basic_unit = bo.MatrixBasic(4)
    basic_unit.matrix[0][0].change_fill(PURE_RED, 1)
    basic_unit.matrix[0][1].change_fill(GREEN, 1)
    basic_unit.matrix[0][2].change_fill(GREEN, 1)
    basic_unit.matrix[0][3].change_fill(GREEN, 1)
    basic_unit.matrix[1][0].change_fill(ORANGE, 1)
    basic_unit.matrix[2][0].change_fill(ORANGE, 1)
    basic_unit.matrix[3][0].change_fill(ORANGE, 1)
    for i in range(1, 4):
      for j in range(1, 4):
        basic_unit.matrix[i][j].change_fill(BLUE, 1)

    basic_unit.move_to(ORIGIN + LEFT * 7)
    all_objects = VGroup(*peg_array, *fifo_lines, basic_unit)
    self.camera.frame.set_width(all_objects.width * 1.1).move_to(all_objects.get_center())

    upper_unit = bo.MatrixBasic(4)
    for i in range(4):
      upper_unit.matrix[0][i].change_fill(GREEN, 1)
      for j in range(1, 4):
        upper_unit.matrix[j][i].change_fill(BLUE, 1)
    upper_unit.move_to(basic_unit.get_center())

    self.add(*peg_array, *fifo_lines, basic_unit)

    division_symbol = Text("/=", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + DOWN)
    left_objets = VGroup(peg_array[0], basic_unit)

    self.play(
      self.camera.frame.animate.set_width(left_objets.width * 1.2).move_to(left_objets.get_center()),
    )

    self.wait(0.5)

    self.play(
      AnimationGroup(
        [basic_unit.matrix[i][0].animate.move_to(peg_array[0].get_center() + LEFT + UP + DOWN * i) for i in range(4)],
        basic_unit.matrix[0][0].animate.move_to(peg_array[0].get_center() + RIGHT + DOWN),
        FadeIn(division_symbol),
      )
    )

    self.wait(2)

    subtract = Text("-=", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + DOWN + LEFT)
    multiplication = Text("x", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + DOWN + RIGHT)
    self.play(
      AnimationGroup(
        #column 0
        FadeOut(division_symbol),
        [basic_unit.matrix[i][0].animate.shift(RIGHT * 10) for i in range(4)],
        [basic_unit.matrix[i][0].copy().animate.shift(RIGHT) for i in range(1,4)],
        #column 1
        [basic_unit.matrix[i][1].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        basic_unit.matrix[0][1].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
        Create(subtract),
        Create(multiplication),
      )
    )

    self.wait(2)

    self.play(
      AnimationGroup(
        #column 1
        [basic_unit.matrix[i][1].animate.shift(RIGHT * 10) for i in range(4)],
        #column 2
        [basic_unit.matrix[i][2].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        basic_unit.matrix[0][2].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        #column 2
        [basic_unit.matrix[i][2].animate.shift(RIGHT * 10) for i in range(4)],
        #column 3
        [basic_unit.matrix[i][3].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        basic_unit.matrix[0][3].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )

    self.wait(1)
    self.play(
      AnimationGroup(
        #column 3
        [basic_unit.matrix[i][3].animate.shift(RIGHT * 10) for i in range(4)],
      )
    )

    self.wait(3)
    self.play(FadeIn(upper_unit))

    self.wait(1)
    self.play(
      AnimationGroup(
        [upper_unit.matrix[i][0].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        upper_unit.matrix[0][0].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )

    self.wait(1)
    self.play(
      AnimationGroup(
        #column 0
        [upper_unit.matrix[i][0].animate.shift(RIGHT * 10) for i in range(4)],
        #column 1
        [upper_unit.matrix[i][1].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        upper_unit.matrix[0][1].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )
    self.wait(1)
    self.play(
      AnimationGroup(
        #column 1
        [upper_unit.matrix[i][1].animate.shift(RIGHT * 10) for i in range(4)],
        #column 2
        [upper_unit.matrix[i][2].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        upper_unit.matrix[0][2].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )
    self.wait(1)
    self.play(
      AnimationGroup(
        #column 2
        [upper_unit.matrix[i][2].animate.shift(RIGHT * 10) for i in range(4)],
        #column 3
        [upper_unit.matrix[i][3].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        upper_unit.matrix[0][3].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + DOWN),
      )
    )
    self.wait(1)
    self.play(
      AnimationGroup(
        #column 3
        [upper_unit.matrix[i][3].animate.shift(RIGHT * 10) for i in range(4)],
      )
    )


class systolicArrayLower(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    peg_array = []
    for i in range(4):
      element = bo.RectTxt(txt=f"PEG {i} \n 4 x {4 - i}", h=7, w = 6, txt_offset=UP * 2.5)
      element.move_to(ORIGIN + i * RIGHT * 7)
      element.set_color(BLACK, 1)
      peg_array.append(element)
    
    corner_unit = bo.MatrixBasic(4)
    corner_unit.matrix[0][0].change_fill(PURE_RED, 1)
    corner_unit.matrix[0][1].change_fill(GREEN, 1)
    corner_unit.matrix[0][2].change_fill(GREEN, 1)
    corner_unit.matrix[0][3].change_fill(GREEN, 1)
    corner_unit.matrix[1][0].change_fill(ORANGE, 1)
    corner_unit.matrix[2][0].change_fill(ORANGE, 1)
    corner_unit.matrix[3][0].change_fill(ORANGE, 1)
    for i in range(1, 4):
      for j in range(1, 4):
        corner_unit.matrix[i][j].change_fill(BLUE, 1)

    corner_unit.move_to(peg_array[0].get_center() + UP * 6)
    # corner_label = Text("Corner block", font_size=50, color=PURE_RED).move_to(corner_unit.get_center() + UP * 2.5)

    dummpy_corner_unit = bo.MatrixBasic(4)
    dummpy_corner_unit.matrix[1][1].change_fill(PURE_RED, 1)
    dummpy_corner_unit.matrix[1][2].change_fill(GREEN, 1)
    dummpy_corner_unit.matrix[1][3].change_fill(GREEN, 1)
    dummpy_corner_unit.matrix[2][1].change_fill(ORANGE, 1)
    dummpy_corner_unit.matrix[3][1].change_fill(ORANGE, 1)
    for i in range(4):
      dummpy_corner_unit.matrix[i][0].change_fill(GREY, 1)
      dummpy_corner_unit.matrix[0][i].change_fill(GREY, 1)
    for i in range(2, 4):
      for j in range(2, 4):
        dummpy_corner_unit.matrix[i][j].change_fill(BLUE, 1)
    dummpy_corner_unit.move_to(peg_array[1].get_center() + UP * 6)

    lower_unit = bo.MatrixBasic(4)
    for i in range(4):
      lower_unit.matrix[i][0].change_fill(ORANGE, 1)
    for i in range(4):
      for j in range(1, 4):
        lower_unit.matrix[i][j].change_fill(BLUE, 1)

    lower_unit.move_to(ORIGIN + LEFT * 7)
    
    fifo_lines = []
    for i in range(3):
      fifo_lines.append(
        Line(start = peg_array[i].get_right(),
             end = peg_array[i+1].get_left(),
             color=BLACK, stroke_width=8).add_tip()
      )

    all_objects = VGroup(*peg_array, lower_unit)
    self.camera.frame.set_width(all_objects.width * 1.1).move_to(all_objects.get_center())
    self.add(*peg_array, lower_unit, *fifo_lines)

    partial_objects = VGroup(peg_array[0], lower_unit, corner_unit)
    self.play(
      FadeIn(corner_unit, dummpy_corner_unit),
      self.camera.frame.animate.set_height(partial_objects.height * 1.1).move_to(partial_objects.get_center()),
    )

    self.wait(1)

    division_symbol = Text("/=", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + DOWN * 0.5)
    self.play(
      AnimationGroup(
        FadeIn(division_symbol),
        [lower_unit.matrix[i][0].animate.move_to(peg_array[0].get_center() + LEFT + UP + DOWN * i) for i in range(4)],
        corner_unit.matrix[0][0].animate.move_to(peg_array[0].get_center() + RIGHT + DOWN * 0.5),
      )
    )

    self.wait(2)
    
    subtract = Text("-=", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + 0.5 * DOWN + LEFT)
    multiplication = Text("x", font_size=50, color=BLACK).move_to(peg_array[0].get_center() + 0.5 * DOWN + RIGHT)
    self.play(
      AnimationGroup(
        #column 0
        [lower_unit.matrix[i][0].animate.move_to(peg_array[1].get_center() + LEFT * 2 + UP + DOWN * i).change_fill(GREY,1) for i in range(4)],
        [lower_unit.matrix[i][0].copy().animate.shift(RIGHT) for i in range(4)],
        FadeOut(corner_unit.matrix[0][0]),
        #column 1
        [lower_unit.matrix[i][1].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        corner_unit.matrix[0][1].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + 0.5 * DOWN),
        Create(subtract),
        Create(multiplication),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        #column 1
        [lower_unit.matrix[i][1].animate.move_to(peg_array[1].get_center() + LEFT + UP + DOWN * i).change_fill(ORANGE,1) for i in range(4)],
        FadeOut(corner_unit.matrix[0][1]),
        #clumn 2
        [lower_unit.matrix[i][2].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        corner_unit.matrix[0][2].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + 0.5 * DOWN),
      ) 
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        #column 2
        [lower_unit.matrix[i][2].animate.move_to(peg_array[1].get_center() + UP + DOWN * i) for i in range(4)],
        FadeOut(corner_unit.matrix[0][2]),
        #column 3
        [lower_unit.matrix[i][3].animate.move_to(peg_array[0].get_center() + LEFT * 2 + UP + DOWN * i) for i in range(4)],
        corner_unit.matrix[0][3].animate.move_to(peg_array[0].get_center() + RIGHT * 2 + 0.5 * DOWN),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        #column 3
        [lower_unit.matrix[i][3].animate.move_to(peg_array[1].get_center() + RIGHT + UP + DOWN * i) for i in range(4)],
        FadeOut(corner_unit.matrix[0][3]),
        FadeOut(multiplication),
        FadeOut(subtract),
      )
    )

    self.wait(1)
    self.play(
      self.camera.frame.animate.shift(RIGHT * 3)
    )
    


class systolicArrayUpper(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)
    basic_unit.matrix[0][0].change_fill(PURE_RED, 1)
    basic_unit.matrix[0][1].change_fill(GREEN, 1)
    basic_unit.matrix[0][2].change_fill(GREEN, 1)
    basic_unit.matrix[0][3].change_fill(GREEN, 1)
    basic_unit.matrix[1][0].change_fill(ORANGE, 1)
    basic_unit.matrix[2][0].change_fill(ORANGE, 1)
    basic_unit.matrix[3][0].change_fill(ORANGE, 1)
    
    for i in range(1, 4):
      for j in range(1, 4):
        basic_unit.matrix[i][j].change_fill(BLUE, 1)
    basic_unit.move_to(ORIGIN)
    corner_label = Text("C", font_size=50, color=BLACK).move_to(basic_unit.matrix[0][0].get_center())
    upper_label = Text("U", font_size=50, color=BLACK).move_to(basic_unit.matrix[0][2].get_center())
    lower_label = Text("L", font_size=50, color=BLACK).move_to(basic_unit.matrix[2][0].get_center())
    trailing_label = Text("T", font_size=50, color=BLACK).move_to(basic_unit.matrix[2][2].get_center())

    systolicArray = bo.RectTxt(txt="Systolic Array", h=5, w=5, txt_offset= UP * 2)
    systolicArray.move_to(ORIGIN + RIGHT * 7)

    all_objects = VGroup(basic_unit, systolicArray)
    self.camera.frame.set_width(all_objects.width * 1.5).move_to(all_objects.get_center() + RIGHT * 2)

    self.add(basic_unit, systolicArray, corner_label, upper_label, lower_label, trailing_label)

    self.play(
      AnimationGroup(
        [FadeOut(basic_unit.matrix[j][i]) for i in range(4) for j in range(1,4)],
        FadeOut(lower_label, trailing_label),
      )
    )
    self.play(
      AnimationGroup(
      basic_unit.matrix[0][0].animate.move_to(systolicArray.get_center()),
      corner_label.animate.move_to(systolicArray.get_center()),
      )
    )

    self.wait(1)

    corner_copy = basic_unit.matrix[0][0].copy()
    corner_label_copy = corner_label.copy()
    self.play(
      AnimationGroup(
        corner_copy.animate.shift(1.5 * DOWN),
        corner_label_copy.animate.shift(1.5 * DOWN),
        basic_unit.matrix[0][0].animate.shift(RIGHT * 4),
        corner_label.animate.shift(RIGHT * 4),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        Create(Line(start=basic_unit.matrix[0][3].get_right() + 0.5 * RIGHT + DOWN * 1.5,
                    end = systolicArray.get_left() + 0.5 * LEFT,
                    color=BLACK, stroke_width=2).add_tip()
        ),
        [basic_unit.matrix[0][i].animate.shift(DOWN * 1.5) for i in range(1, 4)],
        upper_label.animate.shift(DOWN * 1.5),
        FadeOut(basic_unit.matrix[0][0]),
        FadeOut(corner_label),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        [basic_unit.matrix[0][i].animate.shift(RIGHT * 6.5) for i in range(1, 4)],
        upper_label.animate.shift(RIGHT * 6.5),
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        [basic_unit.matrix[0][i].animate.shift(RIGHT * 5) for i in range(1, 4)],
        upper_label.animate.shift(RIGHT * 5),
      )
    )

class systolicArrayTrail(MovingCameraScene):
  def construct(self):
    self.camera.background_color = WHITE

    basic_unit = bo.MatrixBasic(4)
    basic_unit.matrix[0][0].change_fill(PURE_RED, 1)
    basic_unit.matrix[0][1].change_fill(GREEN, 1)
    basic_unit.matrix[0][2].change_fill(GREEN, 1)
    basic_unit.matrix[0][3].change_fill(GREEN, 1)
    basic_unit.matrix[1][0].change_fill(ORANGE, 1)
    basic_unit.matrix[2][0].change_fill(ORANGE, 1)
    basic_unit.matrix[3][0].change_fill(ORANGE, 1)
    
    for i in range(1, 4):
      for j in range(1, 4):
        basic_unit.matrix[i][j].change_fill(BLUE, 1)
    basic_unit.move_to(ORIGIN)
    corner_label = Text("C", font_size=50, color=BLACK).move_to(basic_unit.matrix[0][0].get_center())
    upper_label = Text("U", font_size=50, color=BLACK).move_to(basic_unit.matrix[0][2].get_center())
    lower_label = Text("L", font_size=50, color=BLACK).move_to(basic_unit.matrix[2][0].get_center())
    trailing_label = Text("T", font_size=50, color=BLACK).move_to(basic_unit.matrix[2][2].get_center())

    systolicArray = bo.RectTxt(txt="Systolic Array", h=5, w=5, txt_offset= UP * 2)
    systolicArray.move_to(ORIGIN + RIGHT * 9)

    all_objects = VGroup(basic_unit, systolicArray)
    self.camera.frame.set_width(all_objects.width * 1.3).move_to(all_objects.get_center() + UP + RIGHT * 1)

    self.add(basic_unit, systolicArray, corner_label, upper_label, lower_label, trailing_label)

    self.play(
      AnimationGroup(
        [FadeOut(basic_unit.matrix[1][i]) for i in range(4)],
        [FadeOut(basic_unit.matrix[3][i]) for i in range(4)],
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        basic_unit.matrix[2][0].animate.move_to(systolicArray.get_center() + LEFT * 5),
        lower_label.animate.move_to(systolicArray.get_center() + LEFT * 5),
        basic_unit.matrix[0][0].animate.move_to(systolicArray.get_center() + UP * 5),
        corner_label.animate.move_to(systolicArray.get_center() + UP * 5),
      )
    )

    self.play(
      AnimationGroup(
        Create(Line(start=basic_unit.matrix[2][0].get_right() + 0.5 * RIGHT,
                    end = systolicArray.get_left() + 0.5 * LEFT,
                      color=BLACK, stroke_width=2).add_tip()
        ),
        Create(Line(start=basic_unit.matrix[0][0].get_bottom() + 0.5 * DOWN,
                    end = systolicArray.get_top() + 0.5 * UP,
                      color=BLACK, stroke_width=2).add_tip()
        )
      )
    )

    self.wait(1)

    self.play(
      AnimationGroup(
        basic_unit.matrix[2][0].animate.move_to(systolicArray.get_center()),
        lower_label.animate.move_to(systolicArray.get_center()),
      )
    )

    self.play(
      AnimationGroup(
        basic_unit.matrix[2][0].copy().animate.shift(DOWN * 1.5),
        basic_unit.matrix[2][0].animate.shift(RIGHT * 4),
        lower_label.copy().animate.shift(DOWN * 1.5),
        lower_label.animate.shift(RIGHT * 4),
      )
    )

    self.wait(1)

    upper_group = VGroup(basic_unit.matrix[0][1], basic_unit.matrix[0][2], basic_unit.matrix[0][3], upper_label)
    self.play(
      AnimationGroup(
        FadeOut(basic_unit.matrix[0][0]),
        FadeOut(corner_label),
        FadeOut(basic_unit.matrix[2][0]),
        FadeOut(lower_label),
        # Move rest
        [basic_unit.matrix[2][i].animate.shift(UP * 0.5 + RIGHT * 2) for i in range(1, 4)],
        trailing_label.animate.shift(UP * 0.5 + RIGHT * 2),
        upper_group.animate.move_to(systolicArray.get_center() + UP * 5),
      )
    )

    self.wait(1)
    self.play(
      AnimationGroup(
        [basic_unit.matrix[2][i].animate.shift(RIGHT * 6.5) for i in range(1, 4)],
        trailing_label.animate.shift(RIGHT * 6.5),
      )
    )

    self.play(
      AnimationGroup(
        [basic_unit.matrix[2][i].animate.shift(RIGHT * 5) for i in range(1, 4)],
        trailing_label.animate.shift(RIGHT * 5),
      )
    )

