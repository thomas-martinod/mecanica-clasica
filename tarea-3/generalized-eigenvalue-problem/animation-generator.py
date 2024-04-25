from manimlib.imports import *

class Vectors(VectorScene):
    CONFIG = {
        "show_basis_vectors" : True,
        "foreground_plane_kwargs" : {
            "x_max" : 10,
            "x_min" : -10,
            "y_max" : 10,
            "y_min" : -10,
        },
    }

    def construct(self):
        self.add_axes(animate = False)
        self.add_plane(animate = False)
        self.wait()

        myVec = Vector([3,2])
        myVec.set_color(YELLOW)
        self.add_vector(myVec)

        labelVector = vector_coordinate_label(myVec, color = YELLOW)
        self.play(ShowCreation(labelVector))



class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors" : True,
        "foreground_plane_kwargs" : {
            "x_max" : 10,
            "x_min" : -10,
            "y_max" : 10,
            "y_min" : -10,
            "faded_line_ratio" : 0
        },
    }
    
    def construct(self):
        self.setup()
        self.wait()

        myVec = Vector([3,2])
        myVec.set_color(YELLOW)
        self.add_vector(myVec)

        labelVector = vector_coordinate_label(myVec, color = YELLOW)
        self.add_moving_mobject(myVec)

        text = TexMobject("Shear")
        text.scale(2)
        self.add_transformable_mobject(text)

        self.apply_matrix([[2,-1], [3,-5]])
