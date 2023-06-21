import os

DEBUG = False
DEBUG_BOARD = False
PLOT = False
SPARSE = False
INIT_OBSERVATIONS = True
Board_State = None
aiAgent = None
Opponent = None
TicTacToe = None
ORIGINAL_STATES = None
REAL_MODEL_PARAMETERS = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0}
MAX = float('+inf')
MIN = float('-inf')
ITERATIONS = 25000
GAMES_TEST = int(ITERATIONS / 4)
WIN_REWARD = 10
LOSE_REWARD = -10
DRAW_REWARD = 0
DISCOUNT_FACTOR = 0.95
ALPHA = 0.5
EPSILON = 0.2
THETA = 1e-5
IMMEDIATE_REWARD = -1
INIT_OBSERVATIONS_LEN = 10
LOG_FILE = os.path.join("logs", "observations")
INIT_MODEL_PARAMETERS = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.8, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0}
