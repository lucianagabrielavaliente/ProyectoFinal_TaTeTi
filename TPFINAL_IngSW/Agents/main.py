from boardworld import BoardEnvironment
from useragent import UserAgent
import random

if __name__ == '__main__':
    env = BoardEnvironment()

    if random.randint(0, 1) == 0:
        agent_1 = UserAgent(env, 'X')
        agent_2 = UserAgent(env, 'O')
    else:
        agent_1 = UserAgent(env, 'O')
        agent_2 = UserAgent(env, 'X')

    c = ' '
    agent_1.actuators["draw"].act(random.choice(agent_1.moves()))
    agent_1.print_board()
    last_player = agent_1.id
    print('\n')
    while c == ' ':
        if last_player == agent_1.id:
            agent_2.actuators["draw"].act(random.choice(agent_2.moves()))
            agent_2.print_board()
            last_player = agent_2.id
            print('\n')
        else:
            agent_1.actuators["draw"].act(random.choice(agent_1.moves()))
            agent_1.print_board()
            last_player = agent_1.id
            print('\n')
        c = agent_1.state()
    if c == 'Tie':
        print('Tie')
    else:
        print('The winner is:', c)
