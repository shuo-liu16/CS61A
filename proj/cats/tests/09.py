test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match = time_per_word(words, p)
          >>> get_all_words(match)
          ['This', 'is', 'fun']
          >>> get_all_times(match)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> match = time_per_word(['hello', 'world'], p)
          >>> get_word(match, word_index=1)
          'world'
          >>> get_all_times(match)
          [[2, 1], [2, 3]]
          >>> time(match, player_num=0, word_index=1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[49, 53, 57, 58, 61, 63], [57, 61, 65, 69, 74, 76], [58, 61, 62, 65, 69, 72]]
          >>> match = time_per_word(['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible'], p)
          >>> get_all_words(match)
          ['gonalgia', 'smopple', 'modernizer', 'posticum', 'undiscernible']
          >>> match['times']
          [[4, 4, 1, 3, 2], [4, 4, 4, 5, 2], [3, 1, 3, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[47, 50, 54, 55, 58], [88, 90, 91, 96, 97], [91, 95, 99, 101, 103]]
          >>> match = time_per_word(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds'], p)
          >>> get_all_words(match)
          ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds']
          >>> match['times']
          [[3, 4, 1, 3], [2, 1, 5, 1], [4, 4, 2, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[91, 95, 99, 100, 103, 108, 113], [73, 75, 77, 80, 85, 89, 90]]
          >>> match = time_per_word(['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate'], p)
          >>> get_all_words(match)
          ['unsupposable', 'seeingly', 'essexite', 'policemanism', 'havenet', 'ammonionitrate']
          >>> match['times']
          [[4, 4, 1, 3, 5, 5], [2, 2, 3, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 62, 66, 67, 69, 72, 76]]
          >>> match = time_per_word(['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun'], p)
          >>> get_all_words(match)
          ['unsanitariness', 'probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun']
          >>> match['times']
          [[4, 4, 1, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 39, 43, 45, 50, 52]]
          >>> match = time_per_word(['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming'], p)
          >>> get_all_words(match)
          ['extort', 'elysia', 'cungeboi', 'cams', 'plagueproof', 'overdeeming']
          >>> match['times']
          [[1, 3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 27, 29], [54, 57, 61], [96, 101, 103]]
          >>> match = time_per_word(['glassine', 'supplies'], p)
          >>> get_all_words(match)
          ['glassine', 'supplies']
          >>> match['times']
          [[5, 2], [3, 4], [5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 90, 95], [83, 84, 89], [88, 92, 95]]
          >>> match = time_per_word(['epinaos', 'unpresented'], p)
          >>> get_all_words(match)
          ['epinaos', 'unpresented']
          >>> match['times']
          [[1, 5], [1, 5], [4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9], [24]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[0], [20]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[46, 49, 51], [48, 53, 57]]
          >>> match = time_per_word(['hypsochrome', 'isoborneol'], p)
          >>> get_all_words(match)
          ['hypsochrome', 'isoborneol']
          >>> match['times']
          [[3, 2], [5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[18, 22]]
          >>> match = time_per_word(['nailless'], p)
          >>> get_all_words(match)
          ['nailless']
          >>> match['times']
          [[4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62, 65], [93, 97]]
          >>> match = time_per_word(['ringcraft'], p)
          >>> get_all_words(match)
          ['ringcraft']
          >>> match['times']
          [[3], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[68, 69, 70, 71], [66, 71, 74, 78], [18, 19, 21, 24]]
          >>> match = time_per_word(['rug', 'misinstruction', 'durian'], p)
          >>> get_all_words(match)
          ['rug', 'misinstruction', 'durian']
          >>> match['times']
          [[1, 1, 1], [5, 3, 4], [1, 2, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 6, 11, 13, 14]]
          >>> match = time_per_word(['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach'], p)
          >>> get_all_words(match)
          ['epitomization', 'orchestrion', 'snideness', 'universalization', 'accroach']
          >>> match['times']
          [[3, 2, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 30, 33, 35]]
          >>> match = time_per_word(['hecatontome', 'glioma', 'dispiteousness'], p)
          >>> get_all_words(match)
          ['hecatontome', 'glioma', 'dispiteousness']
          >>> match['times']
          [[1, 3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 95, 96, 101], [30, 32, 34, 35]]
          >>> match = time_per_word(['irenically', 'spaceful', 'cautery'], p)
          >>> get_all_words(match)
          ['irenically', 'spaceful', 'cautery']
          >>> match['times']
          [[3, 1, 5], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 46], [91, 95]]
          >>> match = time_per_word(['hieromachy'], p)
          >>> get_all_words(match)
          ['hieromachy']
          >>> match['times']
          [[2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[27, 31, 32, 34, 39], [20, 21, 24, 28, 29], [10, 11, 16, 21, 23]]
          >>> match = time_per_word(['onliest', 'tubuliporoid', 'malleability', 'scusation'], p)
          >>> get_all_words(match)
          ['onliest', 'tubuliporoid', 'malleability', 'scusation']
          >>> match['times']
          [[4, 1, 2, 5], [1, 3, 4, 1], [1, 5, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 37, 41, 44, 48, 51, 54]]
          >>> match = time_per_word(['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], p)
          >>> get_all_words(match)
          ['caulicle', 'shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright']
          >>> match['times']
          [[4, 4, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[73], [55]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 61], [43, 47], [30, 33]]
          >>> match = time_per_word(['lithosis'], p)
          >>> get_all_words(match)
          ['lithosis']
          >>> match['times']
          [[1], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 97, 98, 101, 105, 109], [55, 56, 58, 59, 61, 65], [82, 85, 87, 88, 92, 96]]
          >>> match = time_per_word(['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic'], p)
          >>> get_all_words(match)
          ['pemmicanize', 'diplosphenal', 'cholecystogram', 'maximization', 'arenilitic']
          >>> match['times']
          [[4, 1, 3, 4, 4], [1, 2, 1, 2, 4], [3, 2, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37], [3], [0]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[92, 96, 99, 102], [43, 45, 47, 51], [34, 36, 38, 39]]
          >>> match = time_per_word(['distressedly', 'gibbet', 'cannily'], p)
          >>> get_all_words(match)
          ['distressedly', 'gibbet', 'cannily']
          >>> match['times']
          [[4, 3, 3], [2, 2, 4], [2, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 8, 11], [0, 4, 6, 10], [62, 65, 66, 68]]
          >>> match = time_per_word(['paramorphic', 'triplocaulescent', 'postprandially'], p)
          >>> get_all_words(match)
          ['paramorphic', 'triplocaulescent', 'postprandially']
          >>> match['times']
          [[4, 3, 3], [4, 2, 4], [3, 1, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63, 64, 69], [90, 93, 94]]
          >>> match = time_per_word(['sheered', 'electrofused'], p)
          >>> get_all_words(match)
          ['sheered', 'electrofused']
          >>> match['times']
          [[1, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87, 91, 94, 96, 99, 102], [50, 54, 58, 60, 63, 66], [57, 61, 64, 66, 69, 73]]
          >>> match = time_per_word(['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma'], p)
          >>> get_all_words(match)
          ['crotonaldehyde', 'unhabitableness', 'nidification', 'lampless', 'fibrochondroma']
          >>> match['times']
          [[4, 3, 2, 3, 3], [4, 4, 2, 3, 3], [4, 3, 2, 3, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[63]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[51, 54]]
          >>> match = time_per_word(['prissy'], p)
          >>> get_all_words(match)
          ['prissy']
          >>> match['times']
          [[3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 39, 42, 47, 50], [73, 75, 78, 81, 86, 89]]
          >>> match = time_per_word(['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia'], p)
          >>> get_all_words(match)
          ['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia']
          >>> match['times']
          [[3, 5, 3, 5, 3], [2, 3, 3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[93, 95, 97, 98, 101], [75, 80, 84, 89, 93]]
          >>> match = time_per_word(['traitor', 'tablespoon', 'anytime', 'ungotten'], p)
          >>> get_all_words(match)
          ['traitor', 'tablespoon', 'anytime', 'ungotten']
          >>> match['times']
          [[2, 2, 1, 3], [5, 4, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[66, 69], [85, 86]]
          >>> match = time_per_word(['boucherism'], p)
          >>> get_all_words(match)
          ['boucherism']
          >>> match['times']
          [[3], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 75], [74, 75], [41, 43]]
          >>> match = time_per_word(['uncertainty'], p)
          >>> get_all_words(match)
          ['uncertainty']
          >>> match['times']
          [[1], [1], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[15, 18, 19, 23]]
          >>> match = time_per_word(['redominate', 'dugong', 'cryptodiran'], p)
          >>> get_all_words(match)
          ['redominate', 'dugong', 'cryptodiran']
          >>> match['times']
          [[3, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 60, 62, 66]]
          >>> match = time_per_word(['estivage', 'hypersensualism', 'aminoacetal'], p)
          >>> get_all_words(match)
          ['estivage', 'hypersensualism', 'aminoacetal']
          >>> match['times']
          [[3, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 54, 55, 58, 62], [85, 86, 90, 94, 95, 100], [23, 25, 27, 32, 33, 37]]
          >>> match = time_per_word(['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation'], p)
          >>> get_all_words(match)
          ['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation']
          >>> match['times']
          [[5, 1, 1, 3, 4], [1, 4, 4, 1, 5], [2, 2, 5, 1, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[35, 36, 40, 44, 46, 47, 50], [53, 58, 62, 67, 68, 70, 74]]
          >>> match = time_per_word(['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous'], p)
          >>> get_all_words(match)
          ['otoconial', 'puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous']
          >>> match['times']
          [[1, 4, 4, 2, 1, 3], [5, 4, 5, 1, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 9, 10]]
          >>> match = time_per_word(['unsculptured', 'quagginess', 'indisputableness'], p)
          >>> get_all_words(match)
          ['unsculptured', 'quagginess', 'indisputableness']
          >>> match['times']
          [[3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[55], [37], [18]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[12, 13, 15, 20, 24], [51, 55, 56, 59, 60], [82, 83, 85, 90, 94]]
          >>> match = time_per_word(['extol', 'siscowet', 'nevo', 'driftweed'], p)
          >>> get_all_words(match)
          ['extol', 'siscowet', 'nevo', 'driftweed']
          >>> match['times']
          [[1, 2, 5, 4], [4, 1, 3, 1], [1, 2, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[57, 61, 65, 67, 72, 76], [28, 33, 35, 37, 42, 45]]
          >>> match = time_per_word(['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify'], p)
          >>> get_all_words(match)
          ['tomtate', 'holland', 'nursedom', 'epidictical', 'defortify']
          >>> match['times']
          [[4, 4, 2, 5, 4], [5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25], [24], [2]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[42]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[84, 87, 88, 89, 90], [39, 43, 45, 49, 51], [52, 53, 57, 59, 63]]
          >>> match = time_per_word(['pharyngognathous', 'metamerically', 'toxone', 'nucleiform'], p)
          >>> get_all_words(match)
          ['pharyngognathous', 'metamerically', 'toxone', 'nucleiform']
          >>> match['times']
          [[3, 1, 1, 1], [4, 2, 4, 2], [1, 4, 2, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[13, 16, 20, 22, 27, 29]]
          >>> match = time_per_word(['missile', 'tillot', 'douser', 'twankingly', 'eccentrate'], p)
          >>> get_all_words(match)
          ['missile', 'tillot', 'douser', 'twankingly', 'eccentrate']
          >>> match['times']
          [[3, 4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[70]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[67, 68, 73, 74, 79], [12, 17, 20, 21, 25], [55, 58, 62, 66, 67]]
          >>> match = time_per_word(['unambiguously', 'standing', 'cameroon', 'unpretendingly'], p)
          >>> get_all_words(match)
          ['unambiguously', 'standing', 'cameroon', 'unpretendingly']
          >>> match['times']
          [[1, 5, 1, 5], [5, 3, 1, 4], [3, 4, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 57], [76, 80], [24, 25]]
          >>> match = time_per_word(['megascleric'], p)
          >>> get_all_words(match)
          ['megascleric']
          >>> match['times']
          [[3], [4], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[6, 11], [91, 95], [60, 63]]
          >>> match = time_per_word(['designee'], p)
          >>> get_all_words(match)
          ['designee']
          >>> match['times']
          [[5], [4], [3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[14, 15, 20, 24, 25]]
          >>> match = time_per_word(['dextrousness', 'whirley', 'coldly', 'compendiary'], p)
          >>> get_all_words(match)
          ['dextrousness', 'whirley', 'coldly', 'compendiary']
          >>> match['times']
          [[1, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 24]]
          >>> match = time_per_word(['plowfoot', 'caducicorn'], p)
          >>> get_all_words(match)
          ['plowfoot', 'caducicorn']
          >>> match['times']
          [[2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[61, 66, 69, 74, 79, 80]]
          >>> match = time_per_word(['signist', 'plash', 'unbraceleted', 'runner', 'nickeline'], p)
          >>> get_all_words(match)
          ['signist', 'plash', 'unbraceleted', 'runner', 'nickeline']
          >>> match['times']
          [[5, 3, 5, 5, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7, 9, 12, 15, 18], [53, 54, 58, 63, 64], [28, 30, 35, 36, 41]]
          >>> match = time_per_word(['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride'], p)
          >>> get_all_words(match)
          ['ergastoplasmic', 'sulphurage', 'audibility', 'deuteride']
          >>> match['times']
          [[2, 3, 3, 3], [1, 4, 5, 1], [2, 5, 1, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 31, 32, 37, 39, 40]]
          >>> match = time_per_word(['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography'], p)
          >>> get_all_words(match)
          ['uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography']
          >>> match['times']
          [[4, 5, 1, 5, 2, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[26, 31], [40, 44]]
          >>> match = time_per_word(['remissful'], p)
          >>> get_all_words(match)
          ['remissful']
          >>> match['times']
          [[5], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91, 93, 95, 98, 100, 101], [83, 88, 92, 93, 95, 96, 98], [48, 50, 54, 56, 60, 64, 67]]
          >>> match = time_per_word(['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana'], p)
          >>> get_all_words(match)
          ['sacculus', 'sarcodous', 'microbiological', 'ruddy', 'gobble', 'pozzuolana']
          >>> match['times']
          [[2, 2, 2, 3, 2, 1], [5, 4, 1, 2, 1, 2], [2, 4, 2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86, 87], [90, 94]]
          >>> match = time_per_word(['monothelious'], p)
          >>> get_all_words(match)
          ['monothelious']
          >>> match['times']
          [[1], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[74, 76, 78, 83]]
          >>> match = time_per_word(['boy', 'leaverwood', 'bounteousness'], p)
          >>> get_all_words(match)
          ['boy', 'leaverwood', 'bounteousness']
          >>> match['times']
          [[2, 2, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[16, 17, 20, 21, 25, 26], [46, 49, 52, 57, 61, 63], [96, 97, 98, 100, 103, 108]]
          >>> match = time_per_word(['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous'], p)
          >>> get_all_words(match)
          ['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous']
          >>> match['times']
          [[1, 3, 1, 4, 1], [3, 3, 5, 4, 2], [1, 1, 2, 3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[89, 91], [37, 39], [63, 67]]
          >>> match = time_per_word(['sulphurproof'], p)
          >>> get_all_words(match)
          ['sulphurproof']
          >>> match['times']
          [[2], [2], [4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[62], [50], [26]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[44, 47, 51, 56, 58, 60], [4, 7, 11, 16, 19, 22]]
          >>> match = time_per_word(['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar'], p)
          >>> get_all_words(match)
          ['neoza', 'detinet', 'repolymerization', 'alchemy', 'caphar']
          >>> match['times']
          [[3, 4, 5, 2, 2], [3, 4, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[56, 61]]
          >>> match = time_per_word(['deediness'], p)
          >>> get_all_words(match)
          ['deediness']
          >>> match['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[60, 62, 65, 68], [55, 56, 59, 60], [89, 92, 97, 100]]
          >>> match = time_per_word(['outstartle', 'varicosed', 'ventilator'], p)
          >>> get_all_words(match)
          ['outstartle', 'varicosed', 'ventilator']
          >>> match['times']
          [[2, 3, 3], [1, 3, 1], [3, 5, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[1, 4, 9, 14, 17, 22, 27]]
          >>> match = time_per_word(['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander'], p)
          >>> get_all_words(match)
          ['evaporability', 'ultradolichocephalic', 'kinetophone', 'supernaturalness', 'schout', 'woodlander']
          >>> match['times']
          [[3, 5, 5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[11], [37], [36]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[54, 55, 58, 62], [74, 76, 81, 82], [41, 43, 46, 47]]
          >>> match = time_per_word(['payable', 'jaunt', 'oleostearin'], p)
          >>> get_all_words(match)
          ['payable', 'jaunt', 'oleostearin']
          >>> match['times']
          [[1, 3, 4], [2, 5, 1], [2, 3, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[33, 34], [39, 40]]
          >>> match = time_per_word(['entropium'], p)
          >>> get_all_words(match)
          ['entropium']
          >>> match['times']
          [[1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[72, 77, 82, 85, 90, 91], [5, 9, 14, 17, 21, 22]]
          >>> match = time_per_word(['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch'], p)
          >>> get_all_words(match)
          ['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch']
          >>> match['times']
          [[5, 5, 3, 5, 1], [4, 5, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[29, 34], [69, 70], [71, 72]]
          >>> match = time_per_word(['battlewise'], p)
          >>> get_all_words(match)
          ['battlewise']
          >>> match['times']
          [[5], [1], [1]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 10, 15, 18, 23, 26], [3, 7, 12, 13, 16, 17], [86, 89, 90, 95, 98, 101]]
          >>> match = time_per_word(['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant'], p)
          >>> get_all_words(match)
          ['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant']
          >>> match['times']
          [[2, 5, 3, 5, 3], [4, 5, 1, 3, 1], [3, 1, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[71, 73, 75, 80, 84], [3, 8, 10, 14, 16]]
          >>> match = time_per_word(['hexatomic', 'trophobiosis', 'parascenium', 'gibbet'], p)
          >>> get_all_words(match)
          ['hexatomic', 'trophobiosis', 'parascenium', 'gibbet']
          >>> match['times']
          [[2, 2, 5, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[2], [83], [56]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 18, 19, 23, 26, 29], [85, 89, 92, 94, 97, 102, 105], [5, 9, 12, 13, 14, 15, 18]]
          >>> match = time_per_word(['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize'], p)
          >>> get_all_words(match)
          ['unimpressed', 'unexcusableness', 'bismuthyl', 'adapt', 'refutable', 'fluoridize']
          >>> match['times']
          [[4, 5, 1, 4, 3, 3], [4, 3, 2, 3, 5, 3], [4, 3, 1, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[82, 86], [16, 18]]
          >>> match = time_per_word(['ab'], p)
          >>> get_all_words(match)
          ['ab']
          >>> match['times']
          [[4], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 82, 83, 88, 92]]
          >>> match = time_per_word(['theophysical', 'penceless', 'bromothymol', 'reticuloramose'], p)
          >>> get_all_words(match)
          ['theophysical', 'penceless', 'bromothymol', 'reticuloramose']
          >>> match['times']
          [[5, 1, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[90, 91, 93, 97, 98], [64, 68, 70, 73, 78], [95, 100, 103, 108, 113]]
          >>> match = time_per_word(['beshag', 'monument', 'appressor', 'tutu'], p)
          >>> get_all_words(match)
          ['beshag', 'monument', 'appressor', 'tutu']
          >>> match['times']
          [[1, 2, 4, 1], [4, 2, 3, 5], [5, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[86], [26], [8]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[25, 26, 30], [50, 54, 59], [52, 55, 60]]
          >>> match = time_per_word(['confidentiality', 'inclementness'], p)
          >>> get_all_words(match)
          ['confidentiality', 'inclementness']
          >>> match['times']
          [[1, 4], [4, 5], [3, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[58, 63]]
          >>> match = time_per_word(['sardius'], p)
          >>> get_all_words(match)
          ['sardius']
          >>> match['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[77, 81, 85, 89]]
          >>> match = time_per_word(['bluehearts', 'repugnatorial', 'bescorch'], p)
          >>> get_all_words(match)
          ['bluehearts', 'repugnatorial', 'bescorch']
          >>> match['times']
          [[4, 4, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[75, 78, 80]]
          >>> match = time_per_word(['efflorescency', 'presay'], p)
          >>> get_all_words(match)
          ['efflorescency', 'presay']
          >>> match['times']
          [[3, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[53, 54, 59, 61], [47, 50, 54, 56]]
          >>> match = time_per_word(['myologist', 'dualistic', 'becense'], p)
          >>> get_all_words(match)
          ['myologist', 'dualistic', 'becense']
          >>> match['times']
          [[1, 5, 2], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[85, 90, 93, 95, 98, 102, 105], [5, 10, 12, 13, 14, 18, 22], [91, 94, 97, 100, 102, 105, 108]]
          >>> match = time_per_word(['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically'], p)
          >>> get_all_words(match)
          ['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically']
          >>> match['times']
          [[5, 3, 2, 3, 4, 3], [5, 2, 1, 1, 4, 4], [3, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[95, 98, 100, 103], [1, 3, 8, 13]]
          >>> match = time_per_word(['clique', 'spuriae', 'introspectable'], p)
          >>> get_all_words(match)
          ['clique', 'spuriae', 'introspectable']
          >>> match['times']
          [[3, 2, 3], [2, 5, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[10, 15, 19, 24, 28, 31]]
          >>> match = time_per_word(['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious'], p)
          >>> get_all_words(match)
          ['epicotyledonary', 'hiro', 'tremolo', 'ringgiving', 'pignoratitious']
          >>> match['times']
          [[5, 4, 5, 4, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 39, 42, 44, 47, 50]]
          >>> match = time_per_word(['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily'], p)
          >>> get_all_words(match)
          ['wickerworker', 'disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily']
          >>> match['times']
          [[5, 3, 3, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[7]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[87]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[37, 40, 43, 44, 48, 53]]
          >>> match = time_per_word(['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear'], p)
          >>> get_all_words(match)
          ['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear']
          >>> match['times']
          [[3, 3, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[69]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[3, 8]]
          >>> match = time_per_word(['subframe'], p)
          >>> get_all_words(match)
          ['subframe']
          >>> match['times']
          [[5]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[40], [49]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[8, 12, 16, 21, 26, 30]]
          >>> match = time_per_word(['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define'], p)
          >>> get_all_words(match)
          ['waling', 'sycophantishly', 'mistresshood', 'lazzarone', 'define']
          >>> match['times']
          [[4, 4, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[31, 35], [97, 102], [27, 29]]
          >>> match = time_per_word(['donary'], p)
          >>> get_all_words(match)
          ['donary']
          >>> match['times']
          [[4], [5], [2]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[5], [86], [1]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[]]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> p = [[59], [68], [75]]
          >>> match = time_per_word([], p)
          >>> get_all_words(match)
          []
          >>> match['times']
          [[], [], []]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> match = cats.time_per_word(words, p)
          >>> cats.get_word(match, 0)
          'This'
          >>> cats.time(match, 0, 0)
          3
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
