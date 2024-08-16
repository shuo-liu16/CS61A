test = {
  'name': 'using-pair',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
          'choices': [
            "Pair('+', Pair('-', Pair(2, Pair(4, Pair(6, Pair(8, nil))))))",
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4))), Pair(6, Pair(8))))",
            'Pair(+, Pair(Pair(-, Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))',
            "Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))",
            'None of these'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Write out the Python expression that returns a `Pair` representing the given expression: (+ (- 2 4) 6 8)'
        },
        {
          'answer': '+',
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the operator of the call expression?'
        },
        {
          'answer': 'p.first',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed in the previous part was bound to the name `p`,
          how would you retrieve the operator?
          """
        },
        {
          'answer': 'p.rest',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          If the `Pair` you constructed was bound to the name `p`, 
          how would you retrieve a list containing all of the operands?
          """
        },
        {
          'answer': 'p.rest.first',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How would you retrieve only the first operand?'
        },
        {
          'answer': "Pair('-', Pair(2, Pair(4, nil)))",
          'choices': [
            "'-'",
            "'+'",
            '2',
            '4',
            '-2',
            "Pair('-', Pair(2, Pair(4, nil)))",
            'Pair(2, Pair(4, nil))'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What is the first operand of the call expression (prior to evaluation)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
