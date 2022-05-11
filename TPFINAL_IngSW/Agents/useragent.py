from agents import Agent
from environments import SimulatedSensor, SimulatedActuator, SimulatedEnvironment


class ScoreSensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="score")
        return response["score"]


class BoardSensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="board")
        return response["board"]


class EmptySensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="empty")
        return response["empty"]


class DrawActuator(SimulatedActuator):

    def act(self, move: int):
        self._env.take_action(self._agent.id, "play", move)


class UserAgent(Agent):

    def function(self, percept):
        pass

    def __init__(self, env: SimulatedEnvironment, letter):
        super().__init__(letter)
        env.add(self.id)

        draw = DrawActuator(env)
        draw.agent = self
        self.add_actuator("draw", draw)

        score = ScoreSensor(env)
        score.agent = self
        self.add_sensor("score_sensor", score)

        board = BoardSensor(env)
        board.agent = self
        self.add_sensor("board_sensor", board)

        empty = EmptySensor(env)
        empty.agent = self
        self.add_sensor("empty_sensor", empty)

        # self.setup_function()

    def print_board(self):
        return self._sensors["board_sensor"].sense()

    def state(self):
        return self._sensors["score_sensor"].sense()

    def moves(self):
        return self._sensors["empty_sensor"].sense()
