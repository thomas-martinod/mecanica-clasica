from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            *kwargs
        )

    def construct(self):
        # Ask the user for the matrix input
        matrix_str = input("Enter the elements of the 2x2 matrix separated by spaces: ")
        matrix_elements = [float(x) for x in matrix_str.split()]
        matrix = [[matrix_elements[0], matrix_elements[1]], 
                  [matrix_elements[2], matrix_elements[3]]]

        # Apply the user-defined matrix
        self.apply_matrix(matrix)
        self.wait()

# Run the scene
scene = LinearTransformationSceneExample()
scene.render()
