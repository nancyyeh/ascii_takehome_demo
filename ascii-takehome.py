# def create_canvas(rows=10, cols=10):
#     """create canvas - not part of assignment but used for testing"""
#     matrix = [[" " for x in range(cols)] for y in range(rows)]

#     return matrix

CANVAS = [[" " for x in range(10)] for y in range(10)]


def add_shape(shape):
    """add shape - assume only rect - loop thru the shape and input onto the canvas"""
    for idx_row, row in enumerate(shape):
        for idx_col, item in enumerate(row):
            if item != ' ':
                CANVAS[idx_row][idx_col] = item


@app.route('/api/create_rect', methods=['POST'])
def create_rect(start_x, end_x, start_y, end_y, fill_char):
    """create a rectangle"""

    matrix = [[" " for x in range(10)] for y in range(10)]

    for px in range(start_x, start_x + end_x):
        for py in range(start_y, start_y + end_y):
            matrix[py][px] = fill_char

    return matrix


@app.route('/api/create_rect', methods=['POST'])
def change_char(rectangle, char):
    """change the char of the rectangle"""
    for idx_row, row in enumerate(rectangle):
        for idx_col, item in enumerate(row):
            if item != ' ':
                rectangle[idx_row][idx_col] = char


def translate(rectangle, axis, num):
    ### DID NOT COMPLETE ##
    """ Translate (move left, right, up, or down)
    Translating on the X-axis will cause the rectangle to move left and right. 
    Translating on the Y-axis will cause the rectangle to move up and down.
    num is how much to move the rectangle. 
    Negative numbers will cause the rectangle to shift left or down. 
    Positive numbers will cause the rectangle to shift right or up."""

    #CREAT A NEW MATRIX#
    new_matrix = [[" " for x in range(10)] for y in range(10)]

    # LOOP THRU MATRIX - need to check if the idx will be over 10 or to -1, if cannnot translate
    # if not, else create a new matrix that moved!
    for idx_row, row in enumerate(rectangle):
        for idx_col, item in enumerate(row):
            # check if the idx will be over 10 or to -1, if cannnot translate
            if axis == 'x':
                new_col = idx_col + num
                new_matrix[idx_row][new_col] = item
            elif axis == 'y':
                new_row = idx_row + num
                new_matrix[new_row][col] = item
        return new_matrix


def clear():
    """get rid of all shape on canvas"""
    for idx_row, row in enumerate(CANVAS):
        for idx_col, item in enumerate(row):
            if item != ' ':
                CANVAS[idx_row][idx_col] = ' '

    return ('canvas is cleared')


def render():
    """render the canvas"""
    lst = []
    for i in CANVAS:
        lst.append(''.join(i))

    str_ver = '\n'.join(lst)

    print(str_ver)
