test = {
  'name': 'Problem 8b',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': 'When exactly one of the Ant instances is a container and the container ant does not already contain another ant',
          'choices': [
            r"""
            When exactly one of the Ant instances is a container and the
            container ant does not already contain another ant
            """,
            'When exactly one of the Ant instances is a container',
            'When both Ant instances are containers',
            'There can never be two Ant instances in the same place'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'When can a second Ant be added to a place that already contains an Ant?'
        },
        {
          'answer': 'The Container Ant',
          'choices': [
            'The Container Ant',
            'The Ant being contained',
            'A list containing both Ants',
            'Whichever Ant was placed there first'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          If two Ants occupy the same Place, what is stored in that place's ant
          instance attribute?
          """
        },
        {
          'answer': 'The Ant instance that is in the same place as itself',
          'choices': [
            'The Ant instance that is in the same place as itself',
            'The Ant instance in the place closest to its own place',
            'A random Ant instance in the gamestate',
            'All the Ant instances in the gamestate'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Which Ant does a ContainerAnt guard?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Container ant added before another ant
          >>> container = ContainerAnt(1)
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(container)  # ContainerAnt in place first
          >>> place.add_insect(other_ant)
          >>> place.ant is other_ant
          False
          >>> place.ant is container
          True
          >>> container.ant_contained is other_ant
          True
          >>> container.place is place
          True
          >>> other_ant.place is container.place  # ThrowerAnt should have the same place attribute as ContainerAnt
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Any Container Ant can be added after another ant
          >>> container = ContainerAnt(1)
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(other_ant)  # Other ant in place first
          >>> place.ant is other_ant
          True
          >>> place.add_insect(container)
          >>> place.ant is container
          True
          >>> container.ant_contained is other_ant
          True
          >>> container.place is place
          True
          >>> other_ant.place is container.place  # ThrowerAnt should have the same place attribute as ContainerAnt
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Only one ant can be added to a container
          >>> container = ContainerAnt(1)
          >>> a = ThrowerAnt()
          >>> b = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(container)
          >>> place.add_insect(a)
          >>> place.add_insect(b)
          Traceback (most recent call last):
          ...
          AssertionError: Too many ants in tunnel_0_0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Combination of add and remove
          >>> container = ContainerAnt(1)
          >>> a = ThrowerAnt()
          >>> b = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(a)
          >>> place.add_insect(container)
          >>> container.remove_from(place)
          >>> place.ant is a
          True
          >>> container = ContainerAnt(1)
          >>> place.add_insect(container)
          >>> a.remove_from(place)
          >>> place.add_insect(b)
          >>> place.ant is container
          True
          >>> b.place is place
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
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
