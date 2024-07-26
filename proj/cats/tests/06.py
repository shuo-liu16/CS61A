test = {
  'name': 'Problem 6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_fixes("car", "cad", big_limit)
          1
          >>> feline_fixes("this", "that", big_limit)
          2
          >>> feline_fixes("one", "two", big_limit)
          3
          >>> feline_fixes("from", "form", big_limit)
          2
          >>> feline_fixes("awe", "awesome", big_limit)
          4
          >>> feline_fixes("awful", "awesome", big_limit)
          5
          >>> feline_fixes("awful", "awesome", 3) > 3
          True
          >>> feline_fixes("awful", "awesome", 4) > 4
          True
          >>> feline_fixes("awful", "awesome", 5) > 5
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
          1
          >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
          2
          >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
          3
          >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
          5
          >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> feline_fixes("goodbye", "good", big_limit)
          3
          >>> feline_fixes("pront", "print", big_limit)
          1
          >>> feline_fixes("misspollid", "misspelled", big_limit)
          2
          >>> feline_fixes("worry", "word", big_limit)
          2
          >>> feline_fixes("first", "flashy", big_limit)
          4
          >>> feline_fixes("hash", "ash", big_limit)
          4
          >>> feline_fixes("ash", "hash", big_limit)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 0
          >>> feline_fixes("baste", "bastion", big_limit) > big_limit
          True
          >>> feline_fixes("awesome", "awesome", big_limit)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "peeling", "gestate", "west",
          ...                     "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, feline_fixes, 10)
          'peeling'
          >>> autocorrect("abstrction", small_words_list, feline_fixes, 10)
          'abstract'
          >>> autocorrect("wird", small_words_list, feline_fixes, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, feline_fixes, 10)
          'nest'
          >>> # ban iteration, list comprehensions
          >>> test.check('cats.py', 'feline_fixes', ['While', 'For', 'ListComp'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Check that the recursion stops when the limit is reached
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(feline_fixes, "someaweqwertyuio", "awesomeasdfghjkl", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) < 12
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('rut', 'ruhw', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('yo', 'yo', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('slurp', 'slurpn', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('nice', 'nica', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('owen', 'owen', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('donee', 'shush', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('drest', 'dresm', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('cand', 'towy', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('drawn', 'terry', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('stour', 'shows', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('plash', 'cw', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('cube', 'cube', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('envy', 'en', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('panto', 'panto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('herem', 'herem', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('zanze', 'culm', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('kauri', 'kourj', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('hiver', 'hicer', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('tulip', 'lulipi', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('aside', 'ataxy', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('volt', 'vol', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('sleep', 'sleop', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('cet', 'duad', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('opal', 'oral', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('pathy', 'pathy', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('drive', 'dritebcx', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('bater', 'bateri', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('ward', 'crier', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('massy', 'massy', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('tonk', 'tonhbx', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('sith', 'demit', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('arty', 'ar', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('exist', 'exisp', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('plot', 'plotf', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('wreak', 'wreak', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('icon', 'ipog', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('caza', 'scale', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('rann', 'daw', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('natal', 'natalj', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('tji', 'tjv', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('input', 'input', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('lysin', 'lzsunl', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('bed', 'bey', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('topsl', 'topsl', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('becap', 'becap', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('tiny', 'sizes', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('plots', 'plotss', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('plote', 'plot', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('libra', 'unact', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('shed', 'shetg', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('lunes', 'lunes', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('shooi', 'sgcoi', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('cahow', 'cahow', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('watch', 'watch', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('jeans', 'uefnp', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('floey', 'uvea', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('pew', 'pe', k) > k for k in range(3)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('tec', 'teca', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('chef', 'drib', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('sowel', 'evert', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('zebu', 'zbb', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('magma', 'magmasm', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('shood', 'ketal', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('stall', 'ftall', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('towd', 'tow', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('doty', 'dsto', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('prime', 'huso', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('raspy', 'raeiya', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('sight', 'szghtw', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('scho', 'sc', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('sher', 'sided', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('glime', 'plane', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('canon', 'canon', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('soon', 'sb', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('would', 'douldtl', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('yeat', 'yeat', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('lexus', 'lexrs', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('randy', 'lose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('thee', 'theea', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('pilot', 'pilot', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('irk', 'hokey', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('foody', 'lough', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('mensa', 'ken', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('spung', 'spu', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('db', 'db', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('beala', 'beama', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('bepun', 'bepu', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('film', 'fblu', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('espn', 'esp', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('hondo', 'hbndao', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('reps', 'gata', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('tirr', 'tsr', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('slote', 'svotjg', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('beeve', 'jegvd', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('evade', 'evade', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('sinew', 'dineb', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('goods', 'good', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('kiley', 'kiley', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([feline_fixes('score', 'score', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> feline_fixes('flags', 'flaq', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import feline_fixes, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
