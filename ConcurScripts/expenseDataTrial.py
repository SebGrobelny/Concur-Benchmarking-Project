# coding=utf-8
class expense_data:
	
	amount_max = 2000
	amount_min = 100

	record_max=100000
	record_min=0

	department_max=4
	department_min=0

	hotel_max=224
	hotel_min=0

	# hotel_max = 2
	# hotel_min = 0

	airline_max = 37
	airline_min = 0

	carRental_max = 13
	carRental_min = 0 

	location_max = 18
	location_min = 0

	expense_max = 3
	expense_min = 0

	employee_max = 5
	employee_min = 0

	industry_max = 15
	industry_min = 0

	company_max = 2
	company_min = 0

	#37
	#make a hashtable pertaining to airlines and have the hash be ticket id
	airlineList = ['Aer Lingus',' Aero Mexico',' Air Canada',' Air France',' Air New Zealand',' AirTran Airways',' Alaska Airlines',' Alitalia',' Alitalia Airlines',' America West',' American Airlines',' British Airways',' British Midland',' Continental Airlines',' Delta Air Lines',' Frontier Airlines',' Horizon Air',' JAL',' JetBlue',' Lufthansa',' Northwest Airlines',' Northwest Airlines Inc. / KLM',' Qantas',' Reno Airlines',' Ryan Air',' Sabena',' SAS',' Saudi Arabian Airlines',' Singapore Airlines',' SkyJet',' Southwest Airlines',' Swiss Air',' Trans World Airlines',' U.S. Airways',' United Airlines',' Virgin',' WestJet'];
	#penton attribute 
	airClass= ['First','Business','Economy'] ;
	airCraftCapacity = ['0']

	# 224
	# make a hashtable pertaining to hotels and have the hash be reservation no.
	hotelList = ['A.H.M.I. Hotels','All Suites International',' Allegro Resdorts',' Allstar Hotels','Alp\'Azur Hotels',' Alpine Classics Private Hotels',' Althoff Hotels',' Amari Hotels',' AmeriHost Inn',' Amsterdam Hotels Org.',' Arcantis','Ashley House','Astotel\'Astron Hotels','Ata Hotels','Atlas Hotels','Atlas Hotels Israel','Bali1 Bali Hotels','Bali1 Hotels','Bali1 Kuta Hotels','Bali1 Nusa Dua & Benoa Hotels','Bali1 Sanur Hotels','Balldins','Bally\'s','Barcelo Hotels','Best Western International','Bettoja Hotels','Bilderberg','Bleu Marine','Bonaparte Hotel Group','Bristol Hotels and Resorts','Cadena Hotelera Asturiana','Caesar Resort Hotels','Caesars','Camberley Hotel Company','Camino Real Hotels & Resorts','Campanile','Canadian Pacific Hotels','Candlewood Suites','Century Plaza Hotels & Suites','Chase Suite Hotels','Châteaux & Hôtels de Charme','Choice Hotels International','Choice Hotels Ireland','Citadines Apart\'Hotel','City & Country Line Hotels','Clarine','Clarion Hotels','Climat de France','Club Med','Coast and Country Hotels','Coast Hotels and Resorts','Coastal Inns','Comfort Inns','Concorde Hotels','Concorde Hotels and Resorts','Consort Hotels','Consul Hotels','Copthorne Hotels','Coralia Hotels','Countryside Hotels','Courtyards','Crowne Plaza','Dan Hotels','Dansk-Kroferie Hotels','Days Inn','Delta','Derby Hotels','Dorint Hotels','DoubleTree Hotels','Drury Inn & Suites','Dusit Group','Dynasty Suites Hotels','Econo Lodge','Edda Hotels','Elegant Resorts','Embassy Suites','Etap Hotel','Executive Inns & Suites','Fairfield Inns','Fasthotel','FDR Holidays','Felix Hotels & Resorts','Firmdale Hotels','Flair Hotels','Formule1','Forte Hotels','Fountainhead Hotels','Four Points Hotels by Sheraton','Four Seasons','Friendship Inns','Furama Hotels','Geat Hotels Group Venice','Global Home Network',' Inc','Golden Leaf Hotels & Residences','Golden Tulip','Grand Heritage','Great Southern Hotels','Groupe Lucien Barrière','Gruppo Pancioli','Hampton Inn & Suites','Hampton Inns','Hankyu Group','Harrah\'s',' Hawthorn Suites',' Helnan International Hotels',' Heritage Hotels (India)',' Hilton Hotels',' Holiday Inn',' Hoteles Catalonia',' Howard Johnsons',' Hyatt Hotels',' Keells Hotels',' Kempinski Hotels',' Kibbutz Hotels Chain',' Killarney Hotels Ltd',' Knights Inn',' La Quinta',' Le Meridien Hotels',' Leading Hotels of the World',' Lee Hotels',' Les Jardins de Paris',' Loews Hotels',' Maksu Group of Hotels',' Mandarin Oriental',' Manhattan East Suite Hotels',' Manor Houses - Portugal',' Maritim Hotels',' Marriott Hotels',' McMillan Lux. Hotels',' Med Playa Hotels',' Mercure Hotels',' Metro Inns',' Microtel Inns',' Millenium Hotels',' Milner Hotels',' Minotel',' Motel 6',' Mövenpick',' Naco Hotels',' New Hotel',' Novotel','Nuit d\'Hotel',' Oasis Hotels',' Oberoi Hotels',' Omni Hotels',' Orient-Express Hotels',' Pan Pacific Hotels',' Pannonia Hotels',' Paris Honotel',' Park Plaza International',' Pearl Resorts',' Peninsula Group',' Peru Hotel',' Pestana Hotels',' Phoenix Inn',' Première Classe',' Prima Hotels',' Primotel',' Prince Hotels',' Protea Hotels',' Quality Inns',' Radisson Hotels & Resorts',' Ramada',' Red Roof Inns',' Regal Hotels International',' Regent International',' Relais & Chateaux',' Remmen Hotels',' Renaissance',' Residence Inns',' Ringhotels',' Ritz-Carlton',' Rodd Hotels & Resorts',' Rodeway Inns',' Romantik Hotels',' Rosewood Hotels & Resorts',' RRR Hotels',' Rydges Hotels and Resorts','Scotland\'s Personal Hotels',' Sedona Hotels International',' Settle Inn',' Shangri-La',' Sheraton',' Shilo Inns','Shoney\'s Inns',' Sierra Suites',' Silencehotels Austria',' Silencehotels Netherlands',' Silken Hotels',' Sinnott Hotels',' Sleep Inns',' Sofitel',' Sokos Hotels',' Sol Meliá',' Solitaire Aparthotels',' Sorat hotels',' South Seas Resorts',' Sovereign Hotels',' Stakis Hotels',' Starwood Hotels & Resorts',' Staybridge Suites',' Steigenberger Hotels',' StudioPLUS',' Summerfield Suites',' Summit Hotels & resorts',' Super 8 Motels',' Swiss International Hotels',' Thalassa Hotels',' TOP International Hotels',' Travelodge/Thriftlodge',' Tropiclub hotels',' Unique Hotels and Resorts',' Utell International',' Village Inn Hotels',' Villager Lodge',' W Hotels',' Warwick International Hotels',' Westin Hotels and Resorts',' Williams Hospitality Group',' Windmill Inns of America',' Wingate Inns',' Woodfin Suite Hotels',' Wyndham Hotels and Resorts'];
	# make a hashtable pertaining to carRentals and have the hash be car reservation no.
	
	#trial for benchmarking
	# hotelList = ['Hilton', 'Concur User']

	hotelClass = ['Business Hotel', 'Airport Hotel','Suite Hotel', 'Extended Stay Hotels', 'Serviced Apartments', 'Resort Hotel', 'Bed and Breakfast', 'Timeshare / Rental Hotel', 'Casino Hotel', 'Conference and Convention Centres']

	#13
	carRentalList = ['Agency','Alamo','Avis','Budget','Dollar','Enterprise','Eurodollar','General','Hertz','National Car Rental','Rent a Wreck','Sixt','Thrifty'];

	#18
	#need populated list for this
	locationList = ['San Francisco','Chicago','New York City','Los Angeles','Boston','Seattle','Houston','New Orleans','Austin','Atlanta','Philadelphia','Denver','Portland','Dallas','Baltimore','San Antonio','Pheonix','Pittsburg' ]
	#stateList =['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming',]

	employeeDepartment = ['Legal','Sales','Services','Human Resources'];

	# companyName = ['GoodData','Concur User']

	#
	expenseType = ['Hotel','Car Rental','Air Travel'];

	#53
	industryName = [ 'Agriculture & Agribusiness','Apparel & Accessories','Banking','Communication','Consulting','Fashion','Financial Services ','Health ','Legal Services','Public Relation','Publishing','Real Estate','Technology ','Travel','Web Services'];
	#amount paid is a random decimal number
	def __init__(self,name):
		self.name=name




