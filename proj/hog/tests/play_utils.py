import random

SUMMARY = "Start scores = ({s0}, {s1}).\nPlayer {w} rolls {nr} dice and gets outcomes {rv}.\nEnd scores = ({e0}, {e1})"

def trace_play(play, strategy0, strategy1, update, score0, score1, dice, goal, say):
    """Wraps the user's play function and
        (1) ensures that strategy0 and strategy1 are called exactly once per turn
        (2) records the entire game, returning the result as a list of dictionaries,
            each with keys "s0_start", "s1_start", "who", "num_dice", "dice_values"
    Returns (s0, s1, trace) where s0, s1 are the return values from play and trace
        is the trace as specified above.
    This might seem a bit overcomplicated but it will also used to create the game
        traces for the fuzz test (when run against the staff solution).
    """
    game_trace = []

    def mod_strategy(who, my_score, opponent_score):
        if game_trace:
            prev_total_score = game_trace[-1]["s0_start"] + game_trace[-1]["s1_start"]
            if prev_total_score == my_score + opponent_score:
                # game is still on last turn since the total number of points
                # goes up every turn
                return game_trace[-1]["num_dice"]
        current_num_dice = (strategy0, strategy1)[who](my_score, opponent_score)
        current_turn = {
            "s0_start": [my_score, opponent_score][who],
            "s1_start": [my_score, opponent_score][1 - who],
            "who": who,
            "num_dice": current_num_dice,
            "dice_values": [],  # no dice rolled yet
        }
        game_trace.append(current_turn)
        return current_num_dice

    def mod_dice():
        roll = dice()
        if not game_trace:
            raise RuntimeError("roll_dice called before either strategy function")
        game_trace[-1]["dice_values"].append(roll)
        return roll

    s0, s1 = play(
        lambda a, b: mod_strategy(0, a, b),
        lambda a, b: mod_strategy(1, a, b),
        update,
        score0,
        score1,
        dice=mod_dice,
        goal=goal,
        #say=safe(say),
    )
    return s0, s1, game_trace

def safe(commentary):
    def new_commentary(score0, score1, leader=None):
        try:
            leader, message = commentary(score0, score1, leader)
        except TypeError as e:
            print("Error in commentary function")
        return leader, message
    return new_commentary

def describe_game(hog, test_number, score0, score1, goal, update):
    strat_seed0, strat_seed1, dice_seed = run_with_seed(test_number, lambda: [random.randrange(2**32) for _ in range(3)])
    strategy0 = random_strat(strat_seed0)
    strategy1 = random_strat(strat_seed1)
    dice = get_dice(dice_seed)
    s0last, s1last, game_trace = trace_play(
        hog.play,
        strategy0,
        strategy1,
        update=update,
        score0=score0,
        score1=score1,
        dice=dice,
        goal=goal,
        say=None
        )

    end_of_turn = [(turn["s0_start"], turn["s1_start"]) for turn in game_trace[1:]]
    end_of_turn.append((s0last, s1last))
    summary = []
    for turn, end in zip(game_trace, end_of_turn):
        summary.append(SUMMARY.format(
            s0=turn["s0_start"],
            s1=turn["s1_start"],
            w=turn["who"],
            nr=turn["num_dice"],
            rv=turn["dice_values"],
            e0=end[0],
            e1=end[1]
        ))
    summary.append("Game Over")
    return summary

def random_strat(seed):
    """
    Makes a random strategy from based on the given seed
    """
    def random_strat(score, opponent_score):
        # Save the state of the random generator, so strategy calls don't
        # impact dice rolls.
        # using this because python's hash function is NOT CONSISTENT ACROSS OSs!!!!!!!!!!!!11!!22!!2!
        conditional_seed = score * 314159265358979 + opponent_score * 27182818284590452353602874713527 + seed * 161803398874989484820
        return run_with_seed(conditional_seed % (2 ** 32), lambda: random.randrange(0, 11))
    return random_strat

def run_with_seed(seed, fn):
    state = random.getstate()
    random.seed(seed)
    result = fn()
    random.setstate(state)
    return result

def get_dice(seed):
    def dice():
        nonlocal seed
        seed, value = run_with_seed(seed, lambda: (random.randrange(0, 2**32), random.randrange(1, 7)))
        return value
    return dice