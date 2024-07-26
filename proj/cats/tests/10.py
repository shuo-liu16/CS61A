test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
          [['What', 'luck'], ['great']]
          >>> p2 = [4, 3, 1]
          >>> fastest_words(match(['What', 'great', 'luck'], [p0, p1, p2]))
          [['What'], ['great'], ['luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p0 = [5, 1, 3]
          >>> p1 = [4, 1, 6]
          >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
          [['have', 'fun'], ['Just']]
          >>> p0  # input lists should not be mutated
          [5, 1, 3]
          >>> p1
          [4, 1, 6]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3], [5]]
          >>> fastest_words(match(['smopple'], p))
          [['smopple'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [2], [4]]
          >>> fastest_words(match(['seeingly'], p))
          [[], ['seeingly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 2, 3, 4], [1, 5, 3, 4, 1], [5, 1, 5, 2, 3]]
          >>> fastest_words(match(['reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], p))
          [['unweld', 'handgun'], ['reundergo', 'recessionary'], ['hydrometra']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2]]
          >>> fastest_words(match(['prebeleve', 'upanishadic', 'ftp'], p))
          [['prebeleve', 'upanishadic', 'ftp']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 5, 2, 4], [2, 4, 5, 1, 2], [1, 5, 2, 1, 3]]
          >>> fastest_words(match(['supplies', 'underivedly', 'henter', 'undeserving', 'uncope'], p))
          [['underivedly'], ['undeserving', 'uncope'], ['supplies', 'henter']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(match([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 5, 5, 5]]
          >>> fastest_words(match(['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber'], p))
          [['pentarch', 'nihilification', 'krieker', 'laureate', 'antechamber']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 4, 3, 4]]
          >>> fastest_words(match(['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation'], p))
          [['urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 1, 1, 4, 1], [5, 3, 3, 4, 5, 3], [1, 2, 3, 1, 3, 5]]
          >>> fastest_words(match(['isoborneol', 'glabrate', 'excision', 'octobass', 'prevolitional', 'archtreasurership'], p))
          [['excision', 'octobass', 'archtreasurership'], [], ['isoborneol', 'glabrate', 'prevolitional']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 4, 3, 1], [3, 1, 2, 1, 3]]
          >>> fastest_words(match(['singletree', 'apocyneous', 'imminution', 'uncensuring', 'fungiform'], p))
          [['fungiform'], ['singletree', 'apocyneous', 'imminution', 'uncensuring']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2], [3, 2]]
          >>> fastest_words(match(['snideness', 'universalization'], p))
          [['snideness', 'universalization'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [3]]
          >>> fastest_words(match(['dependably'], p))
          [['dependably'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1]]
          >>> fastest_words(match(['spaceful', 'cautery', 'wiseness'], p))
          [['spaceful', 'cautery', 'wiseness']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 5, 3, 5, 1], [4, 4, 1, 2, 5, 3]]
          >>> fastest_words(match(['investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker', 'associated'], p))
          [['investigatable', 'quadrigenarious', 'provoker', 'associated'], ['protonemal', 'cardiodysneuria']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1]]
          >>> fastest_words(match(['tubuliporoid', 'malleability'], p))
          [['tubuliporoid', 'malleability']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 2, 4, 4], [3, 4, 3, 3, 5], [1, 2, 5, 1, 2]]
          >>> fastest_words(match(['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], p))
          [['shrubbiness', 'demoded'], [], ['shilling', 'commentary', 'housewright']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 3, 4, 1]]
          >>> fastest_words(match(['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular'], p))
          [['ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 4, 3, 1], [5, 5, 1, 2, 3]]
          >>> fastest_words(match(['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird'], p))
          [['lithosis', 'bogland', 'thumbbird'], ['interclash', 'widespread']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2], [3, 3]]
          >>> fastest_words(match(['diplosphenal', 'cholecystogram'], p))
          [['diplosphenal', 'cholecystogram'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2]]
          >>> fastest_words(match(['eugenist', 'karyopyknosis'], p))
          [['eugenist', 'karyopyknosis']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 3]]
          >>> fastest_words(match(['cannily', 'lune', 'heathless'], p))
          [['cannily', 'lune', 'heathless']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 3, 3], [2, 1, 3, 4], [2, 2, 4, 4]]
          >>> fastest_words(match(['postprandially', 'helicogyrate', 'coccidology', 'circumradius'], p))
          [['coccidology', 'circumradius'], ['postprandially', 'helicogyrate'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3], [1, 3], [5, 1]]
          >>> fastest_words(match(['electrofused', 'incontinent'], p))
          [[], ['electrofused'], ['incontinent']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 2, 5, 3], [3, 3, 5, 5, 3]]
          >>> fastest_words(match(['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], p))
          [['trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 1, 1, 2], [1, 1, 5, 3, 4]]
          >>> fastest_words(match(['boucherism', 'rutabaga', 'fomentation', 'swampside', 'unpopularness'], p))
          [['rutabaga', 'fomentation', 'swampside', 'unpopularness'], ['boucherism']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [1, 2]]
          >>> fastest_words(match(['introspectionist', 'teeting'], p))
          [['teeting'], ['introspectionist']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 1, 2, 3, 3]]
          >>> fastest_words(match(['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient'], p))
          [['cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 2, 2, 3], [1, 2, 5, 1, 3]]
          >>> fastest_words(match(['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter'], p))
          [['nonviscous', 'arterioverter'], ['quodlibetic', 'previdence', 'reduplicatively']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 1, 2, 1], [4, 2, 1, 4, 5, 3]]
          >>> fastest_words(match(['cactoid', 'quadrialate', 'preflattery', 'emancipation', 'recedent', 'haustement'], p))
          [['cactoid', 'quadrialate', 'emancipation', 'recedent', 'haustement'], ['preflattery']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 5, 4, 4, 4], [5, 2, 1, 1, 2, 3], [4, 5, 4, 2, 3, 2]]
          >>> fastest_words(match(['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete'], p))
          [['puboprostatic', 'tumescent'], ['keraunograph', 'telecaster', 'selenigenous'], ['phycomycete']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 2, 4, 2], [1, 5, 1, 4, 5]]
          >>> fastest_words(match(['indisputableness', 'breastrope', 'hypocist', 'supersemination', 'ethnographically'], p))
          [['breastrope', 'supersemination', 'ethnographically'], ['indisputableness', 'hypocist']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 3, 3, 5, 4]]
          >>> fastest_words(match(['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery'], p))
          [['repetitiously', 'lecideiform', 'debtless', 'stream', 'loquent', 'leery']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 3, 3, 3, 1, 4]]
          >>> fastest_words(match(['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations'], p))
          [['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 5, 4], [5, 4, 2, 2]]
          >>> fastest_words(match(['holland', 'nursedom', 'epidictical', 'defortify'], p))
          [['holland', 'nursedom'], ['epidictical', 'defortify']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 3]]
          >>> fastest_words(match(['sunbird', 'renewal', 'predivinable'], p))
          [['sunbird', 'renewal', 'predivinable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 4, 2], [5, 2, 2, 3]]
          >>> fastest_words(match(['tillot', 'douser', 'twankingly', 'eccentrate'], p))
          [['tillot', 'eccentrate'], ['douser', 'twankingly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 5, 3]]
          >>> fastest_words(match(['reest', 'predigest', 'adipocellulose', 'warriorwise'], p))
          [['reest', 'predigest', 'adipocellulose', 'warriorwise']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 5, 3, 5]]
          >>> fastest_words(match(['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm'], p))
          [['standing', 'cameroon', 'unpretendingly', 'puppydom', 'lardworm']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4], [5, 5]]
          >>> fastest_words(match(['cardioarterial', 'statolatry'], p))
          [['cardioarterial', 'statolatry'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4, 1]]
          >>> fastest_words(match(['whirley', 'coldly', 'compendiary', 'grovel'], p))
          [['whirley', 'coldly', 'compendiary', 'grovel']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [3, 3], [2, 4]]
          >>> fastest_words(match(['caducicorn', 'monociliated'], p))
          [['caducicorn', 'monociliated'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 4, 5, 3]]
          >>> fastest_words(match(['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx'], p))
          [['audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [4], [4]]
          >>> fastest_words(match(['millage'], p))
          [[], ['millage'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1], [5, 4]]
          >>> fastest_words(match(['inyoite', 'complications'], p))
          [['inyoite', 'complications'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2], [2, 2], [4, 1]]
          >>> fastest_words(match(['sarcodous', 'microbiological'], p))
          [['sarcodous'], [], ['microbiological']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 1], [2, 2, 3]]
          >>> fastest_words(match(['chromophilic', 'brabant', 'detailed'], p))
          [['detailed'], ['chromophilic', 'brabant']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1, 1], [3, 1, 3, 3]]
          >>> fastest_words(match(['allochiral', 'hear', 'snur', 'myosarcomatous'], p))
          [['hear', 'snur', 'myosarcomatous'], ['allochiral']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [5]]
          >>> fastest_words(match(['studiedly'], p))
          [['studiedly'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 3, 5, 2, 5]]
          >>> fastest_words(match(['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion'], p))
          [['katatonia', 'myoporaceous', 'tribunitive', 'mungofa', 'demodectic', 'kolobion']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 2], [2, 2]]
          >>> fastest_words(match(['cheeser', 'cumulation'], p))
          [['cumulation'], ['cheeser']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2], [1, 3]]
          >>> fastest_words(match(['overemphatic', 'telpherway'], p))
          [['telpherway'], ['overemphatic']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 4], [1, 2], [3, 5]]
          >>> fastest_words(match(['ultradolichocephalic', 'kinetophone'], p))
          [[], ['ultradolichocephalic', 'kinetophone'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 3]]
          >>> fastest_words(match(['protosaurian', 'plumbable', 'siroccoishly'], p))
          [['protosaurian', 'plumbable', 'siroccoishly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4, 5, 1, 1]]
          >>> fastest_words(match(['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize'], p))
          [['hydroidean', 'pesterer', 'seedcase', 'rudder', 'muttering', 'individualize']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1, 2], [2, 3, 5, 3]]
          >>> fastest_words(match(['oleostearin', 'stitching', 'theanthropism', 'blate'], p))
          [['stitching', 'theanthropism', 'blate'], ['oleostearin']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1], [2, 2]]
          >>> fastest_words(match(['oscillatory', 'geophyte'], p))
          [['oscillatory', 'geophyte'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1], [2]]
          >>> fastest_words(match(['withsave'], p))
          [['withsave'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1], [5, 3, 4]]
          >>> fastest_words(match(['battlewise', 'dare', 'halibiu'], p))
          [['battlewise', 'dare', 'halibiu'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 4, 2], [4, 3, 5, 5]]
          >>> fastest_words(match(['muscoid', 'reliquidation', 'broad', 'tugging'], p))
          [['muscoid', 'reliquidation', 'broad', 'tugging'], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 5]]
          >>> fastest_words(match(['trophobiosis', 'parascenium', 'gibbet'], p))
          [['trophobiosis', 'parascenium', 'gibbet']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 1, 4]]
          >>> fastest_words(match(['nonsparking', 'calool', 'dorsopleural'], p))
          [['nonsparking', 'calool', 'dorsopleural']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 4], [4, 4], [5, 3]]
          >>> fastest_words(match(['unexcusableness', 'bismuthyl'], p))
          [['unexcusableness'], [], ['bismuthyl']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 5, 5, 2], [1, 4, 1, 2, 4]]
          >>> fastest_words(match(['evolution', 'intransigency', 'improperly', 'angiophorous', 'urinogenital'], p))
          [['intransigency', 'urinogenital'], ['evolution', 'improperly', 'angiophorous']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 1]]
          >>> fastest_words(match(['penceless', 'bromothymol', 'reticuloramose'], p))
          [['penceless', 'bromothymol', 'reticuloramose']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 5, 2, 2, 3]]
          >>> fastest_words(match(['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid'], p))
          [['monument', 'appressor', 'tutu', 'gentilize', 'trihemimeral', 'bifid']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 3, 3, 5, 2]]
          >>> fastest_words(match(['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer'], p))
          [['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [4], [3]]
          >>> fastest_words(match(['inclementness'], p))
          [['inclementness'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(match([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 3, 1, 2, 4]]
          >>> fastest_words(match(['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis'], p))
          [['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4], [5], [4]]
          >>> fastest_words(match(['transmundane'], p))
          [['transmundane'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 3]]
          >>> fastest_words(match(['becense', 'hyperingenuity'], p))
          [['becense', 'hyperingenuity']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 4], [5, 5, 3], [3, 2, 3]]
          >>> fastest_words(match(['interventional', 'demiditone', 'chrysophilite'], p))
          [[], ['chrysophilite'], ['interventional', 'demiditone']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 3, 5, 1, 3], [1, 4, 3, 1, 3, 4], [1, 3, 1, 4, 4, 5]]
          >>> fastest_words(match(['pyritology', 'marbleize', 'blooddrop', 'prickingly', 'ecole', 'capitellar'], p))
          [['ecole', 'capitellar'], ['pyritology', 'prickingly'], ['marbleize', 'blooddrop']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 4, 5, 4, 3], [1, 3, 1, 1, 3, 5]]
          >>> fastest_words(match(['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious', 'untakableness'], p))
          [['untakableness'], ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 3], [4, 3], [5, 5]]
          >>> fastest_words(match(['tutoyer', 'fibrilliferous'], p))
          [['tutoyer', 'fibrilliferous'], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 2, 1]]
          >>> fastest_words(match(['aneuploidy', 'unrubified', 'dynamic', 'twistable'], p))
          [['aneuploidy', 'unrubified', 'dynamic', 'twistable']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 2, 3]]
          >>> fastest_words(match(['pholadoid', 'toxicodermatitis', 'gallification', 'survival'], p))
          [['pholadoid', 'toxicodermatitis', 'gallification', 'survival']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 3, 1, 4, 5], [5, 2, 3, 2, 3]]
          >>> fastest_words(match(['principiate', 'archinfamy', 'cacomixle', 'endonuclear', 'writer'], p))
          [['principiate', 'cacomixle'], ['archinfamy', 'endonuclear', 'writer']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2, 4]]
          >>> fastest_words(match(['mechanicalist', 'losing', 'emancipation', 'counterquarterly'], p))
          [['mechanicalist', 'losing', 'emancipation', 'counterquarterly']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1], [2, 1, 3]]
          >>> fastest_words(match(['subframe', 'infinitude', 'astrochemist'], p))
          [['astrochemist'], ['subframe', 'infinitude']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2]]
          >>> fastest_words(match(['isocheimal'], p))
          [['isocheimal']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 4, 5], [5, 4, 5, 2]]
          >>> fastest_words(match(['mistresshood', 'lazzarone', 'define', 'unmudded'], p))
          [['mistresshood', 'lazzarone', 'define'], ['unmudded']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 2, 2, 4], [3, 5, 4, 5, 1]]
          >>> fastest_words(match(['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting'], p))
          [['ungenuine', 'dealable', 'pejorism'], ['either', 'cointersecting']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 1]]
          >>> fastest_words(match(['narcoanesthesia', 'tanbur'], p))
          [['narcoanesthesia', 'tanbur']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(match([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4]]
          >>> fastest_words(match(['overappraise', 'disdiapason'], p))
          [['overappraise', 'disdiapason']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import match, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> cats.fastest_words(cats.match(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test # Make sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
