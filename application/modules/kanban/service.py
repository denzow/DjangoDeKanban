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


def get_board_data_board_id(board_id):
    """
    borad and pipeline and card.
    :param int board_id:
    :return:
    :rtype: dict
    """
    board = Board.get_by_id(board_id)
    board_data = {
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
    card_list = Card.get_list_by_pipe_line(pipe_line=pipe_line)
    card_id_map = {c.id: c for c in card_list}
    for i, card_id in enumerate(card_id_list):
        card = card_id_map.get(card_id)
        card.order = i
        card.save()
