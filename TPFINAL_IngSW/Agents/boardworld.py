from environments import SimulatedEnvironment


class BoardEnvironment(SimulatedEnvironment):

    def __init__(self):
        super(BoardEnvironment, self).__init__()
        self._board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def add(self, agent_id: str) -> None:
        super(BoardEnvironment, self).add(agent_id)

    def remove(self, agent_id: str) -> None:
        super(BoardEnvironment, self).remove(agent_id)

    def draw_board(self):
        print(' ' + self._board[0] + ' | ' + self._board[1] + ' | ' + self._board[2])
        print('-----------')
        print(' ' + self._board[3] + ' | ' + self._board[4] + ' | ' + self._board[5])
        print('-----------')
        print(' ' + self._board[6] + ' | ' + self._board[7] + ' | ' + self._board[8])

    def winner(self):
        winners = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                   [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in winners:
            pos_winner = self._board[win[0]]
            if (pos_winner != ' ' and
                    pos_winner == self._board[win[1]] and
                    pos_winner == self._board[win[2]]):
                return pos_winner
        # No hay ganador aún, quedan casillas vacías?
        for i in range(9):
            if self._board[i] == ' ':
                return ' '
        # El tablero está lleno y no hay tres en línea
        if self.game_over():
            return 'Tie'

    def move_options(self):
        return [i for i in range(9) if self._board[i] == ' ']

    def game_over(self):
        return len(self.move_options()) == 0

    def get_property(self,agent_id:str, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id}
            if property_name == "score":
                response["score"] = self.winner()
            elif property_name == "board":
                response["board"] = self.draw_board()
            elif property_name == "empty":
                response["empty"] = self.move_options()
            return response
        else:
            return {}

    def _make_draw(self, agent_id: str, move: int):
        self._board[move] = agent_id

    def take_action(self, agent_id: str, action_name: str, move: int) -> None:
        if agent_id in self._agents:
            if action_name == "play":
                self._make_draw(agent_id, move)
