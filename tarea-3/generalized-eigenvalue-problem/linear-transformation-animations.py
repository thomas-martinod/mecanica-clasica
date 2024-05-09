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
        
        # Add vec_label as a submobject of vec
        vec.add(vec_label)
        
        self.add_transformable_mobject(vec)
        self.add_foreground_mobject(matrix_tex)

        # Detach vec_label from vec before applying transformation
        vec.remove(vec_label)
        self.add_foreground_mobject(vec_label)

        self.apply_matrix(matrix)
        self.wait()
