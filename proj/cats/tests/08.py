test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> typed = ['I', 'have', 'begun']
          >>> source = ['I', 'have', 'begun', 'to', 'type']
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> report_progress(typed, source, 1, print_progress) # print_progress is called on the report
          ID: 1 Progress: 0.6
          0.6
          >>> report_progress(['I', 'begun'], source, 2, print_progress)
          ID: 2 Progress: 0.2
          0.2
          >>> report_progress(['I', 'hve', 'begun', 'to', 'type'], source, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
          >>> # The above function displays progress in the format ID: __ Progress: __
          >>> print_progress({'id': 1, 'progress': 0.6})
          ID: 1 Progress: 0.6
          >>> typed = ['how', 'are', 'you']
          >>> source = ['how', 'are', 'you', 'doing', 'today']
          >>> report_progress(typed, source, 2, print_progress)
          ID: 2 Progress: 0.6
          0.6
          >>> report_progress(['how', 'aree'], source, 3, print_progress)
          ID: 3 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['smopple'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['equalizing', 'phrymaceous', 'jFluidimeter'], ['equalizing', 'phrymaceous', 'fluidimeter', 'seeds'], 48, print_progress)
          ID: 48 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['seeingly'], 13, print_progress)
          ID: 13 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['iprObaT\\ively', 'unabatedly', 'reundergo'], ['probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary'], 35, print_progress)
          ID: 35 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['elysia'], 90, print_progress)
          ID: 90 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['entomical'], 52, print_progress)
          ID: 52 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['choirwise', 'uncircumstantial', 'glassine', 'supplies', 'underivedly', 'henter', 'undeserving'], 47, print_progress)
          ID: 47 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['epinaos'], ['epinaos', 'unpresented'], 89, print_progress)
          ID: 89 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['cuir'], 29, print_progress)
          ID: 29 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['enterohelcosis', 'furo*deled'], ['enterohelcosis', 'urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation', 'peepeye', 'nonuterine'], 81, print_progress)
          ID: 81 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['excision', 'octobass', 'prevolitional', 'archtreasurership', 'metadiazine'], 0, print_progress)
          ID: 0 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['nailless'], 11, print_progress)
          ID: 11 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['FnonexpiryT', 'toywoman', 'impercipient'], ['nonexpiry', 'toywoman', 'impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['misinstruction', 'durian', 'underriding', 'chillroom', 'unabsorb', 'chromolithographic', 'hemadynamometer', 'frailly'], 63, print_progress)
          ID: 63 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['Xsnideness^-'], ['snideness', 'universalization'], 20, print_progress)
          ID: 20 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hecatontome', 'glioma', 'dispiteousness'], 29, print_progress)
          ID: 29 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['spaceful'], ['spaceful', 'cautery', 'wiseness'], 80, print_progress)
          ID: 80 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['hemicranic', 'hieromachy'], ['hemicranic', 'hieromachy', 'investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker'], 47, print_progress)
          ID: 47 Progress: 0.2857142857142857
          0.2857142857142857
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tubuliporoid', 'malleability'], 75, print_progress)
          ID: 75 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['K~sh~iLlingp', 'shrubbiness', 'Ndemode}D'], ['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright'], 53, print_progress)
          ID: 53 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['beydom', 'ungraspable', 'owrelay', 'ztanglep=roof', 'musterable'], ['beydom', 'ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular', 'recuperator', 'goto'], 74, print_progress)
          ID: 74 Progress: 0.375
          0.375
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['lithosis', 'bogland', 'interclash'], ['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird'], 96, print_progress)
          ID: 96 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['diplosphenal', 'cholecystogram'], 49, print_progress)
          ID: 49 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['metatatic', 'eugenist', 'karyopyknosis'], ['metatatic', 'eugenist', 'karyopyknosis', 'nightwork', 'short', 'insee', 'unmated', 'capacitation'], 84, print_progress)
          ID: 84 Progress: 0.375
          0.375
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['distressedly', 'gibbet'], ['distressedly', 'gibbet', 'cannily'], 34, print_progress)
          ID: 34 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['triplocaulescent', 'postprandially', 'helicogyrate'], ['triplocaulescent', 'postprandially', 'helicogyrate', 'coccidology', 'circumradius', 'repairer'], 6, print_progress)
          ID: 6 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['electrofused'], ['electrofused', 'incontinent'], 72, print_progress)
          ID: 72 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unhabitableness'], 50, print_progress)
          ID: 50 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['tetragynian'], ['tetragynian', 'persistently', 'becolme', 'seafare', 'bimillennium', 'valviform', 'thyridial', 'umbones'], 13, print_progress)
          ID: 13 Progress: 0.125
          0.125
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unwarrant'], 51, print_progress)
          ID: 51 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['sinfonietta'], ['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia'], 66, print_progress)
          ID: 66 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['tablespoon', 'anytime', 'ungotten', 'periostracal', 'laparogastrotomy'], ['tablespoon', 'anytime', 'ungotten', 'periostracal', 'laparogastrotomy', 'nucleonics', 'diaclase'], 45, print_progress)
          ID: 45 Progress: 0.7142857142857143
          0.7142857142857143
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['boucherism'], 15, print_progress)
          ID: 15 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['pyr!aNYl@', 'uncertainty', 'nl', 'intros!pecTi;onist', 'teeting'], ['pyranyl', 'uncertainty', 'nl', 'introspectionist', 'teeting', 'unbroiled', 'plumosity'], 24, print_progress)
          ID: 24 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['d/ugong', 'cryptodiran'], ['dugong', 'cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient', 'ritelessness'], 83, print_progress)
          ID: 83 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['quodlibetic', 'previdence', 'nonviscous'], ['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter'], 82, print_progress)
          ID: 82 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['semipervious', 'O:ca?ctoidj'], ['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation'], 43, print_progress)
          ID: 43 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous'], ['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete'], 38, print_progress)
          ID: 38 Progress: 0.8333333333333334
          0.8333333333333334
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['unsculptured', 'quagginess', 'indisputableness'], 2, print_progress)
          ID: 2 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['intraperitoneally'], 55, print_progress)
          ID: 55 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['siscowet', 'nevo', 'driftweed'], ['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations'], 48, print_progress)
          ID: 48 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['holland'], ['holland', 'nursedom', 'epidictical', 'defortify'], 28, print_progress)
          ID: 28 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['vegasite'], 66, print_progress)
          ID: 66 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['tularemia', 'booming', 'retrothyroid', 'decarnate', 'lobbyism', 'playa', 'nonreception', 'amphictyonic'], 79, print_progress)
          ID: 79 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['metamerically'], 96, print_progress)
          ID: 96 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['scrofulism', 'missile', 'tillot', 'douser', 'twankingly'], ['scrofulism', 'missile', 'tillot', 'douser', 'twankingly', 'eccentrate', 'cacoglossia'], 97, print_progress)
          ID: 97 Progress: 0.7142857142857143
          0.7142857142857143
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['encourager'], 70, print_progress)
          ID: 70 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unambiguously', 'standing'], ['unambiguously', 'standing', 'cameroon', 'unpretendingly'], 55, print_progress)
          ID: 55 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['megascleric'], 18, print_progress)
          ID: 18 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['cardioarterial', 'statolatry'], 91, print_progress)
          ID: 91 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['dextrousness', 'whirley', 'coldly', 'compendiary'], 14, print_progress)
          ID: 14 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['plowfoot', 'caducicorn'], 21, print_progress)
          ID: 21 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['plash', 'unbraceleted', 'runner', 'lnickeLineY', 'cellulous', 'interlocutorily'], ['plash', 'unbraceleted', 'runner', 'nickeline', 'cellulous', 'interlocutorily', 'ophthalmodynia'], 7, print_progress)
          ID: 7 Progress: 0.42857142857142855
          0.42857142857142855
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['sulphurage'], ['sulphurage', 'audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx', 'refractively'], 11, print_progress)
          ID: 11 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['whitecapper', 'uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography'], 22, print_progress)
          ID: 22 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['remissful'], 69, print_progress)
          ID: 69 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['microbiological'], ['microbiological', 'ruddy', 'gobble', 'pozzuolana', 'adscript'], 48, print_progress)
          ID: 48 Progress: 0.2
          0.2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['chromophilic', 'brabant', 'detailed', 'exulcerative', 'artillery', 'tachylytic', 'sinnable'], 58, print_progress)
          ID: 58 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['bounteousness', 'unimperious'], ['bounteousness', 'unimperious', 'twixt', 'benzolize', 'ebenaceous', 'buncal', 'cladoptosis', 'archvampire'], 50, print_progress)
          ID: 50 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['impedienTC', 'allochiralA', 'hear'], ['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous'], 76, print_progress)
          ID: 76 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['sulphurproof'], 89, print_progress)
          ID: 89 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['zygosporophore'], 62, print_progress)
          ID: 62 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['detinet'], 21, print_progress)
          ID: 21 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['monarchize', 'prankster', 'egomaniacal', 'deediness'], ['monarchize', 'prankster', 'egomaniacal', 'deediness', 'cheeser', 'cumulation', 'endorsee'], 73, print_progress)
          ID: 73 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['varicosed'], 18, print_progress)
          ID: 18 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['ultradolichocephalic'], ['ultradolichocephalic', 'kinetophone'], 1, print_progress)
          ID: 1 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['somatoplasm'], 75, print_progress)
          ID: 75 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['trackback'], 55, print_progress)
          ID: 55 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['payable', 'jaunt'], ['payable', 'jaunt', 'oleostearin'], 96, print_progress)
          ID: 96 Progress: 0.6666666666666666
          0.6666666666666666
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['oscillatory'], ['oscillatory', 'geophyte'], 1, print_progress)
          ID: 1 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(["stook'ie"], ['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch'], 24, print_progress)
          ID: 24 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['battlewise'], 74, print_progress)
          ID: 74 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['om%uscoid', 'reliquidation'], ['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant'], 33, print_progress)
          ID: 33 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['hexatomic', 'trophobiosis', 'parascenium'], ['hexatomic', 'trophobiosis', 'parascenium', 'gibbet'], 89, print_progress)
          ID: 89 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['incommensurable'], 58, print_progress)
          ID: 58 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['unexcusableness'], ['unexcusableness', 'bismuthyl'], 85, print_progress)
          ID: 85 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['intransigency', 'improperly'], 5, print_progress)
          ID: 5 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['penceless', 'bromothymol', 'reticuloramose'], 77, print_progress)
          ID: 77 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['beshag', 'monument'], ['beshag', 'monument', 'appressor', 'tutu'], 37, print_progress)
          ID: 37 Progress: 0.5
          0.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['uncivilized', 'pairer'], ['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer', 'tootler', 'perithelium'], 62, print_progress)
          ID: 62 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['confidentiality', 'inclementness'], 25, print_progress)
          ID: 25 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['sardius'], 76, print_progress)
          ID: 76 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['Wbescorch', 'rodding', 'disawa', 'gastradenitis'], ['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis'], 44, print_progress)
          ID: 44 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['transmundane'], 83, print_progress)
          ID: 83 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['Fdualisticu', 'becense', 'hyperingenuity'], ['dualistic', 'becense', 'hyperingenuity', 'pulpalgia'], 95, print_progress)
          ID: 95 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['tentacle', 'nonrestitution'], ['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically'], 84, print_progress)
          ID: 84 Progress: 0.3333333333333333
          0.3333333333333333
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['clique'], ['clique', 'spuriae', 'introspectable', 'pyritology', 'marbleize', 'blooddrop', 'prickingly'], 4, print_progress)
          ID: 4 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['hiro'], 33, print_progress)
          ID: 33 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly'], ['disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily', 'ternarious', 'riven'], 34, print_progress)
          ID: 34 Progress: 0.5714285714285714
          0.5714285714285714
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['nonfanciful', 'aneuploidy', 'lUnrubified', 'dynamic', 'twistable', 'mesmerically'], ['nonfanciful', 'aneuploidy', 'unrubified', 'dynamic', 'twistable', 'mesmerically', 'heyday', 'hipmold'], 27, print_progress)
          ID: 27 Progress: 0.25
          0.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['prorectorate'], ['prorectorate', 'snappable', 'pholadoid', 'toxicodermatitis', 'gallification', 'survival', 'rakshasa'], 5, print_progress)
          ID: 5 Progress: 0.14285714285714285
          0.14285714285714285
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['quadratical', 'principiate', 'archinfamyQ', 'cacomixle'], ['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear'], 90, print_progress)
          ID: 90 Progress: 0.4
          0.4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['upraisal', 'mechanicalist', 'losing', 'emancipation', 'counterquarterly', 'oppress'], ['upraisal', 'mechanicalist', 'losing', 'emancipation', 'counterquarterly', 'oppress', 'dishonorable', 'liang'], 57, print_progress)
          ID: 57 Progress: 0.75
          0.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['subframe'], 3, print_progress)
          ID: 3 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['Og>mbh', 'isocheimal', 'overusually'], ['gmbh', 'isocheimal', 'overusually', 'supercargoship', 'contemptuous', 'undrawn', 'catchpollery', 'unfinishedness'], 49, print_progress)
          ID: 49 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['lazzarone'], 5, print_progress)
          ID: 5 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['either', 'ungenuine', 'dealable'], ['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting'], 3, print_progress)
          ID: 3 Progress: 0.6
          0.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['reinsertion', 'moted', 'narcoanesthesia', 'tanbur', 'sulphamidic', "monopersu'lfuric"], ['reinsertion', 'moted', 'narcoanesthesia', 'tanbur', 'sulphamidic', 'monopersulfuric', 'heartsickening'], 26, print_progress)
          ID: 26 Progress: 0.7142857142857143
          0.7142857142857143
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress([], ['yond'], 79, print_progress)
          ID: 79 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> report_progress(['randann[=iteI'], ['randannite', 'overappraise', 'disdiapason', 'unclement', 'cesser', 'repatronize', 'sacerdotalist', 'atelectatic'], 80, print_progress)
          ID: 80 Progress: 0.0
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import report_progress
      >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
