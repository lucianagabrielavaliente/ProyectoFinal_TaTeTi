from boardworld import BoardEnvironment


class TestWinner:

    def test_winner_X(self):
        env = BoardEnvironment()
        env._board = ['X', ' ', 'X', 'O', 'X', ' ', ' ', 'O', 'X']
        assert env.winner() == 'X'

    def test_winner_O(self):
        env = BoardEnvironment()
        env._board = [' ', 'O', 'X', 'O', 'O', ' ', ' ', 'O', 'X']
        assert env.winner() == 'O'

    def test_winner_tie(self):
        env = BoardEnvironment()
        env._board = ['O', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X']
        assert env.winner() == 'Tie'

    def test_winner_empty(self):
        env = BoardEnvironment()
        env._board = ['O', ' ', 'O', ' ', 'X', 'O', 'X', ' ', 'X']
        assert env.winner() == ' '


class TestMoveOptions:

    def test_move_options_0(self):
        env = BoardEnvironment()
        env._board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        assert env.move_options() == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def test_move_options_1(self):
        env = BoardEnvironment()
        env._board = ['O', ' ', 'O', ' ', 'X', 'O', 'X', ' ', 'X']
        assert env.move_options() == [1, 3, 7]

    def test_move_options_2(self):
        env = BoardEnvironment()
        env._board = ['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']
        assert env.move_options() == []


class TestMakeDraw:

    def test_make_draw(self):
        env = BoardEnvironment()
        env._board = ['O', ' ', 'O', ' ', 'X', 'O', 'X', ' ', 'X']
        env._make_draw('X', 1)
        assert env._board == ['O', 'X', 'O', ' ', 'X', 'O', 'X', ' ', 'X']
