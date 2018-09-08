from .models import Board, PipeLine, Card


def get_board_list_by_owner(owner):
    """
    :param owner:
    :return:
    :rtype: list of Board
    """
    return Board.get_list_by_owner(owner=owner)


def get_board_by_board_id(board_id):
    """
    :param int board_id:
    :return:
    :rtype: Board or None
    """
    return Board.get_by_id(board_id)


def get_card_by_card_id(card_id):
    """
    :param int card_id:
    :return:
    """
    return Card.get_by_id(card_id)


def get_board_data_board_id(board_id):
    """
    borad and pipeline and card.
    :param int board_id:
    :return:
    :rtype: dict
    """
    board = Board.get_by_id(board_id)
    board_data = {
        'board_id': board.id,
        'name': board.name,
        'pipe_line_list': []
    }
    for pipe_line in PipeLine.get_list_by_board(board):
        pipe_line_data = {
            'pipe_line_id': pipe_line.id,
            'name': pipe_line.name,
            'card_list': []
        }
        for card in Card.get_list_by_pipe_line(pipe_line):
            pipe_line_data['card_list'].append({
                'card_id': card.id,
                'title': card.title,
                'content': card.content,
            })
        board_data['pipe_line_list'].append(pipe_line_data)

    return board_data


def update_card_order(pipe_line_id, card_id_list):
    """
    :param int pipe_line_id:
    :param list card_id_list:
    :return:
    """
    pipe_line = PipeLine.get_by_id(pipe_line_id)
    for i, card_id in enumerate(card_id_list):
        card = Card.get_by_id(card_id)
        card.order = i
        card.pipe_line = pipe_line
        card.save()


def update_pipe_line_order(board_id, pipe_line_id_list):
    board = Board.get_by_id(board_id)
    for i, pipe_line_id in enumerate(pipe_line_id_list):
        pipe_line = PipeLine.get_by_id(pipe_line_id)
        pipe_line.order = i
        pipe_line.save()


def add_pipe_line(board_id, pipe_line_name):
    board = Board.get_by_id(board_id)
    current_count = PipeLine.get_current_pipe_line_count_by_board(board)
    return PipeLine.create(
        board=board,
        name=pipe_line_name,
        order=current_count + 1,
    )


def add_card(pipe_line_id, card_title):
    pipe_line = PipeLine.get_by_id(pipe_line_id)
    current_count = Card.get_current_card_count_by_pipe_line(pipe_line)
    return Card.create(
        title=card_title,
        content=None,
        pipe_line=pipe_line,
        order=current_count + 1,
    )
