test = {
  'name': 'Problem 5',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'By accessing the place instance attribute, which is a Place object',
          'choices': [
            'By accessing the place instance attribute, which is a Place object',
            r"""
            By accessing the place instance attribute, which is the name of
            some Place object
            """,
            'By calling the Place constructor, passing in the FireAnt instance',
            'By calling the FireAnt constructor'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How can you obtain the current place of a FireAnt?'
        },
        {
          'answer': 'By accessing the bees instance attribute, which is a list of Bee objects',
          'choices': [
            r"""
            By accessing the bees instance attribute, which is a list of Bee
            objects
            """,
            r"""
            By accessing the bees instance attribute, which is a dictionary of
            Bee objects
            """,
            'By calling the add_insect method on the place instance',
            'By calling the Bee constructor, passing in the place instance'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How can you obtain all of the Bees currently in a given place?'
        },
        {
          'answer': 'Yes, but you should iterate over a copy of the list to avoid skipping elements',
          'choices': [
            r"""
            Yes, but you should iterate over a copy of the list to avoid skipping
            elements
            """,
            'Yes, you can mutate a list while iterating over it with no problems',
            r"""
            No, Python doesn't allow list mutation on a list that is being
            iterated through
            """
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Can you iterate over a list while mutating it?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing FireAnt parameters
          >>> fire = FireAnt()
          >>> FireAnt.food_cost
          5
          >>> fire.health
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = Ant.__init__
          >>> Ant.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
          >>> fire = FireAnt()
          init
          >>> Ant.__init__ = original
          >>> fire = FireAnt()
          >>> original = Ant.reduce_health
          >>> Ant.reduce_health = lambda self, amount: print("reduced") #If this errors, you are not calling the inherited method correctly
          >>> place = gamestate.places['tunnel_0_4']
          >>> place.add_insect(fire)
          >>> fire.reduce_health(1)
          reduced
          >>> Ant.reduce_health = original
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = gamestate.places['tunnel_0_4']
          >>> fire = FireAnt(health=1)
          >>> place.add_insect(fire)        # Add a FireAnt with 1 health
          >>> place.add_insect(Bee(3))      # Add a Bee with 3 health
          >>> place.add_insect(Bee(5))      # Add a Bee with 5 health
          >>> len(place.bees)               # How many bees are there?
          2
          >>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
          >>> fire.health
          0
          >>> fire.place is None
          True
          >>> len(place.bees)               # How many bees are left?
          1
          >>> place.bees[0].health           # What is the health of the remaining Bee?
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> place = gamestate.places['tunnel_0_4']
          >>> ant = FireAnt(health=1)           # Create a FireAnt with 1 health
          >>> place.add_insect(ant)      # Add a FireAnt to place
          >>> ant.place is place
          True
          >>> place.remove_insect(ant)   # Remove FireAnt from place
          >>> ant.place is place         # Is the ant's place still that place?
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire damage when the fire ant does not die
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(5)
          >>> ant = FireAnt(health=100)
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(gamestate) # attack the FireAnt
          >>> ant.health
          99
          >>> bee.health
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing no hardcoded 3
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(100)
          >>> ant = FireAnt(health=1)
          >>> ant.damage = 49
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(gamestate) # attack the FireAnt
          >>> ant.health
          0
          >>> bee.health
          50
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire damage when the fire ant does die
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(5)
          >>> ant = FireAnt(health=1)
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(gamestate) # attack the FireAnt
          >>> ant.health
          0
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire does damage to all Bees in its Place
          >>> place = gamestate.places['tunnel_0_4']
          >>> place.add_insect(FireAnt(1))
          >>> for i in range(100):          # Add 100 Bees with 3 health
          ...     place.add_insect(Bee(3))
          >>> place.bees[0].action(gamestate)  # The first Bee attacks FireAnt
          >>> len(place.bees)               # How many bees are left?
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing fire damage is instance attribute
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(900)
          >>> buffAnt = FireAnt(1)
          >>> buffAnt.damage = 500   # Feel the burn!
          >>> place.add_insect(bee)
          >>> place.add_insect(buffAnt)
          >>> bee.action(gamestate) # attack the FireAnt
          >>> bee.health  # is damage an instance attribute?
          399
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt(1)
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(gamestate)    # Attack the FireAnt
          >>> bee.health
          6
          >>> ant.health
          0
          >>> place.ant is None     # The FireAnt should not occupy the place anymore
          True
          >>> bee.action(gamestate)
          >>> bee.health             # Bee should not get damaged again
          6
          >>> bee.place.name        # Bee should not have been blocked
          'tunnel_0_3'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # General FireAnt Test
          >>> place = gamestate.places['tunnel_0_4']
          >>> bee = Bee(10)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> ant.reduce_health(0.1) # Poke the FireAnt
          >>> bee.health             # Bee should only get slightly damaged
          9.9
          >>> ant.health
          2.9
          >>> place.ant is ant      # The FireAnt should still be at place
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
          >>> place = gamestate.places["tunnel_0_0"]
          >>> bee = Bee(3)
          >>> ant = FireAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> bee.action(gamestate)
          >>> bee.action(gamestate)
          >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
          insect died
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
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
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
          >>> from ants import *
          >>> FireAnt.implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
