def find_range_overlap(point1, length1, point2, length2):

    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    if highest_start_point >= lowest_end_point:
        return (None, None)

    overlap_length = lowest_end_point - highest_start_point
    return (highest_start_point, overlap_length)


def find_rectangular_overlap(rect1, rect2):

    x_overlap_point, overlap_width  = find_range_overlap(rect1['left_x'],rect1['width'],rect2['left_x'],rect2['width'])
    y_overlap_point, overlap_height = find_range_overlap(rect1['bottom_y'],rect1['height'],rect2['bottom_y'],rect2['height'])

    if not overlap_width or not overlap_height:
        return {'left_x': None,'bottom_y': None,'width': None,'height': None,
        }

    return {
        'left_x': x_overlap_point,'bottom_y': y_overlap_point,'width': overlap_width,'height': overlap_height,
    }

if __name__ == '__main__':

    left_x_1 = int(input("Enter left x(1): "))
    bottom_y_1 = int(input("Enter bottom y(1): "))
    width_1 = int(input("Enter width(1): "))
    height_1 = int(input("Enter height(1): "))
    left_x_2 = int(input("Enter left x(2): "))
    bottom_y_2 = int(input("Enter bottom y(2): "))
    width_2 = int(input("Enter width(2): "))
    height_2 = int(input("Enter height(2): "))

    rect1 = {
        'left_x': 1,
        'bottom_y': 1,
        'width': 6,
        'height': 3,
    }
    rect2 = {
        'left_x': 5,
        'bottom_y': 2,
        'width': 3,
        'height': 6,
    }
    print(str(find_rectangular_overlap(rect1,rect2)))