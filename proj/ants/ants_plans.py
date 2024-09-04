import ants
import argparse
from ants import AssaultPlan


def make_test_assault_plan(ants_impl=None):
    ants_impl = ants_impl or ants
    return AssaultPlan().add_wave(ants_impl.Bee, 3, 2, 1).add_wave(ants_impl.Bee, 3, 3, 1)


def make_easy_assault_plan(ants_impl=None):
    ants_impl = ants_impl or ants_impl
    plan = AssaultPlan()
    for time in range(3, 16, 2):
        plan.add_wave(ants_impl.Bee, 3, time, 1) # Adding 1 bee of health 3 at timestamp TIME
    plan.add_wave(ants_impl.Wasp, 3, 4, 1) # Assing 1 wasp of health 3 at timestamp 4
    plan.add_wave(ants_impl.Wasp, 3, 8, 1)
    plan.add_wave(ants_impl.Wasp, 3, 12, 1)
    plan.add_wave(ants_impl.Boss, 15, 16, 1)
    return plan


def make_normal_assault_plan(ants_impl=None):
    ants_impl = ants_impl or ants
    plan = AssaultPlan()

    for time in range(3, 16, 2): # Adding 2 bees (1 bee for time = 3, 5) of health 3 at timestamp 3, 5, 7, 9, 11, 13, 15
        if time == 3 or time == 5:
            # Change number of bees to 1
            plan.add_wave(ants_impl.Bee, 3, time, 1)
        else:
            plan.add_wave(ants_impl.Bee, 3, time, 2)

    for time in range(6, 13, 3): # Adding 1 Wasp of health 2 at time 6, 9, 12
        plan.add_wave(ants_impl.Wasp, 2, time, 1)

    for time in range(7, 11, 3): # Adding 1 Ninja of health 1 at time 7, 10
        plan.add_wave(ants_impl.Wasp, 1, time, 1)

    for time in range(12, 15, 2): # Adding 1 Wasp (health 3) and 1 Ninja (health 2) at time 12, 14
        plan.add_wave(ants_impl.Wasp, 3, time, 1)
        plan.add_wave(ants_impl.Wasp, 2, time, 1)

    for time in range(13, 19, 2): # Adding 2 Wasp (health 3) + 2 Ninja (health 3) at time 13, 15, 17
        plan.add_wave(ants_impl.Wasp, 3, time, 2)
        plan.add_wave(ants_impl.Wasp, 3, time, 2)

    for time in range(16, 23, 2): # Adding 2 bees of health 5 at timestamp 16, 18, 20, 22
        plan.add_wave(ants_impl.Bee, 5, time, 2)

    for time in range(24, 31, 2): # Adding 2 bees of health 6 at timestamp 24, 26, 28, 30
        plan.add_wave(ants_impl.Bee, 6, time, 2)

    for time in range(20, 30, 3): # Adding 2 Ninja of health 3 at time 20, 23, 26, 29
        plan.add_wave(ants_impl.Wasp, 3, time, 2)

    for time in range(21, 26, 2): # Adding 1 Wasp of health 5 at time 21, 23, 25
        plan.add_wave(ants_impl.Wasp, 5, time, 1)

    for time in range(28, 31): # Adding 2 Wasp of health 6 at time 28, 29, 30
        plan.add_wave(ants_impl.Wasp, 6, time, 2)

    plan.add_wave(ants_impl.Boss, 50, 30, 1)

    return plan


def make_hard_assault_plan(ants_impl=None):
    ants_impl = ants_impl or ants
    plan = AssaultPlan()

    for time in range(3, 9, 2): # Adding 2 bees (1 bee for time = 3) of health 3 at timestamp 3, 5, 7
        if time == 3:
            # Change number of bees to 1
            plan.add_wave(ants_impl.Bee, 3, time, 1)
        else:
            plan.add_wave(ants_impl.Bee, 3, time, 2)

    for time in range(9, 16, 2): # Adding 3 bees of health 3 at timestamp 9, 11, 13, 15
        plan.add_wave(ants_impl.Bee, 3, time, 3)

    for time in range(5, 9, 3): # Adding 1 Wasp of health 2 at time 5, 8
        plan.add_wave(ants_impl.Wasp, 2, time, 1)

    for time in range(7, 12, 2): # Adding 3 Ninja of health 1 at time 7, 9
        plan.add_wave(ants_impl.Wasp, 1, time, 3)

    for time in range(10, 15, 2): # Adding 2 Wasp (health 3) and 1 Ninja (health 3) at time 10, 12, 14
        plan.add_wave(ants_impl.Wasp, 3, time, 2)
        plan.add_wave(ants_impl.Wasp, 3, time, 1)

    for time in range(13, 19, 2): # Adding 3 Wasp (health 3) + 3 Ninja (health 3) at time 13, 15, 17
        plan.add_wave(ants_impl.Wasp, 3, time, 3)
        plan.add_wave(ants_impl.Wasp, 3, time, 3)

    for time in range(16, 23, 2): # Adding 3 bees of health 5 at timestamp 16, 18, 20, 22
        plan.add_wave(ants_impl.Bee, 5, time, 3)

    for time in range(24, 31, 2): # Adding 3 bees of health 6 at timestamp 24, 26, 28, 30
        plan.add_wave(ants_impl.Bee, 6, time, 3)

    for time in range(20, 30, 2): # Adding 2 Ninja of health 3 at time 20, 22, 24, 26, 28
        plan.add_wave(ants_impl.Wasp, 3, time, 2)

    for time in range(21, 26, 2): # Adding 2 Wasp of health 6 at time 21, 23, 25
        plan.add_wave(ants_impl.Wasp, 6, time, 2)

    for time in range(28, 31): # Adding 4 Wasp of health 8 at time 28, 29, 30
        plan.add_wave(ants_impl.Wasp, 8, time, 4)

    plan.add_wave(ants_impl.Boss, 65, 30, 1)

    return plan


def make_extra_hard_assault_plan(ants_impl=None):
    ants_impl = ants_impl or ants
    plan = AssaultPlan()

    for time in range(3, 9, 2): # Adding 2 bees of health 3 at timestamp 3, 5, 7
        plan.add_wave(ants_impl.Bee, 3, time, 2)

    for time in range(9, 16, 2): # Adding 3 bees of health 3 at timestamp 9, 11, 13, 15
        plan.add_wave(ants_impl.Bee, 3, time, 3)

    for time in range(5, 12, 2): # Adding 1 Wasp of health 2 at time 5, 7, 9, 11
        plan.add_wave(ants_impl.Wasp, 2, time, 1)

    for time in range(7, 12, 2): # Adding 3 Ninja of health 2 at time 7, 9, 11
        plan.add_wave(ants_impl.Wasp, 2, time, 3)

    for time in range(10, 15, 2): # Adding 2 Wasp (health 3) and 2 Ninja (health 3) at time 10, 12, 14
        plan.add_wave(ants_impl.Wasp, 3, time, 2)
        plan.add_wave(ants_impl.Wasp, 3, time, 2)

    for time in range(13, 19, 2): # Adding 3 Wasp (health 4) + 3 Ninja (health 3) at time 13, 15, 17
        plan.add_wave(ants_impl.Wasp, 4, time, 3)
        plan.add_wave(ants_impl.Wasp, 3, time, 3)

    plan.add_wave(ants_impl.Boss, 10, 15, 1)

    for time in range(16, 25, 2): # Adding 3 bees of health 6 at timestamp 16, 18, 20, 22, 24
        plan.add_wave(ants_impl.Bee, 6, time, 3)

    for time in range(26, 31, 2): # Adding 4 bees of health 6 at timestamp 26, 28, 30
        plan.add_wave(ants_impl.Bee, 6, time, 4)

    for time in range(20, 30, 2): # Adding 2 Ninja of health 3 at time 20, 22, 24, 26, 28
        plan.add_wave(ants_impl.Wasp, 3, time, 2)

    for time in range(21, 26, 2): # Adding 2 Wasp of health 8 at time 21, 23, 25
        plan.add_wave(ants_impl.Wasp, 8, time, 2)

    for time in range(28, 31): # Adding 4 Wasp of health 10 at time 28, 29, 30
        plan.add_wave(ants_impl.Wasp, 10, time, 4)

    plan.add_wave(ants_impl.Boss, 75, 30, 1)

    return plan


def create_game_state():
    """Reads command-line arguments and returns a game state with these options."""

    parser = argparse.ArgumentParser(description="Play Ants vs. SomeBees")

    parser.add_argument('-d', type=str, metavar='DIFFICULTY', help='sets difficulty of game (test/easy/normal/hard/extra-hard)')
    parser.add_argument('-w', '--water', action='store_true', help='loads a full layout with water')
    parser.add_argument('--food', type=int, help='number of food to start with when testing', default=2)
    args = parser.parse_args()

    if args.d in ['t', 'test']:
        assault_plan = make_test_assault_plan(ants)
        num_tunnels = 1
    elif args.d in ['e', 'easy']:
        assault_plan = make_easy_assault_plan(ants)
        num_tunnels = 2
    elif args.d in ['h', 'hard']:
        assault_plan = make_hard_assault_plan(ants)
        num_tunnels = 4
    elif args.d in ['i', 'extra-hard']:
        assault_plan = make_extra_hard_assault_plan(ants)
        num_tunnels = 4
    else:
        assault_plan = make_normal_assault_plan(ants)
        num_tunnels = 4

    beehive = ants.Hive(assault_plan)
    layout = ants.wet_layout if args.water else ants.dry_layout
    food = args.food
    tunnel_length = 10
    dimensions = (num_tunnels, tunnel_length)

    return ants.GameState(beehive, ants.ant_types(), layout, dimensions, food)