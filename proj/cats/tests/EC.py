test = {
  'name': 'Extra Credit',
  'points': 1,
  'suites': [
      {
      'cases': [
        {
          'answer': 'A function that takes another function as an input and returns a new function that extends or modifies the behavior of the original function',
          'choices': [
            'A type of design pattern',
            'A function that takes another function as an input and returns a new function that extends or modifies the behavior of the original function',
            'A method for declaring class properties',
            'A way to loop through an iterable'
          ],
          'hidden': False,
          'multiline': False,
          'question': 'What is a decorator in Python?'
        },
        {
          'answer': 'To add functionality to existing code',
          'choices': [
            'To add functionality to existing code',
            'To loop through arrays',
            'To declare variables',
            'To check for syntax errors in code'
          ],
          'hidden': False,
          'multiline': False,
          'question': 'Why do we use decorators in Python?'
        },
        {
          'answer': 'Using the "@decorator_name" syntax above the function definition',
          'choices': [
            'Using the "#" symbol before the function',
            'By passing the decorator as a parameter to the function',
            'Using the "@decorator_name" syntax above the function definition',
            'By importing the decorator from a library'
          ],
          'hidden': False,
          'multiline': False,
          'question': 'How is a decorator applied to a function?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def my_decorator(func):
          ...   def wrapper():
          ...       print("Say Hello")
          ...       func()
          ...       print("Say Goodbye")
          ...   return wrapper

          >>> @my_decorator
          ... def say_hello():
          ...     print("Hello World")

          >>> say_hello()
          Say Hello
          Hello World
          Say Goodbye
          """,
          'hidden': False,
          'multiline': True
        },
                {
          'code': r"""
          >>> def magic_decorator(func):
          ...   def wrapper(x):
          ...     return func(x * 2)
          ...   return wrapper

          >>> @magic_decorator
          ... def myfunc(x):
          ...   return x * 3

          >>> print(myfunc(4))
          24
          """,
          'hidden': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations.call_count = 0
          >>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          3
          >>> minimum_mewtations.call_count <= 350 # see if you removed redundant recursive calls
          True
          >>> minimum_mewtations.call_count = 0
          >>> minimum_mewtations("ckiteus", "kittens", big_limit)
          3
          >>> minimum_mewtations.call_count <= 320
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Check that you're only using the minimum_mewtations func.
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "abc", "def", 3)
          ...     output = buf.getvalue()
          >>> lines = [line for line in output.split('\n') if 'funcname' in line]
          >>> func_names = set([l.split(",")[1].split(":")[1].strip() for l in lines])
          >>> func_names == {'counted', 'minimum_mewtations', 'memoized'}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)
          'well'
          >>> minimum_mewtations.call_count <= 72000 # minimum_mewtations should be memoized
          True
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, feline_fixes, 4)
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)  # identical to the first call
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 4)
          'well'
          >>> minimum_mewtations.call_count
          0
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", common_words, minimum_mewtations, 3)
          'well'
          >>> minimum_mewtations.call_count < 2500
          True
          >>> minimum_mewtations.call_count = 0
          >>> autocorrect("woll", all_words, minimum_mewtations, 2)
          'will'
          >>> minimum_mewtations.call_count < 2700000
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import minimum_mewtations, feline_fixes, autocorrect, lines_from_file
      >>> all_words = lines_from_file("data/words.txt")
      >>> common_words = lines_from_file("data/common_words.txt")
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}