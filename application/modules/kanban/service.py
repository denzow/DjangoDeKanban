from .models import Board


def get_board_list_by_owner(owner):
    """
    :param owner:
    :return:
    :rtype: list of Board
    """
    return Board.get_list_by_owner(owner=owner)
