test = {
  'name': 'Problem 10',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'If the insect is not waterproof, its health is reduced to 0. Otherwise, nothing happens.',
          'choices': [
            r"""
            If the insect is not waterproof, its health is reduced to 0.
            Otherwise, nothing happens.
            """,
            "The insect's health is reduced to 0.",
            'Nothing happens.',
            'The insect goes for a swim.'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What happens when an insect is added to a Water Place?'
        },
        {
          'answer': 'class, all ants of a subclass should either be waterproof or not',
          'choices': [
            'class, all ants of a subclass should either be waterproof or not',
            'class, all ants should be waterproof',
            'instance, the is_waterproof attribute depends on the amount of health a given ant has left',
            'instance, the is_waterproof attribute depends on the given place of an ant'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What type of attribute should "is_waterproof" be?'
        },
        {
          'answer': 'reduce_health, in the Insect class',
          'choices': [
            'reduce_health, in the Insect class',
            'remove_insect, in the Place class',
            'sting, in the Bee class',
            'remove_ant, in the GameState class'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What method deals damage to an Insect and removes it from its place
          if its health reaches 0?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water with Ants
          >>> test_water = Water('Water Test1')
          >>> ant = HarvesterAnt()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          >>> ant = Ant()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          >>> ant = ThrowerAnt()
          >>> test_water.add_insect(ant)
          >>> (ant.health, test_water.ant is None)
          (0, True)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing water with soggy (non-waterproof) bees
          >>> test_bee = Bee(1000000)
          >>> test_bee.is_waterproof = False    # Make Bee non-waterproof
          >>> test_water = Water('Water Test2')
          >>> test_water.add_insect(test_bee)
          >>> test_bee.health
          0
          >>> len(test_water.bees)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing water with waterproof bees
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test3')
          >>> test_water.add_insect(test_bee)
          >>> test_bee.health
          1
          >>> test_bee in test_water.bees
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # test proper call to zero-health callback
          >>> original_zero_health_callback = Insect.zero_health_callback
          >>> Insect.zero_health_callback = lambda x: print("insect died")
          >>> place = Water('Water Test4')
          >>> soggy_bee = Bee(1)
          >>> soggy_bee.is_waterproof = False
          >>> place.add_insect(soggy_bee)
          insect died
          >>> place.add_insect(Bee(1))
          >>> place.add_insect(ThrowerAnt())
          insect died
          >>> Insect.zero_health_callback = original_zero_health_callback
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
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing water inheritance
          >>> old_add_insect = Place.add_insect
          >>> def new_add_insect(self, insect):
          ...     print("called add_insect")
          ...     old_add_insect(self, insect)
          >>> Place.add_insect = new_add_insect
          >>> test_bee = Bee(1)
          >>> test_water = Water('Water Test4')
          >>> test_water.add_insect(test_bee) # if this fails you probably didn't call `add_insect`
          called add_insect
          >>> Place.add_insect = old_add_insect
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
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(beehive, ant_types(), layout, dimensions)
      >>> old_add_insect = Place.add_insect
      """,
      'teardown': r"""
      >>> Place.add_insect = old_add_insect
      """,
      'type': 'doctest'
    }
  ]
}
