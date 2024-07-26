test = {
  'name': 'Problem 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
          20.0
          >>> wpm("a b c", 20)
          3.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> wpm('hello friend hello buddy hello', 15)
          24.0
          >>> wpm('0123456789',60)
          2.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> wpm("a  b  c  d", 5)
          24.0
          >>> wpm("a b c", 120)
          0.5
          >>> wpm("abc", 1)
          36.0
          >>> wpm(" a b \tc" , 1)
          84.0
          >>> wpm("", 10)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> source_text = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string1 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art."
          >>> typed_string2 = "Abstraction, in general, is a fundamentl concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction usd in other fields such as art."
          >>> typed_string3 = "Abstraction,"
          >>> typed_string4 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. extra"
          >>> typed_string5 = "Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. Abstraction, in general, is a fundamental concept to computer science and software development. The process of abstraction can also be referred to as modeling and is closely related to the concepts of theory and design. Models can also be considered types of abstractions per their generalization of aspects of reality. Abstraction in computer science is also closely related to abstraction in mathematics due to their common focus on building abstractions as objects, but is also related to other notions of abstraction used in other fields such as art. art"
          >>> typed_string6 = "abstraction"
          >>> round(wpm(typed_string1, 67), 1)
          99.2
          >>> round(wpm(typed_string2, 67), 1)
          98.9
          >>> round(wpm(typed_string3, 67), 1)
          2.1
          >>> round(wpm(typed_string4, 67), 1)
          100.3
          >>> round(wpm(typed_string5, 67), 1)
          199.3
          >>> round(wpm(typed_string6, 1), 1)
          132.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('smopple', 52.11), 2)
          1.61
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('equalizing phrymaceous fluidimeter seeds', 30.6), 2)
          15.69
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('seeingly', 28.34), 2)
          3.39
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('probatively unabatedly reundergo unweld handgun hydrometra recessionary', 10.84), 2)
          78.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 40.74), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 24.25), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('choirwise uncircumstantial glassine supplies underivedly henter undeserving', 14.91), 2)
          60.36
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('epinaos unpresented', 46.73), 2)
          4.88
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 4.28), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('enterohelcosis urodele sporoid auximone nomenclatural misappreciation peepeye nonuterine', 24.14), 2)
          43.74
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('excision octobass prevolitional archtreasurership metadiazine', 92.55), 2)
          7.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('nailless', 1.39), 2)
          69.06
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('ringcraft nonexpiry toywoman impercipient overrude hyperingenuity piligerous molybdocolic toxicum', 2.72), 2)
          427.94
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('misinstruction durian underriding chillroom unabsorb chromolithographic hemadynamometer frailly', 39.83), 2)
          28.62
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('snideness universalization', 1.85), 2)
          168.65
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('hecatontome glioma dispiteousness', 30.44), 2)
          13.01
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('spaceful cautery wiseness', 31.29), 2)
          9.59
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('hemicranic hieromachy investigatable quadrigenarious protonemal cardiodysneuria provoker', 27.44), 2)
          38.48
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('tubuliporoid malleability', 8.5), 2)
          35.29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('shilling shrubbiness demoded commentary housewright', 80.33), 2)
          7.62
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('beydom ungraspable owrelay tangleproof musterable multivincular recuperator goto', 17.64), 2)
          54.42
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('lithosis bogland interclash widespread thumbbird gymnophiona unfond parageusia neurographic', 69.98), 2)
          15.6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('diplosphenal cholecystogram', 5.07), 2)
          63.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('metatatic eugenist karyopyknosis nightwork short insee unmated capacitation', 89.98), 2)
          10.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('distressedly gibbet cannily', 47.12), 2)
          6.88
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('triplocaulescent postprandially helicogyrate coccidology circumradius repairer', 82.31), 2)
          11.37
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('electrofused incontinent', 38.96), 2)
          7.39
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 47.25), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('tetragynian persistently becolme seafare bimillennium valviform thyridial umbones', 24.94), 2)
          38.97
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('prissy unwarrant bareboned krennerite thwartover autoinduction moity pyrolaceous dosimetry', 15.13), 2)
          71.38
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('sinfonietta trigon effluviate unhuman energeia', 1.11), 2)
          497.3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('tablespoon anytime ungotten periostracal laparogastrotomy nucleonics diaclase', 85.04), 2)
          10.87
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('boucherism', 82.3), 2)
          1.46
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('pyranyl uncertainty nl introspectionist teeting unbroiled plumosity', 21.89), 2)
          36.73
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('dugong cryptodiran coll staurolatry allthing cheatrie inexpedient ritelessness', 1.1), 2)
          850.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('quodlibetic previdence nonviscous reduplicatively arterioverter', 30.44), 2)
          24.84
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('semipervious cactoid quadrialate preflattery emancipation', 31.83), 2)
          21.49
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('puboprostatic tumescent keraunograph telecaster selenigenous phycomycete', 1.38), 2)
          626.09
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unsculptured quagginess indisputableness', 41.12), 2)
          11.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 4.56), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('siscowet nevo driftweed chevronelly victoryless illustrations', 1.04), 2)
          703.85
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('holland nursedom epidictical defortify', 86.07), 2)
          5.3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 4.99), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('tularemia booming retrothyroid decarnate lobbyism playa nonreception amphictyonic', 38.44), 2)
          25.29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 54.97), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('scrofulism missile tillot douser twankingly eccentrate cacoglossia', 76.76), 2)
          10.32
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 47.24), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unambiguously standing cameroon unpretendingly', 57.43), 2)
          9.61
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('megascleric', 33.57), 2)
          3.93
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('designee cardioarterial statolatry bossism latitudinal stringless hypsobathymetric coinfinity autotype', 27.29), 2)
          44.85
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('dextrousness whirley coldly compendiary', 89.3), 2)
          5.24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('plowfoot caducicorn', 86.49), 2)
          2.64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('plash unbraceleted runner nickeline cellulous interlocutorily ophthalmodynia', 1.14), 2)
          800.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('sulphurage audibility deuteride mimiambic isoimmunity rhinopharynx refractively', 12.32), 2)
          76.95
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('whitecapper uncontestable millage unbudging hydrostatic enterospasm ectypography', 40.87), 2)
          23.49
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('remissful', 57.91), 2)
          1.86
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('microbiological ruddy gobble pozzuolana adscript', 32.88), 2)
          17.52
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('monothelious chromophilic brabant detailed exulcerative artillery tachylytic sinnable clival', 26.63), 2)
          41.46
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('leaverwood bounteousness unimperious twixt benzolize ebenaceous buncal cladoptosis archvampire', 1.2), 2)
          940.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('impedient allochiral hear snur myosarcomatous', 32.74), 2)
          16.49
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('sulphurproof', 25.08), 2)
          5.74
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 6.8), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 47.77), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('monarchize prankster egomaniacal deediness cheeser cumulation endorsee', 71.5), 2)
          11.75
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('varicosed', 17.62), 2)
          6.13
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('ultradolichocephalic kinetophone', 13.09), 2)
          29.34
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 1.36), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 52.75), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('payable jaunt oleostearin', 13.95), 2)
          21.51
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('entropium oscillatory geophyte menthenone aerobatic begrease darklings ropable overcharity', 23.89), 2)
          45.21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('stookie withsave subchoroid briefing upbelch', 86.91), 2)
          6.08
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('battlewise', 15.17), 2)
          7.91
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('muscoid reliquidation broad tugging retardant', 68.87), 2)
          7.84
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('hexatomic trophobiosis parascenium gibbet', 49.49), 2)
          9.94
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 16.95), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('unexcusableness bismuthyl', 67.53), 2)
          4.44
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('ab evolution intransigency improperly angiophorous urinogenital episodial clatty pamphletary', 30.93), 2)
          35.69
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('penceless bromothymol reticuloramose', 34.55), 2)
          12.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('beshag monument appressor tutu', 37.27), 2)
          9.66
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('uncivilized pairer keratonyxis chemitypy checkroll hymnographer tootler perithelium', 5.52), 2)
          180.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('confidentiality inclementness', 81.52), 2)
          4.27
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('sardius', 12.9), 2)
          6.51
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('bescorch rodding disawa gastradenitis cottabus prescapularis', 1.44), 2)
          500.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('transmundane', 18.66), 2)
          7.72
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('dualistic becense hyperingenuity pulpalgia', 46.99), 2)
          10.73
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('tentacle nonrestitution interventional demiditone chrysophilite idiosyncratically', 47.79), 2)
          20.34
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('clique spuriae introspectable pyritology marbleize blooddrop prickingly', 1.26), 2)
          676.19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 3.13), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('disdiaclastic tutoyer fibrilliferous undiscernedly gloomily ternarious riven', 74.44), 2)
          12.25
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('nonfanciful aneuploidy unrubified dynamic twistable mesmerically heyday hipmold', 4.43), 2)
          214.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('prorectorate snappable pholadoid toxicodermatitis gallification survival rakshasa', 5.32), 2)
          182.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('quadratical principiate archinfamy cacomixle endonuclear', 77.93), 2)
          8.62
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('upraisal mechanicalist losing emancipation counterquarterly oppress dishonorable liang', 98.11), 2)
          10.52
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('subframe', 20.78), 2)
          4.62
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('gmbh isocheimal overusually supercargoship contemptuous undrawn catchpollery unfinishedness', 83.77), 2)
          13.04
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('lazzarone', 1.67), 2)
          64.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('donary either ungenuine dealable pejorism cointersecting outerly rifter glimmering', 29.25), 2)
          33.64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('reinsertion moted narcoanesthesia tanbur sulphamidic monopersulfuric heartsickening', 29.4), 2)
          33.88
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('', 54.09), 2)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(wpm('randannite overappraise disdiapason unclement cesser repatronize sacerdotalist atelectatic', 1.11), 2)
          972.97
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import wpm
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
