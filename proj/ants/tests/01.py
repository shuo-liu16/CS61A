test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': "Placing an ant into the colony will decrease the colony's total available food by that ant's food_cost",
          'choices': [
            r"""
            Placing an ant into the colony will decrease the colony's total
            available food by that ant's food_cost
            """,
            r"""
            Each turn, each Ant in the colony eats food_cost food from the
            colony's total available food
            """,
            r"""
            Each turn, each Ant in the colony adds food_cost food to the
            colony's total available food
            """
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the purpose of the food_cost attribute?'
        },
        {
          'answer': 'class, all Ants of the same subclass cost the same to place',
          'choices': [
            'class, all Ants of the same subclass cost the same to place',
            'class, all Ants cost the same to place no matter what type of Ant it is',
            'instance, the food_cost of an Ant depends on the location it is placed',
            'instance, the food_cost of an Ant is randomized upon initialization'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What type of attribute is food_cost?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> Ant.food_cost
          0
          >>> HarvesterAnt.food_cost
          2
          >>> ThrowerAnt.food_cost
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HarvesterAnt action
          >>> # Create a test layout where the colony is a single row with 9 tiles
          >>> beehive = Hive(make_test_assault_plan())
          >>> gamestate = GameState(beehive, ant_types(), dry_layout, (1, 9))
          >>> #
          >>> gamestate.food = 4
          >>> harvester = HarvesterAnt()
          >>> # Note: initializing an Ant doesn't cost food,
          >>> # only deploying an Ant in the game layout does.
          >>> # For this test case, Ants can still take actions
          >>> # without being deployed in the game layout.
          >>> #
          >>> gamestate.food
          4
          >>> harvester.action(gamestate)
          >>> gamestate.food
          5
          >>> harvester.action(gamestate)
          >>> gamestate.food
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from ants import *
          >>> HarvesterAnt.implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> from ants_plans import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
