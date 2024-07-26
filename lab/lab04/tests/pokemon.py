test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> 'mewtwo' in pokemon
          False
          >>> 'pikachu' in pokemon
          True
          >>> 25 in pokemon
          False
          >>> 148 in pokemon.values()
          True
          >>> 151 in pokemon.keys()
          False
          >>> 'mew' in pokemon.keys()
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
