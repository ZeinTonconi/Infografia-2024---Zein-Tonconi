import numpy as np
import arcade


class Object3D:
    def __init__(self, vertices, edges, color):
        self.vertices = vertices
        self.edges = edges
        self.color = color
        self.points_2d = None

        self.angle_X = 0
        self.angle_Y = 0
        self.facing = np.array([400,400])

    def translate(self, dx, dy, dz):
        TM = np.array([
            [1, 0, 0, dx], 
            [0, 1, 0, dy], 
            [0, 0, 1, dz], 
            [0, 0, 0, 1]
        ])

        self.vertices = self.apply_transform(TM)
    
    def rotate(self, theta, axis, pivot=None):

        xc, yc, zc = pivot if pivot is not None else self.get_center()

        if axis.lower() == "z":
            Mr = np.array([
                [np.cos(theta), -np.sin(theta), 0, 0], 
                [np.sin(theta), np.cos(theta), 0, 0], 
                [0, 0, 1, 0], 
                [0, 0, 0, 1]
            ])
        elif axis.lower() == "y":
            Mr = np.array([
                [np.cos(theta), 0, np.sin(theta), 0], 
                [0, 1, 0, 0], 
                [-np.sin(theta), 0, np.cos(theta), 0], 
                [0, 0, 0, 1]
            ])
        elif axis.lower() == "x":
            Mr = np.array([
                [1, 0, 0, 0],
                [0, np.cos(theta), -np.sin(theta), 0], 
                [0, np.sin(theta), np.cos(theta), 0], 
                [0, 0, 0, 1]
            ])

        Mt1 = np.array([
            [1, 0, 0, -xc], 
            [0, 1, 0, -yc], 
            [0, 0, 1, -zc], 
            [0, 0, 0, 1]
        ])
        
        Mt2 = np.array([
            [1, 0, 0, xc], 
            [0, 1, 0, yc], 
            [0, 0, 1, zc], 
            [0, 0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Mr, Mt1))
  
        self.vertices = self.apply_transform(TM)

    def scale(self, sx, sy, sz, pivot=None):
        xc, yc, zc = pivot if pivot is not None else self.get_center()
        Mt1 = np.array([
            [1, 0, 0, -xc], 
            [0, 1, 0, -yc], 
            [0, 0, 1, -zc], 
            [0, 0, 0, 1]
        ])
        Ms = np.array([
            [sx, 0, 0, 0], 
            [0, sy, 0, 0], 
            [0, 0, sz, 0], 
            [0, 0, 0, 1]
        ])
        Mt2 = np.array([
            [1, 0, 0, xc], 
            [0, 1, 0, yc], 
            [0, 0, 1, zc], 
            [0, 0, 0, 1]
        ])

        TM = np.dot(Mt2, np.dot(Ms, Mt1))
  
        self.vertices = self.apply_transform(TM)

    def apply_transform(self, tr_matrix):
        v_array = np.transpose(np.array(
            [[v[0], v[1], v[2], 1] for v in self.vertices]
        ))

        return np.transpose(
            np.dot(tr_matrix, v_array)[0:3, :]
        ).tolist()

    def get_center(self):
        return np.mean(np.array(self.vertices), axis=0)

    def project_2d(self):
        TM = np.array([
            [1, 0, 0, 0], 
            [0, 1, 0, 0], 
            [0, 0, 0, 0], 
            [0, 0, 0, 1]
        ])

        self.points_2d = [
            (int(r[0]), int(r[1])) for r in self.apply_transform(TM)
        ]

    def draw(self):
        self.project_2d()
        arcade.draw_points(self.points_2d, self.color, 5)
        edge_points = [
            (self.points_2d[e[0]], self.points_2d[e[1]]) 
            for e in self.edges
        ]
        for (x0, y0), (x1, y1) in edge_points:
            arcade.draw_line(x0, y0, x1, y1, self.color, 2)
    
    def angle_vectors(self, a,b):
        a = np.array(a)
        b = np.array(b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)

        cos_theta = np.dot(a,b)/(norm_a*norm_b)

        cos_theta = np.clip(cos_theta, -1, 1)

        angle = np.arccos(cos_theta)
        return angle

    def unit_vector(self,a):
        a = np.array(a)
        norm = np.linalg.norm(a)
        return a/norm

    def follow_mouse(self, mouse, delta_time):

        unit_mouse = self.unit_vector([mouse[0]-400, -200])
        unit_facing = self.unit_vector([self.facing[0]-400, -200])

        theta_Y = np.atan2(unit_mouse[0], unit_mouse[1]) - np.atan2(unit_facing[0], unit_facing[1])

        self.facing[0]=mouse[0]

        unit_mouse = self.unit_vector([-200, mouse[1]-400])
        unit_facing = self.unit_vector([-200, self.facing[1]-400])

        theta_X = np.atan2(unit_mouse[0], unit_mouse[1]) - np.atan2(unit_facing[0], unit_facing[1])

        self.facing[0]=mouse[0]
        self.facing[1]=mouse[1]

        self.rotate(theta_Y, "y") 
        self.rotate(theta_X,"x")  


if __name__ == "__main__":
    vertices = [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
    ]

    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
    ]

    cube_obj = Object3D(
        vertices=vertices, 
        edges=edges, 
        color=arcade.color.YELLOW
    )
    print(cube_obj.vertices)
    print(cube_obj.points_2d)
    cube_obj.translate(1, 0, 0)
    print(cube_obj.vertices)
    cube_obj.rotate(0.1, "x")
    cube_obj.rotate(0.1, "y")
    cube_obj.rotate(0.1, "z")
    print(cube_obj.vertices)
    cube_obj.project_2d()
    print(cube_obj.points_2d)
