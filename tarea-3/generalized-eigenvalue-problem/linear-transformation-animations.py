from manim import *

class AnimateMatrixA(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        A = [[-2, 1],[1, 2]]
        A_tex = MathTex('A = \\left[\\begin{matrix}1 & -2\\\\-2 & -1\\end{matrix}\\right]').to_edge(UL).add_background_rectangle()
        v1_tex = MathTex('\\mathbf{v}_1 = \\left[\\begin{matrix}-1 + \\frac{\\sqrt{6}}{2}\\\\1\\end{matrix}\\right]', color = YELLOW).to_edge(UR).add_background_rectangle()
        v2_tex = MathTex('\\mathbf{v}_2 = \\left[\\begin{matrix}- \\frac{\\sqrt{6}}{2} - 1\\\\1\\end{matrix}\\right]', color = PURPLE_C).next_to(v1_tex, DOWN).add_background_rectangle()

        v1 = [0.224744871391589, 1]
        v2 = [-2.22474487139159, 1]

        vec1 = self.get_vector(v1, color=YELLOW, tip_length = 0.2)
        vec2 = self.get_vector(v2, color=PURPLE_C, tip_length = 0.2)

        self.add_transformable_mobject(vec1, vec2)
        self.add_foreground_mobject(A_tex, v1_tex, v2_tex)
        self.apply_matrix(A)

        self.wait()


class AnimateMatrixB(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        B = [[-0.5, -2],[-1, -1.5]]
        B_tex = MathTex('B = \\left[\\begin{matrix}- \\frac{1}{2} & -2\\\\-1 & - \\frac{3}{2}\\end{matrix}\\right]').to_edge(UL).add_background_rectangle()
        v1_tex = MathTex('\\mathbf{v}_1 = \\left[\\begin{matrix}-1 \\\\1\\end{matrix}\\right]', color = YELLOW).to_edge(UR).add_background_rectangle()
        v2_tex = MathTex('\\mathbf{v}_2 = \\left[\\begin{matrix}1 \\\\1\\end{matrix}\\right]', color = PURPLE_C).next_to(v1_tex, DOWN).add_background_rectangle()

        v1 = [0.224744871391589, 1]
        v2 = [-2.22474487139159, 1]
        
        vec1 = self.get_vector(v1, color=YELLOW, tip_length = 0.2)
        vec2 = self.get_vector(v2, color=PURPLE_C, tip_length = 0.2)

        self.add_transformable_mobject(vec1, vec2)
        self.add_foreground_mobject(B_tex, v1_tex, v2_tex)
        self.apply_matrix(B)

        self.wait()


class AnimateMatrixBinvA(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        H = [[-0.5, -2],[-1, -1.5]]
        B_tex = MathTex('B = \\left[\\begin{matrix}- \\frac{1}{2} & -2\\\\-1 & - \\frac{3}{2}\\end{matrix}\\right]').to_edge(UL).add_background_rectangle()
        v1_tex = MathTex('\\mathbf{v}_1 = \\left[\\begin{matrix}-1 \\\\1\\end{matrix}\\right]', color = YELLOW).to_edge(UR).add_background_rectangle()
        v2_tex = MathTex('\\mathbf{v}_2 = \\left[\\begin{matrix}1 \\\\1\\end{matrix}\\right]', color = PURPLE_C).next_to(v1_tex, DOWN).add_background_rectangle()

        v1 = [0.224744871391589, 1]
        v2 = [-2.22474487139159, 1]
        
        vec1 = self.get_vector(v1, color=YELLOW, tip_length = 0.2)
        vec2 = self.get_vector(v2, color=PURPLE_C, tip_length = 0.2)

        self.add_transformable_mobject(vec1, vec2)
        self.add_foreground_mobject(B_tex, v1_tex, v2_tex)
        self.apply_matrix(H)

        self.wait()