test = {
  'name': 'Problem 5',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
          'cult'
          >>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
          'cul'
          >>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
          'car'
          >>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
          >>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
          'word'
          >>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
          'inside'
          >>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
          'idea'
          >>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
          'outside'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> length_ratio = lambda w1, w2, limit: len(w2) / len(w1) # An asymmetric diff function
          >>> autocorrect("aaa", ["a"], length_ratio, 2) # typed_word ("aaa") is passed in as the first argument to a diff function
          'a'
          >>> autocorrect("cats", ["panthers", "lions"], length_ratio, 2)
          'lions'
          >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
          >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
          'butter'
          >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
          'testing'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> matching_diff = lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) # Num matching chars
          >>> autocorrect("tosting", ["testing", "asking", "fasting"], matching_diff, 10)
          'testing'
          >>> autocorrect("tsting", ["testing", "rowing"], matching_diff, 10)
          'rowing'
          >>> autocorrect("bwe", ["awe", "bye"], matching_diff, 10)
          'awe'
          >>> autocorrect("bwe", ["bye", "awe"], matching_diff, 10)
          'bye'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> words_list = sorted(lines_from_file('data/words.txt')[:10000])
          >>> autocorrect("testng", words_list, lambda w1, w2, limit: 1, 10)
          'a'
          >>> autocorrect("testing", words_list, lambda w1, w2, limit: 1, 10)
          'testing'
          >>> autocorrect("gesting", words_list, lambda w1, w2, limit: sum([w1[i] != w2[i] for i in range(min(len(w1), len(w2)))]) + abs(len(w1) - len(w2)), 10)
          'getting'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stilter', ['modernizer', 'posticum', 'undiscernible', 'heterotrophic', 'waller', 'marque', 'dephosphorization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'posticum'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bridgemaking', ['seeds', 'bridgemaking', 'endemiological', 'cobaltinitrite'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'bridgemaking'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('excursively', ['cirsotomy', 'terminableness', 'margaritaceous', 'gawkiness', 'ascon', 'floccose'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'excursively'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('hypertense', ['hyperbrachycranial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'hypertense'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('sporidia', ['intrarachidian', 'solifidianism'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'sporidia'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chanson', ['upanishadic', 'ftp', 'chanson', 'unbeached', 'astrolabical'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'chanson'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('turnrow', ['lokao', 'archipelagian'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'turnrow'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('fc', ['anthracia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'fc'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('crapy', ['nihilification', 'krieker', 'laureate', 'antechamber', 'crapy', 'belkin', 'ixodian', 'scarletseed', 'reliner', 'ebullioscope'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'crapy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('auximone', ['auximone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'auximone'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('semicheviot', ['cinematize', 'struma'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'semicheviot'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('modify', ['imminution', 'uncensuring', 'fungiform', 'cargoose', 'quizzish'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'cargoose'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('testator', ['impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'overrude'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unabsorb', ['unabsorb', 'chromolithographic', 'hemadynamometer', 'frailly', 'diana'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'unabsorb'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bounteously', ['universalization', 'accroach', 'unflinchingly', 'seagoer', 'overlight', 'condoling', 'truckling'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'unflinchingly'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('accomplisher', ['purloin', 'assignable', 'unallayably', 'caeca'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'unallayably'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('zonal', ['cautery', 'wiseness', 'yobi', 'kirk', 'herbalism', 'separata', 'zonal', 'anaglyphic', 'unshrined'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'zonal'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('associated', ['cardiodysneuria', 'provoker'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'provoker'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('scusation', ['tubuliporoid', 'malleability', 'scusation', 'semichivalrous', 'urocele', 'dietetic', 'featureful', 'splenatrophy'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'scusation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('proportionability', ['psychonomic', 'nonfuturity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'proportionability'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('untenanted', ['musterable', 'multivincular', 'recuperator', 'goto', 'turnsole', 'untenanted', 'isopterous', 'carbanilic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'untenanted'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('widespread', ['bogland', 'interclash'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'interclash'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('arenilitic', ['maximization'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'maximization'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('insee', ['karyopyknosis', 'nightwork', 'short', 'insee', 'unmated', 'capacitation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'insee'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('monoxenous', ['thoraces', 'preworldliness', 'monoxenous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'monoxenous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('outskirmisher', ['slatternly', 'hexadic', 'immaculateness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'outskirmisher'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unrepugnant', ['cordiner'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'unrepugnant'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('arisen', ['palaeoatavism', 'drowsiness', 'untopped'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'untopped'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('seafare', ['seafare', 'bimillennium', 'valviform', 'thyridial', 'umbones', 'logitech', 'indigestible', 'unfastidious', 'gammerel', 'valiseful'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'seafare'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('uncranked', ['mesodermic', 'fingerling', 'metallophone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'mesodermic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unmagic', ['effluviate', 'unhuman', 'energeia', 'slouch', 'resource'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'unhuman'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('tablespoon', ['tablespoon'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'tablespoon'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('interwrought', ['rutabaga', 'fomentation', 'swampside', 'unpopularness', 'magnifier'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'fomentation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('plumosity', ['introspectionist', 'teeting', 'unbroiled'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'unbroiled'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('staurolatry', ['staurolatry'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'staurolatry'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('nonviscous', ['previdence'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'previdence'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('sterile', ['emancipation', 'recedent', 'haustement', 'prorebate', 'weatherliness', 'unchristianity', 'nonprotection', 'deviousness', 'strangury', 'mauvine'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'mauvine'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('propylic', ['touch', 'uniparental', 'chomp', 'violety', 'overweave', 'phelloplastics', 'fipple', 'inappreciable', 'melodramatist', 'pawnbrokering'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'propylic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('beechy', ['breastrope', 'hypocist', 'supersemination', 'ethnographically', 'atwitch', 'wraxle'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'wraxle'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('stream', ['lecideiform', 'debtless', 'stream', 'loquent', 'leery', 'antipodean', 'mesothesis', 'ay'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'stream'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chevronelly', ['nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations', 'figent', 'mentality'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'chevronelly'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('windbracing', ['nursedom', 'epidictical', 'defortify', 'taraf'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'epidictical'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('corvina', ['predivinable', 'buchnerite', 'unexplanatory', 'nisei', 'neuronophagia', 'geitjie', 'porticoed', 'corvina'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'corvina'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('nonreception', ['booming', 'retrothyroid', 'decarnate', 'lobbyism', 'playa', 'nonreception', 'amphictyonic', 'antiaesthetic', 'unjoyousness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'nonreception'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('slopingness', ['toxone', 'nucleiform', 'priggish', 'intramuscularly', 'slopingness', 'saccharinated'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'slopingness'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cacoglossia', ['twankingly', 'eccentrate'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'twankingly'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('warriorwise', ['predigest', 'adipocellulose', 'warriorwise', 'sought', 'sciatherically', 'sexuale', 'onionlike'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'warriorwise'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unpretendingly', ['unpretendingly', 'puppydom', 'lardworm', 'equestrianship', 'semolella', 'pauperize', 'athericeran', 'receipt', 'nonrevelation', 'pomacentroid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'unpretendingly'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('antagony', ['devisable', 'mountainet', 'swoony'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'devisable'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('escadrille', ['statolatry', 'bossism', 'latitudinal', 'stringless', 'hypsobathymetric', 'coinfinity', 'autotype', 'figurant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'statolatry'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('anoplocephalic', ['grovel', 'stethoscopy', 'suddenty', 'legislatively', 'anoplocephalic', 'unimportant', 'unplace', 'plouk', 'crossed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'anoplocephalic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('demipauldron', ['inclose', 'indistinctness', 'schemata', 'staying', 'volvent', 'snaringly', 'unflat', 'unruminatingly', 'plurisyllable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'demipauldron'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('hexametrical', ['unbraceleted', 'runner', 'nickeline', 'cellulous', 'interlocutorily', 'ophthalmodynia', 'unthrone', 'pronunciability'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'unbraceleted'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('deuteride', ['deuteride', 'mimiambic', 'isoimmunity'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'deuteride'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pneumohydropericardium', ['spelunk', 'democratifiable', 'vacuous', 'spontaneous', 'supercapable', 'koolokamba', 'nosism', 'diplopia', 'biaxillary'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'pneumohydropericardium'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('archsacrificer', ['complications', 'unprophetical', 'unrevoked', 'profugate', 'voltmeter', 'foregoneness'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'complications'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pilgrimatical', ['cystolithic', 'orderly', 'stupidhead', 'valveless', 'miffiness', 'arrhenotoky', 'curiously', 'gerenuk', 'underbed'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'pilgrimatical'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('artillery', ['chromophilic', 'brabant', 'detailed', 'exulcerative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'detailed'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('buncal', ['twixt', 'benzolize', 'ebenaceous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'twixt'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('dichlorohydrin', ['myosarcomatous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'myosarcomatous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('vaulty', ['mastigopodous', 'fragileness', 'petulance'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'petulance'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('demodectic', ['tribunitive', 'mungofa', 'demodectic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'demodectic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('intersperse', ['lighttight', 'nautilite', 'alastrim', 'acetosalicylic', 'omnigerent', 'divisiveness', 'transubstantiationite', 'macrocyst'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'lighttight'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pratfall', ['quinometry', 'tyste', 'schistosome', 'reinclude', 'noncounty', 'shirtwaist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'reinclude'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bushful', ['actionary', 'pogonologist', 'snack', 'sabromin', 'hypervitalize', 'lakemanship', 'xylographical', 'barytone'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'sabromin'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('undared', ['chorizontes', 'infuriate', 'huddledom', 'pertly', 'bisacromial', 'taihoa', 'eponymize', 'commiserator', 'lightness', 'displeasurement'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'undared'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('tissue', ['plumbable', 'siroccoishly', 'uji', 'mortific', 'unbolt', 'loxodont', 'vasodilation', 'tartarize', 'tissue'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'tissue'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('undulous', ['seedcase', 'rudder', 'muttering', 'individualize', 'undulous', 'adhamant'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'undulous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('mild', ['remittance', 'ropish', 'undetermined', 'sigillographical', 'nounally', 'ununiversitylike'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'ropish'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chrysobull', ['geophyte', 'menthenone', 'aerobatic', 'begrease', 'darklings', 'ropable', 'overcharity', 'fineleaf'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'menthenone'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('upbelch', ['subchoroid', 'briefing'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'briefing'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('neckful', ['denunciator', 'gemmate', 'brigade', 'secondariness', 'verification', 'counteridea'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'gemmate'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('microblephary', ['retardant', 'preadequately'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'preadequately'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('trophobiosis', ['trophobiosis'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'trophobiosis'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cate', ['graphics', 'cate', 'missuppose', 'decalvation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'cate'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('grue', ['synovitis', 'uninsultable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'grue'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('urinogenital', ['intransigency', 'improperly', 'angiophorous'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'angiophorous'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('scarid', ['reticuloramose', 'pseudonymuncule', 'cacoepist', 'scarid', 'carbethoxyl', 'truncatorotund', 'unfelicitated', 'mochras'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'scarid'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('gentilize', ['gentilize', 'trihemimeral', 'bifid'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'gentilize'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chemitypy', ['keratonyxis', 'chemitypy', 'checkroll', 'hymnographer', 'tootler', 'perithelium', 'monodelph', 'manualism', 'neuroglial'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'chemitypy'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('homoeopathician', ['woomerang', 'entempest', 'spratty', 'unabatingly', 'hemocyanin', 'scoptophilic'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'homoeopathician'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unscared', ['unregimented', 'dissuasiveness', 'unissuable', 'soiling', 'connotative'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'soiling'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cottabus', ['cottabus', 'prescapularis', 'revaporization', 'censerless'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'cottabus'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('preshipment', ['typolithographic', 'telephone', 'palatial', 'autocamper'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'preshipment'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('catholicus', ['aestheticism', 'skullful', 'catholicus', 'headphone', 'fiend', 'lordy', 'sarlak', 'presuppositionless', 'squamulae'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'catholicus'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('quadripartition', ['ingress', 'ungag'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 6)
          'quadripartition'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('nacrite', ['behavior', 'aberdevine', 'dd', 'isopetalous', 'rousting', 'nonmonarchist', 'backjoint', 'unhearing', 'notice'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'nacrite'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('beast', ['borderlander', 'vedette', 'uncleverness', 'approaches', 'moviedom'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'vedette'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('presidence', ['bipupillate', 'gilbert', 'cardiagra'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 0)
          'presidence'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('dynamic', ['dynamic', 'twistable'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 7)
          'dynamic'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('pungey', ['toxicodermatitis', 'gallification', 'survival', 'rakshasa', 'pungey', 'overgrossness', 'postconvalescent', 'gander'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 4)
          'pungey'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('clouding', ['cacomixle', 'endonuclear', 'writer'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'cacomixle'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('losing', ['losing'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'losing'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('refederate', ['subframe', 'infinitude', 'astrochemist', 'shoulderer', 'sensation', 'nuclide', 'hallelujah'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 3)
          'infinitude'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('coolie', ['overusually', 'supercargoship', 'contemptuous', 'undrawn', 'catchpollery', 'unfinishedness', 'coolie', 'siruaballi', 'tsia'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 9)
          'coolie'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('chico', ['define', 'unmudded', 'unnourishing', 'fendable', 'spherulitize'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 1)
          'define'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('cointersecting', ['ungenuine', 'dealable', 'pejorism'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'ungenuine'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('does', ['sulphamidic', 'monopersulfuric', 'heartsickening', 'talkathon', 'does', 'beveil', 'aeroperitoneum'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 5)
          'does'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('bullation', ['angiography', 'nonsidereal', 'bullation'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 8)
          'bullation'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> autocorrect('unclement', ['disdiapason', 'unclement', 'cesser', 'repatronize', 'sacerdotalist'], lambda x, y, lim: min(lim + 1, abs(len(x) - len(y))), 2)
          'unclement'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import autocorrect, lines_from_file
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
