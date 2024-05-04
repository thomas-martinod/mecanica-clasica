from manim import *

class AnimateMatrixA(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self, show_coordinates=True, leave_ghost_vectors=True,
                                           show_basis_vectors=True)
    
    def construct(self):
        matrix = [[-2, 1],[1, 2]]
        matrix_tex = MathTex("A = \\begin{bmatrix} -2 & 1 \\\\ 1 & 2 \\end{bmatrix}").to_edge(UL).add_background_rectangle()

        vector_value = [1/3 + (34**0.5)/3, 1]
        vec = self.get_vector(vector_value, color=PURPLE_B, tip_length=0.2)  # Set tip_length to a fixed value
        vec_label = MathTex(r"\left[\begin{matrix} \frac{1}{3} + \frac{\sqrt{34}}{3} \\ 1 \end{matrix}\right]").next_to(vec, UP)

        rect1 = Rectangle(height=2, width=1, stroke_color=BLUE_A, fill_color=BLUE_D,
                          fill_opacity=0.6).shift(UP*2 + LEFT*2)
        
        circ1 = Circle(radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6).shift(DOWN*2 + RIGHT*1)

        self.add_transformable_mobject(vec, rect1, circ1)
        self.add_foreground_mobject(matrix_tex)
        self.add_foreground_mobject(vec_label)  # Add vec_label to foreground
        self.apply_matrix(matrix)

        self.wait()
