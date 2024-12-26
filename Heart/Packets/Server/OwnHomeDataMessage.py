from Heart.Record.ByteStreamHelper import ByteStreamHelper
from Heart.Packets.PiranhaMessage import PiranhaMessage
from datetime import datetime
from DB.DatabaseHandler import DatabaseHandler

import json
import time
import random

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(player.ID)

        self.writeVInt(1688816070)
        self.writeVInt(1191532375)
        self.writeVInt(2023189)
        self.writeVInt(73530)

        self.writeVInt(player.Trophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000)
        self.writeVInt(player.HighestTrophies + 5000) 
        self.writeVInt(player.TrophyRoadTier + 200)
        self.writeVInt(player.Experience)
        self.writeDataReference(28, player.Thumbnail)
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26)
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(len(player.SelectedSkins))
        for brawlerID in player.SelectedSkins:
            self.writeDataReference(29, player.SelectedSkins[str(brawlerID)])

        self.writeVInt(0)

        self.writeVInt(0)
        
        self.writeVInt(len(player.OwnedSkins))
        for x in player.OwnedSkins:
            self.writeDataReference(29, x)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeBoolean(True)
        self.writeVInt(115)
        self.writeVInt(335442)
        self.writeVInt(1001442)
        self.writeVInt(5778642) 

        self.writeVInt(120)
        self.writeVInt(200)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(1) # Shop Offers

        self.writeVInt(1) # RewardCount

        self.writeVInt(56)  # ItemType
        self.writeVInt(1337) # Amount
        self.writeDataReference(0)  # CsvID
        self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
        self.writeVInt(0) # Cost
        self.writeVInt(0) # Time
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
        self.writeString("offer_bgr_sushi") # Background
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
        
        self.writeVInt(20)
        self.writeVInt(1428)

        self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(30)

        self.writeByte(1) # count brawlers selected
        self.writeDataReference(16, player.SelectedBrawlers[0]) # selected brawler

        self.writeString(player.Region) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(21)
        self.writeDataReference(2, 1)  # Unknown
        self.writeDataReference(3, 0)  # Tokens Gained
        self.writeDataReference(4, 0)  # Trophies Gained
        self.writeDataReference(6, 0)  # Demo Account
        self.writeDataReference(7, 0)  # Invites Blocked
        self.writeDataReference(8, 0)  # Star Points Gained
        self.writeDataReference(9, 1)  # Show Star Points
        self.writeDataReference(10, 0)  # Power Play Trophies Gained
        self.writeDataReference(12, 1)  # Unknown
        self.writeDataReference(14, 0)  # Coins Gained
        self.writeDataReference(15, 1)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeDataReference(16, 1)
        self.writeDataReference(17, 0)  # Team Chat Muted
        self.writeDataReference(18, 1)  # Esport Button
        self.writeDataReference(19, 0)  # Champion Ship Lives Buy Popup
        self.writeDataReference(20, 0)  # Gems Gained
        self.writeDataReference(21, 1)  # Looking For Team State
        self.writeDataReference(22, 1)
        self.writeDataReference(23, 0)  # Club Trophies Gained
        self.writeDataReference(24, 1)  # Have already watched club league stupid animation
        self.writeDataReference(32447, 28)

        self.writeVInt(0)

        Free32LVL = 0
        Free64LVL = 0
        Free96LVL = 0

        Pass32LVL = 0
        Pass64LVL = 0
        Pass96LVL = 0

        for LVL in player.BrawlPassFreeLevel:
            if LVL < 30:
                Free32LVL += (2**(LVL + 2))
            if LVL > 30:
                Free64LVL += (2**(LVL-30))
            if LVL > 61:
                Free96LVL += (1**(LVL-61))
        
        for LVL in player.BrawlPassLevel:
            if LVL < 30:
                Pass32LVL += (2**(LVL + 2))
            if LVL > 29:
                Pass64LVL += (2**(LVL-30))
            if LVL > 60:
                Pass96LVL += (1**(LVL-61))
        
        if player.BrawlPassBuy == 0:
            BrawlPassActive = False
            BrawlPassPlusActive = False
        if player.BrawlPassBuy == 1:
            BrawlPassActive = True
            BrawlPassPlusActive = False
        if player.BrawlPassBuy == 2:
            BrawlPassActive = True
            BrawlPassPlusActive = True

        # BrawlPassSeasonData::encode
        self.writeVInt(1)
        for season in range(1):
            self.writeVInt(29)
            self.writeVInt(0)
            self.writeBoolean(True) # BrawlPass buy
            self.writeVInt(0)
            self.writeBoolean(False)

            self.writeBoolean(True)
            self.writeInt(Pass32LVL)
            self.writeInt(Pass64LVL)
            self.writeInt(Pass96LVL)
            self.writeInt(0)

            self.writeBoolean(True)
            self.writeInt(Free32LVL)
            self.writeInt(Free64LVL)
            self.writeInt(Free96LVL)
            self.writeInt(0)

            self.writeBoolean(True) # BrawlPass + Buy
            self.writeBoolean(True)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        # BrawlPassSeasonData::encode

        self.writeBoolean(True)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) 

        self.writeBoolean(True) # Vanity items
        self.writeVInt(len(player.OwnedThumbnails) + len(player.OwnedPins) + 1)
        for ThumbnailID in player.OwnedThumbnails:
            self.writeDataReference(28, ThumbnailID)
            self.writeVInt(0)
        for PinID in player.OwnedPins:
            self.writeDataReference(52, PinID)
            self.writeVInt(0)
        for i in range(1):
            self.writeDataReference(28, 186) # IconCreator
            self.writeVInt(0)


        self.writeBoolean(False) # Power league season data

        self.writeInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, 82) # favoriteBrawler
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2023189)

        self.writeVInt(38) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12)
        self.writeVInt(13) 
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) 
        self.writeVInt(19)
        self.writeVInt(20)
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
        self.writeVInt(32)
        self.writeVInt(33)
        self.writeVInt(34)
        self.writeVInt(35)
        self.writeVInt(36)
        self.writeVInt(37)
        self.writeVInt(38)

        self.writeVInt(1)

        self.writeVInt(-1)
        self.writeVInt(1)
        self.writeVInt(1)
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
        self.writeVInt(0)
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
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeBoolean(False) 
        self.writeBoolean(False) 
        self.writeBoolean(False) 


        self.writeVInt(0)
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800])
        ByteStreamHelper.encodeIntList(self, [30, 80, 170, 360]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [300, 880, 2040, 4680]) # Shop Coins Amount

        # ReleaseEntry::encode
        self.writeVInt(0) 
        # ReleaseEntry::encode

        # IntValueEntry::encode
        self.writeVInt(1)
        for i in range(1):
            self.writeDataReference(41000108, 1) # ThemeID
        # IntValueEntry::encode end

        # TimedIntValueEntry::encode
        self.writeVInt(0) 
        # TimedIntValueEntry::encode end
        # CustomEvent::encode
        self.writeVInt(1)
        for i in range(1):
            self.writeVInt(1)
            self.writeVInt(1)
            for i in range(3):
                self.writeString('ss')
                self.writeVInt(0)
            self.writeVInt(1)
        # CustomEvent::encode end
        self.writeVInt(0)
        for i in range(0):
            self.writeDataReference(16, 1)
            self.writeString('fimos')
            self.writeDataReference(16, 2)
            self.writeVInt(0)
            self.writeBoolean(True)
            for i in range(1):
                self.writeString('penis')
                self.writeVInt(0)
            self.writeBoolean(True)
            for i in range(1):
                self.writeString('penis 1488')
                self.writeVInt(0)
            self.writeVInt(0)

            self.writeBoolean(False)
            self.writeVInt(1)
            self.writeString('pesok')
        self.writeVInt(1)
        for i in range(1):
            self.writeVInt(3)
            self.writeVInt(3)
            self.writeString('pie')
            self.writeString('lol')
            self.writeVInt(3)
            self.writeVInt(1)
            for i in range(1):
                self.writeBoolean(True)
                self.writeVInt(16)
                self.writeVInt(1)
                self.writeDataReference(0, 0)
                self.writeVInt(0)
            self.writeBoolean(True)
            self.writeString('string')
            self.writeVInt(0)
            self.writeDataReference(89, 3)
            self.writeVInt(3)
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
        self.writeVInt(0)
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

        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False) 
        self.writeVInt(0)

        # end LogicClientHome

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
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        self.writeVInt(149100)

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(player.Blings)

        self.writeVInt(len(player.OwnedBrawlers)) # HeroScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["Trophies"])

        self.writeVInt(len(player.OwnedBrawlers)) # HeroHighScore
        for x,i in player.OwnedBrawlers.items():
            self.writeDataReference(16, x)
            self.writeVInt(-1)
            self.writeVInt(i["HighestTrophies"] + 1250)

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
