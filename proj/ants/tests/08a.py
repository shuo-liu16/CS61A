test = {
  'name': 'Problem 8a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': "In the ContainerAnt's ant_contained instance attribute",
          'choices': [
            "In the ContainerAnt's ant_contained instance attribute",
            "In the ContainerAnt's ant_contained class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a ContainerAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Where is the ant contained by a ContainerAnt stored?'
        },
        {
          'answer': 'By protecting the ant from Bees and allowing it to perform its original action',
          'choices': [
            'By protecting the ant from Bees and allowing it to perform its original action',
            'By attacking Bees that try to attack it',
            "By increasing the ant's health",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How does a ContainerAnt guard its ant?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> container = ContainerAnt(1)
          >>> container2 = ContainerAnt(2)
          >>> container3 = ContainerAnt(3)
          >>> throw_long = LongThrower(1)
          >>> container.can_contain(container2)
          False
          >>> container3.can_contain(throw_long)
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> friend = HungryAnt()
          >>> container.ant_contained is None
          True
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> container.ant_contained is not None
          False
          >>> friend = HungryAnt()
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          True
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(container)
          >>> friend.place = place
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> container.action(gamestate)  # Container holds a HungryAnt that loves to eat!
          >>> bee.health
          0
          >>> container.can_contain(FireAnt()) # Container already holds another ant!
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(1)
          >>> container.action(gamestate) # ContainerAnt does not have an ant contained, should not have any action taken!
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
