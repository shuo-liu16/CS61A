test = {
  'name': 'Problem Optional 2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> laser = LaserAnt()
          >>> ant = HarvesterAnt(2)
          >>> bee1 = Bee(2)
          >>> bee2 = Bee(2)
          >>> bee3 = Bee(2)
          >>> bee4 = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(laser)
          >>> gamestate.places["tunnel_0_0"].add_insect(bee4)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee2)
          >>> gamestate.places["tunnel_0_4"].add_insect(ant)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee3)
          >>> laser.action(gamestate)
          >>> bee4.health
          0.0
          >>> bee1.health
          0.8125
          >>> bee2.health
          0.875
          >>> ant.health
          1.1875
          >>> bee3.health
          1.5
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
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> LaserAnt.implemented
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
