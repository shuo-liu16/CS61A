test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dogs = about(['dogs', 'hounds'])
          >>> dogs('A paragraph about cats.')
          False
          >>> dogs('A paragraph about dogs.')
          True
          >>> dogs('Release the Hounds!')
          True
          >>> dogs('"DOGS" stands for Department Of Geophysical Science.')
          True
          >>> dogs('Do gs and ho unds don\'t count')
          False
          >>> dogs("AdogsParagraph")
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
          >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
          'Cute Dog!'
          >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
          'Nice pup.'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      >>> from cats import pick
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> ab = about(['neurine', 'statutably', 'quantivalent', 'intrarachidian', 'itinerantly', 'cloaklet'])
          >>> ab('unhollow simsim dcloakletB itinerantly cloakLet dQUaNtivalentJ gnEurinE fissiparity Mneurinel')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unsimilar', 'conditioning', 'crystallogenical', 'mennom', 'foreannouncement', 'neomorph'])
          >>> ab('#crystallogenIcalW podded reorganizationist neomorPhf hneomorphj')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['smopple', 'modernizer'])
          >>> ab('tongsman smopplek ASmoppleg Bsm(<opPLeF SMopPlES')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['equalizing', 'phrymaceous', 'fluidimeter', 'seeds', 'bridgemaking'])
          >>> ab('xph+rymaceous hobbledehoyism zphrymaceousy ofluidimeter Lseeds?\\ interbank DsEe)dS consumer iatromathematical')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['seeingly', 'essexite'])
          >>> ab('essexite clupeine habeas disrupture faceable phototypography LseeIngly seeingly')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['probatively', 'unabatedly', 'reundergo', 'unweld', 'handgun', 'hydrometra', 'recessionary', 'grippotoxin'])
          >>> ab('DreuNdergo reundergo unabAtedlYM grippotoxin Lre<und!ergoy')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['elysia'])
          >>> ab('hewlett el=ysiA` pamphletic elysia te#Lysiac')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['entomical'])
          >>> ab('obduction polyacid en\\tomical{w entoMicAlP entO[m]icalP befrill zentom[icalr centomi_CAl')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['choirwise', 'uncircumstantial', 'glassine', 'supplies', 'underivedly', 'henter', 'undeserving', 'uncope'])
          >>> ab('tazia uncope glassine glassineW eChoirwis<e& uncircumstaNTIal uninventiveness pentahexahedral')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['epinaos', 'unpresented', 'homotypic'])
          >>> ab('coenoecial synodist tipper unportentous sclerometer epinaos unpresented catnip homotypicy')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['cuir'])
          >>> ab('cuir polystomatous illiterately Hc)uI`re cCuir jc|ui!R cUir CUirG barycentric')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['enterohelcosis', 'urodele', 'sporoid', 'auximone', 'nomenclatural', 'misappreciation', 'peepeye', 'nonuterine', 'antilacrosse'])
          >>> ab('enteRoh<eLcos:ise peepeyep misappreciation enteROhel<co]sis CSporoid peepeyel desoxybenzoin')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['excision', 'octobass', 'prevolitional', 'archtreasurership', 'metadiazine', 'overwomanize'])
          >>> ab('Larchtreasurershipk octobass carder handclasp O`exCiSion ,excisiont scavenger')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['nailless', 'singletree'])
          >>> ab('qualificator accoy crystallogeny players clubfellow')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['nonexpiry', 'toywoman', 'impercipient', 'overrude', 'hyperingenuity', 'piligerous', 'molybdocolic', 'toxicum', 'testator'])
          >>> ab('nonexpiryV testator piligerous noNe,xpiry reconcentrate smolybdocolick')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['misinstruction', 'durian', 'underriding', 'chillroom', 'unabsorb', 'chromolithographic', 'hemadynamometer', 'frailly', 'diana'])
          >>> ab('dodoism wmisinstruction ghemadYnamomeTerg euphonious funderridin!Gm')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['snideness', 'universalization', 'accroach'])
          >>> ab('crock omophagous testamentate Aa=CcroacH<n AccROaChS')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hecatontome', 'glioma', 'dispiteousness', 'dependably'])
          >>> ab('Cd?ependab_ly adipocere ngliomaE glioMaV vigor dispiteousness')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['spaceful', 'cautery', 'wiseness', 'yobi'])
          >>> ab('SwiSenesS* chavicin wisene]ss}z embryoma Tsp|!acefUl')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hemicranic', 'hieromachy', 'investigatable', 'quadrigenarious', 'protonemal', 'cardiodysneuria', 'provoker', 'associated'])
          >>> ab('quadrigenariousE Lpro-tonemalz mesorchial Ohierom]achyh dinveStigatable f')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['tubuliporoid', 'malleability', 'scusation'])
          >>> ab('RtubuLiporoiDA Dmalleability mAlLeabilit@yi malleabilIty scusAtioN bmalleability josh')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['shilling', 'shrubbiness', 'demoded', 'commentary', 'housewright', 'sinusoid'])
          >>> ab('ridgepoled halogen sclerometric sclerochoroiditis odemodEdi opercle')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['beydom', 'ungraspable', 'owrelay', 'tangleproof', 'musterable', 'multivincular', 'recuperator', 'goto', 'turnsole'])
          >>> ab('JrEcupeRatorJ ZgotO t|urnsoLe#K re#cuperatoRZ tAngleproOfu mmultiVincularl ibeydom beydomG')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lithosis', 'bogland', 'interclash', 'widespread', 'thumbbird', 'gymnophiona'])
          >>> ab('CI$nteRc{lash KthumbbirdI FlithosiS crinigerous ElithoSis vthumbBird')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['diplosphenal', 'cholecystogram', 'maximization'])
          >>> ab('diplosphenal cholecYstogramC otherhow gaulin Cmaxim}izaTio]nU fatuism cholecystogram maximization')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['metatatic', 'eugenist', 'karyopyknosis', 'nightwork', 'short', 'insee', 'unmated', 'capacitation', 'constructivist'])
          >>> ab('constructivist dnigHt-woR=kn WnighTworkd o\\k~aryopyknoSis karyopyknosis unrepresentative imetata(tic kaRy&opyknosis ichneumonized')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['distressedly', 'gibbet', 'cannily', 'lune'])
          >>> ab('luneW sesquitertia Wlune fluvioterrestrial wdistressedlyI')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['triplocaulescent', 'postprandially', 'helicogyrate', 'coccidology', 'circumradius', 'repairer', 'passingly'])
          >>> ab('triplocaulescent VtriplocaulescentF postprandially coccidology ccocciDoloGyw bloated ttriplocaulescent ncoccidology repaiRerN')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['electrofused', 'incontinent', 'activize'])
          >>> ab('assart acTi^vI]zeX unsulphonated activizep aincontinent Me}leCtrofused incontinent electrofused dactivized')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unhabitableness'])
          >>> ab('arisen fibrochondroma afflatus drowsiness untopped unberth')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['tetragynian', 'persistently', 'becolme', 'seafare', 'bimillennium', 'valviform', 'thyridial', 'umbones', 'logitech'])
          >>> ab('bi$millenNIu"mx XThyridial unpunishable predeprivation PersiSteNtLy')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unwarrant'])
          >>> ab('unWarrantx resort Junwarran<$TI unwarrantE subdepot reaggravation unwarrant')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['sinfonietta', 'trigon', 'effluviate', 'unhuman', 'energeia', 'slouch'])
          >>> ab('tRigOnz sinfoniEtta trigon trichotomism benergeian lsinfonietta bullsucker effluviate')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['tablespoon', 'anytime', 'ungotten', 'periostracal', 'laparogastrotomy', 'nucleonics', 'diaclase', 'wadmaking'])
          >>> ab('risen tablespoonS bichord coumarinic e]tablespoon')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['boucherism', 'rutabaga'])
          >>> ab('initiate boucherism baniya gnomological wirable superincumbently bouchEri(smg')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['pyranyl', 'uncertainty', 'nl', 'introspectionist', 'teeting', 'unbroiled', 'plumosity', 'restock'])
          >>> ab('Ynl nlS restockM Rnl_ r\\unbroiledH')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['dugong', 'cryptodiran', 'coll', 'staurolatry', 'allthing', 'cheatrie', 'inexpedient', 'ritelessness', 'blastoporal'])
          >>> ab('zinexpediEntV Nritele/ssnessA schizocarp PblAsToporal unluxurious')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['quodlibetic', 'previdence', 'nonviscous', 'reduplicatively', 'arterioverter', 'discrepation'])
          >>> ab('Upr)eviDEnce unvigilant discrepatIon arterioverteR UreduplicativelyE OdiscrEpation di~scRepaTion nonviscous arterioverter')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['semipervious', 'cactoid', 'quadrialate', 'preflattery', 'emancipation', 'recedent'])
          >>> ab('eema@nciPation{T holochroal recedent chewstick cac,t_oid h\\semipervi@Ous cac&toid eManciPatIonb Urece]denTn')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['puboprostatic', 'tumescent', 'keraunograph', 'telecaster', 'selenigenous', 'phycomycete', 'executrix'])
          >>> ab("plastidular tUmesC]ent selen'igenousE tumescent selen<igE;nOuS")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unsculptured', 'quagginess', 'indisputableness', 'breastrope'])
          >>> ab('uNSculp:tureDy IBreastrope FindispuTaBlenessz nbreastr]opea nubile')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['intraperitoneally'])
          >>> ab('leader shipbreaking nondidactic intraperitoneally intraperitOneallyh PIntraperito$neAllY sorgho Intraperi,toneallyp clerklike')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['siscowet', 'nevo', 'driftweed', 'chevronelly', 'victoryless', 'illustrations', 'figent'])
          >>> ab('VFigentU uncommemorated cinchotine viceroy Odriftweed figen!ts zvictorylessQ Dillustrations')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['holland', 'nursedom', 'epidictical', 'defortify', 'taraf'])
          >>> ab('stomatal vep,iDIctica`l n]urS~eDom PepidICtic/a"lx defortify')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['vegasite'])
          >>> ab('vegaSitec vegasiteI forwarder drumheads Sveg<asiteT tannalbin')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['tularemia', 'booming', 'retrothyroid', 'decarnate', 'lobbyism', 'playa', 'nonreception', 'amphictyonic', 'antiaesthetic'])
          >>> ab('KtUlaremia Y{=booMing mlobBYIsm Tular?emiai jeremiad')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['metamerically'])
          >>> ab('slopingness quidnunc priggish nonimpartment drillmaster entreaty nucleiform unimprovableness')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['scrofulism', 'missile', 'tillot', 'douser', 'twankingly', 'eccentrate', 'cacoglossia', 'miss'])
          >>> ab("seccentrAteO dcaCoglossiaF C$acoglossi'AA cacoglossia galera")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['encourager'])
          >>> ab('stratagemical sizableness schnabel encouragerl mythopoeist EncOuragerD')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unambiguously', 'standing', 'cameroon', 'unpretendingly', 'puppydom'])
          >>> ab('mousekin unambiguousl*y standing unAmbigUously fpUppyDoma')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['megascleric', 'devisable'])
          >>> ab('nephrorrhaphy cactiform loaferdom Umegascleric dividing Tmegas`cleric readoption devisableH')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['cardioarterial', 'statolatry', 'bossism'])
          >>> ab('intercounty ost$atolaT)ry statolatrym Tbos(sisMm unsignatured brunch ZcardioArterialF')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['dextrousness', 'whirley', 'coldly', 'compendiary', 'grovel'])
          >>> ab('pseudoglioma co@ldlyt N<dEXtrous@nEss dextrousnessx coetaneously hydroelectricity abstruse')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['plowfoot', 'caducicorn', 'monociliated'])
          >>> ab("sp'lowfOot ploW&fO.oT -{ploWfootL monOciliaTedp yplowfootA")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['plash', 'unbraceleted', 'runner', 'nickeline', 'cellulous', 'interlocutorily', 'ophthalmodynia', 'unthrone'])
          >>> ab('aophthalmodyn`i|a Wun.bRa.celEtedz nIckeline{g cunbrac<eletedY uNthroneX')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['sulphurage', 'audibility', 'deuteride', 'mimiambic', 'isoimmunity', 'rhinopharynx', 'refractively', 'nonseizure'])
          >>> ab('i~soimmUniTy no}nseizure\\ gi"soimmunitY nonseizure bastionary usulph<u}raGet InonseIzur}ez imimiamb+ic odeuTeride')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['whitecapper', 'uncontestable', 'millage', 'unbudging', 'hydrostatic', 'enterospasm', 'ectypography', 'eulamellibranch'])
          >>> ab('HydrostaticH IuncoNtestablE=R renverse millagEt fascicle')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['remissful', 'inyoite'])
          >>> ab('waterlogged subpeduncle warriorhood Riny@oit,e wremis]sfUlm')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['microbiological', 'ruddy', 'gobble', 'pozzuolana', 'adscript', 'ossypite'])
          >>> ab('superadmiration ossypite nossy$pite adsCriptZ %gobble% pozzuolanau untempted')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['chromophilic', 'brabant', 'detailed', 'exulcerative', 'artillery', 'tachylytic', 'sinnable', 'clival'])
          >>> ab('ITac/hylytic snavvle Jchro%moPhili<cJ boundedly artil{lery treacherousness Fsi@~nnablEh')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['bounteousness', 'unimperious', 'twixt', 'benzolize', 'ebenaceous', 'buncal', 'cladoptosis', 'archvampire', 'palaeontographical'])
          >>> ab('polariscopy unimperIousH cLa]dop&tosisk Pbenz]oli>ze frigatoon EebEnaceousw Barchvampire floorer')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['impedient', 'allochiral', 'hear', 'snur', 'myosarcomatous', 'dichlorohydrin'])
          >>> ab('shakefork kh<ea$rq bromine ldichlor$ohydrIN snU,rb qhea|r sN-urX dhe>{Ar rdIchlorohydrin')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['sulphurproof', 'studiedly'])
          >>> ab('solifluctional knowledgeably Hsulphurproof denationalization studiedly polyphyletic')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['zygosporophore'])
          >>> ab('metrosteresis malconduct married semiform gangling szygoSporOpho,rek underdraft')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['detinet'])
          >>> ab('omnigerent alastrim acetosalicylic intersperse detinet macrocyst pathogermic')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['monarchize', 'prankster', 'egomaniacal', 'deediness', 'cheeser', 'cumulation', 'endorsee', 'quinometry'])
          >>> ab('jMon.archizeF ]egoManiacalW leucoplastid cumulatioNw localizable')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['varicosed', 'ventilator'])
          >>> ab('eventIlatorN Cvaricosedd reask ventil]atorb filiform Lvaricosed queak resinol')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['ultradolichocephalic', 'kinetophone', 'supernaturalness'])
          >>> ab('mesepithelial zkinetophone Oultra@Dolichocephalic ultrAdoLichocephaLicS tendant')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['somatoplasm'])
          >>> ab('heartlet JsomAtoplasmT somatoplasm jigginess xanthophane wader tuttiman diabrosis')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['trackback'])
          >>> ab('protiston asimmer vtraCkb-aCk imported trackback')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['payable', 'jaunt', 'oleostearin', 'stitching'])
          >>> ab('payablez feignedness kjaunt IstitchiNgO sti<tchin/gV')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['oscillatory', 'geophyte', 'menthenone'])
          >>> ab('Men*tH:enoney menthenone stalagmite conductometric assorter bardic')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['stookie', 'withsave', 'subchoroid', 'briefing', 'upbelch', 'plessimetric'])
          >>> ab('filterableness KsubchoRoid StookieN bri[efingH hornyhead dragonlike')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['battlewise', 'dare'])
          >>> ab('sulphanilic chondrosis dar<e FDare Ab}attlewi+seb')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['muscoid', 'reliquidation', 'broad', 'tugging', 'retardant', 'preadequately'])
          >>> ab('retarDAnt _muscoi+DY preaDEquAtely tugging disarticulation')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hexatomic', 'trophobiosis', 'parascenium', 'gibbet', 'laser'])
          >>> ab('fideism trophobIosis gib{be$t OGibbetP giBbet nonperjury l|ase~r evincement philoxygenous')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['incommensurable'])
          >>> ab('electroluminescence savanilla gastropleuritis telescope infectionist beetleheaded uncrude laryngograph')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['unexcusableness', 'bismuthyl', 'adapt'])
          >>> ab('undittoed bipennated ton EAdapt bismUthylo TuNexcusableness trisomy')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['intransigency', 'improperly', 'angiophorous'])
          >>> ab('haploid EangiophoroUsu firetrap tonlet SangiophOrouss imPro(Pe-rLyW Angiopho"rouss pintransigency dedimus')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['penceless', 'bromothymol', 'reticuloramose', 'pseudonymuncule'])
          >>> ab('ebromothYmOlj unliteral BromothyMolT pseudOnymuncule aerage pancratical vpe#nce$lEss pseudonyMunculE')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['beshag', 'monument', 'appressor', 'tutu', 'gentilize'])
          >>> ab('northwestward ebeshagb monUmen@>tz sbeshA+g] qtuT<u@ mo=num#enth semiresolute')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['uncivilized', 'pairer', 'keratonyxis', 'chemitypy', 'checkroll', 'hymnographer', 'tootler', 'perithelium', 'monodelph'])
          >>> ab('stoccata ZpeRitheliUmP tooTlerA hcHeckroLl k&eraTonyx$isB Hmonodelphn')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['confidentiality', 'inclementness', 'plicator'])
          >>> ab('dejectory xplicatoR` CConfid(entiAlity (p{licatorm qpliCatorn hincleMenTness pliCa*to;r plicator oinclemENtness')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['sardius', 'tailings'])
          >>> ab('protect ks-ardiusI dTaIlingsr bush CsardiusA sardiusK myxemia moroseness')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['bescorch', 'rodding', 'disawa', 'gastradenitis', 'cottabus', 'prescapularis', 'revaporization'])
          >>> ab('sulfocyan expressionlessly rbes@cor;chx bescorch prEscapularisd r~odding- prescAPularis disawa rOddingB')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['transmundane', 'macintosh'])
          >>> ab('stransMundaneM dir athetoid prelectress transm]undanet unquarrelsome exsanguine Macinto}sho wtran&smundane')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['dualistic', 'becense', 'hyperingenuity', 'pulpalgia', 'gummose'])
          >>> ab('TgumMos#e Ygumm+?osE neuropore seconds YdualisticF tomin tgummosex')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['tentacle', 'nonrestitution', 'interventional', 'demiditone', 'chrysophilite', 'idiosyncratically', 'teosinte'])
          >>> ab('^tenTacle pluriparous alluvial wTEoSi.n}te chrysophilite cinereal')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['clique', 'spuriae', 'introspectable', 'pyritology', 'marbleize', 'blooddrop', 'prickingly', 'ecole'])
          >>> ab('gspuriAe c*l%iQue phosphuret sPUriaen blooDdropm lclique &bloo:ddrop blooddrop')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['hiro'])
          >>> ab('untakableness borderlander hiro moviedom atmosphereless')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['disdiaclastic', 'tutoyer', 'fibrilliferous', 'undiscernedly', 'gloomily', 'ternarious', 'riven', 'concamerated'])
          >>> ab("lTe'rna!riousP theophagous disdiaclastic QfIbrillifeRous ternarious micrography GloomilyD")
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['nonfanciful', 'aneuploidy', 'unrubified', 'dynamic', 'twistable', 'mesmerically', 'heyday', 'hipmold', 'epiprecoracoid'])
          >>> ab('thiophenic munrubi_fied lunRubifiedO circumparallelogram xUnrub/ified Ldynam&ic predelinquently')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['prorectorate', 'snappable', 'pholadoid', 'toxicodermatitis', 'gallification', 'survival', 'rakshasa', 'pungey'])
          >>> ab('silly pholadoid snappable h"s\'nappableH R,aKs-hasa nsnappabLeW snapPable Lsnappab_le')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['quadratical', 'principiate', 'archinfamy', 'cacomixle', 'endonuclear', 'writer'])
          >>> ab('Eprincip*iat_eX ;caco[mixlel writ<eRE qUadraticale Ewriter awRiterK endonucle#arN writer Zwrit|er')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['upraisal', 'mechanicalist', 'losing', 'emancipation', 'counterquarterly', 'oppress', 'dishonorable', 'liang', 'weirdly'])
          >>> ab('JmeChANicalIst bLi.an`g preambular exemplifiable SCoun^ter^quaRteRly versed')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['subframe', 'infinitude'])
          >>> ab('P@iNf{IniTude triakisoctahedrid gyroscope underdoing hinfinitude kulang Minfinitude')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['gmbh', 'isocheimal', 'overusually', 'supercargoship', 'contemptuous', 'undrawn', 'catchpollery', 'unfinishedness', 'coolie'])
          >>> ab('unfinishednessA ZGmbh stoneweed ksuper[cargoshi>pw unf*inis)hednessu')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['lazzarone', 'define'])
          >>> ab('coffeegrowing glaz:zaronev coralloidal strombite faky')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['either', 'ungenuine', 'dealable', 'pejorism', 'cointersecting', 'outerly'])
          >>> ab('twal ouTe(rl!yB ungenuinel bianisidine ipeJoRism')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['reinsertion', 'moted', 'narcoanesthesia', 'tanbur', 'sulphamidic', 'monopersulfuric', 'heartsickening', 'talkathon'])
          >>> ab('organoid Kmoted precollege dtalkathOnQ BtalKaThon')
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['yond'])
          >>> ab('refrustrate altered spiderflower N~yond(c yond rectocolonic caner')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ab = about(['randannite', 'overappraise', 'disdiapason', 'unclement', 'cesser', 'repatronize', 'sacerdotalist', 'atelectatic', 'plasma'])
          >>> ab('mat~ElEctatic$ unclement ksacerdot@aliSt saCerdotaliStZ repatronizes rAndanNite}m')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import about
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
