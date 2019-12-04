from collections import defaultdict

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = [r + c for r in rows for c in cols]
history = {}  # history must be declared here so that it exists in the assign_values scope


def extract_units(unitlist, boxes):
    """Initialize a mapping from box names to the units that the boxes belong to

    Parameters
    ----------
    unitlist(list)
        a list containing "units" (rows, columns, diagonals, etc.) of boxes

    boxes(list)
        a list of strings identifying each box on a sudoku board (e.g., "A1", "C7", etc.)

    Returns
    -------
    dict
        a dictionary with a key for each box (string) whose value is a list
        containing the units that the box belongs to (i.e., the "member units")
    """
    # the value for keys that aren't in the dictionary are initialized as an empty list
    units = defaultdict(list)
    for current_box in boxes:
        for unit in unitlist:
            if current_box in unit:
                # defaultdict avoids this raising a KeyError when new keys are added
                units[current_box].append(unit)
    return units


def extract_peers(units, boxes):
    """Initialize a mapping from box names to a list of peer boxes (i.e., a flat list
    of boxes that are in a unit together with the key box)

    Parameters
    ----------
    units(dict)
        a dictionary with a key for each box (string) whose value is a list
        containing the units that the box belongs to (i.e., the "member units")

    boxes(list)
        a list of strings identifying each box on a sudoku board (e.g., "A1", "C7", etc.)

    Returns
    -------
    dict
        a dictionary with a key for each box (string) whose value is a set
        containing all boxes that are peers of the key box (boxes that are in a unit
        together with the key box)
    """
    # the value for keys that aren't in the dictionary are initialized as an empty list
    peers = defaultdict(set)  # set avoids duplicates
    for key_box in boxes:
        for unit in units[key_box]:
            for peer_box in unit:
                if peer_box != key_box:
                    # defaultdict avoids this raising a KeyError when new keys are added
                    peers[key_box].add(peer_box)
    return peers


def assign_value(values, box, value):
    """You must use this function to update your values dictionary if you want to
    try using the provided visualization tool. This function records each assignment
    (in order) for later reconstruction.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers
    """
    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    prev = values2grid(values)
    values[box] = value
    if len(value) == 1:
        history[values2grid(values)] = (prev, (box, value))
    return values


def cross(A, B):
    """Cross product of elements in A and elements in B """
    return [x + y for x in A for y in B]


def values2grid(values):
    """Convert the dictionary board representation to as string

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    """
    res = []
    for r in rows:
        for c in cols:
            v = values[r + c]
            res.append(v if len(v) == 1 else '.')
    return ''.join(res)


def grid2values(grid):
    """Convert grid into a dict of {square: char} with '123456789' for empties.

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.

        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value,
            then the value will be '123456789'.
    """
    sudoku_grid = {}
    for val, key in zip(grid, boxes):
        if val == '.':
            sudoku_grid[key] = '123456789'
        else:
            sudoku_grid[key] = val
    return sudoku_grid


def display(values):
    """Display the values as a 2-D grid.

    Parameters
    ----------
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()


def reconstruct(values, history):
    """Returns the solution as a sequence of value assignments

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    history(dict)
        a dictionary of the form {key: (key, (box, value))} encoding a linked
        list where each element points to the parent and identifies the value
        assignment that connects from the parent to the current state

    Returns
    -------
    list
        a list of (box, value) assignments that can be applied in order to the
        starting Sudoku puzzle to reach the solution
    """
    path = []
    prev = values2grid(values)
    while prev in history:
        prev, step = history[prev]
        path.append(step)
    return path[::-1]


row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

unitlist = row_units + column_units + square_units

diagonal1 = [i + j for i, j in zip(rows, cols)]
diagonal2 = [i + str(j) for i, j in zip(rows, range(9, 0, -1))]

diagonal = [diagonal1, diagonal2]

unitlist = unitlist + diagonal

# Must be called after all units (including diagonals) are added to the unitlist
units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    The naked twins strategy says that if you have two or more unallocated boxes
    in a unit and there are only two digits that can go in those two boxes, then
    those two digits can be eliminated from the possible assignments of all other
    boxes in the same unit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers

    Notes
    -----
    Your solution can either process all pairs of naked twins from the input once,
    or it can continue processing pairs of naked twins until there are no such
    pairs remaining -- the project assistant test suite will accept either
    convention. However, it will not accept code that does not process all pairs
    of naked twins from the original input. (For example, if you start processing
    pairs of twins and eliminate another pair of twins before the second pair
    is processed then your code will fail the PA test suite.)

    The first convention is preferred for consistency with the other strategies,
    and because it is simpler (since the reduce_puzzle function already calls this
    strategy repeatedly).

    See Also
    --------
    Pseudocode for this algorithm on github:
    https://github.com/udacity/artificial-intelligence/blob/master/Projects/1_Sudoku/pseudocode.md
    """

    out = values.copy()
    for boxA in values:
        for boxB in peers[boxA]:
            if values[boxB] == values[boxA] and len(values[boxB]) == 2:
                intersection = [key for key in peers[boxA] if key in peers[boxB]]
                for i in intersection:
                    for d in values[boxA]:
                        out[i] = out[i].replace(d, '')
    return out


def eliminate(values):
    """Apply the eliminate strategy to a Sudoku puzzle

    The eliminate strategy says that if a box has a value assigned, then none
    of the peers of that box can have the same value.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """

    ones = [v for v in values if len(values[v]) == 1]
    for one in ones:
        for p in peers[one]:
            values[p] = values[p].replace(values[one], '')

    return values


def only_choice(values):
    """Apply the only choice strategy to a Sudoku puzzle

    The only choice strategy says that if only one box in a unit allows a certain
    digit, then that box must be assigned that digit.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    """

    vals = [str(i) for i in range(1, 10)]

    for unit in unitlist:
        for v in vals:
            temp = []
            for u in unit:
                if v in values[u]:
                    temp.append(u)
            if len(temp) == 1:
                values[temp[0]] = v

    return values


def reduce_puzzle(values):
    """Reduce a Sudoku puzzle by repeatedly applying all constraint strategies

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable 
    """
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def find_lowest(values):
    lowest = 9
    box = ""

    for k in values:
        if len(values[k]) < lowest and len(values[k]) > 1:
            lowest = len(values[k])
            box = k
    return box


def search(values):
    """Apply depth first search to solve Sudoku puzzles in order to solve puzzles
    that cannot be solved by repeated reduction alone.

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

    Notes
    -----
    You should be able to complete this function by copying your code from the classroom
    and extending it to call the naked twins strategy.
    """

    values = reduce_puzzle(values)
    if values is False:
        return False
    if sum([len(values[v]) for v in values]) == 81:
        return values

    lowest = find_lowest(values)
    for l in values[lowest]:
        temp = values.copy()
        temp[lowest] = l
        tried = search(temp)
        if tried:
            return tried


def solve(grid):
    """Find the solution to a Sudoku puzzle using search and constraint propagation

    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.
        
        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    # diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    # diag_sudoku_grid = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)
