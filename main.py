import random


size = 3
total_size = pow(size, 2)
answer = range(1, total_size)
answer.append(0)


def initial_state():
    start_matrix = (answer)[:]
    for _ in range(10):
        start_matrix = get_possibility(start_matrix)
    return start_matrix


def expand_matrix(matrix):
    position_expands = {}
    for key in range(total_size):
        position_expands[key] = get_values(key)
    pos = matrix.index(0)
    moves = position_expands[pos]
    expanded_states = []
    for mv in moves:
        nstate = matrix[:]
        (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos +
                                                               mv])
        expanded_states.append(nstate)
    return expanded_states


def print_matrix(matrix):
    for (index, value) in enumerate(matrix):
        print ' %s ' % value,
        if index in [x for x in range(size - 1, total_size,
                                      size)]:
            print
    print


def get_possibility(matrix):
    exp_matrix = expand_matrix(matrix)
    rand_matrix = random.choice(exp_matrix)
    return rand_matrix


def get_distance(matrix):
    mdist = 0
    for node in matrix:
        if node != 0:
            gdist = abs(answer.index(node) - matrix.index(node))
            (jumps, steps) = (gdist // size, gdist % size)
            mdist += jumps + steps
    return mdist


def get_next_state(matrix):
    exp_matrices = expand_matrix(matrix)
    m_distances = []
    for matrix in exp_matrices:
        m_distances.append(get_distance(matrix))
    m_distances.sort()
    short_path = m_distances[0]
    if m_distances.count(short_path) > 1:
        least_paths = [
            matrix for matrix in exp_matrices if get_distance(matrix) == short_path]
        return random.choice(least_paths)
    else:
        for matrix in exp_matrices:
            if get_distance(matrix) == short_path:
                return matrix


def get_values(key):
    values = [1, -1, size, -size]
    valid_values = []
    for x in values:
        if 0 <= key + x < total_size:
            if x == 1 and key in range(size - 1, total_size,
                                       size):
                continue
            if x == -1 and key in range(0, total_size, size):
                continue
            valid_values.append(x)
    return valid_values


def is_game_over(matrix):
    return matrix == answer


def solve(matrix):
    while not is_game_over(matrix):
        matrix = get_next_state(matrix)
        print_matrix(matrix)


print 'Initial State:'
start = initial_state()
print_matrix(start)
print 'Step by Step:'
print_matrix(start)
solve(start)
