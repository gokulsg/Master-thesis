README for dataset TWITTER-Real-Graph-Partial


=== Usage ===

This folder contains the following comma separated text files 
(replace DS by the name of the dataset):

n = total number of nodes
m = total number of edges
N = number of graphs

(1) 	DS_A.txt (m lines) 
	sparse (block diagonal) adjacency matrix for all graphs,
	each line corresponds to (row, col) resp. (node_id, node_id)

(2) 	DS_graph_indicator.txt (n lines)
	column vector of graph identifiers for all nodes of all graphs,
	the value in the i-th line is the graph_id of the node with node_id i

(3) 	DS_graph_labels.txt (N lines) 
	class labels for all graphs in the dataset,
	the value in the i-th line is the class label of the graph with graph_id i

(4) 	DS_node_labels.txt (n lines)
	column vector of node labels,
	the value in the i-th line corresponds to the node with node_id i

There are OPTIONAL files if the respective information is available:

(5) 	DS_edge_labels.txt (m lines; same size as DS_A_sparse.txt)
	labels for the edges in DS_A_sparse.txt 

(6) 	DS_edge_attributes.txt (m lines; same size as DS_A.txt)
	attributes for the edges in DS_A.txt 

(7) 	DS_node_attributes.txt (n lines) 
	matrix of node attributes,
	the comma seperated values in the i-th line is the attribute vector of the node with node_id i

(8) 	DS_graph_attributes.txt (N lines) 
	regression values for all graphs in the dataset,
	the value in the i-th line is the attribute of the graph with graph_id i


=== Node Label Conversion === 


Node labels were converted to integer values using this map:

Component 0:
	0	apple
	1	store
	2	buy
	3	mac
	4	move
	5	dad
	6	butter
	7	peanut
	8	fan
	9	laker
	10	die
	11	tummy
	12	hurt
	13	feel
	14	museum
	15	night
	16	rest
	17	day
	18	book
	19	mention
	20	dont
	21	follow
	22	reply
	23	sunday
	24	haha
	25	realize
	26	life
	27	people
	28	guess
	29	matter
	30	reach
	31	hope
	32	gonna
	33	time
	34	decide
	35	watch
	36	bed
	37	house
	38	home
	39	walk
	40	run
	41	dog
	42	call
	43	wake
	44	xoxo
	45	hey
	46	wait
	47	bus
	48	water
	49	yesterday
	50	laugh
	51	fight
	52	fun
	53	school
	54	bit
	55	birthday
	56	share
	57	hate
	58	front
	59	tip
	60	lady
	61	tonight
	62	game
	63	play
	64	sleep
	65	sim
	66	wont
	67	iphone
	68	lol
	69	cos
	70	bye
	71	party
	72	grad
	73	tomorrow
	74	news
	75	god
	76	hear
	77	wow
	78	stuff
	79	luck
	80	lot
	81	care
	82	clothes
	83	wear
	84	coffee
	85	break
	86	series
	87	love
	88	cover
	89	http
	90	friday
	91	friend
	92	charge
	93	battery
	94	phone
	95	cell
	96	drink
	97	tweet
	98	sound
	99	flu
	100	kid
	101	stay
	102	exam
	103	update
	104	shit
	105	happen
	106	reason
	107	piss
	108	alarm
	109	drive
	110	body
	111	start
	112	sit
	113	finish
	114	sister
	115	talk
	116	yeah
	117	meet
	118	dream
	119	cry
	120	lie
	121	shower
	122	shop
	123	shirt
	124	post
	125	message
	126	yay
	127	week
	128	month
	129	july
	130	june
	131	hahaha
	132	movie
	133	business
	134	live
	135	king
	136	bore
	137	understand
	138	stop
	139	spend
	140	bout
	141	morning
	142	church
	143	brother
	144	concert
	145	jona
	146	leave
	147	miss
	148	guy
	149	tour
	150	band
	151	cut
	152	twitter
	153	block
	154	learn
	155	deprive
	156	hour
	157	math
	158	nap
	159	homework
	160	soo
	161	read
	162	wanna
	163	thursday
	164	txt
	165	weekend
	166	ticket
	167	trip
	168	save
	169	send
	170	fuck
	171	eat
	172	google
	173	search
	174	text
	175	hero
	176	mama
	177	download
	178	file
	179	fall
	180	bear
	181	midnight
	182	enjoy
	183	laptop
	184	fix
	185	internet
	186	join
	187	gain
	188	lose
	189	win
	190	follower
	191	family
	192	son
	193	folk
	194	cuz
	195	baby
	196	omg
	197	hehe
	198	rain
	199	coz
	200	bug
	201	class
	202	chat
	203	change
	204	info
	205	app
	206	song
	207	dinner
	208	starbuck
	209	ive
	210	facebook
	211	ugh
	212	addict
	213	roll
	214	girl
	215	hair
	216	couch
	217	mom
	218	pay
	219	vip
	220	add
	221	train
	222	england
	223	tune
	224	date
	225	orlando
	226	pick
	227	suck
	228	stick
	229	test
	230	job
	231	interview
	232	damn
	233	throw
	234	mtv
	235	award
	236	plan
	237	answer
	238	question
	239	site
	240	ride
	241	twurl
	242	watchin
	243	pass
	244	dvd
	245	afternoon
	246	weather
	247	leg
	248	summer
	249	check
	250	def
	251	eye
	252	head
	253	headache
	254	car
	255	kick
	256	lake
	257	remember
	258	camp
	259	island
	260	choice
	261	vote
	262	gotta
	263	tom
	264	waste
	265	germany
	266	til
	267	speak
	268	sport
	269	bitch
	270	mess
	271	notice
	272	goin
	273	mine
	274	mark
	275	road
	276	write
	277	throat
	278	ball
	279	sell
	280	plant
	281	close
	282	dress
	283	chocolate
	284	milk
	285	visit
	286	boyfriend
	287	couple
	288	nite
	289	breakfast
	290	spa
	291	gym
	292	money
	293	sun
	294	catch
	295	shine
	296	office
	297	worth
	298	cook
	299	vacation
	300	project
	301	beat
	302	blog
	303	fit
	304	schedule
	305	hotel
	306	father
	307	exercise
	308	ruin
	309	pack
	310	account
	311	upload
	312	mail
	313	youtube
	314	pool
	315	email
	316	picture
	317	wine
	318	box
	319	seat
	320	myloc
	321	season
	322	tho
	323	thinking
	324	city
	325	cross
	326	finger
	327	race
	328	lay
	329	page
	330	peep
	331	fave
	332	bring
	333	world
	334	bike
	335	album
	336	jonasbrothers
	337	create
	338	version
	339	sing
	340	kiss
	341	burger
	342	taste
	343	reading
	344	yep
	345	waffle
	346	bet
	347	donniewahlberg
	348	word
	349	spread
	350	aww
	351	pic
	352	computer
	353	remind
	354	lil
	355	sandwich
	356	pasta
	357	memory
	358	video
	359	mother
	360	crap
	361	hang
	362	fam
	363	sunshine
	364	forget
	365	window
	366	smile
	367	ton
	368	awww
	369	shopping
	370	food
	371	ass
	372	pain
	373	york
	374	woohoo
	375	boo
	376	atm
	377	hmm
	378	act
	379	suppose
	380	blip
	381	angel
	382	art
	383	idea
	384	sign
	385	blackberry
	386	marry
	387	bank
	388	holiday
	389	force
	390	accident
	391	xxx
	392	yea
	393	moon
	394	drop
	395	trailer
	396	excite
	397	listen
	398	round
	399	joe
	400	followfriday
	401	kevin
	402	dancing
	403	weight
	404	swim
	405	kill
	406	mind
	407	person
	408	half
	409	ahhh
	410	park
	411	fly
	412	cleaning
	413	tomfelton
	414	size
	415	star
	416	trek
	417	gettin
	418	club
	419	tired
	420	youre
	421	gosh
	422	training
	423	rock
	424	science
	425	grandma
	426	assignment
	427	fish
	428	chip
	429	errand
	430	grocery
	431	knee
	432	website
	433	ppl
	434	wedding
	435	agree
	436	conan
	437	minute
	438	leno
	439	hell
	440	station
	441	event
	442	brand
	443	lunch
	444	rice
	445	wius
	446	xbox
	447	cup
	448	stanley
	449	feeling
	450	marathon
	451	universe
	452	list
	453	story
	454	theme
	455	pop
	456	bottle
	457	touch
	458	support
	459	babe
	460	fail
	461	cool
	462	continue
	463	connection
	464	mileycyrus
	465	chance
	466	blah
	467	sooo
	468	mum
	469	relaxing
	470	mitchelmusso
	471	mitchel
	472	joke
	473	airport
	474	packing
	475	didnt
	476	confuse
	477	hospital
	478	theater
	479	town
	480	chapter
	481	revise
	482	type
	483	rent
	484	film
	485	team
	486	challenge
	487	step
	488	dawn
	489	ipod
	490	tea
	491	manage
	492	london
	493	deal
	494	boy
	495	kinda
	496	fav
	497	flight
	498	france
	499	air
	500	monday
	501	swift
	502	taylor
	503	episode
	504	grow
	505	twilight
	506	nose
	507	tweeter
	508	blow
	509	music
	510	votetom
	511	hit
	512	foot
	513	wave
	514	miley
	515	btw
	516	link
	517	travel
	518	jay
	519	heart
	520	david
	521	daddy
	522	glass
	523	grade
	524	memorial
	525	bday
	526	celebrate
	527	review
	528	peace
	529	chill
	530	guitar
	531	singing
	532	count
	533	cream
	534	ice
	535	myspace
	536	nightmare
	537	stomach
	538	promise
	539	beach
	540	sense
	541	humor
	542	tan
	543	pie
	544	mmm
	545	evening
	546	background
	547	ohh
	548	match
	549	plz
	550	bbq
	551	invite
	552	tuesday
	553	inspire
	554	company
	555	track
	556	wife
	557	saturday
	558	salad
	559	hmmm
	560	land
	561	jonathanrknight
	562	hill
	563	ring
	564	macbook
	565	pro
	566	driver
	567	row
	568	toy
	569	board
	570	plane
	571	hug
	572	luv
	573	article
	574	mood
	575	cousin
	576	epic
	577	swine
	578	coast
	579	west
	580	bath
	581	pizza
	582	degree
	583	spring
	584	ear
	585	infection
	586	build
	587	middle
	588	figure
	589	hold
	590	drinking
	591	radio
	592	dude
	593	pray
	594	hangover
	595	trend
	596	topic
	597	allergy
	598	photo
	599	wasnt
	600	student
	601	college
	602	wind
	603	jump
	604	arm
	605	umbrella
	606	dance
	607	tooth
	608	dentist
	609	bar
	610	button
	611	press
	612	sigh
	613	offer
	614	junk
	615	msg
	616	carradine
	617	pour
	618	wash
	619	football
	620	meeting
	621	channel
	622	note
	623	nut
	624	sam
	625	cake
	626	butt
	627	shift
	628	daughter
	629	poem
	630	crack
	631	drag
	632	woot
	633	laundry
	634	finale
	635	field
	636	comment
	637	bgt
	638	feed
	639	blast
	640	picnic
	641	unus
	642	country
	643	worry
	644	space
	645	lautner
	646	archuleta
	647	wtf
	648	morrow
	649	diversity
	650	burn
	651	mix
	652	cancel
	653	woman
	654	jason
	655	mraz
	656	chicken
	657	flickr
	658	design
	659	ignore
	660	thunder
	661	storm
	662	freak
	663	bill
	664	bean
	665	sort
	666	parent
	667	shoot
	668	hockey
	669	prob
	670	contact
	671	machine
	672	nephew
	673	vid
	674	cli
	675	chick
	676	puppy
	677	furniture
	678	ustre
	679	issue
	680	ddlovato
	681	moment
	682	aim
	683	tire
	684	prison
	685	load
	686	texa
	687	mouth
	688	shut
	689	click
	690	spam
	691	desk
	692	cat
	693	bag
	694	log
	695	experience
	696	street
	697	swear
	698	teacher
	699	joeymcintyre
	700	ache
	701	crush
	702	bite
	703	dnt
	704	hav
	705	voice
	706	afford
	707	idk
	708	prepare
	709	hand
	710	ahaha
	711	fill
	712	sale
	713	yard
	714	beer
	715	husband
	716	chuck
	717	apartment
	718	doesnt
	719	gunna
	720	media
	721	lesson
	722	choose
	723	imma
	724	tha
	725	sprint
	726	nkotb
	727	mon
	728	online
	729	streaming
	730	record
	731	pants
	732	amazon
	733	hahah
	734	advertisement
	735	clean
	736	cheese
	737	parking
	738	isnt
	739	wat
	740	aint
	741	wit
	742	child
	743	scare
	744	screen
	745	surprise
	746	wing
	747	nyc
	748	traffic
	749	woo
	750	hoo
	751	energy
	752	bak
	753	palm
	754	goodnight
	755	mario
	756	aunt
	757	diet
	758	line
	759	ebay
	760	apprentice
	761	service
	762	wee
	763	garden
	764	smell
	765	net
	766	contest
	767	relax
	768	buddah
	769	twitterverse
	770	cancer
	771	client
	772	jam
	773	shoe
	774	exhaust
	775	bing
	776	view
	777	thx
	778	chillin
	779	top
	780	bunch
	781	blame
	782	wknd
	783	tennis
	784	age
	785	umm
	786	leon
	787	anniversary
	788	singer
	789	hat
	790	chair
	791	floor
	792	bro
	793	mile
	794	session
	795	profile
	796	demon
	797	baseball
	798	boom
	799	pow
	800	shot
	801	return
	802	sex
	803	tear
	804	shorts
	805	gift
	806	fml
	807	bother
	808	cav
	809	lebron
	810	kobe
	811	stand
	812	huh
	813	cyrus
	814	alot
	815	mornin
	816	havin
	817	brighten
	818	jesus
	819	piece
	820	grrr
	821	chemistry
	822	cereal
	823	web
	824	egg
	825	itune
	826	war
	827	goodness
	828	hun
	829	tweep
	830	gig
	831	loss
	832	wisdom
	833	wednesday
	834	buddy
	835	bird
	836	pull
	837	idol
	838	card
	839	prayer
	840	msn
	841	donut
	842	doubt
	843	mall
	844	lottery
	845	uncle
	846	graduation
	847	harry
	848	australia
	849	gossip
	850	tree
	851	efron
	852	zac
	853	dye
	854	power
	855	earn
	856	door
	857	talent
	858	britain
	859	soccer
	860	spain
	861	honey
	862	adam
	863	color
	864	shame
	865	rise
	866	doin
	867	lookin
	868	yall
	869	meal
	870	bless
	871	mommy
	872	feelin
	873	dat
	874	center
	875	essay
	876	horse
	877	arrive
	878	light
	879	boyle
	880	susan
	881	deserve
	882	twit
	883	shake
	884	yum
	885	copy
	886	sum
	887	lmfao
	888	replay
	889	selly
	890	beg
	891	selenagomez
	892	haircut
	893	snuggle
	894	mypict
	895	cloud
	896	stair
	897	festival
	898	release
	899	nature
	900	fire
	901	frus
	902	jus
	903	access
	904	camera
	905	pump
	906	feedback
	907	paint
	908	jon
	909	bff
	910	lack
	911	swimming
	912	freakin
	913	nick
	914	hannah
	915	cnt
	916	antonio
	917	san
	918	sky
	919	davidarchie
	920	hop
	921	hip
	922	momma
	923	nigga
	924	workout
	925	john
	926	bake
	927	receive
	928	fax
	929	nighter
	930	mate
	931	congrat
	932	edward
	933	bellum
	934	kristen
	935	stewartkris
	936	communicate
	937	hahahaha
	938	treat
	939	draw
	940	crash
	941	suit
	942	respond
	943	rumor
	944	metro
	945	expect
	946	zoo
	947	teach
	948	californium
	949	delay
	950	recital
	951	golf
	952	fault
	953	price
	954	stage
	955	credit
	956	charger
	957	prize
	958	pen
	959	yup
	960	terminator
	961	trust
	962	pleasure
	963	musso
	964	customer
	965	prom
	966	attention
	967	eating
	968	sunburn
	969	skin
	970	disney
	971	forecast
	972	practice
	973	flick
	974	cheer
	975	jack
	976	hubby
	977	hehehe
	978	demus
	979	myfax
	980	hassle
	981	handle
	982	toast
	983	sonny
	984	brush
	985	vine
	986	market
	987	amount
	988	basketball
	989	begin
	990	winter
	991	living
	992	curl
	993	shareholder
	994	dividend
	995	asia
	996	recommend
	997	insomnia
	998	sneak
	999	federer
	1000	atl
	1001	spider
	1002	complain
	1003	lyric
	1004	diego
	1005	tweetdeck
	1006	blood
	1007	august
	1008	server
	1009	lvatt
	1010	kno
	1011	sack
	1012	november
	1013	migraine
	1014	australium
	1015	bell
	1016	taco
	1017	allen
	1018	kris
	1019	attack
	1020	studio
	1021	zone
	1022	playing
	1023	tht
	1024	stress
	1025	address
	1026	havent
	1027	skye
	1028	planet
	1029	heidimontag
	1030	kitty
	1031	dish
	1032	shout
	1033	chicago
	1034	request
	1035	hurry
	1036	paste
	1037	nail
	1038	skool
	1039	ima
	1040	jeans
	1041	push
	1042	daisy
	1043	talkin
	1044	perform
	1045	cable
	1046	salon
	1047	law
	1048	neck
	1049	kate
	1050	pixar
	1051	lauren
	1052	noon
	1053	lord
	1054	nbc
	1055	scene
	1056	graduate
	1057	potter
	1058	bread
	1059	ahh
	1060	suffer
	1061	greet
	1062	goodbye
	1063	francisco
	1064	nxt
	1065	nba
	1066	ttyl
	1067	delete
	1068	killer
	1069	hide
	1070	respect
	1071	preview
	1072	chri
	1073	imagine
	1074	american
	1075	hole
	1076	vega
	1077	depress
	1078	doctor
	1079	nah
	1080	loved
	1081	mosquito
	1082	bbc
	1083	player
	1084	death
	1085	cough
	1086	inspiration
	1087	history
	1088	term
	1089	jordanknight
	1090	relay
	1091	fever
	1092	crawl
	1093	clock
	1094	spear
	1095	britney
	1096	flower
	1097	matt
	1098	heat
	1099	bnp
	1100	workin
	1101	lag
	1102	jet
	1103	skip
	1104	steal
	1105	pound
	1106	smh
	1107	rob
	1108	trouble
	1109	ooh
	1110	youuu
	1111	woop
	1112	niece
	1113	cartoon
	1114	ace
	1115	anqju
	1116	retweeting
	1117	heel
	1118	tryna
	1119	status
	1120	competition
	1121	farmer
	1122	outta
	1123	pattinson
	1124	robert
	1125	quality
	1126	praise
	1127	vibes
	1128	softball
	1129	cookie
	1130	wrk
	1131	muscle
	1132	difference
	1133	joy
	1134	knock
	1135	lovato
	1136	pari
	1137	boss
	1138	lambert
	1139	blister
	1140	pair
	1141	code
	1142	tool
	1143	bone
	1144	wolverine
	1145	engine
	1146	spell
	1147	cold
	1148	vet
	1149	stoke
	1150	beginning
	1151	wrap
	1152	repeat
	1153	electro
	1154	suggest
	1155	promote
	1156	toe
	1157	polish
	1158	ashley
	1159	csus
	1160	motorcycle
	1161	piano
	1162	bee
	1163	sting
	1164	tmrw
	1165	bathing
	1166	rip
	1167	donnie
	1168	soup
	1169	spot
	1170	wall
	1171	scream
	1172	fran
	1173	enter
	1174	illusion
	1175	ariel
	1176	report
	1177	shuffle
	1178	philippine
	1179	ouch
	1180	mistake
	1181	quote
	1182	vista
	1183	forum
	1184	library
	1185	depot
	1186	earth
	1187	revision
	1188	spending
	1189	grass
	1190	jerry
	1191	ben
	1192	attempt
	1193	drama
	1194	gaga
	1195	stewart
	1196	neighbor
	1197	soooo
	1198	duty
	1199	key
	1200	bowl
	1201	celeb
	1202	wud
	1203	fruit
	1204	jone
	1205	loser
	1206	america
	1207	tetris
	1208	wen
	1209	pet
	1210	hook
	1211	rerun
	1212	garage
	1213	bark
	1214	hater
	1215	blessing
	1216	brain
	1217	dvr
	1218	straighten
	1219	hulu
	1220	tix
	1221	table
	1222	jacob
	1223	tax
	1224	reality
	1225	guinea
	1226	pig
	1227	bum
	1228	score
	1229	puerto
	1230	rico
	1231	lawn
	1232	mow
	1233	sheet
	1234	health
	1235	drum
	1236	option
	1237	fool
	1238	heck
	1239	youu
	1240	editing
	1241	wap
	1242	flatley
	1243	stavro
	1244	install
	1245	yeh
	1246	letter
	1247	ashleytisdale
	1248	lightning
	1249	florida
	1250	meat
	1251	premiere
	1252	entry
	1253	hack
	1254	danny
	1255	awwww
	1256	wht
	1257	explode
	1258	yoga
	1259	abt
	1260	carry
	1261	pill
	1262	host
	1263	roller
	1264	coaster
	1265	sweetie
	1266	plenty
	1267	coke
	1268	sea
	1269	blink
	1270	shoulder
	1271	virus
	1272	dollar
	1273	tgif
	1274	makeup
	1275	layin
	1276	jose
	1277	grind
	1278	voting
	1279	queen
	1280	freedom
	1281	boat
	1282	aha
	1283	gomez
	1284	selena
	1285	hol
	1286	hawkcam
	1287	attend
	1288	doughnut
	1289	annoy
	1290	oil
	1291	robbin
	1292	fulfillment
	1293	contribution
	1294	clip
	1295	magic
	1296	podcast
	1297	hut
	1298	tryin
	1299	title
	1300	goodmorning
	1301	conference
	1302	surgery
	1303	focus
	1304	canada
	1305	rite
	1306	xxxx
	1307	brazil
	1308	survive
	1309	gut
	1310	gas
	1311	pulse
	1312	potential
	1313	truck
	1314	soak
	1315	passenger
	1316	horror
	1317	saga
	1318	katy
	1319	perry
	1320	connect
	1321	style
	1322	giveaway

=== References ===
https://github.com/shiruipan/graph_datasets/tree/master/Graph_Repository

=== Previous Use of the Dataset ===
Shirui Pan, Jia Wu, and Xingquan Zhu “CogBoost: Boosting for Fast Cost-sensitive Graph Classification",  IEEE Transactions on Knowledge and Data Engineering (TKDE),  27(11): 2933-2946 (2015)

Shirui Pan, Jia Wu, Xingquan Zhu, and Chengqi Zhang, “Graph Ensemble Boosting for Imbalanced Noisy Graph Stream Classification",  IEEE Transactions on Cybernetics (TCYB), 45(5): 940-954 (2015)
