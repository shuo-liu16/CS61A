test = {
  'name': 'Problem 12',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': "Attacks the nearest bee and doubles the damage of all the ants behind her (that haven't already been doubled)",
          'choices': [
            r"""
            Attacks the nearest bee and doubles the damage of all the ants
            behind her (that haven't already been doubled)
            """,
            r"""
            Doubles the damage of all the ants behind her (that haven't
            already been doubled)
            """,
            r"""
            Doubles the damage of all the ants in front of her (that haven't
            already been doubled)
            """,
            r"""
            Doubles the damage of all the ants in the colony (that haven't
            already been doubled)
            """
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What does a QueenAnt do each turn?'
        },
        {
          'answer': 'If a Bee reaches the end of a tunnel or a QueenAnt dies',
          'choices': [
            'If a Bee reaches the end of a tunnel or a QueenAnt dies',
            'If there are no ants left in the colony',
            'If a second QueenAnt is placed in the colony',
            'If a Bee attacks a QueenAnt'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Under what circumstances do Ants lose the game?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing QueenAnt parameters
          >>> QueenAnt.food_cost
          7
          >>> queen = QueenAnt()
          >>> queen.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive = Hive(AssaultPlan())
      >>> dimensions = (2, 9)
      >>> gamestate = GameState(beehive, ant_types(), dry_layout, dimensions, food=100)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # QueenAnt Placement
          >>> queen = ants.QueenAnt()
          >>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
          >>> tunnel = [gamestate.places['tunnel_0_{0}'.format(i)]
          ...         for i in range(9)]
          >>> tunnel[1].add_insect(back_ant)
          >>> tunnel[7].add_insect(front_ant)
          >>> tunnel[4].ant is None
          True
          >>> back_ant.damage           # Ants should not have double damage yet
          1
          >>> front_ant.damage
          1
          >>> tunnel[4].add_insect(queen)
          >>> queen.action(gamestate)
          >>> back_ant.damage           # Ants behind queen should have double damage
          2
          >>> front_ant.damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing damage multiplier
          >>> queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> # layout
          >>> # queen_tunnel: [Back, Guard/Guarded, Queen, Front, Bee     ]
          >>> # side_tunnel : [Side,              ,      ,      , Side Bee]
          >>> queen = ants.QueenAnt()
          >>> back = ants.ThrowerAnt()
          >>> front = ants.ThrowerAnt()
          >>> guard = ants.BodyguardAnt()
          >>> guarded = ants.ThrowerAnt()
          >>> side = ants.ThrowerAnt()
          >>> bee = ants.Bee(10)
          >>> side_bee = ants.Bee(10)
          >>> queen_tunnel[0].add_insect(back)
          >>> queen_tunnel[1].add_insect(guard)
          >>> queen_tunnel[1].add_insect(guarded)
          >>> queen_tunnel[2].add_insect(queen)
          >>> queen_tunnel[3].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> queen_tunnel[4].add_insect(bee)
          >>> side_tunnel[4].add_insect(side_bee)
          >>> queen.action(gamestate)
          >>> bee.health
          9
          >>> back.action(gamestate)
          >>> bee.health
          7
          >>> front.action(gamestate)
          >>> bee.health
          6
          >>> guard.action(gamestate)
          >>> bee.health # if this is 5 you probably forgot to double the damage of the guard's contents
          4
          >>> side.action(gamestate)
          >>> side_bee.health
          9
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> beehive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> gamestate = ants.GameState(beehive, ants.ant_types(),
      ...                            ants.dry_layout, dimensions, food=20)
      >>> ants.ants_lose = lambda: None
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing game over
          >>> queen = ants.QueenAnt()
          >>> tunnel = [gamestate.places['tunnel_0_{0}'.format(i)]
          ...           for i in range(9)]
          >>> tunnel[4].add_insect(queen)
          >>> bee = ants.Bee(3)
          >>> tunnel[6].add_insect(bee)     # Bee in a different place from the queen
          >>> bee.action(gamestate)         # Game should not end
          >>> bee.move_to(tunnel[4])        # Bee moved to place with queen
          >>> bee.action(gamestate)         # Game should end
          AntsLoseException
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing if queen will not crash with no one to double
          >>> queen = ants.QueenAnt()
          >>> gamestate.places['tunnel_0_2'].add_insect(queen)
          >>> queen.action(gamestate)
          >>> # Attack a bee
          >>> bee = ants.Bee(3)
          >>> gamestate.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(gamestate)
          >>> bee.health # Queen should still hit the bee
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing QueenAnt action method
          >>> queen = ants.QueenAnt()
          >>> bee = ants.Bee(10)
          >>> ant = ants.ThrowerAnt()
          >>> gamestate.places['tunnel_0_0'].add_insect(ant)
          >>> gamestate.places['tunnel_0_1'].add_insect(queen)
          >>> gamestate.places['tunnel_0_4'].add_insect(bee)
          >>> queen.action(gamestate)
          >>> bee.health   # Queen should damage bee
          9
          >>> ant.damage  # Queen should double damage
          2
          >>> ant.action(gamestate)
          >>> bee.health   # If failed, ThrowerAnt has incorrect damage
          7
          >>> queen.health   # Long live the Queen
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Extensive damage doubling tests
          >>> queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)]
          ...         for j in range(9)] for i in range(2)]
          >>> queen = ants.QueenAnt()
          >>> queen_tunnel[7].add_insect(queen)
          >>> # Turn 0
          >>> thrower = ants.ThrowerAnt()
          >>> fire = ants.FireAnt()
          >>> side = ants.ThrowerAnt()
          >>> front = ants.ThrowerAnt()
          >>> queen_tunnel[0].add_insect(thrower)
          >>> queen_tunnel[1].add_insect(fire)
          >>> queen_tunnel[8].add_insect(front)
          >>> side_tunnel[0].add_insect(side)
          >>> # layout right now
          >>> # [thrower, fire, , , , , , queen, front]
          >>> # [side   ,     , , , , , ,      ,      ]
          >>> thrower.damage, fire.damage = 101, 102
          >>> front.damage, side.damage = 104, 105
          >>> queen.action(gamestate)
          >>> (thrower.damage, fire.damage)
          (202, 204)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> # Turn 1
          >>> tank = ants.TankAnt()
          >>> guard = ants.BodyguardAnt()
          >>> queen_tank = ants.TankAnt()
          >>> queen_tunnel[6].add_insect(tank)          # Not protecting an ant
          >>> queen_tunnel[1].add_insect(guard)         # Guarding FireAnt
          >>> queen_tunnel[7].add_insect(queen_tank)    # Guarding QueenAnt
          >>> # layout right now
          >>> # [thrower, guard/fire, , , , , tank, queen_tank/queen, front]
          >>> # [side   ,           , , , , ,     ,                 ,      ]
          >>> tank.damage, guard.damage, queen_tank.damage = 1001, 1002, 1003
          >>> queen.action(gamestate)
          >>> # unchanged
          >>> (thrower.damage, fire.damage)
          (202, 204)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> (tank.damage, guard.damage)
          (2002, 2004)
          >>> queen_tank.damage
          1003
          >>> # Turn 2
          >>> thrower1 = ants.ThrowerAnt()
          >>> thrower2 = ants.ThrowerAnt()
          >>> queen_tunnel[6].add_insect(thrower1)      # Add thrower1 in TankAnt
          >>> queen_tunnel[5].add_insect(thrower2)
          >>> # layout right now
          >>> # [thrower, guard/fire, , , , thrower2, tank/thrower1, queen_tank/queen, front]
          >>> # [side   ,           , , , ,         ,              ,                 ,      ]
          >>> thrower1.damage, thrower2.damage = 10001, 10002
          >>> queen.action(gamestate)
          >>> (thrower.damage, fire.damage)
          (202, 204)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> (tank.damage, guard.damage)
          (2002, 2004)
          >>> queen_tank.damage
          1003
          >>> (thrower1.damage, thrower2.damage)
          (20002, 20004)
          >>> # Turn 3
          >>> tank.reduce_health(tank.health)             # Expose thrower1
          >>> queen.action(gamestate)
          >>> (thrower.damage, fire.damage)
          (202, 204)
          >>> (front.damage, side.damage)
          (104, 105)
          >>> guard.damage
          2004
          >>> queen_tank.damage
          1003
          >>> (thrower1.damage, thrower2.damage)
          (20002, 20004)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Adding/Removing QueenAnt with Container
          >>> place = gamestate.places['tunnel_0_3']
          >>> queen = ants.QueenAnt()
          >>> container = ants.TankAnt()
          >>> place.add_insect(container)
          >>> place.ant is container
          True
          >>> container.place is place
          True
          >>> container.ant_contained is None
          True
          >>> place.add_insect(queen)
          >>> container.ant_contained is queen
          True
          >>> queen.place is place
          True
          >>> queen.action(gamestate) # should not error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # test proper call to zero_health_callback
          >>> original_zero_health_callback = ants.Insect.zero_health_callback
          >>> ants.Insect.zero_health_callback = lambda x: print("insect died")
          >>> real = ants.QueenAnt()
          >>> gamestate.places['tunnel_0_2'].add_insect(real)
          >>> ants.Insect.zero_health_callback = original_zero_health_callback
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from ants import *
          >>> QueenAnt.implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import ants, importlib
      >>> importlib.reload(ants)
      >>> beehive = ants.Hive(ants.AssaultPlan())
      >>> dimensions = (2, 9)
      >>> gamestate = ants.GameState(beehive, ants.ant_types(),
      ...                            ants.dry_layout, dimensions, food=20)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
