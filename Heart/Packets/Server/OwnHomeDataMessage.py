from Heart.Record.ByteStreamHelper import ByteStreamHelper
from Heart.Packets.PiranhaMessage import PiranhaMessage
from DB.DatabaseHandler import DatabaseHandler

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)
        # LogicClientHome::encode
        # LogicDailyData::encode
        self.writeVInt(1688816070) # timestamp
        self.writeVInt(1191532375) # timestamp
        self.writeVInt(2023189) # timestamp
        self.writeVInt(73530) # timestamp

        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(player.TrophyRoadTier) # Trophy Road Tier
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(26) # played Game Mode
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(0) # selected skins

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.OwnedSkins)) # Owned skins array
        for x in player.OwnedSkins:
            self.writeDataReference(29, x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0) # Leaderboard region
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(0) # tokens used in battle
        self.writeVInt(2) # control mode
        self.writeBoolean(True) # battle hints
        self.writeVInt(115) # maybe starr drop timer ? #v50
        self.writeVInt(335442) # trophy league timer
        self.writeVInt(1001442) # power play timer
        self.writeVInt(5778642) # Brawl pass season timer

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0) # drop chance of characters in boxes

        self.writeBoolean(True)
        self.writeVInt(2) # token doubler  new tag state
        self.writeVInt(2) # event tickets new tag state
        self.writeVInt(2) # coins pack new tag state
        self.writeVInt(0) # name change cost
        self.writeVInt(0) # timer for next name change

        self.writeVInt(1) # Shop Offers

        self.writeVInt(1) # RewardCount

        self.writeVInt(56)  # ItemType
        self.writeVInt(1) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(100000000000000) # Time
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # Daily Offer
        self.writeVInt(0) # Old price
        self.writeString("BSDS V57") # Text
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeString("offer_bgr_sb") # Background
        self.writeVInt(0)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(0) # Type Benefit
        self.writeVInt(0) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        self.writeVInt(20) # tokens for battle
        self.writeVInt(1428) # timer until new token

        self.writeVInt(0) #count

        self.writeVInt(1) #unk
        self.writeVInt(30) #unk

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.SelectedBrawlers[0]) # selected brawler

        self.writeString(player.Region) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(6) # count
        self.writeVInt(1) # resources id
        self.writeVInt(9) # resources gained
        self.writeVInt(1) # resources id
        self.writeVInt(22) # resources gained
        self.writeVInt(3) # resources id
        self.writeVInt(25) # resources gained
        self.writeVInt(1) # resources id
        self.writeVInt(24) # resources gained
        self.writeVInt(0) # resources id
        self.writeVInt(15) # resources gained
        self.writeVInt(32447) # resources id
        self.writeVInt(28) # resources gained

        self.writeVInt(0) # count 0
        
        # BrawlPassSeasonData::encode
        self.writeVInt(1)
        for season in range(1):
            self.writeVInt(30 - 1) # season id
            self.writeVInt(40000) # season token collected
            self.writeBoolean(True) # ?
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True)
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        # BrawlPassSeasonData::encode end

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) # club league quest count

        self.writeBoolean(True) # Vanity items
        self.writeVInt(len(player.OwnedThumbnails)+len(player.OwnedPins))
        for x in player.OwnedThumbnails:
            self.writeVInt(28)
            self.writeVInt(x)
            self.writeVInt(0)
        for x in player.OwnedPins:
            self.writeVInt(52)
            self.writeVInt(x)
            self.writeVInt(0)


        self.writeBoolean(False) # Power league season data
        # Power League Data Array Start #
        #self.writeVInt(1) # Season
        #self.writeVInt(10000) # Rank Solo League (Tokens)
        #self.writeVInt(1) # Season
        #self.writeVInt(10000) # Rank Team League (Tokens)
        #self.writeVInt(0) # Unk
        #self.writeVInt(10000) # High Rank Solo League (Tokens)
        #self.writeVInt(0) # Unk
        #self.writeVInt(10000) # High Rank Team League (Tokens)
        #self.writeVInt(0) # Unk
        #self.writeBoolean(True) # ?
        #self.writeVInt(0) # ?
        #self.writeVInt(0) # ?
        # Power League Data Array End #

        self.writeInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, 85)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # LogicDailyData::encode end

        # LogicConfData::encode
        self.writeVInt(2023189) # Timestamp for begin

        self.writeVInt(38) # Event array
        self.writeVInt(1) # GemGrab
        self.writeVInt(2) # Heist
        self.writeVInt(3) # Bounty
        self.writeVInt(4)
        self.writeVInt(5) # BrawlBall
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12) # map maker candidate
        self.writeVInt(13) # map maker winner
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) # "mystery" mode
        self.writeVInt(19)
        self.writeVInt(20) # championship challenge
        self.writeVInt(21) 
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32) # BrawlBall5v5
        self.writeVInt(33) # GemGrab5v5
        self.writeVInt(34) # hypercharge 
        self.writeVInt(35) # mega pig
        self.writeVInt(36)
        self.writeVInt(37)
        self.writeVInt(38)

        self.writeVInt(1)  # event count

        self.writeVInt(-1)
        self.writeVInt(1) # event id
        self.writeVInt(1) # v52
        self.writeVInt(0)
        self.writeVInt(72292)
        self.writeVInt(10) 
        self.writeDataReference(15, 636) # map id 
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeString("")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) # count
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False) # MapMaker map structure array
        self.writeVInt(0)
        self.writeBoolean(False) # Power League array entry
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeVInt(0) # new count v51
        self.writeVInt(0) # new count v51
        self.writeVInt(0) # new count v51
        self.writeBoolean(False) 
        self.writeBoolean(False) 
        self.writeBoolean(False) 

        self.writeVInt(0) # upcoming event count
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        # ReleaseEntry::encode
        self.writeVInt(0) # Locked Brawler
        for i in range(0):
            self.writeDataReference(16, 83)
            self.writeInt(3600) # Time
            self.writeInt(3500)
            self.writeInt(3400)
            self.writeBoolean(True)
        # ReleaseEntry::encode
        
        # IntValueEntry::encode
        self.writeVInt(1)
        self.writeVInt(41000108) # theme
        self.writeVInt(1)
        # IntValueEntry::encode end

        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)

        ByteStreamHelper.encodeIntList(self, [0, 29, 79, 169, 349, 699])
        ByteStreamHelper.encodeIntList(self, [0, 160, 450, 500, 1250, 2500])

        self.writeLong(0, 1) # Player ID

        self.writeVInt(0) # Notification factory
        
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(0) # gatcha drop
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeBoolean(True) # Starr Road
        for i in range(7):
            self.writeVInt(0)

        self.writeVInt(len(player.OwnedBrawlers)) # Mastery
        for brawlerID,brawlerData in player.OwnedBrawlers.items():
            self.writeVInt(24800) #Mastery Points
            self.writeVInt(0) #Claimed Rewards
            self.writeDataReference(16, brawlerID) #brawlers

        #BattleCard
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0) #Brawler's BattleCards

        self.writeVInt(14)
        for i in range(14):
            self.writeDataReference(80, i)
            self.writeVInt(-1)
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeInt(-1435281534)
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(86400*24)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False) 
        self.writeVInt(0)

        # end LogicClientHome::encode

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(player.ID[0], player.ID[1])
        self.writeStringReference(player.Name)
        self.writeBoolean(player.Registered)
        self.writeInt(-1)

        self.writeVInt(17)
        unlocked_brawler = [i['CardID'] for x,i in player.OwnedBrawlers.items()]
        self.writeVInt(len(unlocked_brawler) + 3)
        for x in unlocked_brawler:
            self.writeDataReference(23, x)
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins) # coins

        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        self.writeVInt(300000) # alien fame 3

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.Blings) # blings

        self.writeVInt(len(player.OwnedBrawlers)) # HeroScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.OwnedBrawlers)) # HeroHighScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"])

        self.writeVInt(0) # Array

        self.writeVInt(0) # HeroPower
        
        self.writeVInt(len(player.OwnedBrawlers)) # HeroLevel
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["PowerLevel"]-1)

        self.writeVInt(0) # hero star power gadget and hypercharge

        self.writeVInt(len(player.OwnedBrawlers)) # HeroSeenState
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(2)

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array

        self.writeVInt(player.Gems) # Diamonds
        self.writeVInt(player.Gems) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion
