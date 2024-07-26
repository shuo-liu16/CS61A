test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
          100.0
          >>> accuracy("a b c", "a b c")
          100.0
          >>> accuracy("a  b  c  d", "b  a  c  d")
          50.0
          >>> accuracy("a b", "c d e")
          0.0
          >>> accuracy("Cat", "cat") # the function is case-sensitive
          0.0
          >>> accuracy("a b c d", "a d")
          25.0
          >>> accuracy("abc", " ")
          0.0
          >>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
          100.0
          >>> accuracy("abc", "")
          0.0
          >>> accuracy("", "abc")
          0.0
          >>> accuracy("a b c d", "b c d")
          0.0
          >>> accuracy("cats.", "cats") # punctuation counts
          0.0
          >>> accuracy("", "") # Returns 100.0
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> accuracy('Cute Dog!', 'Cute Dog.')
          50.0
          >>> accuracy('A Cute Dog!', 'Cute Dog.')
          0.0
          >>> accuracy('cute Dog.', 'Cute Dog.')
          50.0
          >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
          50.0
          >>> accuracy('Cute', 'Cute Dog.')
          100.0
          >>> accuracy('', 'Cute Dog.')
          0.0
          >>> accuracy('', '')
          100.0
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
          >>> round(accuracy(typed_string2, source_text), 1)
          97.7
          >>> round(accuracy(typed_string3, source_text), 1)
          100.0
          >>> round(accuracy(typed_string4, source_text), 1)
          98.9
          >>> round(accuracy(typed_string5, source_text), 1)
          49.7
          >>> round(accuracy(typed_string6, source_text), 1)
          0.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('modern[-izer marque_ .roi$t befr+iz. psychologi"c baptizee_', 'modern[-izer marque_ .roi$t befr+iz. psychologi"c baptizee_ u-nflu"ent f]reckleproof'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('phrymaceous bridgema:ki<ng non*support|er (feasible respectability_ mong{relize ul<la}ge sinistrogyration treasur"es(', 'phrymaceous bridgema:ki<ng non*support|er (feasible respectability_'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ammonionitr.ate s>ulpholysis a&dmirative cirso]tomy itin+\\eration preoffensively', 'ammonionitr.ate s>ulpholysis a&dmirative cirso]tomy itin+\\eration preoffensively acardiac +psychophysio;logist nicknameable'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('handgun hydrometra)^ anticentralization unmicrob/#ic paradisal+ vulval dr.oo[py', 'handgun hydrometra)^ anticentralization unmicrob/#ic paradisal+'), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cunge(boi mistressdom sir\\l<oin mol^}eproof ala@creatin$ine', 'cunge(boi mistressdom sir\\l<oin mol^}eproof ala@creatin$ine'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('prebelev`*e astrola<bic}al cheilitis wraw gageable', 'prebelev`*e astrola<bic}al cheilitis wraw gageable v[iolin isocamphori}c gramma@ticaster'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('underivedl[y! s,te&reographical prerich greedygut purpur^*oid nonwinged broo*l', 'underivedl[y! s,te&reographical prerich greedygut purpur^*oid nonwinged'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("unp;r^esented unsti'rra:ble fixatif needlepro_of obtrude madreporitic ne,xus}", "unp;r^esented unsti'rra:ble fixatif needlepro_of obtrude"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('nih-ilification crapy ixodian reliner ebull%ioscope', 'nih-ilification crapy ixodian reliner ebull%ioscope booky'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('au+ximone peepey`e~ sanctiona(ry pse\\udotrachea unvendiblene>s&s', 'au+ximone peepey`e~ sanctiona(ry pse\\udotrachea unvendiblene>s&s'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('prevol"ition(al outknave cryptoagnostic volhy:ni=te wh{iptr:ee preaffect +elopement', 'prevol"ition(al outknave cryptoagnostic volhy:ni=te wh{iptr:ee preaffect +elopement'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('apoc>^yneous hol&oplankton dahoon warning graticul&e unc+hri"stianness', 'apoc>^yneous hol&oplankton dahoon warning graticul&e unc+hri"stianness lacker unvolatile'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('nonexp}iry molybdoc>olic s=tratography. ]unquibbled pa=r;asitotropism counterbuff', 'nonexp}iry molybdoc>olic s=tratography. ]unquibbled pa=r;asitotropism'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('misinstruction underriding ;unabsor{b a|mphi[genetic unbacked le[arn.t an`thoid episcopacy', 'misinstruction underriding ;unabsor{b a|mphi[genetic unbacked'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('accroach s^eag+oer red#isemb)ark mono^dactylate chondroplastic batt/ue sternmost', 'accroach s^eag+oer red#isemb)ark mono^dactylate chondroplastic batt/ue'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('dependa;bly extraessent}ial ~fl$uoborate accomp}lisher zambi^a _ferrado& unprescient strange', 'dependa;bly extraessent}ial ~fl$uoborate accomp}lisher zambi^a _ferrado&'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('irenically caut&ery +y/obi un:shrine%d spe)aker musicpr_oo!f vagotropic dispope', 'irenically caut&ery +y/obi un:shrine%d spe)aker musicpr_oo!f vagotropic dispope doors'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('investigatable protonemal asso:ciated, uni<radiate; carrag>een archipterygia-l', 'investigatable protonemal asso:ciated, uni<radiate; carrag>een archipterygia-l bar)b^arism kah{ar]'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tubuliporoid scus;at)ion splenatr\\ophy` schedular un]leased subconstable vassaldom succin nationaliza\\tion', 'tubuliporoid scus;at)ion splenatr\\ophy` schedular un]leased subconstable vassaldom'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("de{moded sinusoid omi`ssivel~y _{largest h'ematocy~stis na<sial buoyantne(ss", "de{moded sinusoid omi`ssivel~y _{largest h'ematocy~stis"), 2)
          71.43
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('owrelay muste:rabl_e i;sopterous mer=it inf\\u^la', 'owrelay muste:rabl_e i;sopterous mer=it inf\\u^la harrier'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('bogland widespre,ad} unreason hypogonation pillared bestiali+ze', 'bogland widespre,ad} unreason hypogonation pillared bestiali+ze'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cholecystogram ma}ximization ,m:orrow watertig=ht appearance mis">sionize ~tra-nspicuously', 'cholecystogram ma}ximization ,m:orrow watertig=ht appearance mis">sionize ~tra-nspicuously'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('eugenist sho[rt capacitation sonderclass]? discomedusoid', 'eugenist sho[rt capacitation sonderclass]? discomedusoid goo?lah s>alsolaceous'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('gibbet lu{,ne mo"noxeno^us en)terotomy` un~barrable outs_windle w-hunstane "pag@anry', 'gibbet lu{,ne mo"noxeno^us en)terotomy` un~barrable outs_windle w-hunstane "pag@anry ]kerslosh+'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('|postprandiall"y pa>>ssingly nonappr&opriation lat^h dow~nfallen dis|assimilate pa*roecy &d{etachedness', '|postprandiall"y pa>>ssingly nonappr&opriation lat^h dow~nfallen dis|assimilate pa*roecy &d{etachedness slatternly'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('electrofus*ed {unrel|atedness schem-atize dismoun+table~ quernston]>e cervicorn saltly', 'electrofus*ed {unrel|atedness schem-atize dismoun+table~ quernston]>e cervicorn saltly'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('lampless fi|brocho\\ndroma pal#aeoatavism mi<crocephalia qu.\\adrilled', 'lampless fi|brocho\\ndroma pal#aeoatavism mi<crocephalia qu.\\adrilled horror r)ehan?g'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('persistentl^y valvi<form unfastidiou]s cu@s"ser p,ossessio.ner', 'persistentl^y valvi<form unfastidiou]s cu@s"ser p,ossessio.ner'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('unwarrant au"t_oinduction mesoder:mic uncranked arter~ialize jo~llo-ped', 'unwarrant au"t_oinduction mesoder:mic uncranked arter~ialize'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('resour#ce cample aconi?#te assis[ti+ve p;redefault( dern>ier` b(edrape glo_wering andro$morphous', 'resour#ce cample aconi?#te assis[ti+ve p;redefault( dern>ier`'), 2)
          66.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tablespoo_n laparogastrot.omy deprive] .structurali,ze _be{reaven seama=nc.raft encloak ;benj! liter', 'tablespoo_n laparogastrot.omy deprive] .structurali,ze _be{reaven'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('rutab#aga magnif:i|er anisic f}orer;eckon arco]c;entrous ron@tge=n', 'rutab#aga magnif:i|er anisic f}orer;eckon arco]c;entrous ron@tge=n electro;p=olar valv<ulotomy $perc"oid'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('introspection*)ist duck>ing du{cker geocyclic uncar?]ried shriver<', 'introspection*)ist duck>ing du{cker geocyclic uncar?]ried shriver< sulfurate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("du!gong )#cheatrie c+areer/ unemphatica>]l swe(etf'ish atef ^hastingsite xanthen=e", "du!gong )#cheatrie c+areer/ unemphatica>]l swe(etf'ish"), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('previd:ence* crooktoot~hed sifaka &peter% unwiel#$dily de/r!ic footstool# (asynerg]ia', 'previd:ence* crooktoot~hed sifaka &peter% unwiel#$dily'), 2)
          62.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy(',\\emancipation unchristianity mauvine adu!nc mila', ",\\emancipation unchristianity mauvine adu!nc mila 's;uasive"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tel`e.caster bar;retter [t?echnicalize lamell_ated h<e$xastylar', 'tel`e.caster bar;retter [t?echnicalize lamell_ated h<e$xastylar bepu?n sla:ught,erhouse'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('qu-agginess h]ypoc>ist >b*eechy plenilune endermati>c. na$sa u>nbath.ed skogbolite', 'qu-agginess h]ypoc>ist >b*eechy plenilune endermati>c. na$sa'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("s*tre*am mes'othe+sis t;imeworn hydrarthrosis fo+reknowab[le", "s*tre*am mes'othe+sis t;imeworn hydrarthrosis fo+reknowab[le condemnat_o|ry wa-;glike"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('>dr-iftweed *antialbumid rhyptic/ pivalic strawbreadth antiquitarian celidography de)ludable whinnock', '>dr-iftweed *antialbumid rhyptic/ pivalic strawbreadth'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('nursedom taraf{ www p"la^ntsman fosteringl(y chield| biol r_edue c)itharoedic&', 'nursedom taraf{ www p"la^ntsman fosteringl(y chield| biol r_edue'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('_sunbird ~n\\isei fallaci<ous saet~^er talofibular', '_sunbird ~n\\isei fallaci<ous saet~^er talofibular landraker }achro^matically occasionalist'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('boomin/g }playa unjoyou<sness booju"m< suprachoroidal', 'boomin/g }playa unjoyou<sness booju"m< suprachoroidal'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('meta!me?rically nonimpar>)tment joyant kefiric~ &plaid(ed bac>cae mo,lm"an sho!ebl=ack non&farm', 'meta!me?rically nonimpar>)tment joyant kefiric~ &plaid(ed'), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('do]use"r trollf?lower athalli\'ne uniformi;tarian=ism po#lyg&amic up]t*ill dodecamerous u%n\'holy molossine', 'do]use"r trollf?lower athalli\'ne uniformi;tarian=ism po#lyg&amic up]t*ill dodecamerous u%n\'holy molossine'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ree&\\st se=xuale d&indle count[e+rtranslation s^l=avepen', 'ree&\\st se=xuale d&indle count[e+rtranslation s^l=avepen thi&eftaker absorb_er neo$classic va$por>escence'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("cam%eroon puppydom semo'l~ella |pomacen,troid fletcher matriculator reluctan|c(e muffineer pericardiac", "cam%eroon puppydom semo'l~ella |pomacen,troid fletcher"), 2)
          55.56
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy(']de-visable settlor cestoidean aerophotogr+aphy ascendent homo]tr&ansplantation', ']de-visable settlor cestoidean aerophotogr+aphy ascendent'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("cardioarter')ial coi'nfini,ty trillion|ai^re storiological outward!most calligraphical", "cardioarter')ial coi'nfini,ty trillion|ai^re storiological outward!most calligraphical ostosis"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('whirley compendiary gro)v&el anoplocephalic un~pl(ace "somewhiles cet"iosaurian\' +manu+facturess foredispos;e', 'whirley compendiary gro)v&el anoplocephalic un~pl(ace "somewhiles cet"iosaurian\' +manu+facturess foredispos;e'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("caducicorn 'palmately <vas#quine s!exolog=ical unstraying salacious |&uptower", "caducicorn 'palmately <vas#quine s!exolog=ical unstraying salacious |&uptower"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('interlocutorily{ pronunciabi%li?ty ary,late im`pli[al d@isaffection', 'interlocutorily{ pronunciabi%li?ty ary,late im`pli[al d@isaffection'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('deuterid@e( refractive/ly st?aur/acin bureaucrat)ical physic~al helminthic hairband manne`rle~ss hypostatization{}', 'deuterid@e( refractive/ly st?aur/acin bureaucrat)ical physic~al helminthic hairband'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('hydros]tatic :fega`ry mana ca[udotibialis centrob>aric g&eet.', 'hydros]tatic :fega`ry mana ca[udotibialis centrob>aric g&eet. suffr=agettism st@artfulness k`a<ns'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('inyoite unprophetical profugate, anurous orthopteran sponsing', 'inyoite unprophetical profugate, anurous orthopteran sponsing bronch^ioli'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('g[obble o:ssypite h@umanistic i\\soanti>body e+xistentialism isohemopyrr!ole subsa+lt', 'g[obble o:ssypite h@umanistic i\\soanti>body e+xistentialism isohemopyrr!ole'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('chromo!_philic tachylytic rabbin:shi`p v@alentine c*irrol~ite tanti', 'chromo!_philic tachylytic rabbin:shi`p v@alentine c*irrol~ite tanti dec[alescen+t wo<rshipfully'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('le-averwood twix<t c%&ladoptosis archicoele po_]ddy motorphobe thyroidectomize rerope', 'le-averwood twix<t c%&ladoptosis archicoele po_]ddy motorphobe'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('hear ;myosarcomatou/s carbon]ace_ous suprasphanoidal a)d%jectival w;indle~s catering parapsychism\\ bureaux', 'hear ;myosarcomatou/s carbon]ace_ous suprasphanoidal a)d%jectival w;indle~s catering parapsychism\\'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('stud&iedly vaulty" bu[tylation !]sewerman aunc)el overlip', 'stud&iedly vaulty" bu[tylation !]sewerman aunc)el overlip'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tribunitiv=e( sigi?llation end*ocoeliac hydrosta$tician defunctionalize', 'tribunitiv=e( sigi?llation end*ocoeliac hydrosta$tician defunctionalize ?anemoscope asser(toric'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('caph-ar archde#vil restaurant l}ightti~ght pathog<ermic=', 'caph-ar archde#vil restaurant l}ightti~ght pathog<ermic= *_gleg'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cheeser endorsee tyste" pra~tfall dialecticiz<e enodal', 'cheeser endorsee tyste" pra~tfall dialecticiz<e enodal rec]tor'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('varicos/e{d pogonologist {sn#ack _b\\ushful longevi-ty inp$atient moo=nwards tolyl&en-ediamine', 'varicos/e{d pogonologist {sn#ack _b\\ushful longevi-ty inp$atient'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('k`]inetophone form-ature boccaro br@utelike overt_}imer wenny pharmacology', 'k`]inetophone form-ature boccaro br@utelike overt_}imer wenny pharmacology'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('protosa(urian mortific loxodont tartarize underwarden', 'protosa(urian mortific loxodont tartarize underwarden aquatic alti,loquent feasance'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('pesterer muttering undulous enderoni|,c ly<canthrope', 'pesterer muttering undulous enderoni|,c ly<canthrope sp{lanchnapophysial t/hecal waste'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('+j[aunt ne&uterdom ropis),h &mi]ld geront?.es untenantab!leness tomentous crouching', '+j[aunt ne&uterdom ropis),h &mi]ld geront?.es untenantab!leness'), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('oscil"latory aerobatic d(arklings finelea[f ethnic par-abolically', 'oscil"latory aerobatic d(arklings finelea[f ethnic par-abolically rebate'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('subch<oro}id pr%omus{cidate perist/erit%e inductivity nonelemental phytogeography', 'subch<oro}id pr%omus{cidate perist/erit%e inductivity nonelemental phytogeography'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('battl&ew|ise gemm!ate co$unteridea guinea^ bedwell invo&lute;ly', 'battl&ew|ise gemm!ate co$unteridea guinea^ bedwell invo&lute;ly jink.le: su?bdete~rminant'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('re<liqui@dation microblep/hary\\ sple@#nolysis ku%lm! ta;ilorism misintimation *pleapro+of bosch, surpris.er', 're<liqui@dation microblep/hary\\ sple@#nolysis ku%lm! ta;ilorism misintimation *pleapro+of'), 2)
          77.78
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tro(phobiosis transcriptionally riotou$"sness bizardite nebulous fulvous ba%n tra;nsverse transgressive', 'tro(phobiosis transcriptionally riotou$"sness bizardite nebulous fulvous ba%n tra;nsverse'), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('non]spark>ing m\\issuppose erin@^eum ancest`orially i?ndefini?te', 'non]spark>ing m\\issuppose erin@^eum ancest`orially i?ndefini?te prodpr)oof, photogrammeter al|tarist'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("unexc[usableness prank@fulness mammectomy abolishment unwither&ing 'p;rickled p<arade", "unexc[usableness prank@fulness mammectomy abolishment unwither&ing 'p;rickled p<arade sorr.y"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("evolution improperly ang%&iophorous :subclassify coc)kcrowi'ng dra<whead", "evolution improperly ang%&iophorous :subclassify coc)kcrowi'ng dra<whead"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("penceless pseudony-muncule tru$ncator?otund malpais u'navenued l#ig{as cau#licl'e magistr'ative hy`oid", "penceless pseudony-muncule tru$ncator?otund malpais u'navenued l#ig{as cau#licl'e magistr'ative"), 2)
          88.89
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('appre!sso_r propygidium wa,rs\\ bulbose pseudoanaphylactic und]i}scerned geron)tox^on insouciant dim!inishab|leness', 'appre!sso_r propygidium wa,rs\\ bulbose pseudoanaphylactic und]i}scerned geron)tox^on insouciant dim!inishab|leness'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('(pa%irer p%eritheli<um #ha*ire unauspiciou|s s^lumward', '(pa%irer p%eritheli<um #ha*ire unauspiciou|s s^lumward peastaking )myspace'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('in^c`lementness uncostly penum:brous: pi%nnatedly s)wanwort oogamy; ragtimey', 'in^c`lementness uncostly penum:brous: pi%nnatedly s)wanwort oogamy;'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('tailings unreg]imented= uns)cared flo!riferousness. peasant trigonomet\\ric', 'tailings unreg]imented= uns)cared flo!riferousness. peasant'), 2)
          83.33
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('rep{ugnatorial. cottabu\\s a;psis@ unlidded sodless h!ipped \\adoptioni>sm hollowhe\\artedness', 'rep{ugnatorial. cottabu\\s a;psis@ unlidded sodless h!ipped \\adoptioni>sm hollowhe\\artedness c[abine*t'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('transmundane |*peeled coucher flaved)o u*npious sword/ zoril%lo]', 'transmundane |*peeled coucher flaved)o u*npious sword/'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("dualisti@c aestheticism cat'holicus sa@rlak sitio$ a&pyrous. une]xtinct hippish", "dualisti@c aestheticism cat'holicus sa@rlak sitio$ a&pyrous. une]xtinct hippish precorrespondence"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('demiditone teos&inte pr_etransmit rytidos*i[s occipitotha*la!mic wa>kiki# piperi|dge recurs(e', 'demiditone teos&inte pr_etransmit rytidos*i[s occipitotha*la!mic wa>kiki# piperi|dge recurs(e'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("prickingl(y musculocutaneous%' doo]red_ top:)s isopetalous rousting\\! inte/rfilament-ar vikinglike", "prickingl(y musculocutaneous%' doo]red_ top:)s isopetalous rousting\\!"), 2)
          75.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ringgiving unta`kab-leness borderlander uncle!ve/rness unknight', 'ringgiving unta`kab-leness borderlander uncle!ve/rness unknight `la.n'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('fibrill"iferous undiscernedl((y fe^tici#de misun@derstand|able de&legation palaestrics; pam[physical', 'fibrill"iferous undiscernedl((y fe^tici#de misun@derstand|able de&legation palaestrics;'), 2)
          85.71
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("/aneuploidy m'esmer;ically unpilloried `cytodiereti?c diurn!ation", "/aneuploidy m'esmer;ically unpilloried `cytodiereti?c diurn!ation trichoma endoappen~d*icitis pty_alocele radic.ulose"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('p|hola{doid overg"rossness gander an}acan@thine peacebrea&ker', 'p|hola{doid overg"rossness gander an}acan@thine peacebrea&ker dichloramine calotypis(t pha@nerocryst ampelitic'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('cacom{ixle ensa]ff\\ron anticaste predis_tri*ct cyanoacetat?e orthocep>hal(y tin:sman immobilize', 'cacom{ixle ensa]ff\\ron anticaste predis_tri*ct cyanoacetat?e orthocep>hal(y tin:sman'), 2)
          87.5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("mecha~nicalist oppress lia''ng cometlike graphite", "mecha~nicalist oppress lia''ng cometlike graphite uxori!ous desmachym=e# swor(dman unrelentor"), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('subframe astrochemist ha;llelujah replotter %enneasylla*bic w&arden', 'subframe astrochemist ha;llelujah replotter %enneasylla*bic w&arden dharmashastra viato[ria\\l'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('i_socheimal contem.p`tuous mesogna?t`hism gilded nursehou?nd', 'i_socheimal contem.p`tuous mesogna?t`hism gilded nursehou?nd i>gniter'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy("lazzaron!e fendabl[e noetics sartor genisaro brierwood pardonee pubot'ibial disciplina>riani&sm", 'lazzaron!e fendabl[e noetics sartor genisaro brierwood'), 2)
          66.67
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('ungenu`ine ri"f<ter hagioscopic scr!otecto#my mu+/lattress pokerishly', 'ungenu`ine ri"f<ter hagioscopic scr!otecto#my mu+/lattress pokerishly goa@d"'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('n[arcoanesthesia monopersulfuric talkathon does aeroperitoneum', 'n[arcoanesthesia monopersulfuric talkathon does aeroperitoneum lad)le unc]ontrolledl=y'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('mud nonsi+de|real \\unbetraying non{compea<rance filicol^ogist', 'mud nonsi+de|real \\unbetraying non{compea<rance filicol^ogist'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> round(accuracy('overappraise disdiapason c<esser plasm,a vi}ndic*able', 'overappraise disdiapason c<esser plasm,a vi}ndic*able fjerding abacisc_}us'), 2)
          100.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import accuracy
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
