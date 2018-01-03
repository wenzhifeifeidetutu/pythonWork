from math import sqrt,acos

from decimal import Decimal, getcontext
#使用decimal getcontext 将显示变得更精确 防止在arcos时候超过1

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
                #tuple: 将列表转换为元组
            #self.coordinates = tuple(coordinates)
            self.coordinates = tuple( [Decimal(x) for x in coordinates ])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def plus(self, v):
        #zip 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表 
        #返回两个向量的和
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates) ]
        
        return Vector(new_coordinates)

    def minus(self, v):
        #返回两个向量的差
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates) ]

        return Vector(new_coordinates)

    def times_scalar(self, scalar):
        #返回一个数与向量的乘积
        new_coordinates = [Decimal(scalar)*x for x in self.coordinates]

        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def magnitutde(self):
        #返回向量的摸
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        #返回向量的单位向量
        #防止0向量做除数
        try:
            magnitutde = self.magnitutde()
            return self.times_scalar(1 /magnitutde)    

        except ZeroDivisionError:
            raise Exception('Cannot normalize zero Vector')
    
    def dot(self, v):
        #向量的数量乘积
        return sum( [x*y for x, y in zip(v.coordinates, self.coordinates)])

    def angle_with(self, v, in_degrees = False):
        #向量的角度 degrees 用角度来表示

        try:
            u1 = self.normalized()
            u2 = v.normalized()
            #反三角函数
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180 / 3.1415926
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')

            else:
                raise e 

    def is_orthogonal_to(self, v, tolerance = 1e-10):
        #如过两个向量的点乘积小于（精度在1e-10）正交 
        return abs(self.dot(v)) <tolerance

    def is_parallel_to(self, v):
        #角度为0 或者π 或者有一个为0向量就是平行
        return(self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == 3.1415926)


    def is_zero(self, tolerance = 1e-10):
        return self.magnitutde()< tolerance

    def component_orthogonal_to(self, basis):
        #垂直向量表示
        try:
            projection = self.componet_parallel_to(basis)
            return self.minus(projection)


        except:
            pass





    def componet_parallel_to(self, basis):
        #平行向量表示
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except:
            pass
        
    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [y_1 * z_2  - y_2*z_1,
                                -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1]

            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0', ))
                return self_embedded_in_R3.cross(v_embedded_in_R3)

            elif (msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
                
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross(v)
        return cross_product.magnitutde()

    def area_of_triangle_with(self, v):
        return Decimal(self.area_of_parallelogram_with(v))/Decimal('2.0')
