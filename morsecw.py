import math
import pyaudio     #sudo apt-get install python-pyaudio
import numpy
import random
PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 32000     #number of frames per second/frameset. 
FREQUENCY = 200     #Hz, waves per second, 261.63=C4-note.
LENGTH = 1     #seconds to play sound

#{'A0': 27.5, 'A#1': 58.270451376144756, 'B2': 123.47074558471449, 'C3': 261.62531188983456, 'C#4': 554.3645460089207, 'D5': 1174.6571753771404, 'D#6': 2489.0110480528424, 'E7': 2637.015281371802, 'F8': 2793.8203004877823, 'F9': 2959.949427125496, '#G10': 3135.9571013249806, 'G#11': 3322.4307318320953, 'A1': 29.13523437127987, 'A2': 30.867704795251214, 'A3': 32.70319322593177, 'A4': 34.64782543006454, 'A5': 36.70809143127713, 'A6': 38.890867169913825, 'A7': 41.20343745082739, 'A8': 43.653520255717346, 'A9': 46.249292501154116, 'A10': 48.99941732825464, 'A11': 51.91307301508549, 'A#0': 54.999983608286556, 'A#2': 61.7353911914271, 'A#3': 65.40636695872277, 'A#4': 69.29563020786632, 'A#5': 73.41616098224463, 'A#6': 77.78171115844765, 'A#7': 82.40685034183879, 'A#8': 87.3070144912167, 'A#9': 92.4985574348483, 'A#10': 97.99880544980354, 'A#11': 103.8261150867449, 'B0': 109.99993443315606, 'B1': 116.5408680194699, 'B3': 130.81269493117557, 'B4': 138.59121911121952, 'B5': 146.83227820388308, 'B6': 155.5633759541491, 'B7': 164.81365156406036, 'B8': 174.613976942013, 'B9': 184.99705973479294, 'B10': 195.997552486213, 'B11': 207.65216828665626, 'C0': 219.99980329949753, 'C1': 233.08166657332126, 'C2': 246.94141757317166, 'C4': 277.1823556134371, 'C5': 293.6644688865795, 'C6': 311.1266591828336, 'C7': 329.6272048889155, 'C8': 349.2278498032163, 'C9': 369.9940091998119, 'C10': 391.99498814567295, 'C11': 415.3042127996818, 'C#0': 439.99947546540454, 'C#1': 466.1631942154464, 'C#2': 493.88268795387256, 'C#3': 523.2504678346824, 'C#5': 587.3287627308385, 'C#6': 622.2531329147927, 'C#7': 659.2542132994785, 'C#8': 698.4554914448744, 'C#9': 739.9877978601414, 'C#10': 783.9897426379093, 'C#11': 830.6081780521777, 'D0': 879.9986886637072, 'D1': 932.3261105685843, 'D2': 987.7650815228902, 'D3': 1046.5006237794832, 'D4': 1108.7287615820305, 'D6': 1244.5058949279494, 'D7': 1318.5080336423703, 'D8': 1396.910566566758, 'D9': 1479.9751546414482, 'D10': 1567.979017969083, 'D11': 1661.2158610101278, 'D#0': 1759.9968527933668, 'D#1': 1864.6516654127172, 'D#2': 1975.5295742762503, 'D#3': 2093.0006237793914, 'D#4': 2217.4568622926367, 'D#5': 2349.3136505854136, 'D#7': 2637.015281371802, 'D#8': 2793.8203004877823, 'D#9': 2959.949427125496, 'D#10': 3135.9571013249806, 'D#11': 3322.4307318320953, 'E0': 3519.992656518947, 'E1': 3729.3022193768593, 'E2': 3951.0579710137827, 'E3': 4186.000000000001}

morse={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ':' '}
wordlist=['A', 'A', 'ABOUT', 'ABOVE', 'ACROSS', 'ACT', 'ACTOR', 'ACTIVE', 'ACTIVITY', 'ADD', 'AFRAID', 'AFTER', 'AGAIN', 'AGE', 'AGO', 'AGREE', 'AIR', 'ALL', 'ALONE', 'ALONG', 'ALREADY', 'ALWAYS', 'AM', 'AMOUNT', 'AN', 'AND', 'ANGRY', 'ANOTHER', 'ANSWER', 'ANY', 'ANYONE', 'ANYTHING', 'ANYTIME', 'APPEAR', 'APPLE', 'ARE', 'AREA', 'ARM', 'ARMY', 'AROUND', 'ARRIVE', 'ART', 'AS', 'ASK', 'AT', 'ATTACK', 'AUNT', 'AUTUMN', 'AWAY', 'B', 'BABY', 'BASE', 'BACK', 'BAD', 'BAG', 'BALL', 'BANK', 'BASKET', 'BATH', 'BE', 'BEAN', 'BEAR', 'BEAUTIFUL', 'BEER', 'BED', 'BEDROOM', 'BEHAVE', 'BEFORE', 'BEGIN', 'BEHIND', 'BELL', 'BELOW', 'BESIDES', 'BEST', 'BETTER', 'BETWEEN', 'BIG', 'BIRD', 'BIRTH', 'BIRTHDAY', 'BIT', 'BITE', 'BLACK', 'BLEED', 'BLOCK', 'BLOOD', 'BLOW', 'BLUE', 'BOARD', 'BOAT', 'BODY', 'BOIL', 'BONE', 'BOOK', 'BORDER', 'BORN', 'BORROW', 'BOTH', 'BOTTLE', 'BOTTOM', 'BOWL', 'BOX', 'BOY', 'BRANCH', 'BRAVE', 'BREAD', 'BREAK', 'BREAKFAST', 'BREATHE', 'BRIDGE', 'BRIGHT', 'BRING', 'BROTHER', 'BROWN', 'BRUSH', 'BUILD', 'BURN', 'BUSINESS', 'BUS', 'BUSY', 'BUT', 'BUY', 'BY', 'C', 'CAKE', 'CALL', 'CAN', 'CANDLE', 'CAP', 'CAR', 'CARD', 'CARE', 'CAREFUL', 'CARELESS', 'CARRY', 'CASE', 'CAT', 'CATCH', 'CENTRAL', 'CENTURY', 'CERTAIN', 'CHAIR', 'CHANCE', 'CHANGE', 'CHASE', 'CHEAP', 'CHEESE', 'CHICKEN', 'CHILD', 'CHILDREN', 'CHOCOLATE', 'CHOICE', 'CHOOSE', 'CIRCLE', 'CITY', 'CLASS', 'CLEVER', 'CLEAN', 'CLEAR', 'CLIMB', 'CLOCK', 'CLOTH', 'CLOTHES', 'CLOUD', 'CLOUDY', 'CLOSE', 'COFFEE', 'COAT', 'COIN', 'COLD', 'COLLECT', 'COLOUR', 'COMB', 'COME', 'COMFORTABLE', 'COMMON', 'COMPARE', 'COMPLETE', 'COMPUTER', 'CONDITION', 'CONTINUE', 'CONTROL', 'COOK', 'COOL', 'COPPER', 'CORN', 'CORNER', 'CORRECT', 'COST', 'CONTAIN', 'COUNT', 'COUNTRY', 'COURSE', 'COVER', 'CRASH', 'CROSS', 'CRY', 'CUP', 'CUPBOARD', 'CUT', 'D', 'DANCE', 'DANGER', 'DANGEROUS', 'DARK', 'DAUGHTER', 'DAY', 'DEAD', 'DECIDE', 'DECREASE', 'DEEP', 'DEER', 'DEPEND', 'DESK', 'DESTROY', 'DEVELOP', 'DIE', 'DIFFERENT', 'DIFFICULT', 'DINNER', 'DIRECTION', 'DIRTY', 'DISCOVER', 'DISH', 'DO', 'DOG', 'DOOR', 'DOUBLE', 'DOWN', 'DRAW', 'DREAM', 'DRESS', 'DRINK', 'DRIVE', 'DROP', 'DRY', 'DUCK', 'DUST', 'DUTY', 'E', 'EACH', 'EAR', 'EARLY', 'EARN', 'EARTH', 'EAST', 'EASY', 'EAT', 'EDUCATION', 'EFFECT', 'EGG', 'EIGHT', 'EITHER', 'ELECTRIC', 'ELEPHANT', 'ELSE', 'EMPTY', 'END', 'ENEMY', 'ENJOY', 'ENOUGH', 'ENTER', 'EQUAL', 'ENTRANCE', 'ESCAPE', 'EVEN', 'EVENING', 'EVENT', 'EVER', 'EVERY', 'EVERYONE', 'EXACT', 'EVERYBODY', 'EXAMINATION', 'EXAMPLE', 'EXCEPT', 'EXCITED', 'EXERCISE', 'EXPECT', 'EXPENSIVE', 'EXPLAIN', 'EXTREMELY', 'EYE', 'F', 'FACE', 'FACT', 'FAIL', 'FALL', 'FALSE', 'FAMILY', 'FAMOUS', 'FAR', 'FARM', 'FATHER', 'FAST', 'FAT', 'FAULT', 'FEAR', 'FEED', 'FEEL', 'FEMALE', 'FEVER', 'FEW', 'FIGHT', 'FILL', 'FILM', 'FIND', 'FINE', 'FINGER', 'FINISH', 'FIRE', 'FIRST', 'FIT', 'FIVE', 'FIX', 'FLAG', 'FLAT', 'FLOAT', 'FLOOR', 'FLOUR', 'FLOWER', 'FLY', 'FOLD', 'FOOD', 'FOOL', 'FOOT', 'FOOTBALL', 'FOR', 'FORCE', 'FOREIGN','FOREST','FORGET', 'FORGIVE', 'FORK', 'FORM', 'FOX', 'FOUR', 'FREE', 'FREEDOM', 'FREEZE', 'FRESH', 'FRIEND', 'FRIENDLY', 'FROM', 'FRONT', 'FRUIT', 'FULL', 'FUN', 'FUNNY', 'FURNITURE', 'FURTHER', 'FUTURE', 'G', 'GAME', 'GARDEN', 'GATE', 'GENERAL', 'GENTLEMAN', 'GET', 'GIFT', 'GIVE', 'GLAD', 'GLASS', 'GO', 'GOAT', 'GOD', 'GOLD', 'GOOD', 'GOODBYE', 'GRANDFATHER', 'GRANDMOTHER', 'GRASS', 'GRAVE', 'GREAT', 'GREEN', 'GREY', 'GROUND', 'GROUP', 'GROW', 'GUN', 'H', 'HAIR', 'HALF', 'HALL', 'HAMMER', 'HAND', 'HAPPEN', 'HAPPY', 'HARD', 'HAT', 'HATE', 'HAVE', 'HE', 'HEAD', 'HEALTHY', 'HEAR', 'HEAVY', 'HELLO', 'HELP', 'HEART', 'HEAVEN', 'HEIGHT', 'HEN', 'HER', 'HERE', 'HERS', 'HIDE', 'HIGH', 'HILL', 'HIM', 'HIS', 'HIT', 'HOBBY', 'HOLD', 'HOLE', 'HOLIDAY', 'HOME', 'HOPE', 'HORSE', 'HOSPITAL', 'HOT', 'HOTEL', 'HOUSE', 'HOW', 'HUNDRED', 'HUNGRY', 'HOUR', 'HURRY', 'HUSBAND', 'HURT', 'I', 'I', 'ICE', 'IDEA', 'IF', 'IMPORTANT', 'IN', 'INCREASE', 'INSIDE', 'INTO', 'INTRODUCE', 'INVENT', 'IRON', 'INVITE', 'IS', 'ISLAND', 'IT', 'ITS', 'J', 'JELLY', 'JOB', 'JOIN', 'JUICE', 'JUMP', 'JUST', 'K', 'KEEP', 'KEY', 'KID', 'KILL', 'KIND', 'KING', 'KITCHEN', 'KNEE', 'KNIFE', 'KNOCK', 'KNOW', 'L', 'LADDER', 'LADY', 'LAMP', 'LAND', 'LARGE', 'LAST', 'LATE', 'LATELY', 'LAUGH', 'LAZY', 'LEAD', 'LEAF', 'LEARN', 'LEAVE', 'LEG', 'LEFT', 'LEND', 'LENGTH', 'LESS', 'LESSON', 'LET', 'LETTER', 'LIBRARY', 'LIE', 'LIFE', 'LIGHT', 'LIKE', 'LION', 'LIP', 'LIST', 'LISTEN', 'LITTLE', 'LIVE', 'LOCK', 'LONELY', 'LONG', 'LOOK', 'LOSE', 'LOT', 'LOVE', 'LOW', 'LOWER', 'LUCK', 'M', 'MACHINE', 'MAIN', 'MAKE', 'MALE', 'MAN', 'MANY', 'MAP', 'MARK', 'MARKET', 'MARRY', 'MATTER', 'MAY', 'ME', 'MEAL', 'MEAN', 'MEASURE', 'MEAT', 'MEDICINE', 'MEET', 'MEMBER', 'MENTION', 'METHOD', 'MIDDLE', 'MILK', 'MILL', 'MILLION', 'MIND', 'MINE', 'MINUTE', 'MISS', 'MISTAKE', 'MIX', 'MODEL', 'MODERN', 'MOMENT', 'MONEY', 'MONKEY', 'MONTH', 'MOON', 'MORE', 'MORNING', 'MOST', 'MOTHER', 'MOUNTAIN', 'MOUSE', 'MOUTH', 'MOVE', 'MUCH', 'MUSIC', 'MUST', 'MY', 'N', 'NAME', 'NARROW', 'NATION', 'NATURE', 'NEAR', 'NEARLY', 'NECK', 'NEED', 'NEEDLE', 'NEIGHBOUR', 'NEITHER', 'NET', 'NEVER', 'NEW', 'NEWS', 'NEWSPAPER', 'NEXT', 'NICE', 'NIGHT', 'NINE', 'NO', 'NOBLE', 'NOISE', 'NONE', 'NOR', 'NORTH', 'NOSE', 'NOT', 'NOTHING', 'NOTICE', 'NOW', 'NUMBER', 'O', 'OBEY', 'OBJECT', 'OCEAN', 'OF', 'OFF', 'OFFER', 'OFFICE', 'OFTEN', 'OIL', 'OLD', 'ON', 'ONE', 'ONLY', 'OPEN', 'OPPOSITE', 'OR', 'ORANGE', 'ORDER', 'OTHER', 'OUR', 'OUT', 'OUTSIDE', 'OVER', 'OWN', 'P', 'PAGE', 'PAIN', 'PAINT', 'PAIR', 'PAN', 'PAPER', 'PARENT', 'PARK', 'PART', 'PARTNER', 'PARTY', 'PASS', 'PAST', 'PATH', 'PAY', 'PEACE', 'PEN', 'PENCIL', 'PEOPLE', 'PEPPER', 'PER', 'PERFECT', 'PERIOD', 'PERSON', 'PETROL', 'PHOTOGRAPH', 'PIANO', 'PICK', 'PICTURE', 'PIECE', 'PIG', 'PILL', 'PIN', 'PINK', 'PLACE', 'PLANE', 'PLANT', 'PLASTIC', 'PLATE', 'PLAY', 'PLEASE', 'PLEASED', 'PLENTY', 'POCKET', 'POINT', 'POISON', 'POLICE', 'POLITE', 'POOL', 'POOR', 'POPULAR', 'POSITION', 'POSSIBLE', 'POTATO', 'POUR', 'POWER', 'PRESENT', 'PRESS', 'PRETTY', 'PREVENT', 'PRICE', 'PRINCE', 'PRISON', 'PRIVATE', 'PRIZE', 'PROBABLY', 'PROBLEM', 'PRODUCE', 'PROMISE', 'PROPER', 'PROTECT', 'PROVIDE', 'PUBLIC', 'PULL', 'PUNISH', 'PUPIL', 'PUSH', 'PUT', 'Q', 'QUEEN', 'QUESTION', 'QUICK', 'QUIET', 'QUITE', 'R', 'RADIO', 'RAIN', 'RAINY', 'RAISE', 'REACH', 'READ', 'READY', 'REAL', 'REALLY', 'RECEIVE', 'RECORD', 'RED', 'REMEMBER', 'REMIND', 'REMOVE', 'RENT', 'REPAIR', 'REPEAT', 'REPLY', 'REPORT', 'REST', 'RESTAURANT', 'RESULT', 'RETURN', 'RICE', 'RICH', 'RIDE', 'RIGHT', 'RING', 'RISE', 'ROAD', 'ROB', 'ROCK', 'ROOM', 'ROUND', 'RUBBER', 'RUDE', 'RULE', 'RULER', 'RUN', 'RUSH', 'S', 'SAD', 'SAFE', 'SAIL', 'SALT', 'SAME', 'SAND', 'SAVE', 'SAY', 'SCHOOL', 'SCIENCE', 'SCISSORS', 'SEARCH', 'SEAT', 'SECOND', 'SEE', 'SEEM', 'SELL', 'SEND', 'SENTENCE', 'SERVE', 'SEVEN', 'SEVERAL', 'SEX', 'SHADE', 'SHADOW', 'SHAKE', 'SHAPE', 'SHARE', 'SHARP', 'SHE', 'SHEEP', 'SHEET', 'SHELF', 'SHINE', 'SHIP', 'SHIRT', 'SHOE', 'SHOOT', 'SHOP', 'SHORT', 'SHOULD', 'SHOULDER', 'SHOUT', 'SHOW', 'SICK', 'SIDE', 'SIGNAL', 'SILENCE', 'SILLY', 'SILVER', 'SIMILAR', 'SIMPLE', 'SINGLE', 'SINCE', 'SING', 'SINK', 'SISTER', 'SIT', 'SIX', 'SIZE', 'SKILL', 'SKIN', 'SKIRT', 'SKY', 'SLEEP', 'SLIP', 'SLOW', 'SMALL', 'SMELL', 'SMILE', 'SMOKE', 'SNOW', 'SO', 'SOAP', 'SOCK', 'SOFT', 'SOME', 'SOMEONE', 'SOMETHING', 'SOMETIMES', 'SON', 'SOON', 'SORRY', 'SOUND', 'SOUP', 'SOUTH', 'SPACE', 'SPEAK', 'SPECIAL', 'SPEED', 'SPELL', 'SPEND', 'SPOON', 'SPORT', 'SPREAD', 'SPRING', 'SQUARE', 'STAMP', 'STAND', 'STAR', 'START', 'STATION', 'STAY', 'STEAL', 'STEAM', 'STEP', 'STILL', 'STOMACH', 'STONE', 'STOP', 'STORE', 'STORM', 'STORY', 'STRANGE', 'STREET', 'STRONG', 'STRUCTURE', 'STUDENT', 'STUDY', 'STUPID', 'SUBJECT', 'SUBSTANCE', 'SUCCESSFUL', 'SUCH', 'SUDDEN', 'SUGAR', 'SUITABLE', 'SUMMER', 'SUN', 'SUNNY', 'SUPPORT', 'SURE', 'SURPRISE', 'SWEET', 'SWIM', 'SWORD', 'T', 'TABLE', 'TAKE', 'TALK', 'TALL', 'TASTE', 'TAXI', 'TEA', 'TEACH', 'TEAM', 'TEAR', 'TELEPHONE', 'TELEVISION', 'TELL', 'TEN', 'TENNIS', 'TERRIBLE', 'TEST', 'THAN', 'THAT', 'THE', 'THEIR', 'THEIRS', 'THEN', 'THERE', 'THEREFORE', 'THESE', 'THICK', 'THIN', 'THING', 'THINK', 'THIRD', 'THIS', 'THOSE', 'THOUGH', 'THREAT', 'THREE', 'TIDY', 'TIE', 'TITLE', 'TO', 'TODAY', 'TOE', 'TOGETHER', 'TOMORROW', 'TONIGHT', 'TOO', 'TOOL', 'TOOTH', 'TOP', 'TOTAL', 'TOUCH', 'TOWN', 'TRAIN', 'TRAM', 'TRAVEL', 'TREE', 'TROUBLE', 'TRUE', 'TRUST', 'TWICE', 'TRY', 'TURN', 'TYPE', 'U', 'UNCLE', 'UNDER', 'UNDERSTAND', 'UNIT', 'UNTIL', 'UP', 'USE', 'USEFUL', 'USUAL', 'USUALLY', 'V', 'VEGETABLE', 'VERY', 'VILLAGE', 'VOICE', 'VISIT', 'W', 'WAIT', 'WAKE', 'WALK', 'WANT', 'WARM', 'WASH', 'WASTE', 'WATCH', 'WATER', 'WAY', 'WE', 'WEAK', 'WEAR', 'WEATHER', 'WEDDING', 'WEEK', 'WEIGHT', 'WELCOME', 'WELL', 'WEST', 'WET', 'WHAT', 'WHEEL', 'WHEN', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHO', 'WHY', 'WIDE', 'WIFE', 'WILD', 'WILL', 'WIN', 'WIND', 'WINDOW', 'WINE', 'WINTER', 'WIRE', 'WISE', 'WISH', 'WITH', 'WITHOUT', 'WOMAN', 'WONDER', 'WORD', 'WORK', 'WORLD', 'WORRY', 'WORST', 'WRITE', 'WRONG', 'Y', 'YEAR', 'YELLOW', 'YES', 'YESTERDAY', 'YET', 'YOU', 'YOUNG', 'YOUR', 'YOURS', 'Z', 'ZERO', 'ZOO', 'ZOOM']





if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100
NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''
def sound(t):
    global BITRATE
    global k
    curr=''
    for i in range(int(k*BITRATE*t)):
        curr+=chr(int(math.sin(i/((BITRATE/880)/math.pi))*127+128))
    return curr
def sil(t):
    global BITRATE
    global k
    curr=''
    for i in range(int(k*BITRATE*t)):
        curr+=chr(128)
    return curr
def letter(t, lett):
    m=morse[lett]
    curr=''
    for i in m:
        if i=='-':
            curr+=sound(3*t)
            #print('-')
        elif i=='.':
            curr+=sound(t)
            #print('.')
        else:
            print("ERROR code", i)
        curr+=sil(t)
    return curr
def word(t, w):
    curr=''
    for i in w:
        curr+=letter(t, i)
        curr+=sil(2*t)
    curr+=sil(4*t)
    return curr
def filler(w):
    curr=''
    for i in w:
        curr+=chr(128)
    return w+curr
#generating wawes
#for FREQUENCY in range(1500,1510):
#
#    for x in range(NUMBEROFFRAMES):
#        WAVEDATA += chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
#    for x in range(RESTFRAMES):
#        WAVEDATA += chr(128)
k=2
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = BITRATE,
                output = True)
while True:
    w=wordlist[random.randrange(len(wordlist))]
    lettt=chr(random.randrange(65, 91))
    WAVEDATA=word(0.07,w)
    #WAVEDATA=letter(0.08, lettt)

    stream.write(filler(WAVEDATA))
    #print(WAVEDATA)

    #stream.stop_stream()

    if input().upper()==w:
        print('+')
    else:
        #print(w, [morse[i] for i in w])
        print (w)#, morse[lettt])


stream.stop_stream()
stream.close()
p.terminate()
if input().upper()==lettt:
    print('+')
else:
    print(lettt, morse[lettt])
