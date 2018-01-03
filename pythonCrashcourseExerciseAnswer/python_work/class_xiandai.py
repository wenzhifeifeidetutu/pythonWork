import Vector 


v1 = Vector.Vector(['7.887', '4.138'])
v2 = Vector.Vector(['-8.802', '6.776'])
v3 = Vector.Vector(['3.183', '-7.627'])
v4 = Vector.Vector(['-2.668', '5.319'])
v5 = Vector.Vector(['3.039', '1.879'])
v6 = Vector.Vector(['0.825', '2.036'])

print(v1.dot(v2))
print(v3.angle_with(v4))

print(v5.componet_parallel_to(v6))
print(v5.component_orthogonal_to(v6))

v1 = Vector.Vector( ['8.462', '7.893', '-8.187'] )
v2 = Vector.Vector( ['6.984', '-5.975', '4.778'] )

print(v1.cross(v2))
print(v1.area_of_parallelogram_with(v2))
print(v1.area_of_triangle_with(v2) )