test = {
  'name': 'Problem 7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("wind", "wind", big_limit)
          0
          >>> minimum_mewtations("wird", "wiry", big_limit)
          1
          >>> minimum_mewtations("wird", "bird", big_limit)
          1
          >>> minimum_mewtations("wird", "wir", big_limit)
          1
          >>> minimum_mewtations("wird", "bwird", big_limit)
          1
          >>> minimum_mewtations("speling", "spelling", big_limit)
          1
          >>> minimum_mewtations("used", "use", big_limit)
          1
          >>> minimum_mewtations("hash", "ash", big_limit)
          1
          >>> minimum_mewtations("ash", "hash", big_limit)
          1
          >>> minimum_mewtations("roses", "arose", big_limit)     # roses -> aroses -> arose
          2
          >>> minimum_mewtations("tesng", "testing", big_limit)   # tesng -> testng -> testing
          2
          >>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
          3
          >>> minimum_mewtations("", "", big_limit) # nothing to nothing needs no edits
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> big_limit = 10
          >>> minimum_mewtations("cats", "scat", big_limit)
          2
          >>> minimum_mewtations("purng", "purring", big_limit)
          2
          >>> minimum_mewtations("ckiteus", "kittens", big_limit)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_limit = 0
          >>> minimum_mewtations("cats", "cats", small_limit)
          0
          >>> minimum_mewtations("", "", small_limit)
          0
          >>> minimum_mewtations("cats", "scat", small_limit) > small_limit
          True
          >>> minimum_mewtations("purng", "purring", small_limit) > small_limit
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> negative_limit = -1
          >>> minimum_mewtations("cats", "cats", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("cats", "scat", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("purng", "purring", negative_limit) > negative_limit
          True
          >>> minimum_mewtations("", "", negative_limit) > negative_limit
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> small_words_list = ["spell", "nest", "test", "pest", "best", "bird", "wired",
          ...                     "abstraction", "abstract", "wire", "peeling", "gestate",
          ...                     "west", "spelling", "bastion"]
          >>> autocorrect("speling", small_words_list, minimum_mewtations, 10)
          'spelling'
          >>> autocorrect("abstrction", small_words_list, minimum_mewtations, 10)
          'abstraction'
          >>> autocorrect("wird", small_words_list, minimum_mewtations, 10)
          'bird'
          >>> autocorrect("gest", small_words_list, minimum_mewtations, 10)
          'nest'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # ***Check that the recursion stops when the limit is reached***
          >>> import trace, io
          >>> from contextlib import redirect_stdout
          >>> with io.StringIO() as buf, redirect_stdout(buf):
          ...     trace.Trace(trace=True).runfunc(minimum_mewtations, "someawe", "awesome", 3)
          ...     output = buf.getvalue()
          >>> len([line for line in output.split('\n') if 'funcname' in line]) <= 400 # Make sure your base case(s) is as tight as possible
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('rut', 'rzumt', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('yo', 'yo', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('slurp', 'slurpm', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('nice', 'tie', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('owen', 'owen', k) > k for k in range(4)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('donee', 'shush', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('drest', 'drwt', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('cand', 'towy', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('drawn', 'terry', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('stour', 'shows', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('plash', 'cw', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('cube', 'cube', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('envy', 'nv', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('panto', 'panto', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('herem', 'hwerem', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('zanze', 'culm', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('kauri', 'kajr', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('hiver', 'hicer', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('tulip', 'qlulip', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('aside', 'ataxy', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('volt', 'vol', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('sleep', 'sleop', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('cet', 'duad', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('opal', 'oral', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('pathy', 'pathy', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('drive', 'drgitb', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('bater', 'kbater', k) > k for k in range(6)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('ward', 'crier', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('massy', 'massy', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('tonk', 'tobnhn', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('sith', 'demit', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('arty', 'at', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('exist', 'ext', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('plot', 'plkot', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('wreak', 'wreak', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('icon', 'ipnw', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('caza', 'scale', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('rann', 'daw', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('natal', 'nttyl', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('tji', 'j', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('input', 'input', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('lysin', 'lzsbun', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('bed', 'bc', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('topsl', 'topsl', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('becap', 'becap', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('tiny', 'sizes', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('plots', 'gplots', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('plote', 'plot', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('libra', 'unact', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('shed', 'tshged', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('lunes', 'lunes', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('shooi', 'sgcoi', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('cahow', 'cahow', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('watch', 'wotchj', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('jeans', 'anps', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('floey', 'uvea', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('pew', 'pe', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('tec', 'gtec', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('chef', 'drib', k) > k for k in range(4)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('sowel', 'evert', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('zebu', 'eu', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('magma', 'mahgfma', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('shood', 'ketal', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('stall', 'ftall', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('towd', 'owz', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('doty', 'dsto', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('prime', 'huso', 100)
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('raspy', 'eraiepy', k) > k for k in range(7)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('sight', 'szlht', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('scho', 'ho', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('sher', 'sided', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('glime', 'plane', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('canon', 'dcvanon', k) > k for k in range(7)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('soon', 'o', k) > k for k in range(4)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('would', 'wuold', k) > k for k in range(5)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('yeat', 'yawt', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('lexus', 'lexrs', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('randy', 'lose', k) > k for k in range(5)])
          5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('thee', 'thaee', 100)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('pilot', 'pilot', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('irk', 'hokey', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('foody', 'lough', k) > k for k in range(5)])
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('mensa', 'mrvs', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('spung', 'pxkg', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('db', 'db', 100)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('beala', 'beamff', k) > k for k in range(6)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('bepun', 'bpun', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('film', 'fblu', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('espn', 'esp', k) > k for k in range(4)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('hondo', 'gkondo', k) > k for k in range(6)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('reps', 'gata', 100)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('tirr', 'ir', k) > k for k in range(4)])
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('slote', 'svoltj', 100)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('beeve', 'jegvd', k) > k for k in range(5)])
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('evade', 'evade', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('sinew', 'dinw', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('goods', 'goos', k) > k for k in range(5)])
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('kiley', 'kiley', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> sum([minimum_mewtations('score', 'score', k) > k for k in range(5)])
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> minimum_mewtations('flags', 'faqs', 100)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import minimum_mewtations, autocorrect
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
