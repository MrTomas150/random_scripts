import keyboard
import time
import random
import threading as thr
#from random_word import RandomWords
#r=RandomWords()
morse={
	".-":"A",
	"-...":"B",
	"-.-.":"C",
	"-..":"D",
	".":"E",
	"..-.":"F",
	"--.":"G",
	"....":"H",
	"..":"I",
	".---":"J",
	"-.-":"K",
	".-..":"L",
	"--":"M",
	"-.":"N",
	"---":"O",
	".--.":"P",
	"--.-":"Q",
	".-.":"R",
	"...":"S",
	"-":"T",
	"..-":"U",
	"...-":"V",
	".--":"W",
	"-..-":"X",
	"-.--":"Y",
	"--..":"Z",
	"-----":"0",
	".----":"1",
	"..---":"2",
	"...--":"3",
	"....-":"4",
	".....":"5",
	"-....":"6",
	"--...":"7",
	"---..":"8",
	"----.":"9"
        }


morse2={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ':' '}

wordlist=['A', 'A', 'ABOUT', 'ABOVE', 'ACROSS', 'ACT', 'ACTOR', 'ACTIVE', 'ACTIVITY', 'ADD', 'AFRAID', 'AFTER', 'AGAIN', 'AGE', 'AGO', 'AGREE', 'AIR', 'ALL', 'ALONE', 'ALONG', 'ALREADY', 'ALWAYS', 'AM', 'AMOUNT', 'AN', 'AND', 'ANGRY', 'ANOTHER', 'ANSWER', 'ANY', 'ANYONE', 'ANYTHING', 'ANYTIME', \
        'APPEAR', 'APPLE', 'ARE', 'AREA', 'ARM', 'ARMY', 'AROUND', 'ARRIVE', 'ART', 'AS', 'ASK', 'AT', 'ATTACK', 'AUNT', 'AUTUMN', 'AWAY', 'B', 'BABY', 'BASE', 'BACK', 'BAD', 'BAG', 'BALL', 'BANK', 'BASKET', 'BATH', 'BE', 'BEAN', 'BEAR', 'BEAUTIFUL', 'BEER', 'BED', 'BEDROOM', 'BEHAVE', 'BEFORE', 'BEGIN', 'BEHIND', 'BELL', 'BELOW', 'BESIDES', 'BEST', 'BETTER', 'BETWEEN', 'BIG', 'BIRD', 'BIRTH', 'BIRTHDAY', 'BIT', 'BITE', 'BLACK', 'BLEED', 'BLOCK', 'BLOOD', 'BLOW', 'BLUE', 'BOARD', 'BOAT', 'BODY', 'BOIL', 'BONE', 'BOOK', 'BORDER', 'BORN', 'BORROW', 'BOTH', 'BOTTLE', 'BOTTOM', 'BOWL', 'BOX', 'BOY', 'BRANCH', 'BRAVE', 'BREAD', 'BREAK', 'BREAKFAST', 'BREATHE', 'BRIDGE', 'BRIGHT', 'BRING', 'BROTHER', 'BROWN', 'BRUSH', 'BUILD', 'BURN', 'BUSINESS', 'BUS', 'BUSY', 'BUT', 'BUY', 'BY', \
        'C', 'CAKE', 'CALL', 'CAN', 'CANDLE', 'CAP', 'CAR', 'CARD', 'CARE', 'CAREFUL', 'CARELESS', 'CARRY', 'CASE', 'CAT', 'CATCH', 'CENTRAL', 'CENTURY', 'CERTAIN', 'CHAIR', 'CHANCE', 'CHANGE', 'CHASE', 'CHEAP', 'CHEESE', 'CHICKEN', 'CHILD', 'CHILDREN', 'CHOCOLATE', 'CHOICE', 'CHOOSE', 'CIRCLE', 'CITY', 'CLASS', 'CLEVER', 'CLEAN', 'CLEAR', 'CLIMB', 'CLOCK', 'CLOTH', 'CLOTHES', 'CLOUD', 'CLOUDY', 'CLOSE', 'COFFEE', 'COAT', 'COIN', 'COLD', 'COLLECT', 'COLOUR', 'COMB', 'COME', 'COMFORTABLE', 'COMMON', 'COMPARE', 'COMPLETE', 'COMPUTER', 'CONDITION', 'CONTINUE', 'CONTROL', 'COOK', 'COOL', 'COPPER', 'CORN', 'CORNER', 'CORRECT', 'COST', 'CONTAIN', 'COUNT', 'COUNTRY', 'COURSE', 'COVER', 'CRASH', 'CROSS', 'CRY', 'CUP', 'CUPBOARD', 'CUT', 'D', 'DANCE', 'DANGER', 'DANGEROUS', 'DARK', 'DAUGHTER', 'DAY', 'DEAD', 'DECIDE', 'DECREASE', 'DEEP', 'DEER', 'DEPEND', 'DESK', 'DESTROY', 'DEVELOP', 'DIE', 'DIFFERENT', 'DIFFICULT', 'DINNER', 'DIRECTION', 'DIRTY', 'DISCOVER', 'DISH', 'DO', 'DOG', 'DOOR', 'DOUBLE', 'DOWN', 'DRAW', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'DROP', 'DRY', 'DUCK', 'DUST', 'DUTY', 'E', 'EACH', 'EAR', 'EARLY', 'EARN', 'EARTH', 'EAST', 'EASY', 'EAT', 'EDUCATION', 'EFFECT', 'EGG', 'EIGHT', 'EITHER', 'ELECTRIC', 'ELEPHANT', 'ELSE', 'EMPTY', 'END', 'ENEMY', 'ENJOY', 'ENOUGH', 'ENTER', 'EQUAL', 'ENTRANCE', 'ESCAPE', 'EVEN', 'EVENING', 'EVENT', 'EVER', 'EVERY', 'EVERYONE', 'EXACT', 'EVERYBODY', 'EXAMINATION', 'EXAMPLE', 'EXCEPT', 'EXCITED', 'EXERCISE', 'EXPECT', 'EXPENSIVE', 'EXPLAIN', 'EXTREMELY', 'EYE', 'F', 'FACE', 'FACT', 'FAIL', 'FALL', 'FALSE', 'FAMILY', 'FAMOUS', 'FAR', 'FARM', 'FATHER', 'FAST', 'FAT', 'FAULT', 'FEAR', 'FEED', 'FEEL', 'FEMALE', 'FEVER', 'FEW', 'FIGHT', 'FILL', 'FILM', 'FIND', 'FINE', 'FINGER', 'FINISH', 'FIRE', 'FIRST', 'FIT', 'FIVE', 'FIX', 'FLAG', 'FLAT', 'FLOAT', 'FLOOR', 'FLOUR', 'FLOWER', 'FLY', 'FOLD', 'FOOD', 'FOOL', 'FOOT', 'FOOTBALL', 'FOR', 'FORCE', 'FOREIGN', 'FOREST', 'FORGET', 'FORGIVE', 'FORK', 'FORM', 'FOX', 'FOUR', 'FREE', 'FREEDOM', 'FREEZE', 'FRESH', 'FRIEND', 'FRIENDLY', 'FROM', 'FRONT', 'FRUIT', 'FULL', 'FUN', 'FUNNY', 'FURNITURE', 'FURTHER', 'FUTURE', 'G', 'GAME', 'GARDEN', 'GATE', 'GENERAL', 'GENTLEMAN', 'GET', 'GIFT', 'GIVE', 'GLAD', 'GLASS', 'GO', 'GOAT', 'GOD', 'GOLD', 'GOOD', 'GOODBYE', 'GRANDFATHER', 'GRANDMOTHER', 'GRASS', 'GRAVE', 'GREAT', 'GREEN', 'GREY', 'GROUND', 'GROUP', 'GROW', 'GUN', 'H', 'HAIR', 'HALF', 'HALL', 'HAMMER', 'HAND', 'HAPPEN', 'HAPPY', 'HARD', 'HAT', 'HATE', 'HAVE', 'HE', 'HEAD', 'HEALTHY', 'HEAR', 'HEAVY', 'HELLO', 'HELP', 'HEART', 'HEAVEN', 'HEIGHT', 'HEN', 'HER', 'HERE', 'HERS', 'HIDE', 'HIGH', 'HILL', 'HIM', 'HIS', 'HIT', 'HOBBY', 'HOLD', 'HOLE', 'HOLIDAY', 'HOME', 'HOPE', 'HORSE', 'HOSPITAL', 'HOT', 'HOTEL', 'HOUSE', 'HOW', 'HUNDRED', 'HUNGRY', 'HOUR', 'HURRY', 'HUSBAND', 'HURT', 'I', 'I', 'ICE', 'IDEA', 'IF', 'IMPORTANT', 'IN', 'INCREASE', 'INSIDE', 'INTO', 'INTRODUCE', 'INVENT', 'IRON', 'INVITE', 'IS', 'ISLAND', 'IT', 'ITS', 'J', 'JELLY', 'JOB', 'JOIN', 'JUICE', 'JUMP', 'JUST', 'K', 'KEEP', 'KEY', 'KID', 'KILL', 'KIND', 'KING', 'KITCHEN', 'KNEE', 'KNIFE', 'KNOCK', 'KNOW', 'L', 'LADDER', 'LADY', 'LAMP', 'LAND', 'LARGE', 'LAST', 'LATE', 'LATELY', 'LAUGH', 'LAZY', 'LEAD', 'LEAF', 'LEARN', 'LEAVE', 'LEG', 'LEFT', 'LEND', 'LENGTH', 'LESS', 'LESSON', 'LET', 'LETTER', 'LIBRARY', 'LIE', 'LIFE', 'LIGHT', 'LIKE', 'LION', 'LIP', 'LIST', 'LISTEN', 'LITTLE', 'LIVE', 'LOCK', 'LONELY', 'LONG', 'LOOK', 'LOSE', 'LOT', 'LOVE', 'LOW', 'LOWER', 'LUCK', 'M', 'MACHINE', 'MAIN', 'MAKE', 'MALE', 'MAN', 'MANY', 'MAP', 'MARK', 'MARKET', 'MARRY', 'MATTER', 'MAY', 'ME', 'MEAL', 'MEAN', 'MEASURE', 'MEAT', 'MEDICINE', 'MEET', 'MEMBER', 'MENTION', 'METHOD', 'MIDDLE', 'MILK', 'MILL', 'MILLION', 'MIND', 'MINE', 'MINUTE', 'MISS', 'MISTAKE', 'MIX', 'MODEL', 'MODERN', 'MOMENT', 'MONEY', 'MONKEY', 'MONTH', 'MOON', 'MORE', 'MORNING', 'MOST', 'MOTHER', 'MOUNTAIN', 'MOUSE', 'MOUTH', 'MOVE', 'MUCH', 'MUSIC', 'MUST', 'MY', 'N', 'NAME', 'NARROW', 'NATION', 'NATURE', 'NEAR', 'NEARLY', 'NECK', 'NEED', 'NEEDLE', 'NEIGHBOUR', 'NEITHER', 'NET', 'NEVER', 'NEW', 'NEWS', 'NEWSPAPER', 'NEXT', 'NICE', 'NIGHT', 'NINE', 'NO', 'NOBLE', 'NOISE', 'NONE', 'NOR', 'NORTH', 'NOSE', 'NOT', 'NOTHING', 'NOTICE', 'NOW', 'NUMBER', 'O', 'OBEY', 'OBJECT', 'OCEAN', 'OF', 'OFF', 'OFFER', 'OFFICE', 'OFTEN', 'OIL', 'OLD', 'ON', 'ONE', 'ONLY', 'OPEN', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'OTHER', 'OUR', 'OUT', 'OUTSIDE', 'OVER', 'OWN', 'P', 'PAGE', 'PAIN', 'PAINT', 'PAIR', 'PAN', 'PAPER', 'PARENT', 'PARK', 'PART', 'PARTNER', 'PARTY', 'PASS', 'PAST', 'PATH', 'PAY', 'PEACE', 'PEN', 'PENCIL', 'PEOPLE', 'PEPPER', 'PER', 'PERFECT', 'PERIOD', 'PERSON', 'PETROL', 'PHOTOGRAPH', 'PIANO', 'PICK', 'PICTURE', 'PIECE', 'PIG', 'PILL', 'PIN', 'PINK', 'PLACE', 'PLANE', 'PLANT', 'PLASTIC', 'PLATE', 'PLAY', 'PLEASE', 'PLEASED', 'PLENTY', 'POCKET', 'POINT', 'POISON', 'POLICE', 'POLITE', 'POOL', 'POOR', 'POPULAR', 'POSITION', 'POSSIBLE', 'POTATO', 'POUR', 'POWER', 'PRESENT', 'PRESS', 'PRETTY', 'PREVENT', 'PRICE', 'PRINCE', 'PRISON', 'PRIVATE', 'PRIZE', 'PROBABLY', 'PROBLEM', 'PRODUCE', 'PROMISE', 'PROPER', 'PROTECT', 'PROVIDE', 'PUBLIC', 'PULL', 'PUNISH', 'PUPIL', 'PUSH', 'PUT', 'Q', 'QUEEN', 'QUESTION', 'QUICK', 'QUIET', 'QUITE', 'R', 'RADIO', 'RAIN', 'RAINY', 'RAISE', 'REACH', 'READ', 'READY', 'REAL', 'REALLY', 'RECEIVE', 'RECORD', 'RED', 'REMEMBER', 'REMIND', 'REMOVE', 'RENT', 'REPAIR', 'REPEAT', 'REPLY', 'REPORT', 'REST', 'RESTAURANT', 'RESULT', 'RETURN', 'RICE', 'RICH', 'RIDE', 'RIGHT', 'RING', 'RISE', 'ROAD', 'ROB', 'ROCK', 'ROOM', 'ROUND', 'RUBBER', 'RUDE', 'RULE', 'RULER', 'RUN', 'RUSH', 'S', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME', 'SAND', 'SAVE', 'SAY', 'SCHOOL', 'SCIENCE', 'SCISSORS', 'SEARCH', 'SEAT', 'SECOND', 'SEE', 'SEEM', 'SELL', 'SEND', 'SENTENCE', 'SERVE', 'SEVEN', 'SEVERAL', 'SEX', 'SHADE', 'SHADOW', 'SHAKE', 'SHAPE', 'SHARE', 'SHARP', 'SHE', 'SHEEP', 'SHEET', 'SHELF', 'SHINE', 'SHIP', 'SHIRT', 'SHOE', 'SHOOT', 'SHOP', 'SHORT', 'SHOULD', 'SHOULDER', 'SHOUT', 'SHOW', 'SICK', 'SIDE', 'SIGNAL', 'SILENCE', 'SILLY', 'SILVER', 'SIMILAR', 'SIMPLE', 'SINGLE', 'SINCE', 'SING', 'SINK', 'SISTER', 'SIT', 'SIX', 'SIZE', 'SKILL', 'SKIN', 'SKIRT', 'SKY', 'SLEEP', 'SLIP', 'SLOW', 'SMALL', 'SMELL', 'SMILE', 'SMOKE', 'SNOW', 'SO', 'SOAP', 'SOCK', 'SOFT', 'SOME', 'SOMEONE', 'SOMETHING', 'SOMETIMES', 'SON', 'SOON', 'SORRY', 'SOUND', 'SOUP', 'SOUTH', 'SPACE', 'SPEAK', 'SPECIAL', 'SPEED', 'SPELL', 'SPEND', 'SPOON', 'SPORT', 'SPREAD', 'SPRING', 'SQUARE', 'STAMP', 'STAND', 'STAR', 'START', 'STATION', 'STAY', 'STEAL', 'STEAM', 'STEP', 'STILL', 'STOMACH', 'STONE', 'STOP', 'STORE', 'STORM', 'STORY', 'STRANGE', 'STREET', 'STRONG', 'STRUCTURE', 'STUDENT', 'STUDY', 'STUPID', 'SUBJECT', 'SUBSTANCE', 'SUCCESSFUL', 'SUCH', 'SUDDEN', 'SUGAR', 'SUITABLE', 'SUMMER', 'SUN', 'SUNNY', 'SUPPORT', 'SURE', 'SURPRISE', 'SWEET', 'SWIM', 'SWORD', 'T', 'TABLE', 'TAKE', 'TALK', 'TALL', 'TASTE', 'TAXI', 'TEA', 'TEACH', 'TEAM', 'TEAR', 'TELEPHONE', 'TELEVISION', 'TELL', 'TEN', 'TENNIS', 'TERRIBLE', 'TEST', 'THAN', 'THAT', 'THE', 'THEIR', 'THEIRS', 'THEN', 'THERE', 'THEREFORE', 'THESE', 'THICK', 'THIN', 'THING', 'THINK', 'THIRD', 'THIS', 'THOSE', 'THOUGH', 'THREAT', 'THREE', 'TIDY', 'TIE', 'TITLE', 'TO', 'TODAY', 'TOE', 'TOGETHER', 'TOMORROW', 'TONIGHT', 'TOO', 'TOOL', 'TOOTH', 'TOP', 'TOTAL', 'TOUCH', 'TOWN', 'TRAIN', 'TRAM', 'TRAVEL', 'TREE', 'TROUBLE', 'TRUE', 'TRUST', 'TWICE', 'TRY', 'TURN', 'TYPE', 'U', 'UNCLE', 'UNDER', 'UNDERSTAND', 'UNIT', 'UNTIL', 'UP', 'USE', 'USEFUL', 'USUAL', 'USUALLY', 'V', 'VEGETABLE', 'VERY', 'VILLAGE', 'VOICE', 'VISIT', 'W', 'WAIT', 'WAKE', 'WALK', 'WANT', 'WARM', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAY', 'WE', 'WEAK', 'WEAR', 'WEATHER', 'WEDDING', 'WEEK', 'WEIGHT', 'WELCOME', 'WELL', 'WEST', 'WET', 'WHAT', 'WHEEL', 'WHEN', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHO', 'WHY', 'WIDE', 'WIFE', 'WILD', 'WILL', 'WIN', 'WIND', 'WINDOW', 'WINE', 'WINTER', 'WIRE', 'WISE', 'WISH', 'WITH', 'WITHOUT', 'WOMAN', 'WONDER', 'WORD', 'WORK', 'WORLD', 'WORRY', 'WORST', 'WRITE', 'WRONG', 'Y', 'YEAR', 'YELLOW', 'YES', 'YESTERDAY', 'YET', 'YOU', 'YOUNG', 'YOUR', 'YOURS', 'Z', 'ZERO', 'ZOO', 'ZOOM']


def background():
    l=['-','/','|','\\')
    i=0
    while 1:
        i=(i+1)%4
        print(l[i], end='\r')
        time.sleep(0.1)



def calibrate():
	pr=0
	while True:
		if pr==0:
			if keyboard.is_pressed('ctrl'):
				pr+=1
				print(pr)
				tic=time.perf_counter()
				while(keyboard.is_pressed('ctrl')):
					time.sleep(0.1)
		elif pr==4:
				toc=time.perf_counter()
				return (toc-tic)/7
		else:
			if keyboard.is_pressed('ctrl'):
				pr+=1
				print(pr)
				while(keyboard.is_pressed('ctrl')):
					time.sleep(0.1)
def read(t):
	s=""
	curr=""
	start=0
	while True:
		if start==0:
			if keyboard.is_pressed('ctrl'):
				start=1
				tic=time.perf_counter()
				while(keyboard.is_pressed('ctrl')):
					time.sleep(0.01)
				toc=time.perf_counter()
				if toc-tic>2*t:
					curr+="-"
				else:
					curr+='.'
		else:
			if keyboard.is_pressed('ctrl'):
				start=1
				tic=time.perf_counter()
				while(keyboard.is_pressed('ctrl')):
					time.sleep(0.01)
				toc=time.perf_counter()
				if toc-tic>2*t:
					curr+="-"
				else:
					curr+='.'
			else:
				tic=time.perf_counter()
				state=0
				while(keyboard.is_pressed('ctrl')==False):
					#print(time.perf_counter()-tic)
					if state==0:
						if time.perf_counter()-tic>3*t:
							try:
								s+=morse[curr]
								curr=""
								state=1
							except:
								return ("unknown symbol {}".format(curr))
								curr=""
								state=1
					elif state==1:
						if time.perf_counter()-tic>6*t:
							return s
							s=""
							state=2
					time.sleep(0.01)
def test(taim):
    t=wordlist[random.randrange(len(wordlist))]
    #t=r.get_random_word()
    print(t)
    k=read(taim)
    if k==t:
        print(k,"+")
    else:
        print(k,"-", [morse2[i.upper()] for i in t])
taim=calibrate()
print(taim)
while True:
    thread=thr.Thread(target=background, name='timer')
    thread.start()
    test(taim)

