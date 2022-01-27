class StateMachine(object):
    def __init__(self, states):
        self._states = states
        self._curState = 0

    def setState(self, state):
        self._curState = self._states.index(state)

    def getState(self):
        return self._states[self._curState]
