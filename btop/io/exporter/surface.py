import bpy

def create_knots_uniform(n, order):
    knots = [i for i in range(n + order) ]
    return knots

def is_weighted(points):
    for point in points:
        if point.weight != 1.0:
            return True
    return False

class SurfaceIO(object):
    """

    """

    def __init__(self):
        pass

    def write_to_file(self, writer, obj, indent=0):
        assert obj.type == 'SURFACE'
        assert type(obj.data) == bpy.types.SurfaceCurve
        if obj.data.dimensions == '3D':
            for spline in obj.data.splines:
                if spline.type == 'NURBS':
                    nu = spline.point_count_u
                    nv = spline.point_count_v
                    uorder = spline.order_u
                    vorder = spline.order_v
                    diceu = spline.resolution_u * uorder
                    dicev = spline.resolution_v * vorder
                    points = spline.points
                    uknots = create_knots_uniform(nu, uorder) #todo
                    vknots = create_knots_uniform(nv, vorder) #todo

                    writer.write((indent + 0) * '\t' + 'Shape "nurbs" "integer nu" {} "integer nv" {}\n'.format(nu, nv))
                    writer.write((indent + 1) * '\t' + '"integer uorder" {} "integer vorder" {}\n'.format(uorder, vorder))
                    writer.write((indent + 1) * '\t' + '"integer diceu" {} "integer dicev" {}\n'.format(diceu, dicev))
                    writer.write((indent + 1) * '\t' + '"float uknots" [')
                    for knot in uknots:
                        writer.write('{} '.format(knot))
                    writer.write(']\n')
                    writer.write((indent + 1) * '\t' + '"float vknots" [')
                    for knot in vknots:
                        writer.write('{} '.format(knot))
                    writer.write(']\n')
                    if is_weighted(points):
                        writer.write((indent + 1) * '\t' + '"point Pw" [\n')
                        for i, point in enumerate(points):
                            writer.write((indent + 2) * '\t' + '{} {} {} {} \t# {}\n'.format(point.co.x, point.co.y, point.co.z, point.weight, i+1))
                        writer.write((indent + 1) * '\t' + ']\n')
                    else:
                        writer.write((indent + 1) * '\t' + '"point P" [\n')
                        for i, point in enumerate(points):
                            writer.write((indent + 2) * '\t' + '{} {} {} \t# {}\n'.format(point.co.x, point.co.y, point.co.z, i+1))
                        writer.write((indent + 1) * '\t' + ']\n')
                    writer.write('\n')





    def read_from_file(self, parser):
        pass