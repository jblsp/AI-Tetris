from main import font


def text(text_):
    return font.render(text_, False, (0, 0, 0))


def move_down(piece):
    new_rects = []
    for rect in piece.rects:
        new_rects.append(rect.move(0, 26))
    piece.rects = new_rects.copy()


def move_sideways(piece, direction):
    new_rects = []
    match direction:
        case 'right':
            for rect in piece.rects:
                new_rects.append(rect.move(26, 0))
        case 'left':
            for rect in piece.rects:
                new_rects.append(rect.move(-26, 0))
    piece.rects = new_rects.copy()


def rotate(piece, direction):
    match direction:
        case 'clockwise':
            pass
        case 'counter-clockwise':
            pass