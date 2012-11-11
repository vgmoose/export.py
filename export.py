# coding=latin-1
import os, sys, re, string, pickle, traceback, easygui
# -*- coding: latin-1 -*-

#import FileDialog
#
#
#d = FileDialog(sys.argv[0], sys.argv[0])
#file = d.go()
#

def ByteToHex( byteStr ):    
    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip().replace(' ','')

yes = set(['yes','y', 'ye', 'ya', 'yeah', 'affirmative', 'please', 'ok', 'yup', 'yap', 'pls','yep','yessir','of course','Export'])

def HexToBin( my_hexdata ):    
    scale = 16
    
    num_of_bits = 8
    
    return bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

if (len(sys.argv)==1 or (len(sys.argv)==2 and sys.argv[1].lower()=="-gui")):
    files = "%s/Library/Application Support/Bannister/KiGB/Battery RAM/Pokemon Crystal.sav" % os.getenv("HOME")
else:
    files = sys.argv[1]

global gui
gui=False
global allpokedata
allpokedata=""

if ((len(sys.argv)==2 and sys.argv[1]=="-gui") or (len(sys.argv)==3 and sys.argv[2]=="-gui")):
    gui=True

#if (gui):
#    print ("Running in GUI mode. Execute with \"-nogui\" to use the console.")
    
exp = 3

destination = "Pokemon"

maxr=6

items = "None","Master Ball","Ultra Ball","BrightPowder","Great Ball","Poké Ball","Bicycle","Teru-sama","Moon Stone","Antidote","Burn Heal","Ice Heal","Awakening","Parlyz Heal","Full Restore","Max Potion","Hyper Potion","Super Potion","Potion","Escape Rope","Repel","Max Elixer","Fire Stone","Thunderstone","Water Stone","Teru-sama","HP Up","Protein","Iron","Carbos","Lucky Punch","Calcium","Rare Candy","X Accuracy","Leaf Stone","Metal Powder","Nugget","Poké Doll","Full Heal","Revive","Max Revive","Guard Spec.","Super Repel","Max Repel","Dire Hit","Teru-sama","Fresh Water","Soda Pop","Lemonade","X Attack","Teru-sama","X Defend","X Speed","X Special","Coin Case","Itemfinder","Teru-sama","Exp Share","Old Rod","Good Rod","Silver Leaf","Super Rod","PP Up","Ether","Max Ether","Elixer","Red Scale","SecretPotion","S.S. Ticket","Mystery Egg","Clear Bell","Silver Wing","Moomoo Milk","Quick Claw","PSNCureBerry","Gold Leaf","Soft Sand","Sharp Beak","PRZCureBerry","Burnt Berry","Ice Berry","Poison Barb","King's Rock","Bitter Berry","Mint Berry","Red Apricorn","TinyMushroom","Big Mushroom","SilverPowder","Blu Apricorn","Teru-sama","Amulet Coin","Ylw Apricorn","Grn Apricorn","Cleanse Tag","Mystic Water","TwistedSpoon","Wht Apricorn","Black Belt","Blk Apricorn","Teru-sama","Pnk Apricorn","BlackGlasses","SlowpokeTail","Pink Bow","Stick","Smoke Ball","NeverMeltIce","Magnet","MiracleBerry","Pearl","Big Pearl","Everstone","Spell Tag","RageCandyBar","GS Ball","Blue Card","Miracle Seed","Thick Club","Focus Band","Teru-sama","EnergyPowder","Energy Root","Heal Powder","Revival Herb","Hard Stone","Lucky Egg","Card Key","Machine Part","Egg Ticket","Lost Item","Stardust","Star Piece","Basement Key","Pass","Teru-sama","Teru-sama","Teru-sama","Charcoal","Berry Juice","Scope Lens","Teru-sama","Teru-sama","Metal Coat","Dragon Fang","Teru-sama","Leftovers","Teru-sama","Teru-sama","Teru-sama","MysteryBerry","Dragon Scale","Berserk Gene","Teru-sama","Teru-sama","Teru-sama","Sacred Ash","Heavy Ball","Flower Mail","Level Ball","Lure Ball","Fast Ball","Teru-sama","Light Ball","Friend Ball","Moon Ball","Love Ball","Normal Box","Gorgeous Box","Sun Stone","Polkadot Bow","Teru-sama","Up-Grade","Berry","Gold Berry","SquirtBottle","Teru-sama","Park Ball","Rainbow Wing","Teru-sama","Brick Piece","Surf Mail","Litebluemail","Portraitmail","Lovely Mail","Eon Mail","Morph Mail","Bluesky Mail","Music Mail","Mirage Mail","Teru-sama","TM01","TM02","TM03","TM04","Fake TM04","TM05","TM06","TM07","TM08","TM09","TM10","TM11","TM12","TM13","TM14","TM15","TM16","TM17","TM18","TM19","TM20","TM21","TM22","TM23","TM24","TM25","TM26","TM27","TM28","Teru-sama","TM29","TM30","TM31","TM32","TM33","TM34","TM35","TM36","TM37","TM38","TM39","TM40","TM41","TM42","TM43","TM44","TM45","TM46","TM47","TM48","TM49","TM50","HM01","HM02","HM03","HM04","HM05","HM06","HM07","HM08","HM09","HM10","HM11","HM12","Cancel"

pokemon = "Missingno.","Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran (f)","Nidorina","Nidoqueen","Nidoran (m)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-oh","Celebi","Uknown","Egg","Unknown","Unknown"

attacks = "No Move","Pound","Karate Chop","DoubleSlap","Comet Punch","Mega Punch","Pay Day","Fire Punch","Ice Punch","ThunderPunch","Scratch","ViceGrip","Guillotine","Razor Wind","Swords Dance","Cut","Gust","Wing Attack","Whirlwind","Fly","Bind","Slam","Vine Whip","Stomp","Double Kick","Mega Kick","Jump Kick","Rolling Kick","Sand-Attack","Headbutt","Horn Attack","Fury Attack","Horn Drill","Tackle","Body Slam","Wrap","Take Down","Thrash","Double-Edge","Tail Whip","Poison Sting","Twineedle","Pin Missile","Leer","Bite","Growl","Roar","Sing","Supersonic","SonicBoom","Disable","Acid","Ember","Flamethrower","Mist","Water Gun","Hydro Pump","Surf","Ice Beam","Blizzard","Psybeam","BubbleBeam","Aurora Beam","Hyper Beam","Peck","Drill Peck","Submission","Low Kick","Counter","Seismic Toss","Strength","Absorb","Mega Drain","Leech Seed","Growth","Razor Leaf","SolarBeam","PoisonPowder","Stun Spore","Sleep Powder","Petal Dance","String Shot","Dragon Rage","Fire Spin","ThunderShock","Thunderbolt","Thunder Wave","Thunder","Rock Throw","Earthquake","Fissure","Dig","Toxic","Confusion","Psychic","Hypnosis","Meditate","Agility","Quick Attack","Rage","Teleport","Night Shade","Mimic","Screech","Double Team","Recover","Harden","Minimize","SmokeScreen","Confuse Ray","Withdraw","Defense Curl","Barrier","Light Screen","Haze","Reflect","Focus Energy","Bide","Metronome","Mirror Move","Selfdestruct","Egg Bomb","Lick","Smog","Sludge","Bone Club","Fire Blast","Waterfall","Clamp","Swift","Skull Bash","Spike Cannon","Constrict","Amnesia","Kinesis","Softboiled","Hi Jump Kick","Glare","Dream Eater","Poison Gas","Barrage","Leech Life","Lovely Kiss","Sky Attack","Transform","Bubble","Dizzy Punch","Spore","Flash","Psywave","Splash","Acid Armor","Crabhammer","Explosion","Fury Swipes","Bonemerang","Rest","Rock Slide","Hyper Fang","Sharpen","Conversion","Tri Attack","Super Fang","Slash","Substitute","Struggle","Sketch","Triple Kick","Thief","Spider Web","Mind Reader","Nightmare","Flame Wheel","Snore","Curse","Flail","Conversion 2","Aeroblast","Cotton Spore","Reversal","Spite","Powder Snow","Protect","Mach Punch","Scary Face","Faint Attack","Sweet Kiss","Belly Drum","Sludge Bomb","Mud-Slap","Octazooka","Spikes","Zap Cannon","Foresight","Destiny Bond","Perish Song","Icy Wind","Detect","Bone Rush","Lock-On","Outrage","Sandstorm","Giga Drain","Endure","Charm","Rollout","False Swipe","Swagger","Milk Drink","Spark","Fury Cutter","Steel Wing","Mean Look","Attract","Sleep Talk","Heal Bell","Return","Present","Frustration","Safeguard","Pain Split","Sacred Fire","Magnitude","DynamicPunch","Megahorn","DragonBreath","Baton Pass","Encore","Pursuit","Rapid Spin","Sweet Scent","Iron Tail","Metal Claw","Vital Throw","Morning Sun","Synthesis","Moonlight","Hidden Power","Cross Chop","Twister","Rain Dance","Sunny Day","Crunch","Mirror Coat","Psych Up","ExtremeSpeed","AncientPower","Shadow Ball","Future Sight","Rock Smash","Whirlpool","Beat Up","Unknown","Unknown","Unknown","Unknown"

locations = "No Data","New Bark Town","Route 29","Cherrygrove City","Route 30","Route 31","Violet City","Sprout Tower","Route 32","Ruins of Alph","Union Cave","Route 33","Azalea Town","Slowpoke Well","Ilex Forest","Route 34","Goldenrod City","Radio Tower","Route 35","National Park","Route 36","Route 37","Ecruteak City","Tin Tower","Burned Tower","Route 38","Route 39","Olivine City","Lighthouse","Battle Tower","Route 40","Whirl Islands","Route 41","Cianwood City","Route 42","Mt. Mortar","Mahogany Town","Route 43","Lake of Rage","Route 44","Ice Path","Blackthorn City","Dragon's Den","Route 45","Dark Cave","Route 46","Silver Cave","Pallet Town","Route 1","Viridian City","Route 2","Pewter City","Route 3","Mt. Moon","Route 4","Cerulean City","Route 24","Route 25","Route 5","Underground","Route 6","Vermilion City","Diglett's Cave","Route 7","Route 8","Route 9","Rock Tunnel","Route 10","Power Plant","Lavender Town","Lav. Radio Tower","Celadon City","Saffron City","Route 11","Route 12","Route 13","Route 14","Route 15","Route 16","Route 17","Route 18","Fuchsia City","Route 19","Route 20","Seafoam Islands","Cinnabar Island","Route 21","Route 22","Victory Road","Route 23","Indigo Plateau","Route 26","Route 27","Tohjo Falls","Route 28","Fast Ship","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Unknown","Empty","Can't tell","Special"

locationmapping = "0","126","177","127","178","179","139","204","180","209","143","181","129","211","214","182","131","208","183","207","184","185","133","205","206","186","187","132","212","205","188","218","189","130","190","216","134","191","135","192","217","136","222","193","220","194","137","138","149","224","150","140","151","198","152","141","172","173","153","210","154","221","197","155","156","157","200","158","201","142","0","144","148","159","160","161","162","163","164","165","166","145","167","168","203","146","169","170","128","171","147","174","175","223","176","226"

filename = open(files, "r+b")
global namelist
namelist = []
global otlist
otlist = []
global boxlist
boxlist = []
global pokedata
pokedata = ""

#the digit 1 = 0xF7
#each box is 9 characters apart
#box actual names start at 0x1903 (0x2703)
# 0x4000 Box 1 - number of pokemon in box
# 0x4001+21 Start of pokemon 1 pkm data
# FIRST BOX OTs start at 0x4296, take up 8 (but really 11?) characters (+661)
# FIRST BOX pokemon NAMES start at 0x4372, take up 11 characters

# 0x4450 START OF BOX 2 (number of pokemon in it)
# 0x46e6 trainer names start (+662 over from start of pokemon)
# 

def ptext(byte): #converts from pokemon text to ascii
    if (byte>245 and byte<=256):
        return(byte-198)
    elif (byte>=97 and byte<191):
        return(byte-128+65)
    elif (byte!=0 and byte!=80):
        return 63

def pokeinfo(party, num, box=0):
    global namelist
    global pokedata
#    print maxr
    if (party):
        filename.seek(354-37*num,1)
    elif (box==0):
        filename.seek(860-21*num,1)
    else:
        filename.seek(860-21*num,1)
    name=[]
    uppercase = True
    for x in range(0,11):
        name.append(int(ByteToHex(filename.read(1)),16)-128+65)
        print chr(name[x])
        if (chr(name[x]).islower()):
            uppercase=False

    pokedata += "\nNickname:  %s" % ''.join(chr(i) for i in name)#.title()

    if (party):
        filename.seek(-365+37*num,1)
    elif (box==0):
        filename.seek(-871+21*num,1)
    else:
        filename.seek(-871+21*num,1)

    namelist.append(name)
    name = []  
    
    species = int(ByteToHex(filename.read(1)), 16)
#    if (uppercase):
#        pokedata += "\nSpecies:  %s"% pokemon[species].upper()
#    else:
    pokedata += "\nSpecies:  %s"% pokemon[species]
        
    hitem =  int(ByteToHex(filename.read(1)), 16)

    pokedata += "\nHold Item:  %s"% (items[hitem])

    #    print "Moveset: ", int(ByteToHex(filename.read(1)), 16), "/", int(ByteToHex(filename.read(1)), 16), "/", int(ByteToHex(filename.read(1)), 16), "/", int(ByteToHex(filename.read(1)), 16)
    pokedata += "\nMoveset:  %s / %s / %s / %s"% (attacks[int(ByteToHex(filename.read(1)), 16)], attacks[int(ByteToHex(filename.read(1)), 16)], attacks[int(ByteToHex(filename.read(1)), 16)], attacks[int(ByteToHex(filename.read(1)), 16)])

    if (party):
        filename.seek(282-37*num,1)
    elif (box==0):
        filename.seek(634-21*num,1)
    else:
        filename.seek(634-21*num,1)
    
    print filename.tell()

    ot = []
    for x in range(0,8):
        ot.append(int(ByteToHex(filename.read(1)),16)-128+65)
        try: print chr(ot[x])
        except: print ot[x]

#    print ot
#    print ot
    pokedata += "\nTrainer Name:  %s" % (''.join(chr(i) for i in ot)).strip("\x11")

    otlist.append(ot)
    if (party):
        filename.seek(-290+37*num,1)
    elif (box==0):
        filename.seek(-642+21*num,1)
    else:
        filename.seek(-642+21*num,1)
#    print filename.tell()



    pokedata+= "\nTrainer ID:  %00005d" % int(ByteToHex(filename.read(2)), 16)
    pokedata+= "\nExperience:  %s"% int(ByteToHex(filename.read(3)), 16)

    pokedata+= "\nEVs:  %s HP / %s ATK / %s DEF / %s SPEED / %s SPECIAL"% (int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16),  int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16))

    pokedata += "\nIV Data:  %s" % int(ByteToHex(filename.read(2)), 16)

    pokedata += "\nMove PP:  %s / %s / %s / %s" %( int(ByteToHex(filename.read(1)), 16), int(ByteToHex(filename.read(1)), 16), int(ByteToHex(filename.read(1)), 16), int(ByteToHex(filename.read(1)), 16))
    friends = int(ByteToHex(filename.read(1)), 16)
    pokedata += "\nFriendship:  %s"% friends#, "(", (friends/255.0)*100, "%)"
    pokedata += "\nPokérus:  %s"% (bool)(int(ByteToHex(filename.read(1)), 16))
    personality = HexToBin((ByteToHex(filename.read(1))))
    
    if ((personality[:2])=="01"):
        daylight = "Morning"
    elif ((personality[:2])=="10"):
        daylight = "Day"
    elif ((personality[:2])=="11"):
        daylight = "Night"
    else:
        daylight = "No Data"

    pokedata+= "\nTime of Day:  %s"% daylight
    pokedata+= "\nMet at Level:  %s"% int((personality[2:]), 2)
    
    personality = HexToBin((ByteToHex(filename.read(1))))
    
    if (personality[:1]=="0"):
        gender = "Male"
    if (personality[:1]=="1"):
        gender = "Female"
    
    pokedata+= "\nOT Gender: %s "% gender
    
    try:
        pokedata += "\nLocation:  %s"%locations[int(personality[1:],2)]
    except:
        pokedata+= "\nLocation:  Uknown (%s)"% (int(personality[1:],2))
    
    pokedata+= "\nLevel:  %s"% int(ByteToHex(filename.read(1)), 16)  
    
    if (party):
        pokedata+= "\nCondition:  %s"% int(ByteToHex(filename.read(1)), 16)
        pokedata+= "\nNot Used Byte:  %s"% int(ByteToHex(filename.read(1)), 16)
        pokedata+= "\nHP Stats:  %s/%s"% (int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16))
        pokedata+= "\nAll Stats:  %s / %s / %s / %s / %s"% (int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16),  int(ByteToHex(filename.read(2)), 16), int(ByteToHex(filename.read(2)), 16))
    print pokedata


def getparty(reveal):
    filename.seek(6757,0)
    maxr = int(ByteToHex(filename.read(1)), 16)
    if (reveal):
        maxr = 6
    filename.seek(6765,0)
    global pokedata
    global allpokedata
    global gui
    allpokedata = ""
    pokedata = ""
    for x in range(1,maxr+1):
        if (x!=1): allpokedata+="\n"
        allpokedata+= "--------------\n PARTY SLOT %s\n--------------"%x
        pokeinfo(True, x-1)
        allpokedata+=pokedata
        allpokedata+="\n"
        pokedata=""
    allpokedata = allpokedata.strip("\x11")
    
    return maxr

def loadPoke(bits=32, x=0):  #loads to allpokedata
    global pokedata
    global allpokedata
    global gui
    allpokedata = ""
    pokedata = ""
    if (bits==32): pokeinfo(True, x)
    else: pokeinfo(False, x)
    allpokedata+=pokedata
    allpokedata+="\n"
    pokedata=""

def loadSpecificPoke(number, box=0):
    if (box==0):
        filename.seek(6757,0)
        

def getpc( box=0):
    filename.seek(11536,0)
    maxr = int(ByteToHex(filename.read(1)),16)
    filename.seek(21,1)
    
    if (box>0):
        filename.seek(16384+1104*(box-1),0)
        maxr = int(ByteToHex(filename.read(1)),16)
        filename.seek(21,1)
    
    
    global pokedata
    global allpokedata
    global gui
    pokedata = ""
    for x in range(1,maxr+1):
        if (box!=0):    
            pokedata+= "-------------------\n %s  SLOT %s\n-------------------"%(boxlist[box-1],x)
        else:
            pokedata+= "----------------\n BOX SLOT %s\n----------------"%x

        pokeinfo(False, x-1, box)
        allpokedata+=pokedata
        allpokedata+="\n\n"
        pokedata=""
    allpokedata = allpokedata.strip("\x11")
    return maxr

def exportthem(maxrp, maxrc):
    global allpokedata
    allpokedata+="\n"
    if (not gui):
        print allpokedata
        dec = raw_input("\nExport Pokémon to Files? (y/n): ").lower()
    else:
        dec = easygui.codebox("Displaying Pokémon Data:","Rare Candy",allpokedata)

    if dec in yes:
        maxr = 0
        if (maxrp!=None):
            PartyToPkm(maxrp,True)
            maxr+=maxrp
        if (maxrc!=None):
            PartyToPkm(maxrc,False)
            maxr+=maxrc

        print "\nAll",maxr,"Pokémon Successfully Exported!"
 
def PartyToPkm(maxr, mode):
    
    if (mode):
        filename.seek(6765,0)
    else:
        filename.seek(11558,0)
    
    for x in range(1,maxr+1):
        global namelist
        pokename = ''.join(chr(i) for i in namelist[x-1])
        try:
            if not os.path.exists("Pokemon"):
                os.makedirs("Pokemon")
            output = "Pokemon/%s.pkm2" % pokename.strip("\x11")
            yfile = open(output, "w")
        
        except:
            if not os.path.exists("%s/Pokemon" % (os.getenv("HOME"))):
                os.makedirs("Pokemon")
            yfile = open("%s/Pokemon/%s.pkm2" % (os.getenv("HOME"), pokename.strip("\x11")),"w")
        if (mode):
            yfile.write(filename.read(48))
        else:
            yfile.write(filename.read(32))
        yfile.close()
        print "[exported",(''.join(chr(i) for i in namelist[x-1])).lower(),"successfully]" 

def gettrainer():
    print "nope"

def getFormat(exp):
    if (exp==1):
        return ".pkm2"
    elif (exp==2):
        return ".pkm"
    elif (exp==3):
        return ".pkm and .pkm2"

def preferences():
    print "Select Preference to Edit:"
    print "\t1) Export Format: ", getFormat(exp)
    print "\t2) Export Location: ", destination
    print "\t3) <--- Go Back"

    choice = input("Enter the Number: ")

def getBoxList():
    filename.seek(6403,0)
    
    olddefbox=['BOX1', 'BOX2', 'BOX3', 'BOX4', 'BOX5', 'BOX6', 'BOX7', 'BOX8', 'BOX9', 'BOX10','BOX11','BOX12','BOX13','BOX14']
    newdefbox=['First Box', 'Second Box', 'Third Box', 'Fourth Box', 'Fifth Box', 'Sixth Box', 'Seventh Box', 'Eighth Box', 'Ninth Box', 'Tenth Box','Eleventh Box','Twelfth Box','Thirteenth Box','Fourteenth Box']
    
    for y in range(0,14):
        bl = []
        for x in range(0,9):
            byte = int(ByteToHex(filename.read(1)),16)
            if (ptext(byte)!=None):
                bl.append(ptext(byte))
        boxlist.append((''.join(chr(i) for i in bl)).strip("\x11"))
        if (boxlist[y]==olddefbox[y]): boxlist[y]=newdefbox[y]
            
#   Old function for renaming duplicate boxes, but the game does it!
#    boxcountings = [0,0,0,0,0,0,0,0,0,0]
#
#    for x in range(01,10):
#        for y in range(0,10):
#            if (boxlist[x]==boxlist[y] and x!=y):
#                boxcountings[x]+=1
#                boxlist[y] += " %s" % (boxcountings[x]+1)
#
#    print boxcountings
#        boxlist[y]+= "  (%s)"%(y+1)
#    print boxlist


#    for x in range(0,9):
#        boxlist.append(filename.read(8).strip("\x11"))
#        boxlist[x]+=" (Box %s)"%(x+1)


def menu():
    
    if (os.path.getsize(files) == 48):
        loadPoke(48)
        
    elif (os.path.getsize(files) == 32):
        loadPoke()

    elif (os.path.getsize(files) != 32768):
        if (gui): msgbox("Invalid filesize, should be 32768.\nExiting...")
        else: print "Invalid filesize, should be 32768.\nExiting..."
        sys.exit(-1)

#    multchoicebox("Export which Pokémon?","Rare Candy",["Something","Something2","Kiwis"])

    if (len(boxlist)==0):
        getBoxList()
    
    if (gui):
        choice = easygui.choicebox("Choose data to export:","Rare Candy",["Party","Current Box","All Pokémon"]+(boxlist)+["Trainer Info"], False)
    else:
        choice = raw_input("Select Items to Export:\n\t1) Party\n\t2) Current Box\n\t3) All Pokémon\n\t4) Trainer Info\n,Enter the Number: ")
    
    global namelist
    namelist = []
    global otlist
    otlist = []

    if (choice==None):
        return False

    global allpokedata

    if (choice=="1" or choice=="Party"):
        exportthem(getparty(False), None)
    elif (choice=="2" or choice=="Current Box".decode('utf8')):
        allpokedata=""
        exportthem(None, getpc())
    elif (choice=="5" or choice=="Hidden Party".decode('utf8')):
        exportthem(getparty(True), None)
    elif (choice=="3" or choice=="All Pokémon".decode('utf8')):
        allpokedata=""
        exportthem(getparty(False), getpc())
    elif (choice=="4" or choice=="Trainer Info"):
        gettrainer()
#    elif (choice=="6"):
#        preferences()
    elif (choice=="exit" or choice=="quit" or choice == "stop" or choice=="x"):
        return False

    elif choice in boxlist:
        for x in range(0,14):
            if (choice==boxlist[x]):
                allpokedata=""
                exportthem(None, getpc(x+1))
#                print "you picked box number %s"%(x+1) # zero is current
    return True

while(menu()):
    print ""
filename.close();
