test = {
  'name': 'Understanding Eval/Apply',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'Call expressions and special forms',
          'choices': [
            'Call expressions and special forms',
            'Only call expressions',
            'Only special forms',
            'All expressions are represented as Pairs'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What types of expressions are represented as Pairs?'
        },
        {
          'answer': 'env.lookup(expr)',
          'choices': [
            'env.find(name)',
            'scheme_symbolp(expr)',
            'env.lookup(expr)',
            'scheme_forms.SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What expression in the body of scheme_eval finds the value of a name?'
        },
        {
          'answer': 'Check if the first element in the list is a symbol and that the symbol is in the dictionary SPECIAL_FORMS',
          'choices': [
            r"""
            Check if the first element in the list is a symbol and that the
            symbol is in the dictionary SPECIAL_FORMS
            """,
            'Check if the first element in the list is a symbol',
            'Check if the expression is in the dictionary SPECIAL_FORMS'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How do we know if a given combination is a special form?'
        },
        {
          'answer': 'I and II',
          'choices': [
            'I only',
            'II only',
            'III only',
            'I and II',
            'I and III',
            'II and III',
            'I, II and III'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': r"""
          What is the difference between applying builtins and applying user-defined procedures?
          (Choose all that apply)
          
          I.   User-defined procedures open a new frame; builtins do not
          II.  Builtins simply execute a predefined Python function; user-defined
               procedures must evaluate additional expressions in the body
          III. Builtins have a fixed number of arguments; user-defined procedures do not
          
          ---
          """
        },
        {
          'answer': 'SchemeError("1 is not callable")',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("1 is not callable")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
