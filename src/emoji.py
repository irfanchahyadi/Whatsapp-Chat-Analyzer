CLEANER = ['\ufe0f', '\u2068', '\u2069']


# scrape from https://emojipedia.org/whatsapp/2.19.352/
EMOJI = {
    u'\U0001F600': 0,  # Grinning Face
    u'\U0001F603': 1,  # Grinning Face with Big Eyes
    u'\U0001F604': 2,  # Grinning Face with Smiling Eyes
    u'\U0001F601': 3,  # Beaming Face with Smiling Eyes
    u'\U0001F606': 4,  # Grinning Squinting Face
    u'\U0001F605': 5,  # Grinning Face with Sweat
    u'\U0001F923': 6,  # Rolling on the Floor Laughing
    u'\U0001F602': 7,  # Face with Tears of Joy
    u'\U0001F642': 8,  # Slightly Smiling Face
    u'\U0001F643': 9,  # Upside-Down Face
    u'\U0001F609': 10,  # Winking Face
    u'\U0001F60A': 11,  # Smiling Face with Smiling Eyes
    u'\U0001F607': 12,  # Smiling Face with Halo
    u'\U0001F970': 13,  # Smiling Face with Hearts
    u'\U0001F60D': 14,  # Smiling Face with Heart-Eyes
    u'\U0001F929': 15,  # Star-Struck
    u'\U0001F618': 16,  # Face Blowing a Kiss
    u'\U0001F617': 17,  # Kissing Face
    u'\U0000263A': 18,  # Smiling Face
    u'\U0001F61A': 19,  # Kissing Face with Closed Eyes
    u'\U0001F619': 20,  # Kissing Face with Smiling Eyes
    u'\U0001F60B': 21,  # Face Savoring Food
    u'\U0001F61B': 22,  # Face with Tongue
    u'\U0001F61C': 23,  # Winking Face with Tongue
    u'\U0001F92A': 24,  # Zany Face
    u'\U0001F61D': 25,  # Squinting Face with Tongue
    u'\U0001F911': 26,  # Money-Mouth Face
    u'\U0001F917': 27,  # Hugging Face
    u'\U0001F92D': 28,  # Face with Hand Over Mouth
    u'\U0001F92B': 29,  # Shushing Face
    u'\U0001F914': 30,  # Thinking Face
    u'\U0001F910': 31,  # Zipper-Mouth Face
    u'\U0001F928': 32,  # Face with Raised Eyebrow
    u'\U0001F610': 33,  # Neutral Face
    u'\U0001F611': 34,  # Expressionless Face
    u'\U0001F636': 35,  # Face Without Mouth
    u'\U0001F60F': 36,  # Smirking Face
    u'\U0001F612': 37,  # Unamused Face
    u'\U0001F644': 38,  # Face with Rolling Eyes
    u'\U0001F62C': 39,  # Grimacing Face
    u'\U0001F925': 40,  # Lying Face
    u'\U0001F60C': 41,  # Relieved Face
    u'\U0001F614': 42,  # Pensive Face
    u'\U0001F62A': 43,  # Sleepy Face
    u'\U0001F924': 44,  # Drooling Face
    u'\U0001F634': 45,  # Sleeping Face
    u'\U0001F637': 46,  # Face with Medical Mask
    u'\U0001F912': 47,  # Face with Thermometer
    u'\U0001F915': 48,  # Face with Head-Bandage
    u'\U0001F922': 49,  # Nauseated Face
    u'\U0001F92E': 50,  # Face Vomiting
    u'\U0001F927': 51,  # Sneezing Face
    u'\U0001F975': 52,  # Hot Face
    u'\U0001F976': 53,  # Cold Face
    u'\U0001F974': 54,  # Woozy Face
    u'\U0001F635': 55,  # Dizzy Face
    u'\U0001F92F': 56,  # Exploding Head
    u'\U0001F920': 57,  # Cowboy Hat Face
    u'\U0001F973': 58,  # Partying Face
    u'\U0001F60E': 59,  # Smiling Face with Sunglasses
    u'\U0001F913': 60,  # Nerd Face
    u'\U0001F9D0': 61,  # Face with Monocle
    u'\U0001F615': 62,  # Confused Face
    u'\U0001F61F': 63,  # Worried Face
    u'\U0001F641': 64,  # Slightly Frowning Face
    u'\U00002639': 65,  # Frowning Face
    u'\U0001F62E': 66,  # Face with Open Mouth
    u'\U0001F62F': 67,  # Hushed Face
    u'\U0001F632': 68,  # Astonished Face
    u'\U0001F633': 69,  # Flushed Face
    u'\U0001F97A': 70,  # Pleading Face
    u'\U0001F626': 71,  # Frowning Face with Open Mouth
    u'\U0001F627': 72,  # Anguished Face
    u'\U0001F628': 73,  # Fearful Face
    u'\U0001F630': 74,  # Anxious Face with Sweat
    u'\U0001F625': 75,  # Sad but Relieved Face
    u'\U0001F622': 76,  # Crying Face
    u'\U0001F62D': 77,  # Loudly Crying Face
    u'\U0001F631': 78,  # Face Screaming in Fear
    u'\U0001F616': 79,  # Confounded Face
    u'\U0001F623': 80,  # Persevering Face
    u'\U0001F61E': 81,  # Disappointed Face
    u'\U0001F613': 82,  # Downcast Face with Sweat
    u'\U0001F629': 83,  # Weary Face
    u'\U0001F62B': 84,  # Tired Face
    u'\U0001F971': 85,  # Yawning Face
    u'\U0001F624': 86,  # Face with Steam From Nose
    u'\U0001F621': 87,  # Pouting Face
    u'\U0001F620': 88,  # Angry Face
    u'\U0001F92C': 89,  # Face with Symbols on Mouth
    u'\U0001F608': 90,  # Smiling Face with Horns
    u'\U0001F47F': 91,  # Angry Face with Horns
    u'\U0001F480': 92,  # Skull
    u'\U00002620': 93,  # Skull and Crossbones
    u'\U0001F4A9': 94,  # Pile of Poo
    u'\U0001F921': 95,  # Clown Face
    u'\U0001F479': 96,  # Ogre
    u'\U0001F47A': 97,  # Goblin
    u'\U0001F47B': 98,  # Ghost
    u'\U0001F47D': 99,  # Alien
    u'\U0001F47E': 100,  # Alien Monster
    u'\U0001F916': 101,  # Robot
    u'\U0001F63A': 102,  # Grinning Cat
    u'\U0001F638': 103,  # Grinning Cat with Smiling Eyes
    u'\U0001F639': 104,  # Cat with Tears of Joy
    u'\U0001F63B': 105,  # Smiling Cat with Heart-Eyes
    u'\U0001F63C': 106,  # Cat with Wry Smile
    u'\U0001F63D': 107,  # Kissing Cat
    u'\U0001F640': 108,  # Weary Cat
    u'\U0001F63F': 109,  # Crying Cat
    u'\U0001F63E': 110,  # Pouting Cat
    u'\U0001F648': 111,  # See-No-Evil Monkey
    u'\U0001F649': 112,  # Hear-No-Evil Monkey
    u'\U0001F64A': 113,  # Speak-No-Evil Monkey
    u'\U0001F48B': 114,  # Kiss Mark
    u'\U0001F48C': 115,  # Love Letter
    u'\U0001F498': 116,  # Heart with Arrow
    u'\U0001F49D': 117,  # Heart with Ribbon
    u'\U0001F496': 118,  # Sparkling Heart
    u'\U0001F497': 119,  # Growing Heart
    u'\U0001F493': 120,  # Beating Heart
    u'\U0001F49E': 121,  # Revolving Hearts
    u'\U0001F495': 122,  # Two Hearts
    u'\U0001F49F': 123,  # Heart Decoration
    u'\U00002763': 124,  # Heart Exclamation
    u'\U0001F494': 125,  # Broken Heart
    u'\U00002764': 126,  # Red Heart
    u'\U0001F9E1': 127,  # Orange Heart
    u'\U0001F49B': 128,  # Yellow Heart
    u'\U0001F49A': 129,  # Green Heart
    u'\U0001F499': 130,  # Blue Heart
    u'\U0001F49C': 131,  # Purple Heart
    u'\U0001F90E': 132,  # Brown Heart
    u'\U0001F5A4': 133,  # Black Heart
    u'\U0001F90D': 134,  # White Heart
    u'\U0001F4AF': 135,  # Hundred Points
    u'\U0001F4A2': 136,  # Anger Symbol
    u'\U0001F4A5': 137,  # Collision
    u'\U0001F4AB': 138,  # Dizzy
    u'\U0001F4A6': 139,  # Sweat Droplets
    u'\U0001F4A8': 140,  # Dashing Away
    u'\U0001F573': 141,  # Hole
    u'\U0001F4A3': 142,  # Bomb
    u'\U0001F4AC': 143,  # Speech Balloon
    u'\U0001F441\U0000200D\U0001F5E8': 144,  # Eye in Speech Bubble
    u'\U0001F5E8': 145,  # Left Speech Bubble
    u'\U0001F5EF': 146,  # Right Anger Bubble
    u'\U0001F4AD': 147,  # Thought Balloon
    u'\U0001F4A4': 148,  # Zzz
    u'\U0001F44B': 149,  # Waving Hand
    u'\U0001F44B\U0001F3FB\U0001F3FB': 150,  # Waving Hand: Light Skin Tone
    u'\U0001F44B\U0001F3FC\U0001F3FC': 151,  # Waving Hand: Medium-Light Skin Tone
    u'\U0001F44B\U0001F3FD\U0001F3FD': 152,  # Waving Hand: Medium Skin Tone
    u'\U0001F44B\U0001F3FE\U0001F3FE': 153,  # Waving Hand: Medium-Dark Skin Tone
    u'\U0001F44B\U0001F3FF\U0001F3FF': 154,  # Waving Hand: Dark Skin Tone
    u'\U0001F91A': 155,  # Raised Back of Hand
    u'\U0001F91A\U0001F3FB\U0001F3FB': 156,  # Raised Back of Hand: Light Skin Tone
    u'\U0001F91A\U0001F3FC\U0001F3FC': 157,  # Raised Back of Hand: Medium-Light Skin Tone
    u'\U0001F91A\U0001F3FD\U0001F3FD': 158,  # Raised Back of Hand: Medium Skin Tone
    u'\U0001F91A\U0001F3FE\U0001F3FE': 159,  # Raised Back of Hand: Medium-Dark Skin Tone
    u'\U0001F91A\U0001F3FF\U0001F3FF': 160,  # Raised Back of Hand: Dark Skin Tone
    u'\U0001F590': 161,  # Hand with Fingers Splayed
    u'\U0001F590\U0001F3FB\U0001F3FB': 162,  # Hand with Fingers Splayed: Light Skin Tone
    u'\U0001F590\U0001F3FC\U0001F3FC': 163,  # Hand with Fingers Splayed: Medium-Light Skin Tone
    u'\U0001F590\U0001F3FD\U0001F3FD': 164,  # Hand with Fingers Splayed: Medium Skin Tone
    u'\U0001F590\U0001F3FE\U0001F3FE': 165,  # Hand with Fingers Splayed: Medium-Dark Skin Tone
    u'\U0001F590\U0001F3FF\U0001F3FF': 166,  # Hand with Fingers Splayed: Dark Skin Tone
    u'\U0000270B': 167,  # Raised Hand
    u'\U0000270B\U0001F3FB\U0001F3FB': 168,  # Raised Hand: Light Skin Tone
    u'\U0000270B\U0001F3FC\U0001F3FC': 169,  # Raised Hand: Medium-Light Skin Tone
    u'\U0000270B\U0001F3FD\U0001F3FD': 170,  # Raised Hand: Medium Skin Tone
    u'\U0000270B\U0001F3FE\U0001F3FE': 171,  # Raised Hand: Medium-Dark Skin Tone
    u'\U0000270B\U0001F3FF\U0001F3FF': 172,  # Raised Hand: Dark Skin Tone
    u'\U0001F596': 173,  # Vulcan Salute
    u'\U0001F596\U0001F3FB\U0001F3FB': 174,  # Vulcan Salute: Light Skin Tone
    u'\U0001F596\U0001F3FC\U0001F3FC': 175,  # Vulcan Salute: Medium-Light Skin Tone
    u'\U0001F596\U0001F3FD\U0001F3FD': 176,  # Vulcan Salute: Medium Skin Tone
    u'\U0001F596\U0001F3FE\U0001F3FE': 177,  # Vulcan Salute: Medium-Dark Skin Tone
    u'\U0001F596\U0001F3FF\U0001F3FF': 178,  # Vulcan Salute: Dark Skin Tone
    u'\U0001F44C': 179,  # OK Hand
    u'\U0001F44C\U0001F3FB\U0001F3FB': 180,  # OK Hand: Light Skin Tone
    u'\U0001F44C\U0001F3FC\U0001F3FC': 181,  # OK Hand: Medium-Light Skin Tone
    u'\U0001F44C\U0001F3FD\U0001F3FD': 182,  # OK Hand: Medium Skin Tone
    u'\U0001F44C\U0001F3FE\U0001F3FE': 183,  # OK Hand: Medium-Dark Skin Tone
    u'\U0001F44C\U0001F3FF\U0001F3FF': 184,  # OK Hand: Dark Skin Tone
    u'\U0001F90F': 185,  # Pinching Hand
    u'\U0001F90F\U0001F3FB\U0001F3FB': 186,  # Pinching Hand: Light Skin Tone
    u'\U0001F90F\U0001F3FC\U0001F3FC': 187,  # Pinching Hand: Medium-Light Skin Tone
    u'\U0001F90F\U0001F3FD\U0001F3FD': 188,  # Pinching Hand: Medium Skin Tone
    u'\U0001F90F\U0001F3FE\U0001F3FE': 189,  # Pinching Hand: Medium-Dark Skin Tone
    u'\U0001F90F\U0001F3FF\U0001F3FF': 190,  # Pinching Hand: Dark Skin Tone
    u'\U0000270C': 191,  # Victory Hand
    u'\U0000270C\U0001F3FB\U0001F3FB': 192,  # Victory Hand: Light Skin Tone
    u'\U0000270C\U0001F3FC\U0001F3FC': 193,  # Victory Hand: Medium-Light Skin Tone
    u'\U0000270C\U0001F3FD\U0001F3FD': 194,  # Victory Hand: Medium Skin Tone
    u'\U0000270C\U0001F3FE\U0001F3FE': 195,  # Victory Hand: Medium-Dark Skin Tone
    u'\U0000270C\U0001F3FF\U0001F3FF': 196,  # Victory Hand: Dark Skin Tone
    u'\U0001F91E': 197,  # Crossed Fingers
    u'\U0001F91E\U0001F3FB\U0001F3FB': 198,  # Crossed Fingers: Light Skin Tone
    u'\U0001F91E\U0001F3FC\U0001F3FC': 199,  # Crossed Fingers: Medium-Light Skin Tone
    u'\U0001F91E\U0001F3FD\U0001F3FD': 200,  # Crossed Fingers: Medium Skin Tone
    u'\U0001F91E\U0001F3FE\U0001F3FE': 201,  # Crossed Fingers: Medium-Dark Skin Tone
    u'\U0001F91E\U0001F3FF\U0001F3FF': 202,  # Crossed Fingers: Dark Skin Tone
    u'\U0001F91F': 203,  # Love-You Gesture
    u'\U0001F91F\U0001F3FB\U0001F3FB': 204,  # Love-You Gesture: Light Skin Tone
    u'\U0001F91F\U0001F3FC\U0001F3FC': 205,  # Love-You Gesture: Medium-Light Skin Tone
    u'\U0001F91F\U0001F3FD\U0001F3FD': 206,  # Love-You Gesture: Medium Skin Tone
    u'\U0001F91F\U0001F3FE\U0001F3FE': 207,  # Love-You Gesture: Medium-Dark Skin Tone
    u'\U0001F91F\U0001F3FF\U0001F3FF': 208,  # Love-You Gesture: Dark Skin Tone
    u'\U0001F918': 209,  # Sign of the Horns
    u'\U0001F918\U0001F3FB\U0001F3FB': 210,  # Sign of the Horns: Light Skin Tone
    u'\U0001F918\U0001F3FC\U0001F3FC': 211,  # Sign of the Horns: Medium-Light Skin Tone
    u'\U0001F918\U0001F3FD\U0001F3FD': 212,  # Sign of the Horns: Medium Skin Tone
    u'\U0001F918\U0001F3FE\U0001F3FE': 213,  # Sign of the Horns: Medium-Dark Skin Tone
    u'\U0001F918\U0001F3FF\U0001F3FF': 214,  # Sign of the Horns: Dark Skin Tone
    u'\U0001F919': 215,  # Call Me Hand
    u'\U0001F919\U0001F3FB\U0001F3FB': 216,  # Call Me Hand: Light Skin Tone
    u'\U0001F919\U0001F3FC\U0001F3FC': 217,  # Call Me Hand: Medium-Light Skin Tone
    u'\U0001F919\U0001F3FD\U0001F3FD': 218,  # Call Me Hand: Medium Skin Tone
    u'\U0001F919\U0001F3FE\U0001F3FE': 219,  # Call Me Hand: Medium-Dark Skin Tone
    u'\U0001F919\U0001F3FF\U0001F3FF': 220,  # Call Me Hand: Dark Skin Tone
    u'\U0001F448': 221,  # Backhand Index Pointing Left
    u'\U0001F448\U0001F3FB\U0001F3FB': 222,  # Backhand Index Pointing Left: Light Skin Tone
    u'\U0001F448\U0001F3FC\U0001F3FC': 223,  # Backhand Index Pointing Left: Medium-Light Skin Tone
    u'\U0001F448\U0001F3FD\U0001F3FD': 224,  # Backhand Index Pointing Left: Medium Skin Tone
    u'\U0001F448\U0001F3FE\U0001F3FE': 225,  # Backhand Index Pointing Left: Medium-Dark Skin Tone
    u'\U0001F448\U0001F3FF\U0001F3FF': 226,  # Backhand Index Pointing Left: Dark Skin Tone
    u'\U0001F449': 227,  # Backhand Index Pointing Right
    u'\U0001F449\U0001F3FB\U0001F3FB': 228,  # Backhand Index Pointing Right: Light Skin Tone
    u'\U0001F449\U0001F3FC\U0001F3FC': 229,  # Backhand Index Pointing Right: Medium-Light Skin Tone
    u'\U0001F449\U0001F3FD\U0001F3FD': 230,  # Backhand Index Pointing Right: Medium Skin Tone
    u'\U0001F449\U0001F3FE\U0001F3FE': 231,  # Backhand Index Pointing Right: Medium-Dark Skin Tone
    u'\U0001F449\U0001F3FF\U0001F3FF': 232,  # Backhand Index Pointing Right: Dark Skin Tone
    u'\U0001F446': 233,  # Backhand Index Pointing Up
    u'\U0001F446\U0001F3FB\U0001F3FB': 234,  # Backhand Index Pointing Up: Light Skin Tone
    u'\U0001F446\U0001F3FC\U0001F3FC': 235,  # Backhand Index Pointing Up: Medium-Light Skin Tone
    u'\U0001F446\U0001F3FD\U0001F3FD': 236,  # Backhand Index Pointing Up: Medium Skin Tone
    u'\U0001F446\U0001F3FE\U0001F3FE': 237,  # Backhand Index Pointing Up: Medium-Dark Skin Tone
    u'\U0001F446\U0001F3FF\U0001F3FF': 238,  # Backhand Index Pointing Up: Dark Skin Tone
    u'\U0001F595': 239,  # Middle Finger
    u'\U0001F595\U0001F3FB\U0001F3FB': 240,  # Middle Finger: Light Skin Tone
    u'\U0001F595\U0001F3FC\U0001F3FC': 241,  # Middle Finger: Medium-Light Skin Tone
    u'\U0001F595\U0001F3FD\U0001F3FD': 242,  # Middle Finger: Medium Skin Tone
    u'\U0001F595\U0001F3FE\U0001F3FE': 243,  # Middle Finger: Medium-Dark Skin Tone
    u'\U0001F595\U0001F3FF\U0001F3FF': 244,  # Middle Finger: Dark Skin Tone
    u'\U0001F447': 245,  # Backhand Index Pointing Down
    u'\U0001F447\U0001F3FB\U0001F3FB': 246,  # Backhand Index Pointing Down: Light Skin Tone
    u'\U0001F447\U0001F3FC\U0001F3FC': 247,  # Backhand Index Pointing Down: Medium-Light Skin Tone
    u'\U0001F447\U0001F3FD\U0001F3FD': 248,  # Backhand Index Pointing Down: Medium Skin Tone
    u'\U0001F447\U0001F3FE\U0001F3FE': 249,  # Backhand Index Pointing Down: Medium-Dark Skin Tone
    u'\U0001F447\U0001F3FF\U0001F3FF': 250,  # Backhand Index Pointing Down: Dark Skin Tone
    u'\U0000261D': 251,  # Index Pointing Up
    u'\U0000261D\U0001F3FB\U0001F3FB': 252,  # Index Pointing Up: Light Skin Tone
    u'\U0000261D\U0001F3FC\U0001F3FC': 253,  # Index Pointing Up: Medium-Light Skin Tone
    u'\U0000261D\U0001F3FD\U0001F3FD': 254,  # Index Pointing Up: Medium Skin Tone
    u'\U0000261D\U0001F3FE\U0001F3FE': 255,  # Index Pointing Up: Medium-Dark Skin Tone
    u'\U0000261D\U0001F3FF\U0001F3FF': 256,  # Index Pointing Up: Dark Skin Tone
    u'\U0001F44D': 257,  # Thumbs Up
    u'\U0001F44D\U0001F3FB\U0001F3FB': 258,  # Thumbs Up: Light Skin Tone
    u'\U0001F44D\U0001F3FC\U0001F3FC': 259,  # Thumbs Up: Medium-Light Skin Tone
    u'\U0001F44D\U0001F3FD\U0001F3FD': 260,  # Thumbs Up: Medium Skin Tone
    u'\U0001F44D\U0001F3FE\U0001F3FE': 261,  # Thumbs Up: Medium-Dark Skin Tone
    u'\U0001F44D\U0001F3FF\U0001F3FF': 262,  # Thumbs Up: Dark Skin Tone
    u'\U0001F44E': 263,  # Thumbs Down
    u'\U0001F44E\U0001F3FB\U0001F3FB': 264,  # Thumbs Down: Light Skin Tone
    u'\U0001F44E\U0001F3FC\U0001F3FC': 265,  # Thumbs Down: Medium-Light Skin Tone
    u'\U0001F44E\U0001F3FD\U0001F3FD': 266,  # Thumbs Down: Medium Skin Tone
    u'\U0001F44E\U0001F3FE\U0001F3FE': 267,  # Thumbs Down: Medium-Dark Skin Tone
    u'\U0001F44E\U0001F3FF\U0001F3FF': 268,  # Thumbs Down: Dark Skin Tone
    u'\U0000270A': 269,  # Raised Fist
    u'\U0000270A\U0001F3FB\U0001F3FB': 270,  # Raised Fist: Light Skin Tone
    u'\U0000270A\U0001F3FC\U0001F3FC': 271,  # Raised Fist: Medium-Light Skin Tone
    u'\U0000270A\U0001F3FD\U0001F3FD': 272,  # Raised Fist: Medium Skin Tone
    u'\U0000270A\U0001F3FE\U0001F3FE': 273,  # Raised Fist: Medium-Dark Skin Tone
    u'\U0000270A\U0001F3FF\U0001F3FF': 274,  # Raised Fist: Dark Skin Tone
    u'\U0001F44A': 275,  # Oncoming Fist
    u'\U0001F44A\U0001F3FB\U0001F3FB': 276,  # Oncoming Fist: Light Skin Tone
    u'\U0001F44A\U0001F3FC\U0001F3FC': 277,  # Oncoming Fist: Medium-Light Skin Tone
    u'\U0001F44A\U0001F3FD\U0001F3FD': 278,  # Oncoming Fist: Medium Skin Tone
    u'\U0001F44A\U0001F3FE\U0001F3FE': 279,  # Oncoming Fist: Medium-Dark Skin Tone
    u'\U0001F44A\U0001F3FF\U0001F3FF': 280,  # Oncoming Fist: Dark Skin Tone
    u'\U0001F91B': 281,  # Left-Facing Fist
    u'\U0001F91B\U0001F3FB\U0001F3FB': 282,  # Left-Facing Fist: Light Skin Tone
    u'\U0001F91B\U0001F3FC\U0001F3FC': 283,  # Left-Facing Fist: Medium-Light Skin Tone
    u'\U0001F91B\U0001F3FD\U0001F3FD': 284,  # Left-Facing Fist: Medium Skin Tone
    u'\U0001F91B\U0001F3FE\U0001F3FE': 285,  # Left-Facing Fist: Medium-Dark Skin Tone
    u'\U0001F91B\U0001F3FF\U0001F3FF': 286,  # Left-Facing Fist: Dark Skin Tone
    u'\U0001F91C': 287,  # Right-Facing Fist
    u'\U0001F91C\U0001F3FB\U0001F3FB': 288,  # Right-Facing Fist: Light Skin Tone
    u'\U0001F91C\U0001F3FC\U0001F3FC': 289,  # Right-Facing Fist: Medium-Light Skin Tone
    u'\U0001F91C\U0001F3FD\U0001F3FD': 290,  # Right-Facing Fist: Medium Skin Tone
    u'\U0001F91C\U0001F3FE\U0001F3FE': 291,  # Right-Facing Fist: Medium-Dark Skin Tone
    u'\U0001F91C\U0001F3FF\U0001F3FF': 292,  # Right-Facing Fist: Dark Skin Tone
    u'\U0001F44F': 293,  # Clapping Hands
    u'\U0001F44F\U0001F3FB\U0001F3FB': 294,  # Clapping Hands: Light Skin Tone
    u'\U0001F44F\U0001F3FC\U0001F3FC': 295,  # Clapping Hands: Medium-Light Skin Tone
    u'\U0001F44F\U0001F3FD\U0001F3FD': 296,  # Clapping Hands: Medium Skin Tone
    u'\U0001F44F\U0001F3FE\U0001F3FE': 297,  # Clapping Hands: Medium-Dark Skin Tone
    u'\U0001F44F\U0001F3FF\U0001F3FF': 298,  # Clapping Hands: Dark Skin Tone
    u'\U0001F64C': 299,  # Raising Hands
    u'\U0001F64C\U0001F3FB\U0001F3FB': 300,  # Raising Hands: Light Skin Tone
    u'\U0001F64C\U0001F3FC\U0001F3FC': 301,  # Raising Hands: Medium-Light Skin Tone
    u'\U0001F64C\U0001F3FD\U0001F3FD': 302,  # Raising Hands: Medium Skin Tone
    u'\U0001F64C\U0001F3FE\U0001F3FE': 303,  # Raising Hands: Medium-Dark Skin Tone
    u'\U0001F64C\U0001F3FF\U0001F3FF': 304,  # Raising Hands: Dark Skin Tone
    u'\U0001F450': 305,  # Open Hands
    u'\U0001F450\U0001F3FB\U0001F3FB': 306,  # Open Hands: Light Skin Tone
    u'\U0001F450\U0001F3FC\U0001F3FC': 307,  # Open Hands: Medium-Light Skin Tone
    u'\U0001F450\U0001F3FD\U0001F3FD': 308,  # Open Hands: Medium Skin Tone
    u'\U0001F450\U0001F3FE\U0001F3FE': 309,  # Open Hands: Medium-Dark Skin Tone
    u'\U0001F450\U0001F3FF\U0001F3FF': 310,  # Open Hands: Dark Skin Tone
    u'\U0001F932': 311,  # Palms Up Together
    u'\U0001F932\U0001F3FB\U0001F3FB': 312,  # Palms Up Together: Light Skin Tone
    u'\U0001F932\U0001F3FC\U0001F3FC': 313,  # Palms Up Together: Medium-Light Skin Tone
    u'\U0001F932\U0001F3FD\U0001F3FD': 314,  # Palms Up Together: Medium Skin Tone
    u'\U0001F932\U0001F3FE\U0001F3FE': 315,  # Palms Up Together: Medium-Dark Skin Tone
    u'\U0001F932\U0001F3FF\U0001F3FF': 316,  # Palms Up Together: Dark Skin Tone
    u'\U0001F91D': 317,  # Handshake
    u'\U0001F64F': 318,  # Folded Hands
    u'\U0001F64F\U0001F3FB\U0001F3FB': 319,  # Folded Hands: Light Skin Tone
    u'\U0001F64F\U0001F3FC\U0001F3FC': 320,  # Folded Hands: Medium-Light Skin Tone
    u'\U0001F64F\U0001F3FD\U0001F3FD': 321,  # Folded Hands: Medium Skin Tone
    u'\U0001F64F\U0001F3FE\U0001F3FE': 322,  # Folded Hands: Medium-Dark Skin Tone
    u'\U0001F64F\U0001F3FF\U0001F3FF': 323,  # Folded Hands: Dark Skin Tone
    u'\U0000270D': 324,  # Writing Hand
    u'\U0001F91D\U0001F3FB\U0001F3FB': 325,  # Handshake, Type-1-2
    u'\U0001F91D\U0001F3FC\U0001F3FC': 326,  # Handshake, Type-3
    u'\U0000270D\U0001F3FB\U0001F3FB': 327,  # Writing Hand: Light Skin Tone
    u'\U0001F91D\U0001F3FD\U0001F3FD': 328,  # Handshake, Type-4
    u'\U0000270D\U0001F3FC\U0001F3FC': 329,  # Writing Hand: Medium-Light Skin Tone
    u'\U0001F91D\U0001F3FE\U0001F3FE': 330,  # Handshake, Type-5
    u'\U0000270D\U0001F3FD\U0001F3FD': 331,  # Writing Hand: Medium Skin Tone
    u'\U0001F91D\U0001F3FF\U0001F3FF': 332,  # Handshake, Type-6
    u'\U0000270D\U0001F3FE\U0001F3FE': 333,  # Writing Hand: Medium-Dark Skin Tone
    u'\U0000270D\U0001F3FF\U0001F3FF': 334,  # Writing Hand: Dark Skin Tone
    u'\U0001F485': 335,  # Nail Polish
    u'\U0001F485\U0001F3FB\U0001F3FB': 336,  # Nail Polish: Light Skin Tone
    u'\U0001F485\U0001F3FC\U0001F3FC': 337,  # Nail Polish: Medium-Light Skin Tone
    u'\U0001F485\U0001F3FD\U0001F3FD': 338,  # Nail Polish: Medium Skin Tone
    u'\U0001F485\U0001F3FE\U0001F3FE': 339,  # Nail Polish: Medium-Dark Skin Tone
    u'\U0001F485\U0001F3FF\U0001F3FF': 340,  # Nail Polish: Dark Skin Tone
    u'\U0001F933': 341,  # Selfie
    u'\U0001F933\U0001F3FB\U0001F3FB': 342,  # Selfie: Light Skin Tone
    u'\U0001F933\U0001F3FC\U0001F3FC': 343,  # Selfie: Medium-Light Skin Tone
    u'\U0001F933\U0001F3FD\U0001F3FD': 344,  # Selfie: Medium Skin Tone
    u'\U0001F933\U0001F3FE\U0001F3FE': 345,  # Selfie: Medium-Dark Skin Tone
    u'\U0001F933\U0001F3FF\U0001F3FF': 346,  # Selfie: Dark Skin Tone
    u'\U0001F4AA': 347,  # Flexed Biceps
    u'\U0001F4AA\U0001F3FB\U0001F3FB': 348,  # Flexed Biceps: Light Skin Tone
    u'\U0001F4AA\U0001F3FC\U0001F3FC': 349,  # Flexed Biceps: Medium-Light Skin Tone
    u'\U0001F4AA\U0001F3FD\U0001F3FD': 350,  # Flexed Biceps: Medium Skin Tone
    u'\U0001F4AA\U0001F3FE\U0001F3FE': 351,  # Flexed Biceps: Medium-Dark Skin Tone
    u'\U0001F4AA\U0001F3FF\U0001F3FF': 352,  # Flexed Biceps: Dark Skin Tone
    u'\U0001F9BE': 353,  # Mechanical Arm
    u'\U0001F9BF': 354,  # Mechanical Leg
    u'\U0001F9B5': 355,  # Leg
    u'\U0001F9B5\U0001F3FB\U0001F3FB': 356,  # Leg: Light Skin Tone
    u'\U0001F9B5\U0001F3FC\U0001F3FC': 357,  # Leg: Medium-Light Skin Tone
    u'\U0001F9B5\U0001F3FD\U0001F3FD': 358,  # Leg: Medium Skin Tone
    u'\U0001F9B5\U0001F3FE\U0001F3FE': 359,  # Leg: Medium-Dark Skin Tone
    u'\U0001F9B5\U0001F3FF\U0001F3FF': 360,  # Leg: Dark Skin Tone
    u'\U0001F9B6': 361,  # Foot
    u'\U0001F9B6\U0001F3FB\U0001F3FB': 362,  # Foot: Light Skin Tone
    u'\U0001F9B6\U0001F3FC\U0001F3FC': 363,  # Foot: Medium-Light Skin Tone
    u'\U0001F9B6\U0001F3FD\U0001F3FD': 364,  # Foot: Medium Skin Tone
    u'\U0001F9B6\U0001F3FE\U0001F3FE': 365,  # Foot: Medium-Dark Skin Tone
    u'\U0001F9B6\U0001F3FF\U0001F3FF': 366,  # Foot: Dark Skin Tone
    u'\U0001F442': 367,  # Ear
    u'\U0001F442\U0001F3FB\U0001F3FB': 368,  # Ear: Light Skin Tone
    u'\U0001F442\U0001F3FC\U0001F3FC': 369,  # Ear: Medium-Light Skin Tone
    u'\U0001F442\U0001F3FD\U0001F3FD': 370,  # Ear: Medium Skin Tone
    u'\U0001F442\U0001F3FE\U0001F3FE': 371,  # Ear: Medium-Dark Skin Tone
    u'\U0001F442\U0001F3FF\U0001F3FF': 372,  # Ear: Dark Skin Tone
    u'\U0001F9BB': 373,  # Ear with Hearing Aid
    u'\U0001F9BB\U0001F3FB\U0001F3FB': 374,  # Ear with Hearing Aid: Light Skin Tone
    u'\U0001F9BB\U0001F3FC\U0001F3FC': 375,  # Ear with Hearing Aid: Medium-Light Skin Tone
    u'\U0001F9BB\U0001F3FD\U0001F3FD': 376,  # Ear with Hearing Aid: Medium Skin Tone
    u'\U0001F9BB\U0001F3FE\U0001F3FE': 377,  # Ear with Hearing Aid: Medium-Dark Skin Tone
    u'\U0001F9BB\U0001F3FF\U0001F3FF': 378,  # Ear with Hearing Aid: Dark Skin Tone
    u'\U0001F443': 379,  # Nose
    u'\U0001F443\U0001F3FB\U0001F3FB': 380,  # Nose: Light Skin Tone
    u'\U0001F443\U0001F3FC\U0001F3FC': 381,  # Nose: Medium-Light Skin Tone
    u'\U0001F443\U0001F3FD\U0001F3FD': 382,  # Nose: Medium Skin Tone
    u'\U0001F443\U0001F3FE\U0001F3FE': 383,  # Nose: Medium-Dark Skin Tone
    u'\U0001F443\U0001F3FF\U0001F3FF': 384,  # Nose: Dark Skin Tone
    u'\U0001F9E0': 385,  # Brain
    u'\U0001F9B7': 386,  # Tooth
    u'\U0001F9B4': 387,  # Bone
    u'\U0001F440': 388,  # Eyes
    u'\U0001F441': 389,  # Eye
    u'\U0001F445': 390,  # Tongue
    u'\U0001F444': 391,  # Mouth
    u'\U0001F476': 392,  # Baby
    u'\U0001F476\U0001F3FB\U0001F3FB': 393,  # Baby: Light Skin Tone
    u'\U0001F476\U0001F3FC\U0001F3FC': 394,  # Baby: Medium-Light Skin Tone
    u'\U0001F476\U0001F3FD\U0001F3FD': 395,  # Baby: Medium Skin Tone
    u'\U0001F476\U0001F3FE\U0001F3FE': 396,  # Baby: Medium-Dark Skin Tone
    u'\U0001F476\U0001F3FF\U0001F3FF': 397,  # Baby: Dark Skin Tone
    u'\U0001F9D2': 398,  # Child
    u'\U0001F9D2\U0001F3FB\U0001F3FB': 399,  # Child: Light Skin Tone
    u'\U0001F9D2\U0001F3FC\U0001F3FC': 400,  # Child: Medium-Light Skin Tone
    u'\U0001F9D2\U0001F3FD\U0001F3FD': 401,  # Child: Medium Skin Tone
    u'\U0001F9D2\U0001F3FE\U0001F3FE': 402,  # Child: Medium-Dark Skin Tone
    u'\U0001F9D2\U0001F3FF\U0001F3FF': 403,  # Child: Dark Skin Tone
    u'\U0001F466': 404,  # Boy
    u'\U0001F466\U0001F3FB\U0001F3FB': 405,  # Boy: Light Skin Tone
    u'\U0001F466\U0001F3FC\U0001F3FC': 406,  # Boy: Medium-Light Skin Tone
    u'\U0001F466\U0001F3FD\U0001F3FD': 407,  # Boy: Medium Skin Tone
    u'\U0001F466\U0001F3FE\U0001F3FE': 408,  # Boy: Medium-Dark Skin Tone
    u'\U0001F466\U0001F3FF\U0001F3FF': 409,  # Boy: Dark Skin Tone
    u'\U0001F467': 410,  # Girl
    u'\U0001F467\U0001F3FB\U0001F3FB': 411,  # Girl: Light Skin Tone
    u'\U0001F467\U0001F3FC\U0001F3FC': 412,  # Girl: Medium-Light Skin Tone
    u'\U0001F467\U0001F3FD\U0001F3FD': 413,  # Girl: Medium Skin Tone
    u'\U0001F467\U0001F3FE\U0001F3FE': 414,  # Girl: Medium-Dark Skin Tone
    u'\U0001F467\U0001F3FF\U0001F3FF': 415,  # Girl: Dark Skin Tone
    u'\U0001F9D1': 416,  # Person
    u'\U0001F9D1\U0001F3FB\U0001F3FB': 417,  # Person: Light Skin Tone
    u'\U0001F9D1\U0001F3FC\U0001F3FC': 418,  # Person: Medium-Light Skin Tone
    u'\U0001F9D1\U0001F3FD\U0001F3FD': 419,  # Person: Medium Skin Tone
    u'\U0001F9D1\U0001F3FE\U0001F3FE': 420,  # Person: Medium-Dark Skin Tone
    u'\U0001F9D1\U0001F3FF\U0001F3FF': 421,  # Person: Dark Skin Tone
    u'\U0001F471': 422,  # Person: Blond Hair
    u'\U0001F471\U0001F3FB\U0001F3FB': 423,  # Person: Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FC\U0001F3FC': 424,  # Person: Medium-Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FD\U0001F3FD': 425,  # Person: Medium Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FE\U0001F3FE': 426,  # Person: Medium-Dark Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FF\U0001F3FF': 427,  # Person: Dark Skin Tone, Blond Hair
    u'\U0001F468': 428,  # Man
    u'\U0001F468\U0001F3FB\U0001F3FB': 429,  # Man: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0001F3FC': 430,  # Man: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0001F3FD': 431,  # Man: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0001F3FE': 432,  # Man: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0001F3FF': 433,  # Man: Dark Skin Tone
    u'\U0001F9D4': 434,  # Man: Beard
    u'\U0001F9D4\U0001F3FB\U0001F3FB': 435,  # Man: Light Skin Tone, Beard
    u'\U0001F9D4\U0001F3FC\U0001F3FC': 436,  # Man: Medium-Light Skin Tone, Beard
    u'\U0001F9D4\U0001F3FD\U0001F3FD': 437,  # Man: Medium Skin Tone, Beard
    u'\U0001F9D4\U0001F3FE\U0001F3FE': 438,  # Man: Medium-Dark Skin Tone, Beard
    u'\U0001F9D4\U0001F3FF\U0001F3FF': 439,  # Man: Dark Skin Tone, Beard
    u'\U0001F468\U0000200D\U0001F9B0': 440,  # Man: Red Hair
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B0': 441,  # Man: Light Skin Tone, Red Hair
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B0': 442,  # Man: Medium-Light Skin Tone, Red Hair
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B0': 443,  # Man: Medium Skin Tone, Red Hair
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B0': 444,  # Man: Medium-Dark Skin Tone, Red Hair
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B0': 445,  # Man: Dark Skin Tone, Red Hair
    u'\U0001F468\U0000200D\U0001F9B1': 446,  # Man: Curly Hair
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B1': 447,  # Man: Light Skin Tone, Curly Hair
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B1': 448,  # Man: Medium-Light Skin Tone, Curly Hair
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B1': 449,  # Man: Medium Skin Tone, Curly Hair
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B1': 450,  # Man: Medium-Dark Skin Tone, Curly Hair
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B1': 451,  # Man: Dark Skin Tone, Curly Hair
    u'\U0001F468\U0000200D\U0001F9B3': 452,  # Man: White Hair
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B3': 453,  # Man: Light Skin Tone, White Hair
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B3': 454,  # Man: Medium-Light Skin Tone, White Hair
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B3': 455,  # Man: Medium Skin Tone, White Hair
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B3': 456,  # Man: Medium-Dark Skin Tone, White Hair
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B3': 457,  # Man: Dark Skin Tone, White Hair
    u'\U0001F468\U0000200D\U0001F9B2': 458,  # Man: Bald
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9B2': 459,  # Man: Light Skin Tone, Bald
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9B2': 460,  # Man: Medium-Light Skin Tone, Bald
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9B2': 461,  # Man: Medium Skin Tone, Bald
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9B2': 462,  # Man: Medium-Dark Skin Tone, Bald
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9B2': 463,  # Man: Dark Skin Tone, Bald
    u'\U0001F469': 464,  # Woman
    u'\U0001F469\U0001F3FB\U0001F3FB': 465,  # Woman: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0001F3FC': 466,  # Woman: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0001F3FD': 467,  # Woman: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0001F3FE': 468,  # Woman: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0001F3FF': 469,  # Woman: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F9B0': 470,  # Woman: Red Hair
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B0': 471,  # Woman: Light Skin Tone, Red Hair
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B0': 472,  # Woman: Medium-Light Skin Tone, Red Hair
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B0': 473,  # Woman: Medium Skin Tone, Red Hair
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B0': 474,  # Woman: Medium-Dark Skin Tone, Red Hair
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B0': 475,  # Woman: Dark Skin Tone, Red Hair
    u'\U0001F469\U0000200D\U0001F9B1': 476,  # Woman: Curly Hair
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B1': 477,  # Woman: Light Skin Tone, Curly Hair
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B1': 478,  # Woman: Medium-Light Skin Tone, Curly Hair
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B1': 479,  # Woman: Medium Skin Tone, Curly Hair
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B1': 480,  # Woman: Medium-Dark Skin Tone, Curly Hair
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B1': 481,  # Woman: Dark Skin Tone, Curly Hair
    u'\U0001F469\U0000200D\U0001F9B3': 482,  # Woman: White Hair
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B3': 483,  # Woman: Light Skin Tone, White Hair
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B3': 484,  # Woman: Medium-Light Skin Tone, White Hair
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B3': 485,  # Woman: Medium Skin Tone, White Hair
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B3': 486,  # Woman: Medium-Dark Skin Tone, White Hair
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B3': 487,  # Woman: Dark Skin Tone, White Hair
    u'\U0001F469\U0000200D\U0001F9B2': 488,  # Woman: Bald
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9B2': 489,  # Woman: Light Skin Tone, Bald
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9B2': 490,  # Woman: Medium-Light Skin Tone, Bald
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9B2': 491,  # Woman: Medium Skin Tone, Bald
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9B2': 492,  # Woman: Medium-Dark Skin Tone, Bald
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9B2': 493,  # Woman: Dark Skin Tone, Bald
    u'\U0001F471\U0000200D\U00002640': 494,  # Woman: Blond Hair
    u'\U0001F471\U0001F3FB\U0000200D\U00002640': 495,  # Woman: Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FC\U0000200D\U00002640': 496,  # Woman: Medium-Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FD\U0000200D\U00002640': 497,  # Woman: Medium Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FE\U0000200D\U00002640': 498,  # Woman: Medium-Dark Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FF\U0000200D\U00002640': 499,  # Woman: Dark Skin Tone, Blond Hair
    u'\U0001F471\U0000200D\U00002642': 500,  # Man: Blond Hair
    u'\U0001F471\U0001F3FB\U0000200D\U00002642': 501,  # Man: Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FC\U0000200D\U00002642': 502,  # Man: Medium-Light Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FD\U0000200D\U00002642': 503,  # Man: Medium Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FE\U0000200D\U00002642': 504,  # Man: Medium-Dark Skin Tone, Blond Hair
    u'\U0001F471\U0001F3FF\U0000200D\U00002642': 505,  # Man: Dark Skin Tone, Blond Hair
    u'\U0001F9D3': 506,  # Older Person
    u'\U0001F9D3\U0001F3FB\U0001F3FB': 507,  # Older Person: Light Skin Tone
    u'\U0001F9D3\U0001F3FC\U0001F3FC': 508,  # Older Person: Medium-Light Skin Tone
    u'\U0001F9D3\U0001F3FD\U0001F3FD': 509,  # Older Person: Medium Skin Tone
    u'\U0001F9D3\U0001F3FE\U0001F3FE': 510,  # Older Person: Medium-Dark Skin Tone
    u'\U0001F9D3\U0001F3FF\U0001F3FF': 511,  # Older Person: Dark Skin Tone
    u'\U0001F474': 512,  # Old Man
    u'\U0001F474\U0001F3FB\U0001F3FB': 513,  # Old Man: Light Skin Tone
    u'\U0001F474\U0001F3FC\U0001F3FC': 514,  # Old Man: Medium-Light Skin Tone
    u'\U0001F474\U0001F3FD\U0001F3FD': 515,  # Old Man: Medium Skin Tone
    u'\U0001F474\U0001F3FE\U0001F3FE': 516,  # Old Man: Medium-Dark Skin Tone
    u'\U0001F474\U0001F3FF\U0001F3FF': 517,  # Old Man: Dark Skin Tone
    u'\U0001F475': 518,  # Old Woman
    u'\U0001F475\U0001F3FB\U0001F3FB': 519,  # Old Woman: Light Skin Tone
    u'\U0001F475\U0001F3FC\U0001F3FC': 520,  # Old Woman: Medium-Light Skin Tone
    u'\U0001F475\U0001F3FD\U0001F3FD': 521,  # Old Woman: Medium Skin Tone
    u'\U0001F475\U0001F3FE\U0001F3FE': 522,  # Old Woman: Medium-Dark Skin Tone
    u'\U0001F475\U0001F3FF\U0001F3FF': 523,  # Old Woman: Dark Skin Tone
    u'\U0001F64D': 524,  # Person Frowning
    u'\U0001F64D\U0001F3FB\U0001F3FB': 525,  # Person Frowning: Light Skin Tone
    u'\U0001F64D\U0001F3FC\U0001F3FC': 526,  # Person Frowning: Medium-Light Skin Tone
    u'\U0001F64D\U0001F3FD\U0001F3FD': 527,  # Person Frowning: Medium Skin Tone
    u'\U0001F64D\U0001F3FE\U0001F3FE': 528,  # Person Frowning: Medium-Dark Skin Tone
    u'\U0001F64D\U0001F3FF\U0001F3FF': 529,  # Person Frowning: Dark Skin Tone
    u'\U0001F64D\U0000200D\U00002642': 530,  # Man Frowning
    u'\U0001F64D\U0001F3FB\U0000200D\U00002642': 531,  # Man Frowning: Light Skin Tone
    u'\U0001F64D\U0001F3FC\U0000200D\U00002642': 532,  # Man Frowning: Medium-Light Skin Tone
    u'\U0001F64D\U0001F3FD\U0000200D\U00002642': 533,  # Man Frowning: Medium Skin Tone
    u'\U0001F64D\U0001F3FE\U0000200D\U00002642': 534,  # Man Frowning: Medium-Dark Skin Tone
    u'\U0001F64D\U0001F3FF\U0000200D\U00002642': 535,  # Man Frowning: Dark Skin Tone
    u'\U0001F64D\U0000200D\U00002640': 536,  # Woman Frowning
    u'\U0001F64D\U0001F3FB\U0000200D\U00002640': 537,  # Woman Frowning: Light Skin Tone
    u'\U0001F64D\U0001F3FC\U0000200D\U00002640': 538,  # Woman Frowning: Medium-Light Skin Tone
    u'\U0001F64D\U0001F3FD\U0000200D\U00002640': 539,  # Woman Frowning: Medium Skin Tone
    u'\U0001F64D\U0001F3FE\U0000200D\U00002640': 540,  # Woman Frowning: Medium-Dark Skin Tone
    u'\U0001F64D\U0001F3FF\U0000200D\U00002640': 541,  # Woman Frowning: Dark Skin Tone
    u'\U0001F64E': 542,  # Person Pouting
    u'\U0001F64E\U0001F3FB\U0001F3FB': 543,  # Person Pouting: Light Skin Tone
    u'\U0001F64E\U0001F3FC\U0001F3FC': 544,  # Person Pouting: Medium-Light Skin Tone
    u'\U0001F64E\U0001F3FD\U0001F3FD': 545,  # Person Pouting: Medium Skin Tone
    u'\U0001F64E\U0001F3FE\U0001F3FE': 546,  # Person Pouting: Medium-Dark Skin Tone
    u'\U0001F64E\U0001F3FF\U0001F3FF': 547,  # Person Pouting: Dark Skin Tone
    u'\U0001F64E\U0000200D\U00002642': 548,  # Man Pouting
    u'\U0001F64E\U0001F3FB\U0000200D\U00002642': 549,  # Man Pouting: Light Skin Tone
    u'\U0001F64E\U0001F3FC\U0000200D\U00002642': 550,  # Man Pouting: Medium-Light Skin Tone
    u'\U0001F64E\U0001F3FD\U0000200D\U00002642': 551,  # Man Pouting: Medium Skin Tone
    u'\U0001F64E\U0001F3FE\U0000200D\U00002642': 552,  # Man Pouting: Medium-Dark Skin Tone
    u'\U0001F64E\U0001F3FF\U0000200D\U00002642': 553,  # Man Pouting: Dark Skin Tone
    u'\U0001F64E\U0000200D\U00002640': 554,  # Woman Pouting
    u'\U0001F64E\U0001F3FB\U0000200D\U00002640': 555,  # Woman Pouting: Light Skin Tone
    u'\U0001F64E\U0001F3FC\U0000200D\U00002640': 556,  # Woman Pouting: Medium-Light Skin Tone
    u'\U0001F64E\U0001F3FD\U0000200D\U00002640': 557,  # Woman Pouting: Medium Skin Tone
    u'\U0001F64E\U0001F3FE\U0000200D\U00002640': 558,  # Woman Pouting: Medium-Dark Skin Tone
    u'\U0001F64E\U0001F3FF\U0000200D\U00002640': 559,  # Woman Pouting: Dark Skin Tone
    u'\U0001F645': 560,  # Person Gesturing No
    u'\U0001F645\U0001F3FB\U0001F3FB': 561,  # Person Gesturing No: Light Skin Tone
    u'\U0001F645\U0001F3FC\U0001F3FC': 562,  # Person Gesturing No: Medium-Light Skin Tone
    u'\U0001F645\U0001F3FD\U0001F3FD': 563,  # Person Gesturing No: Medium Skin Tone
    u'\U0001F645\U0001F3FE\U0001F3FE': 564,  # Person Gesturing No: Medium-Dark Skin Tone
    u'\U0001F645\U0001F3FF\U0001F3FF': 565,  # Person Gesturing No: Dark Skin Tone
    u'\U0001F645\U0000200D\U00002642': 566,  # Man Gesturing No
    u'\U0001F645\U0001F3FB\U0000200D\U00002642': 567,  # Man Gesturing No: Light Skin Tone
    u'\U0001F645\U0001F3FC\U0000200D\U00002642': 568,  # Man Gesturing No: Medium-Light Skin Tone
    u'\U0001F645\U0001F3FD\U0000200D\U00002642': 569,  # Man Gesturing No: Medium Skin Tone
    u'\U0001F645\U0001F3FE\U0000200D\U00002642': 570,  # Man Gesturing No: Medium-Dark Skin Tone
    u'\U0001F645\U0001F3FF\U0000200D\U00002642': 571,  # Man Gesturing No: Dark Skin Tone
    u'\U0001F645\U0000200D\U00002640': 572,  # Woman Gesturing No
    u'\U0001F645\U0001F3FB\U0000200D\U00002640': 573,  # Woman Gesturing No: Light Skin Tone
    u'\U0001F645\U0001F3FC\U0000200D\U00002640': 574,  # Woman Gesturing No: Medium-Light Skin Tone
    u'\U0001F645\U0001F3FD\U0000200D\U00002640': 575,  # Woman Gesturing No: Medium Skin Tone
    u'\U0001F645\U0001F3FE\U0000200D\U00002640': 576,  # Woman Gesturing No: Medium-Dark Skin Tone
    u'\U0001F645\U0001F3FF\U0000200D\U00002640': 577,  # Woman Gesturing No: Dark Skin Tone
    u'\U0001F646': 578,  # Person Gesturing OK
    u'\U0001F646\U0001F3FB\U0001F3FB': 579,  # Person Gesturing OK: Light Skin Tone
    u'\U0001F646\U0001F3FC\U0001F3FC': 580,  # Person Gesturing OK: Medium-Light Skin Tone
    u'\U0001F646\U0001F3FD\U0001F3FD': 581,  # Person Gesturing OK: Medium Skin Tone
    u'\U0001F646\U0001F3FE\U0001F3FE': 582,  # Person Gesturing OK: Medium-Dark Skin Tone
    u'\U0001F646\U0001F3FF\U0001F3FF': 583,  # Person Gesturing OK: Dark Skin Tone
    u'\U0001F646\U0000200D\U00002642': 584,  # Man Gesturing OK
    u'\U0001F646\U0001F3FB\U0000200D\U00002642': 585,  # Man Gesturing OK: Light Skin Tone
    u'\U0001F646\U0001F3FC\U0000200D\U00002642': 586,  # Man Gesturing OK: Medium-Light Skin Tone
    u'\U0001F646\U0001F3FD\U0000200D\U00002642': 587,  # Man Gesturing OK: Medium Skin Tone
    u'\U0001F646\U0001F3FE\U0000200D\U00002642': 588,  # Man Gesturing OK: Medium-Dark Skin Tone
    u'\U0001F646\U0001F3FF\U0000200D\U00002642': 589,  # Man Gesturing OK: Dark Skin Tone
    u'\U0001F646\U0000200D\U00002640': 590,  # Woman Gesturing OK
    u'\U0001F646\U0001F3FB\U0000200D\U00002640': 591,  # Woman Gesturing OK: Light Skin Tone
    u'\U0001F646\U0001F3FC\U0000200D\U00002640': 592,  # Woman Gesturing OK: Medium-Light Skin Tone
    u'\U0001F646\U0001F3FD\U0000200D\U00002640': 593,  # Woman Gesturing OK: Medium Skin Tone
    u'\U0001F646\U0001F3FE\U0000200D\U00002640': 594,  # Woman Gesturing OK: Medium-Dark Skin Tone
    u'\U0001F646\U0001F3FF\U0000200D\U00002640': 595,  # Woman Gesturing OK: Dark Skin Tone
    u'\U0001F481': 596,  # Person Tipping Hand
    u'\U0001F481\U0001F3FB\U0001F3FB': 597,  # Person Tipping Hand: Light Skin Tone
    u'\U0001F481\U0001F3FC\U0001F3FC': 598,  # Person Tipping Hand: Medium-Light Skin Tone
    u'\U0001F481\U0001F3FD\U0001F3FD': 599,  # Person Tipping Hand: Medium Skin Tone
    u'\U0001F481\U0001F3FE\U0001F3FE': 600,  # Person Tipping Hand: Medium-Dark Skin Tone
    u'\U0001F481\U0001F3FF\U0001F3FF': 601,  # Person Tipping Hand: Dark Skin Tone
    u'\U0001F481\U0000200D\U00002642': 602,  # Man Tipping Hand
    u'\U0001F481\U0001F3FB\U0000200D\U00002642': 603,  # Man Tipping Hand: Light Skin Tone
    u'\U0001F481\U0001F3FC\U0000200D\U00002642': 604,  # Man Tipping Hand: Medium-Light Skin Tone
    u'\U0001F481\U0001F3FD\U0000200D\U00002642': 605,  # Man Tipping Hand: Medium Skin Tone
    u'\U0001F481\U0001F3FE\U0000200D\U00002642': 606,  # Man Tipping Hand: Medium-Dark Skin Tone
    u'\U0001F481\U0001F3FF\U0000200D\U00002642': 607,  # Man Tipping Hand: Dark Skin Tone
    u'\U0001F481\U0000200D\U00002640': 608,  # Woman Tipping Hand
    u'\U0001F481\U0001F3FB\U0000200D\U00002640': 609,  # Woman Tipping Hand: Light Skin Tone
    u'\U0001F481\U0001F3FC\U0000200D\U00002640': 610,  # Woman Tipping Hand: Medium-Light Skin Tone
    u'\U0001F481\U0001F3FD\U0000200D\U00002640': 611,  # Woman Tipping Hand: Medium Skin Tone
    u'\U0001F481\U0001F3FE\U0000200D\U00002640': 612,  # Woman Tipping Hand: Medium-Dark Skin Tone
    u'\U0001F481\U0001F3FF\U0000200D\U00002640': 613,  # Woman Tipping Hand: Dark Skin Tone
    u'\U0001F64B': 614,  # Person Raising Hand
    u'\U0001F64B\U0001F3FB\U0001F3FB': 615,  # Person Raising Hand: Light Skin Tone
    u'\U0001F64B\U0001F3FC\U0001F3FC': 616,  # Person Raising Hand: Medium-Light Skin Tone
    u'\U0001F64B\U0001F3FD\U0001F3FD': 617,  # Person Raising Hand: Medium Skin Tone
    u'\U0001F64B\U0001F3FE\U0001F3FE': 618,  # Person Raising Hand: Medium-Dark Skin Tone
    u'\U0001F64B\U0001F3FF\U0001F3FF': 619,  # Person Raising Hand: Dark Skin Tone
    u'\U0001F64B\U0000200D\U00002642': 620,  # Man Raising Hand
    u'\U0001F64B\U0001F3FB\U0000200D\U00002642': 621,  # Man Raising Hand: Light Skin Tone
    u'\U0001F64B\U0001F3FC\U0000200D\U00002642': 622,  # Man Raising Hand: Medium-Light Skin Tone
    u'\U0001F64B\U0001F3FD\U0000200D\U00002642': 623,  # Man Raising Hand: Medium Skin Tone
    u'\U0001F64B\U0001F3FE\U0000200D\U00002642': 624,  # Man Raising Hand: Medium-Dark Skin Tone
    u'\U0001F64B\U0001F3FF\U0000200D\U00002642': 625,  # Man Raising Hand: Dark Skin Tone
    u'\U0001F64B\U0000200D\U00002640': 626,  # Woman Raising Hand
    u'\U0001F64B\U0001F3FB\U0000200D\U00002640': 627,  # Woman Raising Hand: Light Skin Tone
    u'\U0001F64B\U0001F3FC\U0000200D\U00002640': 628,  # Woman Raising Hand: Medium-Light Skin Tone
    u'\U0001F64B\U0001F3FD\U0000200D\U00002640': 629,  # Woman Raising Hand: Medium Skin Tone
    u'\U0001F64B\U0001F3FE\U0000200D\U00002640': 630,  # Woman Raising Hand: Medium-Dark Skin Tone
    u'\U0001F64B\U0001F3FF\U0000200D\U00002640': 631,  # Woman Raising Hand: Dark Skin Tone
    u'\U0001F9CF': 632,  # Deaf Person
    u'\U0001F9CF\U0001F3FB\U0001F3FB': 633,  # Deaf Person: Light Skin Tone
    u'\U0001F9CF\U0001F3FC\U0001F3FC': 634,  # Deaf Person: Medium-Light Skin Tone
    u'\U0001F9CF\U0001F3FD\U0001F3FD': 635,  # Deaf Person: Medium Skin Tone
    u'\U0001F9CF\U0001F3FE\U0001F3FE': 636,  # Deaf Person: Medium-Dark Skin Tone
    u'\U0001F9CF\U0001F3FF\U0001F3FF': 637,  # Deaf Person: Dark Skin Tone
    u'\U0001F9CF\U0000200D\U00002642': 638,  # Deaf Man
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002642': 639,  # Deaf Man: Light Skin Tone
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002642': 640,  # Deaf Man: Medium-Light Skin Tone
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002642': 641,  # Deaf Man: Medium Skin Tone
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002642': 642,  # Deaf Man: Medium-Dark Skin Tone
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002642': 643,  # Deaf Man: Dark Skin Tone
    u'\U0001F9CF\U0000200D\U00002640': 644,  # Deaf Woman
    u'\U0001F9CF\U0001F3FB\U0000200D\U00002640': 645,  # Deaf Woman: Light Skin Tone
    u'\U0001F9CF\U0001F3FC\U0000200D\U00002640': 646,  # Deaf Woman: Medium-Light Skin Tone
    u'\U0001F9CF\U0001F3FD\U0000200D\U00002640': 647,  # Deaf Woman: Medium Skin Tone
    u'\U0001F9CF\U0001F3FE\U0000200D\U00002640': 648,  # Deaf Woman: Medium-Dark Skin Tone
    u'\U0001F9CF\U0001F3FF\U0000200D\U00002640': 649,  # Deaf Woman: Dark Skin Tone
    u'\U0001F647': 650,  # Person Bowing
    u'\U0001F647\U0001F3FB\U0001F3FB': 651,  # Person Bowing: Light Skin Tone
    u'\U0001F647\U0001F3FC\U0001F3FC': 652,  # Person Bowing: Medium-Light Skin Tone
    u'\U0001F647\U0001F3FD\U0001F3FD': 653,  # Person Bowing: Medium Skin Tone
    u'\U0001F647\U0001F3FE\U0001F3FE': 654,  # Person Bowing: Medium-Dark Skin Tone
    u'\U0001F647\U0001F3FF\U0001F3FF': 655,  # Person Bowing: Dark Skin Tone
    u'\U0001F647\U0000200D\U00002642': 656,  # Man Bowing
    u'\U0001F647\U0001F3FB\U0000200D\U00002642': 657,  # Man Bowing: Light Skin Tone
    u'\U0001F647\U0001F3FC\U0000200D\U00002642': 658,  # Man Bowing: Medium-Light Skin Tone
    u'\U0001F647\U0001F3FD\U0000200D\U00002642': 659,  # Man Bowing: Medium Skin Tone
    u'\U0001F647\U0001F3FE\U0000200D\U00002642': 660,  # Man Bowing: Medium-Dark Skin Tone
    u'\U0001F647\U0001F3FF\U0000200D\U00002642': 661,  # Man Bowing: Dark Skin Tone
    u'\U0001F647\U0000200D\U00002640': 662,  # Woman Bowing
    u'\U0001F647\U0001F3FB\U0000200D\U00002640': 663,  # Woman Bowing: Light Skin Tone
    u'\U0001F647\U0001F3FC\U0000200D\U00002640': 664,  # Woman Bowing: Medium-Light Skin Tone
    u'\U0001F647\U0001F3FD\U0000200D\U00002640': 665,  # Woman Bowing: Medium Skin Tone
    u'\U0001F647\U0001F3FE\U0000200D\U00002640': 666,  # Woman Bowing: Medium-Dark Skin Tone
    u'\U0001F647\U0001F3FF\U0000200D\U00002640': 667,  # Woman Bowing: Dark Skin Tone
    u'\U0001F926': 668,  # Person Facepalming
    u'\U0001F926\U0001F3FB\U0001F3FB': 669,  # Person Facepalming: Light Skin Tone
    u'\U0001F926\U0001F3FC\U0001F3FC': 670,  # Person Facepalming: Medium-Light Skin Tone
    u'\U0001F926\U0001F3FD\U0001F3FD': 671,  # Person Facepalming: Medium Skin Tone
    u'\U0001F926\U0001F3FE\U0001F3FE': 672,  # Person Facepalming: Medium-Dark Skin Tone
    u'\U0001F926\U0001F3FF\U0001F3FF': 673,  # Person Facepalming: Dark Skin Tone
    u'\U0001F926\U0000200D\U00002642': 674,  # Man Facepalming
    u'\U0001F926\U0001F3FB\U0000200D\U00002642': 675,  # Man Facepalming: Light Skin Tone
    u'\U0001F926\U0001F3FC\U0000200D\U00002642': 676,  # Man Facepalming: Medium-Light Skin Tone
    u'\U0001F926\U0001F3FD\U0000200D\U00002642': 677,  # Man Facepalming: Medium Skin Tone
    u'\U0001F926\U0001F3FE\U0000200D\U00002642': 678,  # Man Facepalming: Medium-Dark Skin Tone
    u'\U0001F926\U0001F3FF\U0000200D\U00002642': 679,  # Man Facepalming: Dark Skin Tone
    u'\U0001F926\U0000200D\U00002640': 680,  # Woman Facepalming
    u'\U0001F926\U0001F3FB\U0000200D\U00002640': 681,  # Woman Facepalming: Light Skin Tone
    u'\U0001F926\U0001F3FC\U0000200D\U00002640': 682,  # Woman Facepalming: Medium-Light Skin Tone
    u'\U0001F926\U0001F3FD\U0000200D\U00002640': 683,  # Woman Facepalming: Medium Skin Tone
    u'\U0001F926\U0001F3FE\U0000200D\U00002640': 684,  # Woman Facepalming: Medium-Dark Skin Tone
    u'\U0001F926\U0001F3FF\U0000200D\U00002640': 685,  # Woman Facepalming: Dark Skin Tone
    u'\U0001F937': 686,  # Person Shrugging
    u'\U0001F937\U0001F3FB\U0001F3FB': 687,  # Person Shrugging: Light Skin Tone
    u'\U0001F937\U0001F3FC\U0001F3FC': 688,  # Person Shrugging: Medium-Light Skin Tone
    u'\U0001F937\U0001F3FD\U0001F3FD': 689,  # Person Shrugging: Medium Skin Tone
    u'\U0001F937\U0001F3FE\U0001F3FE': 690,  # Person Shrugging: Medium-Dark Skin Tone
    u'\U0001F937\U0001F3FF\U0001F3FF': 691,  # Person Shrugging: Dark Skin Tone
    u'\U0001F937\U0000200D\U00002642': 692,  # Man Shrugging
    u'\U0001F937\U0001F3FB\U0000200D\U00002642': 693,  # Man Shrugging: Light Skin Tone
    u'\U0001F937\U0001F3FC\U0000200D\U00002642': 694,  # Man Shrugging: Medium-Light Skin Tone
    u'\U0001F937\U0001F3FD\U0000200D\U00002642': 695,  # Man Shrugging: Medium Skin Tone
    u'\U0001F937\U0001F3FE\U0000200D\U00002642': 696,  # Man Shrugging: Medium-Dark Skin Tone
    u'\U0001F937\U0001F3FF\U0000200D\U00002642': 697,  # Man Shrugging: Dark Skin Tone
    u'\U0001F937\U0000200D\U00002640': 698,  # Woman Shrugging
    u'\U0001F937\U0001F3FB\U0000200D\U00002640': 699,  # Woman Shrugging: Light Skin Tone
    u'\U0001F937\U0001F3FC\U0000200D\U00002640': 700,  # Woman Shrugging: Medium-Light Skin Tone
    u'\U0001F937\U0001F3FD\U0000200D\U00002640': 701,  # Woman Shrugging: Medium Skin Tone
    u'\U0001F937\U0001F3FE\U0000200D\U00002640': 702,  # Woman Shrugging: Medium-Dark Skin Tone
    u'\U0001F937\U0001F3FF\U0000200D\U00002640': 703,  # Woman Shrugging: Dark Skin Tone
    u'\U0001F468\U0000200D\U00002695': 704,  # Man Health Worker
    u'\U0001F468\U0001F3FB\U0000200D\U00002695': 705,  # Man Health Worker: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U00002695': 706,  # Man Health Worker: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U00002695': 707,  # Man Health Worker: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U00002695': 708,  # Man Health Worker: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U00002695': 709,  # Man Health Worker: Dark Skin Tone
    u'\U0001F469\U0000200D\U00002695': 710,  # Woman Health Worker
    u'\U0001F469\U0001F3FB\U0000200D\U00002695': 711,  # Woman Health Worker: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U00002695': 712,  # Woman Health Worker: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U00002695': 713,  # Woman Health Worker: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U00002695': 714,  # Woman Health Worker: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U00002695': 715,  # Woman Health Worker: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F393': 716,  # Man Student
    u'\U0001F468\U0001F3FB\U0000200D\U0001F393': 717,  # Man Student: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F393': 718,  # Man Student: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F393': 719,  # Man Student: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F393': 720,  # Man Student: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F393': 721,  # Man Student: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F393': 722,  # Woman Student
    u'\U0001F469\U0001F3FB\U0000200D\U0001F393': 723,  # Woman Student: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F393': 724,  # Woman Student: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F393': 725,  # Woman Student: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F393': 726,  # Woman Student: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F393': 727,  # Woman Student: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F3EB': 728,  # Man Teacher
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3EB': 729,  # Man Teacher: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3EB': 730,  # Man Teacher: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3EB': 731,  # Man Teacher: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3EB': 732,  # Man Teacher: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3EB': 733,  # Man Teacher: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F3EB': 734,  # Woman Teacher
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3EB': 735,  # Woman Teacher: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3EB': 736,  # Woman Teacher: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3EB': 737,  # Woman Teacher: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3EB': 738,  # Woman Teacher: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3EB': 739,  # Woman Teacher: Dark Skin Tone
    u'\U0001F468\U0000200D\U00002696': 740,  # Man Judge
    u'\U0001F468\U0001F3FB\U0000200D\U00002696': 741,  # Man Judge: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U00002696': 742,  # Man Judge: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U00002696': 743,  # Man Judge: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U00002696': 744,  # Man Judge: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U00002696': 745,  # Man Judge: Dark Skin Tone
    u'\U0001F469\U0000200D\U00002696': 746,  # Woman Judge
    u'\U0001F469\U0001F3FB\U0000200D\U00002696': 747,  # Woman Judge: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U00002696': 748,  # Woman Judge: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U00002696': 749,  # Woman Judge: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U00002696': 750,  # Woman Judge: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U00002696': 751,  # Woman Judge: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F33E': 752,  # Man Farmer
    u'\U0001F468\U0001F3FB\U0000200D\U0001F33E': 753,  # Man Farmer: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F33E': 754,  # Man Farmer: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F33E': 755,  # Man Farmer: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F33E': 756,  # Man Farmer: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F33E': 757,  # Man Farmer: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F33E': 758,  # Woman Farmer
    u'\U0001F469\U0001F3FB\U0000200D\U0001F33E': 759,  # Woman Farmer: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F33E': 760,  # Woman Farmer: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F33E': 761,  # Woman Farmer: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F33E': 762,  # Woman Farmer: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F33E': 763,  # Woman Farmer: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F373': 764,  # Man Cook
    u'\U0001F468\U0001F3FB\U0000200D\U0001F373': 765,  # Man Cook: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F373': 766,  # Man Cook: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F373': 767,  # Man Cook: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F373': 768,  # Man Cook: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F373': 769,  # Man Cook: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F373': 770,  # Woman Cook
    u'\U0001F469\U0001F3FB\U0000200D\U0001F373': 771,  # Woman Cook: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F373': 772,  # Woman Cook: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F373': 773,  # Woman Cook: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F373': 774,  # Woman Cook: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F373': 775,  # Woman Cook: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F527': 776,  # Man Mechanic
    u'\U0001F468\U0001F3FB\U0000200D\U0001F527': 777,  # Man Mechanic: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F527': 778,  # Man Mechanic: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F527': 779,  # Man Mechanic: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F527': 780,  # Man Mechanic: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F527': 781,  # Man Mechanic: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F527': 782,  # Woman Mechanic
    u'\U0001F469\U0001F3FB\U0000200D\U0001F527': 783,  # Woman Mechanic: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F527': 784,  # Woman Mechanic: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F527': 785,  # Woman Mechanic: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F527': 786,  # Woman Mechanic: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F527': 787,  # Woman Mechanic: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F3ED': 788,  # Man Factory Worker
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3ED': 789,  # Man Factory Worker: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3ED': 790,  # Man Factory Worker: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3ED': 791,  # Man Factory Worker: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3ED': 792,  # Man Factory Worker: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3ED': 793,  # Man Factory Worker: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F3ED': 794,  # Woman Factory Worker
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3ED': 795,  # Woman Factory Worker: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3ED': 796,  # Woman Factory Worker: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3ED': 797,  # Woman Factory Worker: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3ED': 798,  # Woman Factory Worker: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3ED': 799,  # Woman Factory Worker: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F4BC': 800,  # Man Office Worker
    u'\U0001F468\U0001F3FB\U0000200D\U0001F4BC': 801,  # Man Office Worker: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F4BC': 802,  # Man Office Worker: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F4BC': 803,  # Man Office Worker: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F4BC': 804,  # Man Office Worker: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F4BC': 805,  # Man Office Worker: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F4BC': 806,  # Woman Office Worker
    u'\U0001F469\U0001F3FB\U0000200D\U0001F4BC': 807,  # Woman Office Worker: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F4BC': 808,  # Woman Office Worker: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F4BC': 809,  # Woman Office Worker: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F4BC': 810,  # Woman Office Worker: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F4BC': 811,  # Woman Office Worker: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F52C': 812,  # Man Scientist
    u'\U0001F468\U0001F3FB\U0000200D\U0001F52C': 813,  # Man Scientist: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F52C': 814,  # Man Scientist: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F52C': 815,  # Man Scientist: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F52C': 816,  # Man Scientist: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F52C': 817,  # Man Scientist: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F52C': 818,  # Woman Scientist
    u'\U0001F469\U0001F3FB\U0000200D\U0001F52C': 819,  # Woman Scientist: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F52C': 820,  # Woman Scientist: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F52C': 821,  # Woman Scientist: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F52C': 822,  # Woman Scientist: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F52C': 823,  # Woman Scientist: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F4BB': 824,  # Man Technologist
    u'\U0001F468\U0001F3FB\U0000200D\U0001F4BB': 825,  # Man Technologist: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F4BB': 826,  # Man Technologist: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F4BB': 827,  # Man Technologist: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F4BB': 828,  # Man Technologist: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F4BB': 829,  # Man Technologist: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F4BB': 830,  # Woman Technologist
    u'\U0001F469\U0001F3FB\U0000200D\U0001F4BB': 831,  # Woman Technologist: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F4BB': 832,  # Woman Technologist: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F4BB': 833,  # Woman Technologist: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F4BB': 834,  # Woman Technologist: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F4BB': 835,  # Woman Technologist: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F3A4': 836,  # Man Singer
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3A4': 837,  # Man Singer: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3A4': 838,  # Man Singer: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3A4': 839,  # Man Singer: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3A4': 840,  # Man Singer: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3A4': 841,  # Man Singer: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F3A4': 842,  # Woman Singer
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3A4': 843,  # Woman Singer: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3A4': 844,  # Woman Singer: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3A4': 845,  # Woman Singer: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3A4': 846,  # Woman Singer: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3A4': 847,  # Woman Singer: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F3A8': 848,  # Man Artist
    u'\U0001F468\U0001F3FB\U0000200D\U0001F3A8': 849,  # Man Artist: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F3A8': 850,  # Man Artist: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F3A8': 851,  # Man Artist: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F3A8': 852,  # Man Artist: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F3A8': 853,  # Man Artist: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F3A8': 854,  # Woman Artist
    u'\U0001F469\U0001F3FB\U0000200D\U0001F3A8': 855,  # Woman Artist: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F3A8': 856,  # Woman Artist: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F3A8': 857,  # Woman Artist: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F3A8': 858,  # Woman Artist: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F3A8': 859,  # Woman Artist: Dark Skin Tone
    u'\U0001F468\U0000200D\U00002708': 860,  # Man Pilot
    u'\U0001F468\U0001F3FB\U0000200D\U00002708': 861,  # Man Pilot: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U00002708': 862,  # Man Pilot: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U00002708': 863,  # Man Pilot: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U00002708': 864,  # Man Pilot: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U00002708': 865,  # Man Pilot: Dark Skin Tone
    u'\U0001F469\U0000200D\U00002708': 866,  # Woman Pilot
    u'\U0001F469\U0001F3FB\U0000200D\U00002708': 867,  # Woman Pilot: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U00002708': 868,  # Woman Pilot: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U00002708': 869,  # Woman Pilot: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U00002708': 870,  # Woman Pilot: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U00002708': 871,  # Woman Pilot: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F680': 872,  # Man Astronaut
    u'\U0001F468\U0001F3FB\U0000200D\U0001F680': 873,  # Man Astronaut: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F680': 874,  # Man Astronaut: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F680': 875,  # Man Astronaut: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F680': 876,  # Man Astronaut: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F680': 877,  # Man Astronaut: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F680': 878,  # Woman Astronaut
    u'\U0001F469\U0001F3FB\U0000200D\U0001F680': 879,  # Woman Astronaut: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F680': 880,  # Woman Astronaut: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F680': 881,  # Woman Astronaut: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F680': 882,  # Woman Astronaut: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F680': 883,  # Woman Astronaut: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F692': 884,  # Man Firefighter
    u'\U0001F468\U0001F3FB\U0000200D\U0001F692': 885,  # Man Firefighter: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F692': 886,  # Man Firefighter: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F692': 887,  # Man Firefighter: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F692': 888,  # Man Firefighter: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F692': 889,  # Man Firefighter: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F692': 890,  # Woman Firefighter
    u'\U0001F469\U0001F3FB\U0000200D\U0001F692': 891,  # Woman Firefighter: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F692': 892,  # Woman Firefighter: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F692': 893,  # Woman Firefighter: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F692': 894,  # Woman Firefighter: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F692': 895,  # Woman Firefighter: Dark Skin Tone
    u'\U0001F46E': 896,  # Police Officer
    u'\U0001F46E\U0001F3FB\U0001F3FB': 897,  # Police Officer: Light Skin Tone
    u'\U0001F46E\U0001F3FC\U0001F3FC': 898,  # Police Officer: Medium-Light Skin Tone
    u'\U0001F46E\U0001F3FD\U0001F3FD': 899,  # Police Officer: Medium Skin Tone
    u'\U0001F46E\U0001F3FE\U0001F3FE': 900,  # Police Officer: Medium-Dark Skin Tone
    u'\U0001F46E\U0001F3FF\U0001F3FF': 901,  # Police Officer: Dark Skin Tone
    u'\U0001F46E\U0000200D\U00002642': 902,  # Man Police Officer
    u'\U0001F46E\U0001F3FB\U0000200D\U00002642': 903,  # Man Police Officer: Light Skin Tone
    u'\U0001F46E\U0001F3FC\U0000200D\U00002642': 904,  # Man Police Officer: Medium-Light Skin Tone
    u'\U0001F46E\U0001F3FD\U0000200D\U00002642': 905,  # Man Police Officer: Medium Skin Tone
    u'\U0001F46E\U0001F3FE\U0000200D\U00002642': 906,  # Man Police Officer: Medium-Dark Skin Tone
    u'\U0001F46E\U0001F3FF\U0000200D\U00002642': 907,  # Man Police Officer: Dark Skin Tone
    u'\U0001F46E\U0000200D\U00002640': 908,  # Woman Police Officer
    u'\U0001F46E\U0001F3FB\U0000200D\U00002640': 909,  # Woman Police Officer: Light Skin Tone
    u'\U0001F46E\U0001F3FC\U0000200D\U00002640': 910,  # Woman Police Officer: Medium-Light Skin Tone
    u'\U0001F46E\U0001F3FD\U0000200D\U00002640': 911,  # Woman Police Officer: Medium Skin Tone
    u'\U0001F46E\U0001F3FE\U0000200D\U00002640': 912,  # Woman Police Officer: Medium-Dark Skin Tone
    u'\U0001F46E\U0001F3FF\U0000200D\U00002640': 913,  # Woman Police Officer: Dark Skin Tone
    u'\U0001F575': 914,  # Detective
    u'\U0001F575\U0001F3FB\U0001F3FB': 915,  # Detective: Light Skin Tone
    u'\U0001F575\U0001F3FC\U0001F3FC': 916,  # Detective: Medium-Light Skin Tone
    u'\U0001F575\U0001F3FD\U0001F3FD': 917,  # Detective: Medium Skin Tone
    u'\U0001F575\U0001F3FE\U0001F3FE': 918,  # Detective: Medium-Dark Skin Tone
    u'\U0001F575\U0001F3FF\U0001F3FF': 919,  # Detective: Dark Skin Tone
    u'\U0001F575\U0000200D\U00002642': 920,  # Man Detective
    u'\U0001F575\U0001F3FB\U0000200D\U00002642': 921,  # Man Detective: Light Skin Tone
    u'\U0001F575\U0001F3FC\U0000200D\U00002642': 922,  # Man Detective: Medium-Light Skin Tone
    u'\U0001F575\U0001F3FD\U0000200D\U00002642': 923,  # Man Detective: Medium Skin Tone
    u'\U0001F575\U0001F3FE\U0000200D\U00002642': 924,  # Man Detective: Medium-Dark Skin Tone
    u'\U0001F575\U0001F3FF\U0000200D\U00002642': 925,  # Man Detective: Dark Skin Tone
    u'\U0001F575\U0000200D\U00002640': 926,  # Woman Detective
    u'\U0001F575\U0001F3FB\U0000200D\U00002640': 927,  # Woman Detective: Light Skin Tone
    u'\U0001F575\U0001F3FC\U0000200D\U00002640': 928,  # Woman Detective: Medium-Light Skin Tone
    u'\U0001F575\U0001F3FD\U0000200D\U00002640': 929,  # Woman Detective: Medium Skin Tone
    u'\U0001F575\U0001F3FE\U0000200D\U00002640': 930,  # Woman Detective: Medium-Dark Skin Tone
    u'\U0001F575\U0001F3FF\U0000200D\U00002640': 931,  # Woman Detective: Dark Skin Tone
    u'\U0001F482': 932,  # Guard
    u'\U0001F482\U0001F3FB\U0001F3FB': 933,  # Guard: Light Skin Tone
    u'\U0001F482\U0001F3FC\U0001F3FC': 934,  # Guard: Medium-Light Skin Tone
    u'\U0001F482\U0001F3FD\U0001F3FD': 935,  # Guard: Medium Skin Tone
    u'\U0001F482\U0001F3FE\U0001F3FE': 936,  # Guard: Medium-Dark Skin Tone
    u'\U0001F482\U0001F3FF\U0001F3FF': 937,  # Guard: Dark Skin Tone
    u'\U0001F482\U0000200D\U00002642': 938,  # Man Guard
    u'\U0001F482\U0001F3FB\U0000200D\U00002642': 939,  # Man Guard: Light Skin Tone
    u'\U0001F482\U0001F3FC\U0000200D\U00002642': 940,  # Man Guard: Medium-Light Skin Tone
    u'\U0001F482\U0001F3FD\U0000200D\U00002642': 941,  # Man Guard: Medium Skin Tone
    u'\U0001F482\U0001F3FE\U0000200D\U00002642': 942,  # Man Guard: Medium-Dark Skin Tone
    u'\U0001F482\U0001F3FF\U0000200D\U00002642': 943,  # Man Guard: Dark Skin Tone
    u'\U0001F482\U0000200D\U00002640': 944,  # Woman Guard
    u'\U0001F482\U0001F3FB\U0000200D\U00002640': 945,  # Woman Guard: Light Skin Tone
    u'\U0001F482\U0001F3FC\U0000200D\U00002640': 946,  # Woman Guard: Medium-Light Skin Tone
    u'\U0001F482\U0001F3FD\U0000200D\U00002640': 947,  # Woman Guard: Medium Skin Tone
    u'\U0001F482\U0001F3FE\U0000200D\U00002640': 948,  # Woman Guard: Medium-Dark Skin Tone
    u'\U0001F482\U0001F3FF\U0000200D\U00002640': 949,  # Woman Guard: Dark Skin Tone
    u'\U0001F477': 950,  # Construction Worker
    u'\U0001F477\U0001F3FB\U0001F3FB': 951,  # Construction Worker: Light Skin Tone
    u'\U0001F477\U0001F3FC\U0001F3FC': 952,  # Construction Worker: Medium-Light Skin Tone
    u'\U0001F477\U0001F3FD\U0001F3FD': 953,  # Construction Worker: Medium Skin Tone
    u'\U0001F477\U0001F3FE\U0001F3FE': 954,  # Construction Worker: Medium-Dark Skin Tone
    u'\U0001F477\U0001F3FF\U0001F3FF': 955,  # Construction Worker: Dark Skin Tone
    u'\U0001F477\U0000200D\U00002642': 956,  # Man Construction Worker
    u'\U0001F477\U0001F3FB\U0000200D\U00002642': 957,  # Man Construction Worker: Light Skin Tone
    u'\U0001F477\U0001F3FC\U0000200D\U00002642': 958,  # Man Construction Worker: Medium-Light Skin Tone
    u'\U0001F477\U0001F3FD\U0000200D\U00002642': 959,  # Man Construction Worker: Medium Skin Tone
    u'\U0001F477\U0001F3FE\U0000200D\U00002642': 960,  # Man Construction Worker: Medium-Dark Skin Tone
    u'\U0001F477\U0001F3FF\U0000200D\U00002642': 961,  # Man Construction Worker: Dark Skin Tone
    u'\U0001F477\U0000200D\U00002640': 962,  # Woman Construction Worker
    u'\U0001F477\U0001F3FB\U0000200D\U00002640': 963,  # Woman Construction Worker: Light Skin Tone
    u'\U0001F477\U0001F3FC\U0000200D\U00002640': 964,  # Woman Construction Worker: Medium-Light Skin Tone
    u'\U0001F477\U0001F3FD\U0000200D\U00002640': 965,  # Woman Construction Worker: Medium Skin Tone
    u'\U0001F477\U0001F3FE\U0000200D\U00002640': 966,  # Woman Construction Worker: Medium-Dark Skin Tone
    u'\U0001F477\U0001F3FF\U0000200D\U00002640': 967,  # Woman Construction Worker: Dark Skin Tone
    u'\U0001F934': 968,  # Prince
    u'\U0001F934\U0001F3FB\U0001F3FB': 969,  # Prince: Light Skin Tone
    u'\U0001F934\U0001F3FC\U0001F3FC': 970,  # Prince: Medium-Light Skin Tone
    u'\U0001F934\U0001F3FD\U0001F3FD': 971,  # Prince: Medium Skin Tone
    u'\U0001F934\U0001F3FE\U0001F3FE': 972,  # Prince: Medium-Dark Skin Tone
    u'\U0001F934\U0001F3FF\U0001F3FF': 973,  # Prince: Dark Skin Tone
    u'\U0001F478': 974,  # Princess
    u'\U0001F478\U0001F3FB\U0001F3FB': 975,  # Princess: Light Skin Tone
    u'\U0001F478\U0001F3FC\U0001F3FC': 976,  # Princess: Medium-Light Skin Tone
    u'\U0001F478\U0001F3FD\U0001F3FD': 977,  # Princess: Medium Skin Tone
    u'\U0001F478\U0001F3FE\U0001F3FE': 978,  # Princess: Medium-Dark Skin Tone
    u'\U0001F478\U0001F3FF\U0001F3FF': 979,  # Princess: Dark Skin Tone
    u'\U0001F473': 980,  # Person Wearing Turban
    u'\U0001F473\U0001F3FB\U0001F3FB': 981,  # Person Wearing Turban: Light Skin Tone
    u'\U0001F473\U0001F3FC\U0001F3FC': 982,  # Person Wearing Turban: Medium-Light Skin Tone
    u'\U0001F473\U0001F3FD\U0001F3FD': 983,  # Person Wearing Turban: Medium Skin Tone
    u'\U0001F473\U0001F3FE\U0001F3FE': 984,  # Person Wearing Turban: Medium-Dark Skin Tone
    u'\U0001F473\U0001F3FF\U0001F3FF': 985,  # Person Wearing Turban: Dark Skin Tone
    u'\U0001F473\U0000200D\U00002642': 986,  # Man Wearing Turban
    u'\U0001F473\U0001F3FB\U0000200D\U00002642': 987,  # Man Wearing Turban: Light Skin Tone
    u'\U0001F473\U0001F3FC\U0000200D\U00002642': 988,  # Man Wearing Turban: Medium-Light Skin Tone
    u'\U0001F473\U0001F3FD\U0000200D\U00002642': 989,  # Man Wearing Turban: Medium Skin Tone
    u'\U0001F473\U0001F3FE\U0000200D\U00002642': 990,  # Man Wearing Turban: Medium-Dark Skin Tone
    u'\U0001F473\U0001F3FF\U0000200D\U00002642': 991,  # Man Wearing Turban: Dark Skin Tone
    u'\U0001F473\U0000200D\U00002640': 992,  # Woman Wearing Turban
    u'\U0001F473\U0001F3FB\U0000200D\U00002640': 993,  # Woman Wearing Turban: Light Skin Tone
    u'\U0001F473\U0001F3FC\U0000200D\U00002640': 994,  # Woman Wearing Turban: Medium-Light Skin Tone
    u'\U0001F473\U0001F3FD\U0000200D\U00002640': 995,  # Woman Wearing Turban: Medium Skin Tone
    u'\U0001F473\U0001F3FE\U0000200D\U00002640': 996,  # Woman Wearing Turban: Medium-Dark Skin Tone
    u'\U0001F473\U0001F3FF\U0000200D\U00002640': 997,  # Woman Wearing Turban: Dark Skin Tone
    u'\U0001F472': 998,  # Person With Skullcap
    u'\U0001F472\U0001F3FB\U0001F3FB': 999,  # Person With Skullcap: Light Skin Tone
    u'\U0001F472\U0001F3FC\U0001F3FC': 1000,  # Person With Skullcap: Medium-Light Skin Tone
    u'\U0001F472\U0001F3FD\U0001F3FD': 1001,  # Person With Skullcap: Medium Skin Tone
    u'\U0001F472\U0001F3FE\U0001F3FE': 1002,  # Person With Skullcap: Medium-Dark Skin Tone
    u'\U0001F472\U0001F3FF\U0001F3FF': 1003,  # Person With Skullcap: Dark Skin Tone
    u'\U0001F9D5': 1004,  # Woman with Headscarf
    u'\U0001F9D5\U0001F3FB\U0001F3FB': 1005,  # Woman with Headscarf: Light Skin Tone
    u'\U0001F9D5\U0001F3FC\U0001F3FC': 1006,  # Woman with Headscarf: Medium-Light Skin Tone
    u'\U0001F9D5\U0001F3FD\U0001F3FD': 1007,  # Woman with Headscarf: Medium Skin Tone
    u'\U0001F9D5\U0001F3FE\U0001F3FE': 1008,  # Woman with Headscarf: Medium-Dark Skin Tone
    u'\U0001F9D5\U0001F3FF\U0001F3FF': 1009,  # Woman with Headscarf: Dark Skin Tone
    u'\U0001F935': 1010,  # Person in Tuxedo
    u'\U0001F935\U0001F3FB\U0001F3FB': 1011,  # Person in Tuxedo: Light Skin Tone
    u'\U0001F935\U0001F3FC\U0001F3FC': 1012,  # Person in Tuxedo: Medium-Light Skin Tone
    u'\U0001F935\U0001F3FD\U0001F3FD': 1013,  # Person in Tuxedo: Medium Skin Tone
    u'\U0001F935\U0001F3FE\U0001F3FE': 1014,  # Person in Tuxedo: Medium-Dark Skin Tone
    u'\U0001F935\U0001F3FF\U0001F3FF': 1015,  # Person in Tuxedo: Dark Skin Tone
    u'\U0001F470': 1016,  # Person With Veil
    u'\U0001F470\U0001F3FB\U0001F3FB': 1017,  # Person With Veil: Light Skin Tone
    u'\U0001F470\U0001F3FC\U0001F3FC': 1018,  # Person With Veil: Medium-Light Skin Tone
    u'\U0001F470\U0001F3FD\U0001F3FD': 1019,  # Person With Veil: Medium Skin Tone
    u'\U0001F470\U0001F3FE\U0001F3FE': 1020,  # Person With Veil: Medium-Dark Skin Tone
    u'\U0001F470\U0001F3FF\U0001F3FF': 1021,  # Person With Veil: Dark Skin Tone
    u'\U0001F930': 1022,  # Pregnant Woman
    u'\U0001F930\U0001F3FB\U0001F3FB': 1023,  # Pregnant Woman: Light Skin Tone
    u'\U0001F930\U0001F3FC\U0001F3FC': 1024,  # Pregnant Woman: Medium-Light Skin Tone
    u'\U0001F930\U0001F3FD\U0001F3FD': 1025,  # Pregnant Woman: Medium Skin Tone
    u'\U0001F930\U0001F3FE\U0001F3FE': 1026,  # Pregnant Woman: Medium-Dark Skin Tone
    u'\U0001F930\U0001F3FF\U0001F3FF': 1027,  # Pregnant Woman: Dark Skin Tone
    u'\U0001F931': 1028,  # Breast-Feeding
    u'\U0001F931\U0001F3FB\U0001F3FB': 1029,  # Breast-Feeding: Light Skin Tone
    u'\U0001F931\U0001F3FC\U0001F3FC': 1030,  # Breast-Feeding: Medium-Light Skin Tone
    u'\U0001F931\U0001F3FD\U0001F3FD': 1031,  # Breast-Feeding: Medium Skin Tone
    u'\U0001F931\U0001F3FE\U0001F3FE': 1032,  # Breast-Feeding: Medium-Dark Skin Tone
    u'\U0001F931\U0001F3FF\U0001F3FF': 1033,  # Breast-Feeding: Dark Skin Tone
    u'\U0001F47C': 1034,  # Baby Angel
    u'\U0001F47C\U0001F3FB\U0001F3FB': 1035,  # Baby Angel: Light Skin Tone
    u'\U0001F47C\U0001F3FC\U0001F3FC': 1036,  # Baby Angel: Medium-Light Skin Tone
    u'\U0001F47C\U0001F3FD\U0001F3FD': 1037,  # Baby Angel: Medium Skin Tone
    u'\U0001F47C\U0001F3FE\U0001F3FE': 1038,  # Baby Angel: Medium-Dark Skin Tone
    u'\U0001F47C\U0001F3FF\U0001F3FF': 1039,  # Baby Angel: Dark Skin Tone
    u'\U0001F385': 1040,  # Santa Claus
    u'\U0001F385\U0001F3FB\U0001F3FB': 1041,  # Santa Claus: Light Skin Tone
    u'\U0001F385\U0001F3FC\U0001F3FC': 1042,  # Santa Claus: Medium-Light Skin Tone
    u'\U0001F385\U0001F3FD\U0001F3FD': 1043,  # Santa Claus: Medium Skin Tone
    u'\U0001F385\U0001F3FE\U0001F3FE': 1044,  # Santa Claus: Medium-Dark Skin Tone
    u'\U0001F385\U0001F3FF\U0001F3FF': 1045,  # Santa Claus: Dark Skin Tone
    u'\U0001F936': 1046,  # Mrs. Claus
    u'\U0001F936\U0001F3FB\U0001F3FB': 1047,  # Mrs. Claus: Light Skin Tone
    u'\U0001F936\U0001F3FC\U0001F3FC': 1048,  # Mrs. Claus: Medium-Light Skin Tone
    u'\U0001F936\U0001F3FD\U0001F3FD': 1049,  # Mrs. Claus: Medium Skin Tone
    u'\U0001F936\U0001F3FE\U0001F3FE': 1050,  # Mrs. Claus: Medium-Dark Skin Tone
    u'\U0001F936\U0001F3FF\U0001F3FF': 1051,  # Mrs. Claus: Dark Skin Tone
    u'\U0001F9B8': 1052,  # Superhero
    u'\U0001F9B8\U0001F3FB\U0001F3FB': 1053,  # Superhero: Light Skin Tone
    u'\U0001F9B8\U0001F3FC\U0001F3FC': 1054,  # Superhero: Medium-Light Skin Tone
    u'\U0001F9B8\U0001F3FD\U0001F3FD': 1055,  # Superhero: Medium Skin Tone
    u'\U0001F9B8\U0001F3FE\U0001F3FE': 1056,  # Superhero: Medium-Dark Skin Tone
    u'\U0001F9B8\U0001F3FF\U0001F3FF': 1057,  # Superhero: Dark Skin Tone
    u'\U0001F9B8\U0000200D\U00002642': 1058,  # Man Superhero
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002642': 1059,  # Man Superhero: Light Skin Tone
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002642': 1060,  # Man Superhero: Medium-Light Skin Tone
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002642': 1061,  # Man Superhero: Medium Skin Tone
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002642': 1062,  # Man Superhero: Medium-Dark Skin Tone
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002642': 1063,  # Man Superhero: Dark Skin Tone
    u'\U0001F9B8\U0000200D\U00002640': 1064,  # Woman Superhero
    u'\U0001F9B8\U0001F3FB\U0000200D\U00002640': 1065,  # Woman Superhero: Light Skin Tone
    u'\U0001F9B8\U0001F3FC\U0000200D\U00002640': 1066,  # Woman Superhero: Medium-Light Skin Tone
    u'\U0001F9B8\U0001F3FD\U0000200D\U00002640': 1067,  # Woman Superhero: Medium Skin Tone
    u'\U0001F9B8\U0001F3FE\U0000200D\U00002640': 1068,  # Woman Superhero: Medium-Dark Skin Tone
    u'\U0001F9B8\U0001F3FF\U0000200D\U00002640': 1069,  # Woman Superhero: Dark Skin Tone
    u'\U0001F9B9': 1070,  # Supervillain
    u'\U0001F9B9\U0001F3FB\U0001F3FB': 1071,  # Supervillain: Light Skin Tone
    u'\U0001F9B9\U0001F3FC\U0001F3FC': 1072,  # Supervillain: Medium-Light Skin Tone
    u'\U0001F9B9\U0001F3FD\U0001F3FD': 1073,  # Supervillain: Medium Skin Tone
    u'\U0001F9B9\U0001F3FE\U0001F3FE': 1074,  # Supervillain: Medium-Dark Skin Tone
    u'\U0001F9B9\U0001F3FF\U0001F3FF': 1075,  # Supervillain: Dark Skin Tone
    u'\U0001F9B9\U0000200D\U00002642': 1076,  # Man Supervillain
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002642': 1077,  # Man Supervillain: Light Skin Tone
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002642': 1078,  # Man Supervillain: Medium-Light Skin Tone
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002642': 1079,  # Man Supervillain: Medium Skin Tone
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002642': 1080,  # Man Supervillain: Medium-Dark Skin Tone
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002642': 1081,  # Man Supervillain: Dark Skin Tone
    u'\U0001F9B9\U0000200D\U00002640': 1082,  # Woman Supervillain
    u'\U0001F9B9\U0001F3FB\U0000200D\U00002640': 1083,  # Woman Supervillain: Light Skin Tone
    u'\U0001F9B9\U0001F3FC\U0000200D\U00002640': 1084,  # Woman Supervillain: Medium-Light Skin Tone
    u'\U0001F9B9\U0001F3FD\U0000200D\U00002640': 1085,  # Woman Supervillain: Medium Skin Tone
    u'\U0001F9B9\U0001F3FE\U0000200D\U00002640': 1086,  # Woman Supervillain: Medium-Dark Skin Tone
    u'\U0001F9B9\U0001F3FF\U0000200D\U00002640': 1087,  # Woman Supervillain: Dark Skin Tone
    u'\U0001F9D9': 1088,  # Mage
    u'\U0001F9D9\U0001F3FB\U0001F3FB': 1089,  # Mage: Light Skin Tone
    u'\U0001F9D9\U0001F3FC\U0001F3FC': 1090,  # Mage: Medium-Light Skin Tone
    u'\U0001F9D9\U0001F3FD\U0001F3FD': 1091,  # Mage: Medium Skin Tone
    u'\U0001F9D9\U0001F3FE\U0001F3FE': 1092,  # Mage: Medium-Dark Skin Tone
    u'\U0001F9D9\U0001F3FF\U0001F3FF': 1093,  # Mage: Dark Skin Tone
    u'\U0001F9D9\U0000200D\U00002642': 1094,  # Man Mage
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002642': 1095,  # Man Mage: Light Skin Tone
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002642': 1096,  # Man Mage: Medium-Light Skin Tone
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002642': 1097,  # Man Mage: Medium Skin Tone
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002642': 1098,  # Man Mage: Medium-Dark Skin Tone
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002642': 1099,  # Man Mage: Dark Skin Tone
    u'\U0001F9D9\U0000200D\U00002640': 1100,  # Woman Mage
    u'\U0001F9D9\U0001F3FB\U0000200D\U00002640': 1101,  # Woman Mage: Light Skin Tone
    u'\U0001F9D9\U0001F3FC\U0000200D\U00002640': 1102,  # Woman Mage: Medium-Light Skin Tone
    u'\U0001F9D9\U0001F3FD\U0000200D\U00002640': 1103,  # Woman Mage: Medium Skin Tone
    u'\U0001F9D9\U0001F3FE\U0000200D\U00002640': 1104,  # Woman Mage: Medium-Dark Skin Tone
    u'\U0001F9D9\U0001F3FF\U0000200D\U00002640': 1105,  # Woman Mage: Dark Skin Tone
    u'\U0001F9DA': 1106,  # Fairy
    u'\U0001F9DA\U0001F3FB\U0001F3FB': 1107,  # Fairy: Light Skin Tone
    u'\U0001F9DA\U0001F3FC\U0001F3FC': 1108,  # Fairy: Medium-Light Skin Tone
    u'\U0001F9DA\U0001F3FD\U0001F3FD': 1109,  # Fairy: Medium Skin Tone
    u'\U0001F9DA\U0001F3FE\U0001F3FE': 1110,  # Fairy: Medium-Dark Skin Tone
    u'\U0001F9DA\U0001F3FF\U0001F3FF': 1111,  # Fairy: Dark Skin Tone
    u'\U0001F9DA\U0000200D\U00002642': 1112,  # Man Fairy
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002642': 1113,  # Man Fairy: Light Skin Tone
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002642': 1114,  # Man Fairy: Medium-Light Skin Tone
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002642': 1115,  # Man Fairy: Medium Skin Tone
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002642': 1116,  # Man Fairy: Medium-Dark Skin Tone
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002642': 1117,  # Man Fairy: Dark Skin Tone
    u'\U0001F9DA\U0000200D\U00002640': 1118,  # Woman Fairy
    u'\U0001F9DA\U0001F3FB\U0000200D\U00002640': 1119,  # Woman Fairy: Light Skin Tone
    u'\U0001F9DA\U0001F3FC\U0000200D\U00002640': 1120,  # Woman Fairy: Medium-Light Skin Tone
    u'\U0001F9DA\U0001F3FD\U0000200D\U00002640': 1121,  # Woman Fairy: Medium Skin Tone
    u'\U0001F9DA\U0001F3FE\U0000200D\U00002640': 1122,  # Woman Fairy: Medium-Dark Skin Tone
    u'\U0001F9DA\U0001F3FF\U0000200D\U00002640': 1123,  # Woman Fairy: Dark Skin Tone
    u'\U0001F9DB': 1124,  # Vampire
    u'\U0001F9DB\U0001F3FB\U0001F3FB': 1125,  # Vampire: Light Skin Tone
    u'\U0001F9DB\U0001F3FC\U0001F3FC': 1126,  # Vampire: Medium-Light Skin Tone
    u'\U0001F9DB\U0001F3FD\U0001F3FD': 1127,  # Vampire: Medium Skin Tone
    u'\U0001F9DB\U0001F3FE\U0001F3FE': 1128,  # Vampire: Medium-Dark Skin Tone
    u'\U0001F9DB\U0001F3FF\U0001F3FF': 1129,  # Vampire: Dark Skin Tone
    u'\U0001F9DB\U0000200D\U00002642': 1130,  # Man Vampire
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002642': 1131,  # Man Vampire: Light Skin Tone
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002642': 1132,  # Man Vampire: Medium-Light Skin Tone
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002642': 1133,  # Man Vampire: Medium Skin Tone
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002642': 1134,  # Man Vampire: Medium-Dark Skin Tone
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002642': 1135,  # Man Vampire: Dark Skin Tone
    u'\U0001F9DB\U0000200D\U00002640': 1136,  # Woman Vampire
    u'\U0001F9DB\U0001F3FB\U0000200D\U00002640': 1137,  # Woman Vampire: Light Skin Tone
    u'\U0001F9DB\U0001F3FC\U0000200D\U00002640': 1138,  # Woman Vampire: Medium-Light Skin Tone
    u'\U0001F9DB\U0001F3FD\U0000200D\U00002640': 1139,  # Woman Vampire: Medium Skin Tone
    u'\U0001F9DB\U0001F3FE\U0000200D\U00002640': 1140,  # Woman Vampire: Medium-Dark Skin Tone
    u'\U0001F9DB\U0001F3FF\U0000200D\U00002640': 1141,  # Woman Vampire: Dark Skin Tone
    u'\U0001F9DC': 1142,  # Merperson
    u'\U0001F9DC\U0001F3FB\U0001F3FB': 1143,  # Merperson: Light Skin Tone
    u'\U0001F9DC\U0001F3FC\U0001F3FC': 1144,  # Merperson: Medium-Light Skin Tone
    u'\U0001F9DC\U0001F3FD\U0001F3FD': 1145,  # Merperson: Medium Skin Tone
    u'\U0001F9DC\U0001F3FE\U0001F3FE': 1146,  # Merperson: Medium-Dark Skin Tone
    u'\U0001F9DC\U0001F3FF\U0001F3FF': 1147,  # Merperson: Dark Skin Tone
    u'\U0001F9DC\U0000200D\U00002642': 1148,  # Merman
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002642': 1149,  # Merman: Light Skin Tone
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002642': 1150,  # Merman: Medium-Light Skin Tone
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002642': 1151,  # Merman: Medium Skin Tone
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002642': 1152,  # Merman: Medium-Dark Skin Tone
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002642': 1153,  # Merman: Dark Skin Tone
    u'\U0001F9DC\U0000200D\U00002640': 1154,  # Mermaid
    u'\U0001F9DC\U0001F3FB\U0000200D\U00002640': 1155,  # Mermaid: Light Skin Tone
    u'\U0001F9DC\U0001F3FC\U0000200D\U00002640': 1156,  # Mermaid: Medium-Light Skin Tone
    u'\U0001F9DC\U0001F3FD\U0000200D\U00002640': 1157,  # Mermaid: Medium Skin Tone
    u'\U0001F9DC\U0001F3FE\U0000200D\U00002640': 1158,  # Mermaid: Medium-Dark Skin Tone
    u'\U0001F9DC\U0001F3FF\U0000200D\U00002640': 1159,  # Mermaid: Dark Skin Tone
    u'\U0001F9DD': 1160,  # Elf
    u'\U0001F9DD\U0001F3FB\U0001F3FB': 1161,  # Elf: Light Skin Tone
    u'\U0001F9DD\U0001F3FC\U0001F3FC': 1162,  # Elf: Medium-Light Skin Tone
    u'\U0001F9DD\U0001F3FD\U0001F3FD': 1163,  # Elf: Medium Skin Tone
    u'\U0001F9DD\U0001F3FE\U0001F3FE': 1164,  # Elf: Medium-Dark Skin Tone
    u'\U0001F9DD\U0001F3FF\U0001F3FF': 1165,  # Elf: Dark Skin Tone
    u'\U0001F9DD\U0000200D\U00002642': 1166,  # Man Elf
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002642': 1167,  # Man Elf: Light Skin Tone
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002642': 1168,  # Man Elf: Medium-Light Skin Tone
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002642': 1169,  # Man Elf: Medium Skin Tone
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002642': 1170,  # Man Elf: Medium-Dark Skin Tone
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002642': 1171,  # Man Elf: Dark Skin Tone
    u'\U0001F9DD\U0000200D\U00002640': 1172,  # Woman Elf
    u'\U0001F9DD\U0001F3FB\U0000200D\U00002640': 1173,  # Woman Elf: Light Skin Tone
    u'\U0001F9DD\U0001F3FC\U0000200D\U00002640': 1174,  # Woman Elf: Medium-Light Skin Tone
    u'\U0001F9DD\U0001F3FD\U0000200D\U00002640': 1175,  # Woman Elf: Medium Skin Tone
    u'\U0001F9DD\U0001F3FE\U0000200D\U00002640': 1176,  # Woman Elf: Medium-Dark Skin Tone
    u'\U0001F9DD\U0001F3FF\U0000200D\U00002640': 1177,  # Woman Elf: Dark Skin Tone
    u'\U0001F9DE': 1178,  # Genie
    u'\U0001F9DE\U0000200D\U00002642': 1179,  # Man Genie
    u'\U0001F9DE\U0000200D\U00002640': 1180,  # Woman Genie
    u'\U0001F9DF': 1181,  # Zombie
    u'\U0001F9DF\U0000200D\U00002642': 1182,  # Man Zombie
    u'\U0001F9DF\U0000200D\U00002640': 1183,  # Woman Zombie
    u'\U0001F486': 1184,  # Person Getting Massage
    u'\U0001F486\U0001F3FB\U0001F3FB': 1185,  # Person Getting Massage: Light Skin Tone
    u'\U0001F486\U0001F3FC\U0001F3FC': 1186,  # Person Getting Massage: Medium-Light Skin Tone
    u'\U0001F486\U0001F3FD\U0001F3FD': 1187,  # Person Getting Massage: Medium Skin Tone
    u'\U0001F486\U0001F3FE\U0001F3FE': 1188,  # Person Getting Massage: Medium-Dark Skin Tone
    u'\U0001F486\U0001F3FF\U0001F3FF': 1189,  # Person Getting Massage: Dark Skin Tone
    u'\U0001F486\U0000200D\U00002642': 1190,  # Man Getting Massage
    u'\U0001F486\U0001F3FB\U0000200D\U00002642': 1191,  # Man Getting Massage: Light Skin Tone
    u'\U0001F486\U0001F3FC\U0000200D\U00002642': 1192,  # Man Getting Massage: Medium-Light Skin Tone
    u'\U0001F486\U0001F3FD\U0000200D\U00002642': 1193,  # Man Getting Massage: Medium Skin Tone
    u'\U0001F486\U0001F3FE\U0000200D\U00002642': 1194,  # Man Getting Massage: Medium-Dark Skin Tone
    u'\U0001F486\U0001F3FF\U0000200D\U00002642': 1195,  # Man Getting Massage: Dark Skin Tone
    u'\U0001F486\U0000200D\U00002640': 1196,  # Woman Getting Massage
    u'\U0001F486\U0001F3FB\U0000200D\U00002640': 1197,  # Woman Getting Massage: Light Skin Tone
    u'\U0001F486\U0001F3FC\U0000200D\U00002640': 1198,  # Woman Getting Massage: Medium-Light Skin Tone
    u'\U0001F486\U0001F3FD\U0000200D\U00002640': 1199,  # Woman Getting Massage: Medium Skin Tone
    u'\U0001F486\U0001F3FE\U0000200D\U00002640': 1200,  # Woman Getting Massage: Medium-Dark Skin Tone
    u'\U0001F486\U0001F3FF\U0000200D\U00002640': 1201,  # Woman Getting Massage: Dark Skin Tone
    u'\U0001F487': 1202,  # Person Getting Haircut
    u'\U0001F487\U0001F3FB\U0001F3FB': 1203,  # Person Getting Haircut: Light Skin Tone
    u'\U0001F487\U0001F3FC\U0001F3FC': 1204,  # Person Getting Haircut: Medium-Light Skin Tone
    u'\U0001F487\U0001F3FD\U0001F3FD': 1205,  # Person Getting Haircut: Medium Skin Tone
    u'\U0001F487\U0001F3FE\U0001F3FE': 1206,  # Person Getting Haircut: Medium-Dark Skin Tone
    u'\U0001F487\U0001F3FF\U0001F3FF': 1207,  # Person Getting Haircut: Dark Skin Tone
    u'\U0001F487\U0000200D\U00002642': 1208,  # Man Getting Haircut
    u'\U0001F487\U0001F3FB\U0000200D\U00002642': 1209,  # Man Getting Haircut: Light Skin Tone
    u'\U0001F487\U0001F3FC\U0000200D\U00002642': 1210,  # Man Getting Haircut: Medium-Light Skin Tone
    u'\U0001F487\U0001F3FD\U0000200D\U00002642': 1211,  # Man Getting Haircut: Medium Skin Tone
    u'\U0001F487\U0001F3FE\U0000200D\U00002642': 1212,  # Man Getting Haircut: Medium-Dark Skin Tone
    u'\U0001F487\U0001F3FF\U0000200D\U00002642': 1213,  # Man Getting Haircut: Dark Skin Tone
    u'\U0001F487\U0000200D\U00002640': 1214,  # Woman Getting Haircut
    u'\U0001F487\U0001F3FB\U0000200D\U00002640': 1215,  # Woman Getting Haircut: Light Skin Tone
    u'\U0001F487\U0001F3FC\U0000200D\U00002640': 1216,  # Woman Getting Haircut: Medium-Light Skin Tone
    u'\U0001F487\U0001F3FD\U0000200D\U00002640': 1217,  # Woman Getting Haircut: Medium Skin Tone
    u'\U0001F487\U0001F3FE\U0000200D\U00002640': 1218,  # Woman Getting Haircut: Medium-Dark Skin Tone
    u'\U0001F487\U0001F3FF\U0000200D\U00002640': 1219,  # Woman Getting Haircut: Dark Skin Tone
    u'\U0001F6B6': 1220,  # Person Walking
    u'\U0001F6B6\U0001F3FB\U0001F3FB': 1221,  # Person Walking: Light Skin Tone
    u'\U0001F6B6\U0001F3FC\U0001F3FC': 1222,  # Person Walking: Medium-Light Skin Tone
    u'\U0001F6B6\U0001F3FD\U0001F3FD': 1223,  # Person Walking: Medium Skin Tone
    u'\U0001F6B6\U0001F3FE\U0001F3FE': 1224,  # Person Walking: Medium-Dark Skin Tone
    u'\U0001F6B6\U0001F3FF\U0001F3FF': 1225,  # Person Walking: Dark Skin Tone
    u'\U0001F6B6\U0000200D\U00002642': 1226,  # Man Walking
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002642': 1227,  # Man Walking: Light Skin Tone
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002642': 1228,  # Man Walking: Medium-Light Skin Tone
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002642': 1229,  # Man Walking: Medium Skin Tone
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002642': 1230,  # Man Walking: Medium-Dark Skin Tone
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002642': 1231,  # Man Walking: Dark Skin Tone
    u'\U0001F6B6\U0000200D\U00002640': 1232,  # Woman Walking
    u'\U0001F6B6\U0001F3FB\U0000200D\U00002640': 1233,  # Woman Walking: Light Skin Tone
    u'\U0001F6B6\U0001F3FC\U0000200D\U00002640': 1234,  # Woman Walking: Medium-Light Skin Tone
    u'\U0001F6B6\U0001F3FD\U0000200D\U00002640': 1235,  # Woman Walking: Medium Skin Tone
    u'\U0001F6B6\U0001F3FE\U0000200D\U00002640': 1236,  # Woman Walking: Medium-Dark Skin Tone
    u'\U0001F6B6\U0001F3FF\U0000200D\U00002640': 1237,  # Woman Walking: Dark Skin Tone
    u'\U0001F9CD': 1238,  # Person Standing
    u'\U0001F9CD\U0001F3FB\U0001F3FB': 1239,  # Person Standing: Light Skin Tone
    u'\U0001F9CD\U0001F3FC\U0001F3FC': 1240,  # Person Standing: Medium-Light Skin Tone
    u'\U0001F9CD\U0001F3FD\U0001F3FD': 1241,  # Person Standing: Medium Skin Tone
    u'\U0001F9CD\U0001F3FE\U0001F3FE': 1242,  # Person Standing: Medium-Dark Skin Tone
    u'\U0001F9CD\U0001F3FF\U0001F3FF': 1243,  # Person Standing: Dark Skin Tone
    u'\U0001F9CD\U0000200D\U00002642': 1244,  # Man Standing
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002642': 1245,  # Man Standing: Light Skin Tone
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002642': 1246,  # Man Standing: Medium-Light Skin Tone
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002642': 1247,  # Man Standing: Medium Skin Tone
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002642': 1248,  # Man Standing: Medium-Dark Skin Tone
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002642': 1249,  # Man Standing: Dark Skin Tone
    u'\U0001F9CD\U0000200D\U00002640': 1250,  # Woman Standing
    u'\U0001F9CD\U0001F3FB\U0000200D\U00002640': 1251,  # Woman Standing: Light Skin Tone
    u'\U0001F9CD\U0001F3FC\U0000200D\U00002640': 1252,  # Woman Standing: Medium-Light Skin Tone
    u'\U0001F9CD\U0001F3FD\U0000200D\U00002640': 1253,  # Woman Standing: Medium Skin Tone
    u'\U0001F9CD\U0001F3FE\U0000200D\U00002640': 1254,  # Woman Standing: Medium-Dark Skin Tone
    u'\U0001F9CD\U0001F3FF\U0000200D\U00002640': 1255,  # Woman Standing: Dark Skin Tone
    u'\U0001F9CE': 1256,  # Person Kneeling
    u'\U0001F9CE\U0001F3FB\U0001F3FB': 1257,  # Person Kneeling: Light Skin Tone
    u'\U0001F9CE\U0001F3FC\U0001F3FC': 1258,  # Person Kneeling: Medium-Light Skin Tone
    u'\U0001F9CE\U0001F3FD\U0001F3FD': 1259,  # Person Kneeling: Medium Skin Tone
    u'\U0001F9CE\U0001F3FE\U0001F3FE': 1260,  # Person Kneeling: Medium-Dark Skin Tone
    u'\U0001F9CE\U0001F3FF\U0001F3FF': 1261,  # Person Kneeling: Dark Skin Tone
    u'\U0001F9CE\U0000200D\U00002642': 1262,  # Man Kneeling
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002642': 1263,  # Man Kneeling: Light Skin Tone
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002642': 1264,  # Man Kneeling: Medium-Light Skin Tone
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002642': 1265,  # Man Kneeling: Medium Skin Tone
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002642': 1266,  # Man Kneeling: Medium-Dark Skin Tone
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002642': 1267,  # Man Kneeling: Dark Skin Tone
    u'\U0001F9CE\U0000200D\U00002640': 1268,  # Woman Kneeling
    u'\U0001F9CE\U0001F3FB\U0000200D\U00002640': 1269,  # Woman Kneeling: Light Skin Tone
    u'\U0001F9CE\U0001F3FC\U0000200D\U00002640': 1270,  # Woman Kneeling: Medium-Light Skin Tone
    u'\U0001F9CE\U0001F3FD\U0000200D\U00002640': 1271,  # Woman Kneeling: Medium Skin Tone
    u'\U0001F9CE\U0001F3FE\U0000200D\U00002640': 1272,  # Woman Kneeling: Medium-Dark Skin Tone
    u'\U0001F9CE\U0001F3FF\U0000200D\U00002640': 1273,  # Woman Kneeling: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F9AF': 1274,  # Man with Probing Cane
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9AF': 1275,  # Man with Probing Cane: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9AF': 1276,  # Man with Probing Cane: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9AF': 1277,  # Man with Probing Cane: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9AF': 1278,  # Man with Probing Cane: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9AF': 1279,  # Man with Probing Cane: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F9AF': 1280,  # Woman with Probing Cane
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9AF': 1281,  # Woman with Probing Cane: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9AF': 1282,  # Woman with Probing Cane: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9AF': 1283,  # Woman with Probing Cane: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9AF': 1284,  # Woman with Probing Cane: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9AF': 1285,  # Woman with Probing Cane: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F9BC': 1286,  # Man in Motorized Wheelchair
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9BC': 1287,  # Man in Motorized Wheelchair: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9BC': 1288,  # Man in Motorized Wheelchair: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9BC': 1289,  # Man in Motorized Wheelchair: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9BC': 1290,  # Man in Motorized Wheelchair: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9BC': 1291,  # Man in Motorized Wheelchair: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F9BC': 1292,  # Woman in Motorized Wheelchair
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9BC': 1293,  # Woman in Motorized Wheelchair: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9BC': 1294,  # Woman in Motorized Wheelchair: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9BC': 1295,  # Woman in Motorized Wheelchair: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9BC': 1296,  # Woman in Motorized Wheelchair: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9BC': 1297,  # Woman in Motorized Wheelchair: Dark Skin Tone
    u'\U0001F468\U0000200D\U0001F9BD': 1298,  # Man in Manual Wheelchair
    u'\U0001F468\U0001F3FB\U0000200D\U0001F9BD': 1299,  # Man in Manual Wheelchair: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F9BD': 1300,  # Man in Manual Wheelchair: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F9BD': 1301,  # Man in Manual Wheelchair: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F9BD': 1302,  # Man in Manual Wheelchair: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F9BD': 1303,  # Man in Manual Wheelchair: Dark Skin Tone
    u'\U0001F469\U0000200D\U0001F9BD': 1304,  # Woman in Manual Wheelchair
    u'\U0001F469\U0001F3FB\U0000200D\U0001F9BD': 1305,  # Woman in Manual Wheelchair: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F9BD': 1306,  # Woman in Manual Wheelchair: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F9BD': 1307,  # Woman in Manual Wheelchair: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F9BD': 1308,  # Woman in Manual Wheelchair: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F9BD': 1309,  # Woman in Manual Wheelchair: Dark Skin Tone
    u'\U0001F3C3': 1310,  # Person Running
    u'\U0001F3C3\U0001F3FB\U0001F3FB': 1311,  # Person Running: Light Skin Tone
    u'\U0001F3C3\U0001F3FC\U0001F3FC': 1312,  # Person Running: Medium-Light Skin Tone
    u'\U0001F3C3\U0001F3FD\U0001F3FD': 1313,  # Person Running: Medium Skin Tone
    u'\U0001F3C3\U0001F3FE\U0001F3FE': 1314,  # Person Running: Medium-Dark Skin Tone
    u'\U0001F3C3\U0001F3FF\U0001F3FF': 1315,  # Person Running: Dark Skin Tone
    u'\U0001F3C3\U0000200D\U00002642': 1316,  # Man Running
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002642': 1317,  # Man Running: Light Skin Tone
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002642': 1318,  # Man Running: Medium-Light Skin Tone
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002642': 1319,  # Man Running: Medium Skin Tone
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002642': 1320,  # Man Running: Medium-Dark Skin Tone
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002642': 1321,  # Man Running: Dark Skin Tone
    u'\U0001F3C3\U0000200D\U00002640': 1322,  # Woman Running
    u'\U0001F3C3\U0001F3FB\U0000200D\U00002640': 1323,  # Woman Running: Light Skin Tone
    u'\U0001F3C3\U0001F3FC\U0000200D\U00002640': 1324,  # Woman Running: Medium-Light Skin Tone
    u'\U0001F3C3\U0001F3FD\U0000200D\U00002640': 1325,  # Woman Running: Medium Skin Tone
    u'\U0001F3C3\U0001F3FE\U0000200D\U00002640': 1326,  # Woman Running: Medium-Dark Skin Tone
    u'\U0001F3C3\U0001F3FF\U0000200D\U00002640': 1327,  # Woman Running: Dark Skin Tone
    u'\U0001F483': 1328,  # Woman Dancing
    u'\U0001F483\U0001F3FB\U0001F3FB': 1329,  # Woman Dancing: Light Skin Tone
    u'\U0001F483\U0001F3FC\U0001F3FC': 1330,  # Woman Dancing: Medium-Light Skin Tone
    u'\U0001F483\U0001F3FD\U0001F3FD': 1331,  # Woman Dancing: Medium Skin Tone
    u'\U0001F483\U0001F3FE\U0001F3FE': 1332,  # Woman Dancing: Medium-Dark Skin Tone
    u'\U0001F483\U0001F3FF\U0001F3FF': 1333,  # Woman Dancing: Dark Skin Tone
    u'\U0001F57A': 1334,  # Man Dancing
    u'\U0001F57A\U0001F3FB\U0001F3FB': 1335,  # Man Dancing: Light Skin Tone
    u'\U0001F57A\U0001F3FC\U0001F3FC': 1336,  # Man Dancing: Medium-Light Skin Tone
    u'\U0001F57A\U0001F3FD\U0001F3FD': 1337,  # Man Dancing: Medium Skin Tone
    u'\U0001F57A\U0001F3FE\U0001F3FE': 1338,  # Man Dancing: Medium-Dark Skin Tone
    u'\U0001F57A\U0001F3FF\U0001F3FF': 1339,  # Man Dancing: Dark Skin Tone
    u'\U0001F574': 1340,  # Person in Suit Levitating
    u'\U0001F574\U0001F3FB\U0001F3FB': 1341,  # Person in Suit Levitating: Light Skin Tone
    u'\U0001F574\U0001F3FC\U0001F3FC': 1342,  # Person in Suit Levitating: Medium-Light Skin Tone
    u'\U0001F574\U0001F3FD\U0001F3FD': 1343,  # Person in Suit Levitating: Medium Skin Tone
    u'\U0001F574\U0001F3FE\U0001F3FE': 1344,  # Person in Suit Levitating: Medium-Dark Skin Tone
    u'\U0001F574\U0001F3FF\U0001F3FF': 1345,  # Person in Suit Levitating: Dark Skin Tone
    u'\U0001F46F': 1346,  # People with Bunny Ears
    u'\U0001F46F\U0001F3FB\U0001F3FB': 1347,  # Woman With Bunny Ears, Type-1-2
    u'\U0001F46F\U0001F3FC\U0001F3FC': 1348,  # Woman With Bunny Ears, Type-3
    u'\U0001F46F\U0001F3FD\U0001F3FD': 1349,  # Woman With Bunny Ears, Type-4
    u'\U0001F46F\U0001F3FE\U0001F3FE': 1350,  # Woman With Bunny Ears, Type-5
    u'\U0001F46F\U0001F3FF\U0001F3FF': 1351,  # Woman With Bunny Ears, Type-6
    u'\U0001F46F\U0000200D\U00002642': 1352,  # Men with Bunny Ears
    u'\U0001F46F\U0000200D\U00002640': 1353,  # Women with Bunny Ears
    u'\U0001F9D6': 1354,  # Person in Steamy Room
    u'\U0001F9D6\U0001F3FB\U0001F3FB': 1355,  # Person in Steamy Room: Light Skin Tone
    u'\U0001F9D6\U0001F3FC\U0001F3FC': 1356,  # Person in Steamy Room: Medium-Light Skin Tone
    u'\U0001F9D6\U0001F3FD\U0001F3FD': 1357,  # Person in Steamy Room: Medium Skin Tone
    u'\U0001F9D6\U0001F3FE\U0001F3FE': 1358,  # Person in Steamy Room: Medium-Dark Skin Tone
    u'\U0001F9D6\U0001F3FF\U0001F3FF': 1359,  # Person in Steamy Room: Dark Skin Tone
    u'\U0001F9D6\U0000200D\U00002642': 1360,  # Man in Steamy Room
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002642': 1361,  # Man in Steamy Room: Light Skin Tone
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002642': 1362,  # Man in Steamy Room: Medium-Light Skin Tone
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002642': 1363,  # Man in Steamy Room: Medium Skin Tone
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002642': 1364,  # Man in Steamy Room: Medium-Dark Skin Tone
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002642': 1365,  # Man in Steamy Room: Dark Skin Tone
    u'\U0001F9D6\U0000200D\U00002640': 1366,  # Woman in Steamy Room
    u'\U0001F9D6\U0001F3FB\U0000200D\U00002640': 1367,  # Woman in Steamy Room: Light Skin Tone
    u'\U0001F9D6\U0001F3FC\U0000200D\U00002640': 1368,  # Woman in Steamy Room: Medium-Light Skin Tone
    u'\U0001F9D6\U0001F3FD\U0000200D\U00002640': 1369,  # Woman in Steamy Room: Medium Skin Tone
    u'\U0001F9D6\U0001F3FE\U0000200D\U00002640': 1370,  # Woman in Steamy Room: Medium-Dark Skin Tone
    u'\U0001F9D6\U0001F3FF\U0000200D\U00002640': 1371,  # Woman in Steamy Room: Dark Skin Tone
    u'\U0001F9D7': 1372,  # Person Climbing
    u'\U0001F9D7\U0001F3FB\U0001F3FB': 1373,  # Person Climbing: Light Skin Tone
    u'\U0001F9D7\U0001F3FC\U0001F3FC': 1374,  # Person Climbing: Medium-Light Skin Tone
    u'\U0001F9D7\U0001F3FD\U0001F3FD': 1375,  # Person Climbing: Medium Skin Tone
    u'\U0001F9D7\U0001F3FE\U0001F3FE': 1376,  # Person Climbing: Medium-Dark Skin Tone
    u'\U0001F9D7\U0001F3FF\U0001F3FF': 1377,  # Person Climbing: Dark Skin Tone
    u'\U0001F9D7\U0000200D\U00002642': 1378,  # Man Climbing
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002642': 1379,  # Man Climbing: Light Skin Tone
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002642': 1380,  # Man Climbing: Medium-Light Skin Tone
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002642': 1381,  # Man Climbing: Medium Skin Tone
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002642': 1382,  # Man Climbing: Medium-Dark Skin Tone
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002642': 1383,  # Man Climbing: Dark Skin Tone
    u'\U0001F9D7\U0000200D\U00002640': 1384,  # Woman Climbing
    u'\U0001F9D7\U0001F3FB\U0000200D\U00002640': 1385,  # Woman Climbing: Light Skin Tone
    u'\U0001F9D7\U0001F3FC\U0000200D\U00002640': 1386,  # Woman Climbing: Medium-Light Skin Tone
    u'\U0001F9D7\U0001F3FD\U0000200D\U00002640': 1387,  # Woman Climbing: Medium Skin Tone
    u'\U0001F9D7\U0001F3FE\U0000200D\U00002640': 1388,  # Woman Climbing: Medium-Dark Skin Tone
    u'\U0001F9D7\U0001F3FF\U0000200D\U00002640': 1389,  # Woman Climbing: Dark Skin Tone
    u'\U0001F93A': 1390,  # Person Fencing
    u'\U0001F3C7': 1391,  # Horse Racing
    u'\U0001F3C7\U0001F3FB\U0001F3FB': 1392,  # Horse Racing: Light Skin Tone
    u'\U0001F3C7\U0001F3FC\U0001F3FC': 1393,  # Horse Racing: Medium-Light Skin Tone
    u'\U0001F3C7\U0001F3FD\U0001F3FD': 1394,  # Horse Racing: Medium Skin Tone
    u'\U0001F3C7\U0001F3FE\U0001F3FE': 1395,  # Horse Racing: Medium-Dark Skin Tone
    u'\U0001F3C7\U0001F3FF\U0001F3FF': 1396,  # Horse Racing: Dark Skin Tone
    u'\U000026F7': 1397,  # Skier
    u'\U0001F3C2': 1398,  # Snowboarder
    u'\U0001F3CC': 1399,  # Person Golfing
    u'\U0001F3CC\U0001F3FB\U0001F3FB': 1400,  # Person Golfing: Light Skin Tone
    u'\U0001F3CC\U0001F3FC\U0001F3FC': 1401,  # Person Golfing: Medium-Light Skin Tone
    u'\U0001F3CC\U0001F3FD\U0001F3FD': 1402,  # Person Golfing: Medium Skin Tone
    u'\U0001F3CC\U0001F3FE\U0001F3FE': 1403,  # Person Golfing: Medium-Dark Skin Tone
    u'\U0001F3CC\U0001F3FF\U0001F3FF': 1404,  # Person Golfing: Dark Skin Tone
    u'\U0001F3CC\U0000200D\U00002642': 1405,  # Man Golfing
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002642': 1406,  # Man Golfing: Light Skin Tone
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002642': 1407,  # Man Golfing: Medium-Light Skin Tone
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002642': 1408,  # Man Golfing: Medium Skin Tone
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002642': 1409,  # Man Golfing: Medium-Dark Skin Tone
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002642': 1410,  # Man Golfing: Dark Skin Tone
    u'\U0001F3CC\U0000200D\U00002640': 1411,  # Woman Golfing
    u'\U0001F3CC\U0001F3FB\U0000200D\U00002640': 1412,  # Woman Golfing: Light Skin Tone
    u'\U0001F3CC\U0001F3FC\U0000200D\U00002640': 1413,  # Woman Golfing: Medium-Light Skin Tone
    u'\U0001F3CC\U0001F3FD\U0000200D\U00002640': 1414,  # Woman Golfing: Medium Skin Tone
    u'\U0001F3CC\U0001F3FE\U0000200D\U00002640': 1415,  # Woman Golfing: Medium-Dark Skin Tone
    u'\U0001F3CC\U0001F3FF\U0000200D\U00002640': 1416,  # Woman Golfing: Dark Skin Tone
    u'\U0001F3C4': 1417,  # Person Surfing
    u'\U0001F3C4\U0001F3FB\U0001F3FB': 1418,  # Person Surfing: Light Skin Tone
    u'\U0001F3C4\U0001F3FC\U0001F3FC': 1419,  # Person Surfing: Medium-Light Skin Tone
    u'\U0001F3C4\U0001F3FD\U0001F3FD': 1420,  # Person Surfing: Medium Skin Tone
    u'\U0001F3C4\U0001F3FE\U0001F3FE': 1421,  # Person Surfing: Medium-Dark Skin Tone
    u'\U0001F3C4\U0001F3FF\U0001F3FF': 1422,  # Person Surfing: Dark Skin Tone
    u'\U0001F3C4\U0000200D\U00002642': 1423,  # Man Surfing
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002642': 1424,  # Man Surfing: Light Skin Tone
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002642': 1425,  # Man Surfing: Medium-Light Skin Tone
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002642': 1426,  # Man Surfing: Medium Skin Tone
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002642': 1427,  # Man Surfing: Medium-Dark Skin Tone
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002642': 1428,  # Man Surfing: Dark Skin Tone
    u'\U0001F3C4\U0000200D\U00002640': 1429,  # Woman Surfing
    u'\U0001F3C4\U0001F3FB\U0000200D\U00002640': 1430,  # Woman Surfing: Light Skin Tone
    u'\U0001F3C4\U0001F3FC\U0000200D\U00002640': 1431,  # Woman Surfing: Medium-Light Skin Tone
    u'\U0001F3C4\U0001F3FD\U0000200D\U00002640': 1432,  # Woman Surfing: Medium Skin Tone
    u'\U0001F3C4\U0001F3FE\U0000200D\U00002640': 1433,  # Woman Surfing: Medium-Dark Skin Tone
    u'\U0001F3C4\U0001F3FF\U0000200D\U00002640': 1434,  # Woman Surfing: Dark Skin Tone
    u'\U0001F6A3': 1435,  # Person Rowing Boat
    u'\U0001F6A3\U0001F3FB\U0001F3FB': 1436,  # Person Rowing Boat: Light Skin Tone
    u'\U0001F6A3\U0001F3FC\U0001F3FC': 1437,  # Person Rowing Boat: Medium-Light Skin Tone
    u'\U0001F6A3\U0001F3FD\U0001F3FD': 1438,  # Person Rowing Boat: Medium Skin Tone
    u'\U0001F6A3\U0001F3FE\U0001F3FE': 1439,  # Person Rowing Boat: Medium-Dark Skin Tone
    u'\U0001F6A3\U0001F3FF\U0001F3FF': 1440,  # Person Rowing Boat: Dark Skin Tone
    u'\U0001F6A3\U0000200D\U00002642': 1441,  # Man Rowing Boat
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002642': 1442,  # Man Rowing Boat: Light Skin Tone
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002642': 1443,  # Man Rowing Boat: Medium-Light Skin Tone
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002642': 1444,  # Man Rowing Boat: Medium Skin Tone
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002642': 1445,  # Man Rowing Boat: Medium-Dark Skin Tone
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002642': 1446,  # Man Rowing Boat: Dark Skin Tone
    u'\U0001F6A3\U0000200D\U00002640': 1447,  # Woman Rowing Boat
    u'\U0001F6A3\U0001F3FB\U0000200D\U00002640': 1448,  # Woman Rowing Boat: Light Skin Tone
    u'\U0001F6A3\U0001F3FC\U0000200D\U00002640': 1449,  # Woman Rowing Boat: Medium-Light Skin Tone
    u'\U0001F6A3\U0001F3FD\U0000200D\U00002640': 1450,  # Woman Rowing Boat: Medium Skin Tone
    u'\U0001F6A3\U0001F3FE\U0000200D\U00002640': 1451,  # Woman Rowing Boat: Medium-Dark Skin Tone
    u'\U0001F6A3\U0001F3FF\U0000200D\U00002640': 1452,  # Woman Rowing Boat: Dark Skin Tone
    u'\U0001F3CA': 1453,  # Person Swimming
    u'\U0001F3CA\U0001F3FB\U0001F3FB': 1454,  # Person Swimming: Light Skin Tone
    u'\U0001F3CA\U0001F3FC\U0001F3FC': 1455,  # Person Swimming: Medium-Light Skin Tone
    u'\U0001F3CA\U0001F3FD\U0001F3FD': 1456,  # Person Swimming: Medium Skin Tone
    u'\U0001F3CA\U0001F3FE\U0001F3FE': 1457,  # Person Swimming: Medium-Dark Skin Tone
    u'\U0001F3CA\U0001F3FF\U0001F3FF': 1458,  # Person Swimming: Dark Skin Tone
    u'\U0001F3CA\U0000200D\U00002642': 1459,  # Man Swimming
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002642': 1460,  # Man Swimming: Light Skin Tone
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002642': 1461,  # Man Swimming: Medium-Light Skin Tone
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002642': 1462,  # Man Swimming: Medium Skin Tone
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002642': 1463,  # Man Swimming: Medium-Dark Skin Tone
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002642': 1464,  # Man Swimming: Dark Skin Tone
    u'\U0001F3CA\U0000200D\U00002640': 1465,  # Woman Swimming
    u'\U0001F3CA\U0001F3FB\U0000200D\U00002640': 1466,  # Woman Swimming: Light Skin Tone
    u'\U0001F3CA\U0001F3FC\U0000200D\U00002640': 1467,  # Woman Swimming: Medium-Light Skin Tone
    u'\U0001F3CA\U0001F3FD\U0000200D\U00002640': 1468,  # Woman Swimming: Medium Skin Tone
    u'\U0001F3CA\U0001F3FE\U0000200D\U00002640': 1469,  # Woman Swimming: Medium-Dark Skin Tone
    u'\U0001F3CA\U0001F3FF\U0000200D\U00002640': 1470,  # Woman Swimming: Dark Skin Tone
    u'\U000026F9': 1471,  # Person Bouncing Ball
    u'\U000026F9\U0001F3FB\U0001F3FB': 1472,  # Person Bouncing Ball: Light Skin Tone
    u'\U000026F9\U0001F3FC\U0001F3FC': 1473,  # Person Bouncing Ball: Medium-Light Skin Tone
    u'\U000026F9\U0001F3FD\U0001F3FD': 1474,  # Person Bouncing Ball: Medium Skin Tone
    u'\U000026F9\U0001F3FE\U0001F3FE': 1475,  # Person Bouncing Ball: Medium-Dark Skin Tone
    u'\U000026F9\U0001F3FF\U0001F3FF': 1476,  # Person Bouncing Ball: Dark Skin Tone
    u'\U000026F9\U0000200D\U00002642': 1477,  # Man Bouncing Ball
    u'\U000026F9\U0001F3FB\U0000200D\U00002642': 1478,  # Man Bouncing Ball: Light Skin Tone
    u'\U000026F9\U0001F3FC\U0000200D\U00002642': 1479,  # Man Bouncing Ball: Medium-Light Skin Tone
    u'\U000026F9\U0001F3FD\U0000200D\U00002642': 1480,  # Man Bouncing Ball: Medium Skin Tone
    u'\U000026F9\U0001F3FE\U0000200D\U00002642': 1481,  # Man Bouncing Ball: Medium-Dark Skin Tone
    u'\U000026F9\U0001F3FF\U0000200D\U00002642': 1482,  # Man Bouncing Ball: Dark Skin Tone
    u'\U000026F9\U0000200D\U00002640': 1483,  # Woman Bouncing Ball
    u'\U000026F9\U0001F3FB\U0000200D\U00002640': 1484,  # Woman Bouncing Ball: Light Skin Tone
    u'\U000026F9\U0001F3FC\U0000200D\U00002640': 1485,  # Woman Bouncing Ball: Medium-Light Skin Tone
    u'\U000026F9\U0001F3FD\U0000200D\U00002640': 1486,  # Woman Bouncing Ball: Medium Skin Tone
    u'\U000026F9\U0001F3FE\U0000200D\U00002640': 1487,  # Woman Bouncing Ball: Medium-Dark Skin Tone
    u'\U000026F9\U0001F3FF\U0000200D\U00002640': 1488,  # Woman Bouncing Ball: Dark Skin Tone
    u'\U0001F3CB': 1489,  # Person Lifting Weights
    u'\U0001F3CB\U0001F3FB\U0001F3FB': 1490,  # Person Lifting Weights: Light Skin Tone
    u'\U0001F3CB\U0001F3FC\U0001F3FC': 1491,  # Person Lifting Weights: Medium-Light Skin Tone
    u'\U0001F3CB\U0001F3FD\U0001F3FD': 1492,  # Person Lifting Weights: Medium Skin Tone
    u'\U0001F3CB\U0001F3FE\U0001F3FE': 1493,  # Person Lifting Weights: Medium-Dark Skin Tone
    u'\U0001F3CB\U0001F3FF\U0001F3FF': 1494,  # Person Lifting Weights: Dark Skin Tone
    u'\U0001F3CB\U0000200D\U00002642': 1495,  # Man Lifting Weights
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002642': 1496,  # Man Lifting Weights: Light Skin Tone
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002642': 1497,  # Man Lifting Weights: Medium-Light Skin Tone
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002642': 1498,  # Man Lifting Weights: Medium Skin Tone
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002642': 1499,  # Man Lifting Weights: Medium-Dark Skin Tone
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002642': 1500,  # Man Lifting Weights: Dark Skin Tone
    u'\U0001F3CB\U0000200D\U00002640': 1501,  # Woman Lifting Weights
    u'\U0001F3CB\U0001F3FB\U0000200D\U00002640': 1502,  # Woman Lifting Weights: Light Skin Tone
    u'\U0001F3CB\U0001F3FC\U0000200D\U00002640': 1503,  # Woman Lifting Weights: Medium-Light Skin Tone
    u'\U0001F3CB\U0001F3FD\U0000200D\U00002640': 1504,  # Woman Lifting Weights: Medium Skin Tone
    u'\U0001F3CB\U0001F3FE\U0000200D\U00002640': 1505,  # Woman Lifting Weights: Medium-Dark Skin Tone
    u'\U0001F3CB\U0001F3FF\U0000200D\U00002640': 1506,  # Woman Lifting Weights: Dark Skin Tone
    u'\U0001F6B4': 1507,  # Person Biking
    u'\U0001F6B4\U0001F3FB\U0001F3FB': 1508,  # Person Biking: Light Skin Tone
    u'\U0001F6B4\U0001F3FC\U0001F3FC': 1509,  # Person Biking: Medium-Light Skin Tone
    u'\U0001F6B4\U0001F3FD\U0001F3FD': 1510,  # Person Biking: Medium Skin Tone
    u'\U0001F6B4\U0001F3FE\U0001F3FE': 1511,  # Person Biking: Medium-Dark Skin Tone
    u'\U0001F6B4\U0001F3FF\U0001F3FF': 1512,  # Person Biking: Dark Skin Tone
    u'\U0001F6B4\U0000200D\U00002642': 1513,  # Man Biking
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002642': 1514,  # Man Biking: Light Skin Tone
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002642': 1515,  # Man Biking: Medium-Light Skin Tone
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002642': 1516,  # Man Biking: Medium Skin Tone
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002642': 1517,  # Man Biking: Medium-Dark Skin Tone
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002642': 1518,  # Man Biking: Dark Skin Tone
    u'\U0001F6B4\U0000200D\U00002640': 1519,  # Woman Biking
    u'\U0001F6B4\U0001F3FB\U0000200D\U00002640': 1520,  # Woman Biking: Light Skin Tone
    u'\U0001F6B4\U0001F3FC\U0000200D\U00002640': 1521,  # Woman Biking: Medium-Light Skin Tone
    u'\U0001F6B4\U0001F3FD\U0000200D\U00002640': 1522,  # Woman Biking: Medium Skin Tone
    u'\U0001F6B4\U0001F3FE\U0000200D\U00002640': 1523,  # Woman Biking: Medium-Dark Skin Tone
    u'\U0001F6B4\U0001F3FF\U0000200D\U00002640': 1524,  # Woman Biking: Dark Skin Tone
    u'\U0001F6B5': 1525,  # Person Mountain Biking
    u'\U0001F6B5\U0001F3FB\U0001F3FB': 1526,  # Person Mountain Biking: Light Skin Tone
    u'\U0001F6B5\U0001F3FC\U0001F3FC': 1527,  # Person Mountain Biking: Medium-Light Skin Tone
    u'\U0001F6B5\U0001F3FD\U0001F3FD': 1528,  # Person Mountain Biking: Medium Skin Tone
    u'\U0001F6B5\U0001F3FE\U0001F3FE': 1529,  # Person Mountain Biking: Medium-Dark Skin Tone
    u'\U0001F6B5\U0001F3FF\U0001F3FF': 1530,  # Person Mountain Biking: Dark Skin Tone
    u'\U0001F6B5\U0000200D\U00002642': 1531,  # Man Mountain Biking
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002642': 1532,  # Man Mountain Biking: Light Skin Tone
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002642': 1533,  # Man Mountain Biking: Medium-Light Skin Tone
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002642': 1534,  # Man Mountain Biking: Medium Skin Tone
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002642': 1535,  # Man Mountain Biking: Medium-Dark Skin Tone
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002642': 1536,  # Man Mountain Biking: Dark Skin Tone
    u'\U0001F6B5\U0000200D\U00002640': 1537,  # Woman Mountain Biking
    u'\U0001F6B5\U0001F3FB\U0000200D\U00002640': 1538,  # Woman Mountain Biking: Light Skin Tone
    u'\U0001F6B5\U0001F3FC\U0000200D\U00002640': 1539,  # Woman Mountain Biking: Medium-Light Skin Tone
    u'\U0001F6B5\U0001F3FD\U0000200D\U00002640': 1540,  # Woman Mountain Biking: Medium Skin Tone
    u'\U0001F6B5\U0001F3FE\U0000200D\U00002640': 1541,  # Woman Mountain Biking: Medium-Dark Skin Tone
    u'\U0001F6B5\U0001F3FF\U0000200D\U00002640': 1542,  # Woman Mountain Biking: Dark Skin Tone
    u'\U0001F938': 1543,  # Person Cartwheeling
    u'\U0001F938\U0001F3FB\U0001F3FB': 1544,  # Person Cartwheeling: Light Skin Tone
    u'\U0001F938\U0001F3FC\U0001F3FC': 1545,  # Person Cartwheeling: Medium-Light Skin Tone
    u'\U0001F938\U0001F3FD\U0001F3FD': 1546,  # Person Cartwheeling: Medium Skin Tone
    u'\U0001F938\U0001F3FE\U0001F3FE': 1547,  # Person Cartwheeling: Medium-Dark Skin Tone
    u'\U0001F938\U0001F3FF\U0001F3FF': 1548,  # Person Cartwheeling: Dark Skin Tone
    u'\U0001F938\U0000200D\U00002642': 1549,  # Man Cartwheeling
    u'\U0001F938\U0001F3FB\U0000200D\U00002642': 1550,  # Man Cartwheeling: Light Skin Tone
    u'\U0001F938\U0001F3FC\U0000200D\U00002642': 1551,  # Man Cartwheeling: Medium-Light Skin Tone
    u'\U0001F938\U0001F3FD\U0000200D\U00002642': 1552,  # Man Cartwheeling: Medium Skin Tone
    u'\U0001F938\U0001F3FE\U0000200D\U00002642': 1553,  # Man Cartwheeling: Medium-Dark Skin Tone
    u'\U0001F938\U0001F3FF\U0000200D\U00002642': 1554,  # Man Cartwheeling: Dark Skin Tone
    u'\U0001F938\U0000200D\U00002640': 1555,  # Woman Cartwheeling
    u'\U0001F938\U0001F3FB\U0000200D\U00002640': 1556,  # Woman Cartwheeling: Light Skin Tone
    u'\U0001F938\U0001F3FC\U0000200D\U00002640': 1557,  # Woman Cartwheeling: Medium-Light Skin Tone
    u'\U0001F938\U0001F3FD\U0000200D\U00002640': 1558,  # Woman Cartwheeling: Medium Skin Tone
    u'\U0001F938\U0001F3FE\U0000200D\U00002640': 1559,  # Woman Cartwheeling: Medium-Dark Skin Tone
    u'\U0001F938\U0001F3FF\U0000200D\U00002640': 1560,  # Woman Cartwheeling: Dark Skin Tone
    u'\U0001F93C': 1561,  # People Wrestling
    u'\U0001F93C\U0000200D\U00002642': 1562,  # Men Wrestling
    u'\U0001F93C\U0000200D\U00002640': 1563,  # Women Wrestling
    u'\U0001F93D': 1564,  # Person Playing Water Polo
    u'\U0001F93D\U0001F3FB\U0001F3FB': 1565,  # Person Playing Water Polo: Light Skin Tone
    u'\U0001F93D\U0001F3FC\U0001F3FC': 1566,  # Person Playing Water Polo: Medium-Light Skin Tone
    u'\U0001F46F\U0001F3FB\U0000200D\U00002642': 1567,  # Men With Bunny Ears Partying, Type-1-2
    u'\U0001F93D\U0001F3FD\U0001F3FD': 1568,  # Person Playing Water Polo: Medium Skin Tone
    u'\U0001F93D\U0001F3FE\U0001F3FE': 1569,  # Person Playing Water Polo: Medium-Dark Skin Tone
    u'\U0001F46F\U0001F3FC\U0000200D\U00002642': 1570,  # Men With Bunny Ears Partying, Type-3
    u'\U0001F93D\U0001F3FF\U0001F3FF': 1571,  # Person Playing Water Polo: Dark Skin Tone
    u'\U0001F93D\U0000200D\U00002642': 1572,  # Man Playing Water Polo
    u'\U0001F46F\U0001F3FD\U0000200D\U00002642': 1573,  # Men With Bunny Ears Partying, Type-4
    u'\U0001F93D\U0001F3FB\U0000200D\U00002642': 1574,  # Man Playing Water Polo: Light Skin Tone
    u'\U0001F93D\U0001F3FC\U0000200D\U00002642': 1575,  # Man Playing Water Polo: Medium-Light Skin Tone
    u'\U0001F93D\U0001F3FD\U0000200D\U00002642': 1576,  # Man Playing Water Polo: Medium Skin Tone
    u'\U0001F46F\U0001F3FE\U0000200D\U00002642': 1577,  # Men With Bunny Ears Partying, Type-5
    u'\U0001F93D\U0001F3FE\U0000200D\U00002642': 1578,  # Man Playing Water Polo: Medium-Dark Skin Tone
    u'\U0001F93D\U0001F3FF\U0000200D\U00002642': 1579,  # Man Playing Water Polo: Dark Skin Tone
    u'\U0001F46F\U0001F3FF\U0000200D\U00002642': 1580,  # Men With Bunny Ears Partying, Type-6
    u'\U0001F93D\U0000200D\U00002640': 1581,  # Woman Playing Water Polo
    u'\U0001F93D\U0001F3FB\U0000200D\U00002640': 1582,  # Woman Playing Water Polo: Light Skin Tone
    u'\U0001F93D\U0001F3FC\U0000200D\U00002640': 1583,  # Woman Playing Water Polo: Medium-Light Skin Tone
    u'\U0001F93D\U0001F3FD\U0000200D\U00002640': 1584,  # Woman Playing Water Polo: Medium Skin Tone
    u'\U0001F46F\U0001F3FB\U0000200D\U00002640': 1585,  # Women With Bunny Ears Partying, Type-1-2
    u'\U0001F93D\U0001F3FE\U0000200D\U00002640': 1586,  # Woman Playing Water Polo: Medium-Dark Skin Tone
    u'\U0001F46F\U0001F3FC\U0000200D\U00002640': 1587,  # Women With Bunny Ears Partying, Type-3
    u'\U0001F93D\U0001F3FF\U0000200D\U00002640': 1588,  # Woman Playing Water Polo: Dark Skin Tone
    u'\U0001F93E': 1589,  # Person Playing Handball
    u'\U0001F46F\U0001F3FD\U0000200D\U00002640': 1590,  # Women With Bunny Ears Partying, Type-4
    u'\U0001F93E\U0001F3FB\U0001F3FB': 1591,  # Person Playing Handball: Light Skin Tone
    u'\U0001F93E\U0001F3FC\U0001F3FC': 1592,  # Person Playing Handball: Medium-Light Skin Tone
    u'\U0001F46F\U0001F3FE\U0000200D\U00002640': 1593,  # Women With Bunny Ears Partying, Type-5
    u'\U0001F93E\U0001F3FD\U0001F3FD': 1594,  # Person Playing Handball: Medium Skin Tone
    u'\U0001F93E\U0001F3FE\U0001F3FE': 1595,  # Person Playing Handball: Medium-Dark Skin Tone
    u'\U0001F46F\U0001F3FF\U0000200D\U00002640': 1596,  # Women With Bunny Ears Partying, Type-6
    u'\U0001F93E\U0001F3FF\U0001F3FF': 1597,  # Person Playing Handball: Dark Skin Tone
    u'\U0001F93E\U0000200D\U00002642': 1598,  # Man Playing Handball
    u'\U0001F93E\U0001F3FB\U0000200D\U00002642': 1599,  # Man Playing Handball: Light Skin Tone
    u'\U0001F93E\U0001F3FC\U0000200D\U00002642': 1600,  # Man Playing Handball: Medium-Light Skin Tone
    u'\U0001F93E\U0001F3FD\U0000200D\U00002642': 1601,  # Man Playing Handball: Medium Skin Tone
    u'\U0001F93E\U0001F3FE\U0000200D\U00002642': 1602,  # Man Playing Handball: Medium-Dark Skin Tone
    u'\U0001F93E\U0001F3FF\U0000200D\U00002642': 1603,  # Man Playing Handball: Dark Skin Tone
    u'\U0001F93E\U0000200D\U00002640': 1604,  # Woman Playing Handball
    u'\U0001F93E\U0001F3FB\U0000200D\U00002640': 1605,  # Woman Playing Handball: Light Skin Tone
    u'\U0001F93E\U0001F3FC\U0000200D\U00002640': 1606,  # Woman Playing Handball: Medium-Light Skin Tone
    u'\U0001F93E\U0001F3FD\U0000200D\U00002640': 1607,  # Woman Playing Handball: Medium Skin Tone
    u'\U0001F93E\U0001F3FE\U0000200D\U00002640': 1608,  # Woman Playing Handball: Medium-Dark Skin Tone
    u'\U0001F93E\U0001F3FF\U0000200D\U00002640': 1609,  # Woman Playing Handball: Dark Skin Tone
    u'\U0001F939': 1610,  # Person Juggling
    u'\U0001F939\U0001F3FB\U0001F3FB': 1611,  # Person Juggling: Light Skin Tone
    u'\U0001F939\U0001F3FC\U0001F3FC': 1612,  # Person Juggling: Medium-Light Skin Tone
    u'\U0001F939\U0001F3FD\U0001F3FD': 1613,  # Person Juggling: Medium Skin Tone
    u'\U0001F939\U0001F3FE\U0001F3FE': 1614,  # Person Juggling: Medium-Dark Skin Tone
    u'\U0001F939\U0001F3FF\U0001F3FF': 1615,  # Person Juggling: Dark Skin Tone
    u'\U0001F939\U0000200D\U00002642': 1616,  # Man Juggling
    u'\U0001F939\U0001F3FB\U0000200D\U00002642': 1617,  # Man Juggling: Light Skin Tone
    u'\U0001F939\U0001F3FC\U0000200D\U00002642': 1618,  # Man Juggling: Medium-Light Skin Tone
    u'\U0001F939\U0001F3FD\U0000200D\U00002642': 1619,  # Man Juggling: Medium Skin Tone
    u'\U0001F939\U0001F3FE\U0000200D\U00002642': 1620,  # Man Juggling: Medium-Dark Skin Tone
    u'\U0001F939\U0001F3FF\U0000200D\U00002642': 1621,  # Man Juggling: Dark Skin Tone
    u'\U0001F939\U0000200D\U00002640': 1622,  # Woman Juggling
    u'\U0001F939\U0001F3FB\U0000200D\U00002640': 1623,  # Woman Juggling: Light Skin Tone
    u'\U0001F939\U0001F3FC\U0000200D\U00002640': 1624,  # Woman Juggling: Medium-Light Skin Tone
    u'\U0001F939\U0001F3FD\U0000200D\U00002640': 1625,  # Woman Juggling: Medium Skin Tone
    u'\U0001F939\U0001F3FE\U0000200D\U00002640': 1626,  # Woman Juggling: Medium-Dark Skin Tone
    u'\U0001F939\U0001F3FF\U0000200D\U00002640': 1627,  # Woman Juggling: Dark Skin Tone
    u'\U0001F9D8': 1628,  # Person in Lotus Position
    u'\U0001F9D8\U0001F3FB\U0001F3FB': 1629,  # Person in Lotus Position: Light Skin Tone
    u'\U0001F9D8\U0001F3FC\U0001F3FC': 1630,  # Person in Lotus Position: Medium-Light Skin Tone
    u'\U0001F9D8\U0001F3FD\U0001F3FD': 1631,  # Person in Lotus Position: Medium Skin Tone
    u'\U0001F9D8\U0001F3FE\U0001F3FE': 1632,  # Person in Lotus Position: Medium-Dark Skin Tone
    u'\U0001F9D8\U0001F3FF\U0001F3FF': 1633,  # Person in Lotus Position: Dark Skin Tone
    u'\U0001F9D8\U0000200D\U00002642': 1634,  # Man in Lotus Position
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002642': 1635,  # Man in Lotus Position: Light Skin Tone
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002642': 1636,  # Man in Lotus Position: Medium-Light Skin Tone
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002642': 1637,  # Man in Lotus Position: Medium Skin Tone
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002642': 1638,  # Man in Lotus Position: Medium-Dark Skin Tone
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002642': 1639,  # Man in Lotus Position: Dark Skin Tone
    u'\U0001F9D8\U0000200D\U00002640': 1640,  # Woman in Lotus Position
    u'\U0001F9D8\U0001F3FB\U0000200D\U00002640': 1641,  # Woman in Lotus Position: Light Skin Tone
    u'\U0001F9D8\U0001F3FC\U0000200D\U00002640': 1642,  # Woman in Lotus Position: Medium-Light Skin Tone
    u'\U0001F9D8\U0001F3FD\U0000200D\U00002640': 1643,  # Woman in Lotus Position: Medium Skin Tone
    u'\U0001F9D8\U0001F3FE\U0000200D\U00002640': 1644,  # Woman in Lotus Position: Medium-Dark Skin Tone
    u'\U0001F9D8\U0001F3FF\U0000200D\U00002640': 1645,  # Woman in Lotus Position: Dark Skin Tone
    u'\U0001F6C0': 1646,  # Person Taking Bath
    u'\U0001F6C0\U0001F3FB\U0001F3FB': 1647,  # Person Taking Bath: Light Skin Tone
    u'\U0001F6C0\U0001F3FC\U0001F3FC': 1648,  # Person Taking Bath: Medium-Light Skin Tone
    u'\U0001F6C0\U0001F3FD\U0001F3FD': 1649,  # Person Taking Bath: Medium Skin Tone
    u'\U0001F6C0\U0001F3FE\U0001F3FE': 1650,  # Person Taking Bath: Medium-Dark Skin Tone
    u'\U0001F6C0\U0001F3FF\U0001F3FF': 1651,  # Person Taking Bath: Dark Skin Tone
    u'\U0001F6CC': 1652,  # Person in Bed
    u'\U0001F6CC\U0001F3FB\U0001F3FB': 1653,  # Person in Bed: Light Skin Tone
    u'\U0001F6CC\U0001F3FC\U0001F3FC': 1654,  # Person in Bed: Medium-Light Skin Tone
    u'\U0001F6CC\U0001F3FD\U0001F3FD': 1655,  # Person in Bed: Medium Skin Tone
    u'\U0001F6CC\U0001F3FE\U0001F3FE': 1656,  # Person in Bed: Medium-Dark Skin Tone
    u'\U0001F6CC\U0001F3FF\U0001F3FF': 1657,  # Person in Bed: Dark Skin Tone
    u'\U0001F9D1\U0000200D\U0001F91D\U0000200D\U0001F9D1': 1658,  # People Holding Hands
    u'\U0001F9D1\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': 1659,  # People Holding Hands: Light Skin Tone
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': 1660,  # People Holding Hands: Medium-Light Skin Tone, Light Skin Tone
    u'\U0001F9D1\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': 1661,  # People Holding Hands: Medium-Light Skin Tone
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': 1662,  # People Holding Hands: Medium Skin Tone, Light Skin Tone
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': 1663,  # People Holding Hands: Medium Skin Tone, Medium-Light Skin Tone
    u'\U0001F9D1\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': 1664,  # People Holding Hands: Medium Skin Tone
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': 1665,  # People Holding Hands: Medium-Dark Skin Tone, Light Skin Tone
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': 1666,  # People Holding Hands: Medium-Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': 1667,  # People Holding Hands: Medium-Dark Skin Tone, Medium Skin Tone
    u'\U0001F9D1\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': 1668,  # People Holding Hands: Medium-Dark Skin Tone
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FB': 1669,  # People Holding Hands: Dark Skin Tone, Light Skin Tone
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FC': 1670,  # People Holding Hands: Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FD': 1671,  # People Holding Hands: Dark Skin Tone, Medium Skin Tone
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FE': 1672,  # People Holding Hands: Dark Skin Tone, Medium-Dark Skin Tone
    u'\U0001F9D1\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F9D1\U0001F3FF': 1673,  # People Holding Hands: Dark Skin Tone
    u'\U0001F46D': 1674,  # Women Holding Hands
    u'\U0001F46D\U0001F3FB\U0001F3FB': 1675,  # Women Holding Hands: Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': 1676,  # Women Holding Hands: Medium-Light Skin Tone, Light Skin Tone
    u'\U0001F46D\U0001F3FC\U0001F3FC': 1677,  # Women Holding Hands: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': 1678,  # Women Holding Hands: Medium Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': 1679,  # Women Holding Hands: Medium Skin Tone, Medium-Light Skin Tone
    u'\U0001F46D\U0001F3FD\U0001F3FD': 1680,  # Women Holding Hands: Medium Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': 1681,  # Women Holding Hands: Medium-Dark Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': 1682,  # Women Holding Hands: Medium-Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': 1683,  # Women Holding Hands: Medium-Dark Skin Tone, Medium Skin Tone
    u'\U0001F46D\U0001F3FE\U0001F3FE': 1684,  # Women Holding Hands: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FB': 1685,  # Women Holding Hands: Dark Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FC': 1686,  # Women Holding Hands: Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FD': 1687,  # Women Holding Hands: Dark Skin Tone, Medium Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F469\U0001F3FE': 1688,  # Women Holding Hands: Dark Skin Tone, Medium-Dark Skin Tone
    u'\U0001F46D\U0001F3FF\U0001F3FF': 1689,  # Women Holding Hands: Dark Skin Tone
    u'\U0001F46B': 1690,  # Woman and Man Holding Hands
    u'\U0001F46B\U0001F3FB\U0001F3FB': 1691,  # Woman and Man Holding Hands: Light Skin Tone
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1692,  # Woman and Man Holding Hands: Light Skin Tone, Medium-Light Skin Tone
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1693,  # Woman and Man Holding Hands: Light Skin Tone, Medium Skin Tone
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': 1694,  # Woman and Man Holding Hands: Light Skin Tone, Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': 1695,  # Woman and Man Holding Hands: Light Skin Tone, Dark Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1696,  # Woman and Man Holding Hands: Medium-Light Skin Tone, Light Skin Tone
    u'\U0001F46B\U0001F3FC\U0001F3FC': 1697,  # Woman and Man Holding Hands: Medium-Light Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1698,  # Woman and Man Holding Hands: Medium-Light Skin Tone, Medium Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': 1699,  # Woman and Man Holding Hands: Medium-Light Skin Tone, Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': 1700,  # Woman and Man Holding Hands: Medium-Light Skin Tone, Dark Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1701,  # Woman and Man Holding Hands: Medium Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1702,  # Woman and Man Holding Hands: Medium Skin Tone, Medium-Light Skin Tone
    u'\U0001F46B\U0001F3FD\U0001F3FD': 1703,  # Woman and Man Holding Hands: Medium Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': 1704,  # Woman and Man Holding Hands: Medium Skin Tone, Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': 1705,  # Woman and Man Holding Hands: Medium Skin Tone, Dark Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1706,  # Woman and Man Holding Hands: Medium-Dark Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1707,  # Woman and Man Holding Hands: Medium-Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1708,  # Woman and Man Holding Hands: Medium-Dark Skin Tone, Medium Skin Tone
    u'\U0001F46B\U0001F3FE\U0001F3FE': 1709,  # Woman and Man Holding Hands: Medium-Dark Skin Tone
    u'\U0001F469\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF': 1710,  # Woman and Man Holding Hands: Medium-Dark Skin Tone, Dark Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1711,  # Woman and Man Holding Hands: Dark Skin Tone, Light Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1712,  # Woman and Man Holding Hands: Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1713,  # Woman and Man Holding Hands: Dark Skin Tone, Medium Skin Tone
    u'\U0001F469\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': 1714,  # Woman and Man Holding Hands: Dark Skin Tone, Medium-Dark Skin Tone
    u'\U0001F46B\U0001F3FF\U0001F3FF': 1715,  # Woman and Man Holding Hands: Dark Skin Tone
    u'\U0001F46C': 1716,  # Men Holding Hands
    u'\U0001F46C\U0001F3FB\U0001F3FB': 1717,  # Men Holding Hands: Light Skin Tone
    u'\U0001F468\U0001F3FC\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1718,  # Men Holding Hands: Medium-Light Skin Tone, Light Skin Tone
    u'\U0001F46C\U0001F3FC\U0001F3FC': 1719,  # Men Holding Hands: Medium-Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1720,  # Men Holding Hands: Medium Skin Tone, Light Skin Tone
    u'\U0001F468\U0001F3FD\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1721,  # Men Holding Hands: Medium Skin Tone, Medium-Light Skin Tone
    u'\U0001F46C\U0001F3FD\U0001F3FD': 1722,  # Men Holding Hands: Medium Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1723,  # Men Holding Hands: Medium-Dark Skin Tone, Light Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1724,  # Men Holding Hands: Medium-Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F468\U0001F3FE\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1725,  # Men Holding Hands: Medium-Dark Skin Tone, Medium Skin Tone
    u'\U0001F46C\U0001F3FE\U0001F3FE': 1726,  # Men Holding Hands: Medium-Dark Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FB': 1727,  # Men Holding Hands: Dark Skin Tone, Light Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FC': 1728,  # Men Holding Hands: Dark Skin Tone, Medium-Light Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FD': 1729,  # Men Holding Hands: Dark Skin Tone, Medium Skin Tone
    u'\U0001F468\U0001F3FF\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FE': 1730,  # Men Holding Hands: Dark Skin Tone, Medium-Dark Skin Tone
    u'\U0001F46C\U0001F3FF\U0001F3FF': 1731,  # Men Holding Hands: Dark Skin Tone
    u'\U0001F48F': 1732,  # Kiss
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468': 1733,  # Kiss: Woman, Man
    u'\U0001F468\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F468': 1734,  # Kiss: Man, Man
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F48B\U0000200D\U0001F469': 1735,  # Kiss: Woman, Woman
    u'\U0001F491': 1736,  # Couple with Heart
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F468': 1737,  # Couple with Heart: Woman, Man
    u'\U0001F468\U0000200D\U00002764\U0000200D\U0001F468': 1738,  # Couple with Heart: Man, Man
    u'\U0001F469\U0000200D\U00002764\U0000200D\U0001F469': 1739,  # Couple with Heart: Woman, Woman
    u'\U0001F46A': 1740,  # Family
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F466': 1741,  # Family: Man, Woman, Boy
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467': 1742,  # Family: Man, Woman, Girl
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': 1743,  # Family: Man, Woman, Girl, Boy
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': 1744,  # Family: Man, Woman, Boy, Boy
    u'\U0001F468\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': 1745,  # Family: Man, Woman, Girl, Girl
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F466': 1746,  # Family: Man, Man, Boy
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467': 1747,  # Family: Man, Man, Girl
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467\U0000200D\U0001F466': 1748,  # Family: Man, Man, Girl, Boy
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F466\U0000200D\U0001F466': 1749,  # Family: Man, Man, Boy, Boy
    u'\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467\U0000200D\U0001F467': 1750,  # Family: Man, Man, Girl, Girl
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F466': 1751,  # Family: Woman, Woman, Boy
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467': 1752,  # Family: Woman, Woman, Girl
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': 1753,  # Family: Woman, Woman, Girl, Boy
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': 1754,  # Family: Woman, Woman, Boy, Boy
    u'\U0001F469\U0000200D\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': 1755,  # Family: Woman, Woman, Girl, Girl
    u'\U0001F468\U0000200D\U0001F466': 1756,  # Family: Man, Boy
    u'\U0001F468\U0000200D\U0001F466\U0000200D\U0001F466': 1757,  # Family: Man, Boy, Boy
    u'\U0001F468\U0000200D\U0001F467': 1758,  # Family: Man, Girl
    u'\U0001F468\U0000200D\U0001F467\U0000200D\U0001F466': 1759,  # Family: Man, Girl, Boy
    u'\U0001F468\U0000200D\U0001F467\U0000200D\U0001F467': 1760,  # Family: Man, Girl, Girl
    u'\U0001F469\U0000200D\U0001F466': 1761,  # Family: Woman, Boy
    u'\U0001F469\U0000200D\U0001F466\U0000200D\U0001F466': 1762,  # Family: Woman, Boy, Boy
    u'\U0001F469\U0000200D\U0001F467': 1763,  # Family: Woman, Girl
    u'\U0001F469\U0000200D\U0001F467\U0000200D\U0001F466': 1764,  # Family: Woman, Girl, Boy
    u'\U0001F469\U0000200D\U0001F467\U0000200D\U0001F467': 1765,  # Family: Woman, Girl, Girl
    u'\U0001F5E3': 1766,  # Speaking Head
    u'\U0001F464': 1767,  # Bust in Silhouette
    u'\U0001F465': 1768,  # Busts in Silhouette
    u'\U0001F463': 1769,  # Footprints
    # u'\U0001F3FB': 1770,  # Light Skin Tone
    # u'\U0001F3FC': 1771,  # Medium-Light Skin Tone
    # u'\U0001F3FD': 1772,  # Medium Skin Tone
    # u'\U0001F3FE': 1773,  # Medium-Dark Skin Tone
    # u'\U0001F3FF': 1774,  # Dark Skin Tone
    u'\U0001F435': 1775,  # Monkey Face
    u'\U0001F412': 1776,  # Monkey
    u'\U0001F98D': 1777,  # Gorilla
    u'\U0001F9A7': 1778,  # Orangutan
    u'\U0001F436': 1779,  # Dog Face
    u'\U0001F415': 1780,  # Dog
    u'\U0001F9AE': 1781,  # Guide Dog
    u'\U0001F415\U0000200D\U0001F9BA': 1782,  # Service Dog
    u'\U0001F429': 1783,  # Poodle
    u'\U0001F43A': 1784,  # Wolf
    u'\U0001F98A': 1785,  # Fox
    u'\U0001F99D': 1786,  # Raccoon
    u'\U0001F431': 1787,  # Cat Face
    u'\U0001F408': 1788,  # Cat
    u'\U0001F981': 1789,  # Lion
    u'\U0001F42F': 1790,  # Tiger Face
    u'\U0001F405': 1791,  # Tiger
    u'\U0001F406': 1792,  # Leopard
    u'\U0001F434': 1793,  # Horse Face
    u'\U0001F40E': 1794,  # Horse
    u'\U0001F984': 1795,  # Unicorn
    u'\U0001F993': 1796,  # Zebra
    u'\U0001F98C': 1797,  # Deer
    u'\U0001F42E': 1798,  # Cow Face
    u'\U0001F402': 1799,  # Ox
    u'\U0001F403': 1800,  # Water Buffalo
    u'\U0001F404': 1801,  # Cow
    u'\U0001F437': 1802,  # Pig Face
    u'\U0001F416': 1803,  # Pig
    u'\U0001F417': 1804,  # Boar
    u'\U0001F43D': 1805,  # Pig Nose
    u'\U0001F40F': 1806,  # Ram
    u'\U0001F411': 1807,  # Ewe
    u'\U0001F410': 1808,  # Goat
    u'\U0001F42A': 1809,  # Camel
    u'\U0001F42B': 1810,  # Two-Hump Camel
    u'\U0001F999': 1811,  # Llama
    u'\U0001F992': 1812,  # Giraffe
    u'\U0001F418': 1813,  # Elephant
    u'\U0001F98F': 1814,  # Rhinoceros
    u'\U0001F99B': 1815,  # Hippopotamus
    u'\U0001F42D': 1816,  # Mouse Face
    u'\U0001F401': 1817,  # Mouse
    u'\U0001F400': 1818,  # Rat
    u'\U0001F439': 1819,  # Hamster
    u'\U0001F430': 1820,  # Rabbit Face
    u'\U0001F407': 1821,  # Rabbit
    u'\U0001F43F': 1822,  # Chipmunk
    u'\U0001F994': 1823,  # Hedgehog
    u'\U0001F987': 1824,  # Bat
    u'\U0001F43B': 1825,  # Bear
    u'\U0001F428': 1826,  # Koala
    u'\U0001F43C': 1827,  # Panda
    u'\U0001F9A5': 1828,  # Sloth
    u'\U0001F9A6': 1829,  # Otter
    u'\U0001F9A8': 1830,  # Skunk
    u'\U0001F998': 1831,  # Kangaroo
    u'\U0001F9A1': 1832,  # Badger
    u'\U0001F43E': 1833,  # Paw Prints
    u'\U0001F983': 1834,  # Turkey
    u'\U0001F414': 1835,  # Chicken
    u'\U0001F413': 1836,  # Rooster
    u'\U0001F423': 1837,  # Hatching Chick
    u'\U0001F424': 1838,  # Baby Chick
    u'\U0001F425': 1839,  # Front-Facing Baby Chick
    u'\U0001F426': 1840,  # Bird
    u'\U0001F427': 1841,  # Penguin
    u'\U0001F54A': 1842,  # Dove
    u'\U0001F985': 1843,  # Eagle
    u'\U0001F986': 1844,  # Duck
    u'\U0001F9A2': 1845,  # Swan
    u'\U0001F989': 1846,  # Owl
    u'\U0001F9A9': 1847,  # Flamingo
    u'\U0001F99A': 1848,  # Peacock
    u'\U0001F99C': 1849,  # Parrot
    u'\U0001F438': 1850,  # Frog
    u'\U0001F40A': 1851,  # Crocodile
    u'\U0001F422': 1852,  # Turtle
    u'\U0001F98E': 1853,  # Lizard
    u'\U0001F40D': 1854,  # Snake
    u'\U0001F432': 1855,  # Dragon Face
    u'\U0001F409': 1856,  # Dragon
    u'\U0001F995': 1857,  # Sauropod
    u'\U0001F996': 1858,  # T-Rex
    u'\U0001F433': 1859,  # Spouting Whale
    u'\U0001F40B': 1860,  # Whale
    u'\U0001F42C': 1861,  # Dolphin
    u'\U0001F41F': 1862,  # Fish
    u'\U0001F420': 1863,  # Tropical Fish
    u'\U0001F421': 1864,  # Blowfish
    u'\U0001F988': 1865,  # Shark
    u'\U0001F419': 1866,  # Octopus
    u'\U0001F41A': 1867,  # Spiral Shell
    u'\U0001F40C': 1868,  # Snail
    u'\U0001F98B': 1869,  # Butterfly
    u'\U0001F41B': 1870,  # Bug
    u'\U0001F41C': 1871,  # Ant
    u'\U0001F41D': 1872,  # Honeybee
    u'\U0001F41E': 1873,  # Lady Beetle
    u'\U0001F997': 1874,  # Cricket
    u'\U0001F577': 1875,  # Spider
    u'\U0001F578': 1876,  # Spider Web
    u'\U0001F982': 1877,  # Scorpion
    u'\U0001F99F': 1878,  # Mosquito
    u'\U0001F9A0': 1879,  # Microbe
    u'\U0001F490': 1880,  # Bouquet
    u'\U0001F338': 1881,  # Cherry Blossom
    u'\U0001F4AE': 1882,  # White Flower
    u'\U0001F3F5': 1883,  # Rosette
    u'\U0001F339': 1884,  # Rose
    u'\U0001F940': 1885,  # Wilted Flower
    u'\U0001F33A': 1886,  # Hibiscus
    u'\U0001F33B': 1887,  # Sunflower
    u'\U0001F33C': 1888,  # Blossom
    u'\U0001F337': 1889,  # Tulip
    u'\U0001F331': 1890,  # Seedling
    u'\U0001F332': 1891,  # Evergreen Tree
    u'\U0001F333': 1892,  # Deciduous Tree
    u'\U0001F334': 1893,  # Palm Tree
    u'\U0001F335': 1894,  # Cactus
    u'\U0001F33E': 1895,  # Sheaf of Rice
    u'\U0001F33F': 1896,  # Herb
    u'\U00002618': 1897,  # Shamrock
    u'\U0001F340': 1898,  # Four Leaf Clover
    u'\U0001F341': 1899,  # Maple Leaf
    u'\U0001F342': 1900,  # Fallen Leaf
    u'\U0001F343': 1901,  # Leaf Fluttering in Wind
    u'\U0001F347': 1902,  # Grapes
    u'\U0001F348': 1903,  # Melon
    u'\U0001F349': 1904,  # Watermelon
    u'\U0001F34A': 1905,  # Tangerine
    u'\U0001F34B': 1906,  # Lemon
    u'\U0001F34C': 1907,  # Banana
    u'\U0001F34D': 1908,  # Pineapple
    u'\U0001F96D': 1909,  # Mango
    u'\U0001F34E': 1910,  # Red Apple
    u'\U0001F34F': 1911,  # Green Apple
    u'\U0001F350': 1912,  # Pear
    u'\U0001F351': 1913,  # Peach
    u'\U0001F352': 1914,  # Cherries
    u'\U0001F353': 1915,  # Strawberry
    u'\U0001F95D': 1916,  # Kiwi Fruit
    u'\U0001F345': 1917,  # Tomato
    u'\U0001F965': 1918,  # Coconut
    u'\U0001F951': 1919,  # Avocado
    u'\U0001F346': 1920,  # Eggplant
    u'\U0001F954': 1921,  # Potato
    u'\U0001F955': 1922,  # Carrot
    u'\U0001F33D': 1923,  # Ear of Corn
    u'\U0001F336': 1924,  # Hot Pepper
    u'\U0001F952': 1925,  # Cucumber
    u'\U0001F96C': 1926,  # Leafy Green
    u'\U0001F966': 1927,  # Broccoli
    u'\U0001F9C4': 1928,  # Garlic
    u'\U0001F9C5': 1929,  # Onion
    u'\U0001F344': 1930,  # Mushroom
    u'\U0001F95C': 1931,  # Peanuts
    u'\U0001F330': 1932,  # Chestnut
    u'\U0001F35E': 1933,  # Bread
    u'\U0001F950': 1934,  # Croissant
    u'\U0001F956': 1935,  # Baguette Bread
    u'\U0001F968': 1936,  # Pretzel
    u'\U0001F96F': 1937,  # Bagel
    u'\U0001F95E': 1938,  # Pancakes
    u'\U0001F9C7': 1939,  # Waffle
    u'\U0001F9C0': 1940,  # Cheese Wedge
    u'\U0001F356': 1941,  # Meat on Bone
    u'\U0001F357': 1942,  # Poultry Leg
    u'\U0001F969': 1943,  # Cut of Meat
    u'\U0001F953': 1944,  # Bacon
    u'\U0001F354': 1945,  # Hamburger
    u'\U0001F35F': 1946,  # French Fries
    u'\U0001F355': 1947,  # Pizza
    u'\U0001F32D': 1948,  # Hot Dog
    u'\U0001F96A': 1949,  # Sandwich
    u'\U0001F32E': 1950,  # Taco
    u'\U0001F32F': 1951,  # Burrito
    u'\U0001F959': 1952,  # Stuffed Flatbread
    u'\U0001F9C6': 1953,  # Falafel
    u'\U0001F95A': 1954,  # Egg
    u'\U0001F373': 1955,  # Cooking
    u'\U0001F958': 1956,  # Shallow Pan of Food
    u'\U0001F372': 1957,  # Pot of Food
    u'\U0001F963': 1958,  # Bowl with Spoon
    u'\U0001F957': 1959,  # Green Salad
    u'\U0001F37F': 1960,  # Popcorn
    u'\U0001F9C8': 1961,  # Butter
    u'\U0001F9C2': 1962,  # Salt
    u'\U0001F96B': 1963,  # Canned Food
    u'\U0001F371': 1964,  # Bento Box
    u'\U0001F358': 1965,  # Rice Cracker
    u'\U0001F359': 1966,  # Rice Ball
    u'\U0001F35A': 1967,  # Cooked Rice
    u'\U0001F35B': 1968,  # Curry Rice
    u'\U0001F35C': 1969,  # Steaming Bowl
    u'\U0001F35D': 1970,  # Spaghetti
    u'\U0001F360': 1971,  # Roasted Sweet Potato
    u'\U0001F362': 1972,  # Oden
    u'\U0001F363': 1973,  # Sushi
    u'\U0001F364': 1974,  # Fried Shrimp
    u'\U0001F365': 1975,  # Fish Cake with Swirl
    u'\U0001F96E': 1976,  # Moon Cake
    u'\U0001F361': 1977,  # Dango
    u'\U0001F95F': 1978,  # Dumpling
    u'\U0001F960': 1979,  # Fortune Cookie
    u'\U0001F961': 1980,  # Takeout Box
    u'\U0001F980': 1981,  # Crab
    u'\U0001F99E': 1982,  # Lobster
    u'\U0001F990': 1983,  # Shrimp
    u'\U0001F991': 1984,  # Squid
    u'\U0001F9AA': 1985,  # Oyster
    u'\U0001F366': 1986,  # Soft Ice Cream
    u'\U0001F367': 1987,  # Shaved Ice
    u'\U0001F368': 1988,  # Ice Cream
    u'\U0001F369': 1989,  # Doughnut
    u'\U0001F36A': 1990,  # Cookie
    u'\U0001F382': 1991,  # Birthday Cake
    u'\U0001F370': 1992,  # Shortcake
    u'\U0001F9C1': 1993,  # Cupcake
    u'\U0001F967': 1994,  # Pie
    u'\U0001F36B': 1995,  # Chocolate Bar
    u'\U0001F36C': 1996,  # Candy
    u'\U0001F36D': 1997,  # Lollipop
    u'\U0001F36E': 1998,  # Custard
    u'\U0001F36F': 1999,  # Honey Pot
    u'\U0001F37C': 2000,  # Baby Bottle
    u'\U0001F95B': 2001,  # Glass of Milk
    u'\U00002615': 2002,  # Hot Beverage
    u'\U0001F375': 2003,  # Teacup Without Handle
    u'\U0001F376': 2004,  # Sake
    u'\U0001F37E': 2005,  # Bottle with Popping Cork
    u'\U0001F377': 2006,  # Wine Glass
    u'\U0001F378': 2007,  # Cocktail Glass
    u'\U0001F379': 2008,  # Tropical Drink
    u'\U0001F37A': 2009,  # Beer Mug
    u'\U0001F37B': 2010,  # Clinking Beer Mugs
    u'\U0001F942': 2011,  # Clinking Glasses
    u'\U0001F943': 2012,  # Tumbler Glass
    u'\U0001F964': 2013,  # Cup with Straw
    u'\U0001F9C3': 2014,  # Beverage Box
    u'\U0001F9C9': 2015,  # Mate
    u'\U0001F9CA': 2016,  # Ice
    u'\U0001F962': 2017,  # Chopsticks
    u'\U0001F37D': 2018,  # Fork and Knife with Plate
    u'\U0001F374': 2019,  # Fork and Knife
    u'\U0001F944': 2020,  # Spoon
    u'\U0001F52A': 2021,  # Kitchen Knife
    u'\U0001F3FA': 2022,  # Amphora
    u'\U0001F30D': 2023,  # Globe Showing Europe-Africa
    u'\U0001F30E': 2024,  # Globe Showing Americas
    u'\U0001F30F': 2025,  # Globe Showing Asia-Australia
    u'\U0001F310': 2026,  # Globe with Meridians
    u'\U0001F5FA': 2027,  # World Map
    u'\U0001F5FE': 2028,  # Map of Japan
    u'\U0001F9ED': 2029,  # Compass
    u'\U0001F3D4': 2030,  # Snow-Capped Mountain
    u'\U000026F0': 2031,  # Mountain
    u'\U0001F30B': 2032,  # Volcano
    u'\U0001F5FB': 2033,  # Mount Fuji
    u'\U0001F3D5': 2034,  # Camping
    u'\U0001F3D6': 2035,  # Beach with Umbrella
    u'\U0001F3DC': 2036,  # Desert
    u'\U0001F3DD': 2037,  # Desert Island
    u'\U0001F3DE': 2038,  # National Park
    u'\U0001F3DF': 2039,  # Stadium
    u'\U0001F3DB': 2040,  # Classical Building
    u'\U0001F3D7': 2041,  # Building Construction
    u'\U0001F9F1': 2042,  # Brick
    u'\U0001F3D8': 2043,  # Houses
    u'\U0001F3DA': 2044,  # Derelict House
    u'\U0001F3E0': 2045,  # House
    u'\U0001F3E1': 2046,  # House with Garden
    u'\U0001F3E2': 2047,  # Office Building
    u'\U0001F3E3': 2048,  # Japanese Post Office
    u'\U0001F3E4': 2049,  # Post Office
    u'\U0001F3E5': 2050,  # Hospital
    u'\U0001F3E6': 2051,  # Bank
    u'\U0001F3E8': 2052,  # Hotel
    u'\U0001F3E9': 2053,  # Love Hotel
    u'\U0001F3EA': 2054,  # Convenience Store
    u'\U0001F3EB': 2055,  # School
    u'\U0001F3EC': 2056,  # Department Store
    u'\U0001F3ED': 2057,  # Factory
    u'\U0001F3EF': 2058,  # Japanese Castle
    u'\U0001F3F0': 2059,  # Castle
    u'\U0001F492': 2060,  # Wedding
    u'\U0001F5FC': 2061,  # Tokyo Tower
    u'\U0001F5FD': 2062,  # Statue of Liberty
    u'\U000026EA': 2063,  # Church
    u'\U0001F54C': 2064,  # Mosque
    u'\U0001F6D5': 2065,  # Hindu Temple
    u'\U0001F54D': 2066,  # Synagogue
    u'\U000026E9': 2067,  # Shinto Shrine
    u'\U0001F54B': 2068,  # Kaaba
    u'\U000026F2': 2069,  # Fountain
    u'\U000026FA': 2070,  # Tent
    u'\U0001F301': 2071,  # Foggy
    u'\U0001F303': 2072,  # Night with Stars
    u'\U0001F3D9': 2073,  # Cityscape
    u'\U0001F304': 2074,  # Sunrise Over Mountains
    u'\U0001F305': 2075,  # Sunrise
    u'\U0001F306': 2076,  # Cityscape at Dusk
    u'\U0001F307': 2077,  # Sunset
    u'\U0001F309': 2078,  # Bridge at Night
    u'\U00002668': 2079,  # Hot Springs
    u'\U0001F3A0': 2080,  # Carousel Horse
    u'\U0001F3A1': 2081,  # Ferris Wheel
    u'\U0001F3A2': 2082,  # Roller Coaster
    u'\U0001F488': 2083,  # Barber Pole
    u'\U0001F3AA': 2084,  # Circus Tent
    u'\U0001F682': 2085,  # Locomotive
    u'\U0001F683': 2086,  # Railway Car
    u'\U0001F684': 2087,  # High-Speed Train
    u'\U0001F685': 2088,  # Bullet Train
    u'\U0001F686': 2089,  # Train
    u'\U0001F687': 2090,  # Metro
    u'\U0001F688': 2091,  # Light Rail
    u'\U0001F689': 2092,  # Station
    u'\U0001F68A': 2093,  # Tram
    u'\U0001F69D': 2094,  # Monorail
    u'\U0001F69E': 2095,  # Mountain Railway
    u'\U0001F68B': 2096,  # Tram Car
    u'\U0001F68C': 2097,  # Bus
    u'\U0001F68D': 2098,  # Oncoming Bus
    u'\U0001F68E': 2099,  # Trolleybus
    u'\U0001F690': 2100,  # Minibus
    u'\U0001F691': 2101,  # Ambulance
    u'\U0001F692': 2102,  # Fire Engine
    u'\U0001F693': 2103,  # Police Car
    u'\U0001F694': 2104,  # Oncoming Police Car
    u'\U0001F695': 2105,  # Taxi
    u'\U0001F696': 2106,  # Oncoming Taxi
    u'\U0001F697': 2107,  # Automobile
    u'\U0001F698': 2108,  # Oncoming Automobile
    u'\U0001F699': 2109,  # Sport Utility Vehicle
    u'\U0001F69A': 2110,  # Delivery Truck
    u'\U0001F69B': 2111,  # Articulated Lorry
    u'\U0001F69C': 2112,  # Tractor
    u'\U0001F3CE': 2113,  # Racing Car
    u'\U0001F3CD': 2114,  # Motorcycle
    u'\U0001F6F5': 2115,  # Motor Scooter
    u'\U0001F9BD': 2116,  # Manual Wheelchair
    u'\U0001F9BC': 2117,  # Motorized Wheelchair
    u'\U0001F6FA': 2118,  # Auto Rickshaw
    u'\U0001F6B2': 2119,  # Bicycle
    u'\U0001F6F4': 2120,  # Kick Scooter
    u'\U0001F6F9': 2121,  # Skateboard
    u'\U0001F68F': 2122,  # Bus Stop
    u'\U0001F6E3': 2123,  # Motorway
    u'\U0001F6E4': 2124,  # Railway Track
    u'\U0001F6E2': 2125,  # Oil Drum
    u'\U000026FD': 2126,  # Fuel Pump
    u'\U0001F6A8': 2127,  # Police Car Light
    u'\U0001F6A5': 2128,  # Horizontal Traffic Light
    u'\U0001F6A6': 2129,  # Vertical Traffic Light
    u'\U0001F6D1': 2130,  # Stop Sign
    u'\U0001F6A7': 2131,  # Construction
    u'\U00002693': 2132,  # Anchor
    u'\U000026F5': 2133,  # Sailboat
    u'\U0001F6F6': 2134,  # Canoe
    u'\U0001F6A4': 2135,  # Speedboat
    u'\U0001F6F3': 2136,  # Passenger Ship
    u'\U000026F4': 2137,  # Ferry
    u'\U0001F6E5': 2138,  # Motor Boat
    u'\U0001F6A2': 2139,  # Ship
    u'\U00002708': 2140,  # Airplane
    u'\U0001F6E9': 2141,  # Small Airplane
    u'\U0001F6EB': 2142,  # Airplane Departure
    u'\U0001F6EC': 2143,  # Airplane Arrival
    u'\U0001FA82': 2144,  # Parachute
    u'\U0001F4BA': 2145,  # Seat
    u'\U0001F681': 2146,  # Helicopter
    u'\U0001F69F': 2147,  # Suspension Railway
    u'\U0001F6A0': 2148,  # Mountain Cableway
    u'\U0001F6A1': 2149,  # Aerial Tramway
    u'\U0001F6F0': 2150,  # Satellite
    u'\U0001F680': 2151,  # Rocket
    u'\U0001F6F8': 2152,  # Flying Saucer
    u'\U0001F6CE': 2153,  # Bellhop Bell
    u'\U0001F9F3': 2154,  # Luggage
    u'\U0000231B': 2155,  # Hourglass Done
    u'\U000023F3': 2156,  # Hourglass Not Done
    u'\U0000231A': 2157,  # Watch
    u'\U000023F0': 2158,  # Alarm Clock
    u'\U000023F1': 2159,  # Stopwatch
    u'\U000023F2': 2160,  # Timer Clock
    u'\U0001F570': 2161,  # Mantelpiece Clock
    u'\U0001F55B': 2162,  # Twelve O�Clock
    u'\U0001F567': 2163,  # Twelve-Thirty
    u'\U0001F550': 2164,  # One O�Clock
    u'\U0001F55C': 2165,  # One-Thirty
    u'\U0001F551': 2166,  # Two O�Clock
    u'\U0001F55D': 2167,  # Two-Thirty
    u'\U0001F552': 2168,  # Three O�Clock
    u'\U0001F55E': 2169,  # Three-Thirty
    u'\U0001F553': 2170,  # Four O�Clock
    u'\U0001F55F': 2171,  # Four-Thirty
    u'\U0001F554': 2172,  # Five O�Clock
    u'\U0001F560': 2173,  # Five-Thirty
    u'\U0001F555': 2174,  # Six O�Clock
    u'\U0001F561': 2175,  # Six-Thirty
    u'\U0001F556': 2176,  # Seven O�Clock
    u'\U0001F562': 2177,  # Seven-Thirty
    u'\U0001F557': 2178,  # Eight O�Clock
    u'\U0001F563': 2179,  # Eight-Thirty
    u'\U0001F558': 2180,  # Nine O�Clock
    u'\U0001F564': 2181,  # Nine-Thirty
    u'\U0001F559': 2182,  # Ten O�Clock
    u'\U0001F565': 2183,  # Ten-Thirty
    u'\U0001F55A': 2184,  # Eleven O�Clock
    u'\U0001F566': 2185,  # Eleven-Thirty
    u'\U0001F311': 2186,  # New Moon
    u'\U0001F312': 2187,  # Waxing Crescent Moon
    u'\U0001F313': 2188,  # First Quarter Moon
    u'\U0001F314': 2189,  # Waxing Gibbous Moon
    u'\U0001F315': 2190,  # Full Moon
    u'\U0001F316': 2191,  # Waning Gibbous Moon
    u'\U0001F317': 2192,  # Last Quarter Moon
    u'\U0001F318': 2193,  # Waning Crescent Moon
    u'\U0001F319': 2194,  # Crescent Moon
    u'\U0001F31A': 2195,  # New Moon Face
    u'\U0001F31B': 2196,  # First Quarter Moon Face
    u'\U0001F31C': 2197,  # Last Quarter Moon Face
    u'\U0001F321': 2198,  # Thermometer
    u'\U00002600': 2199,  # Sun
    u'\U0001F31D': 2200,  # Full Moon Face
    u'\U0001F31E': 2201,  # Sun with Face
    u'\U0001FA90': 2202,  # Ringed Planet
    u'\U00002B50': 2203,  # Star
    u'\U0001F31F': 2204,  # Glowing Star
    u'\U0001F320': 2205,  # Shooting Star
    u'\U0001F30C': 2206,  # Milky Way
    u'\U00002601': 2207,  # Cloud
    u'\U000026C5': 2208,  # Sun Behind Cloud
    u'\U000026C8': 2209,  # Cloud with Lightning and Rain
    u'\U0001F324': 2210,  # Sun Behind Small Cloud
    u'\U0001F325': 2211,  # Sun Behind Large Cloud
    u'\U0001F326': 2212,  # Sun Behind Rain Cloud
    u'\U0001F327': 2213,  # Cloud with Rain
    u'\U0001F328': 2214,  # Cloud with Snow
    u'\U0001F329': 2215,  # Cloud with Lightning
    u'\U0001F32A': 2216,  # Tornado
    u'\U0001F32B': 2217,  # Fog
    u'\U0001F32C': 2218,  # Wind Face
    u'\U0001F300': 2219,  # Cyclone
    u'\U0001F308': 2220,  # Rainbow
    u'\U0001F302': 2221,  # Closed Umbrella
    u'\U00002602': 2222,  # Umbrella
    u'\U00002614': 2223,  # Umbrella with Rain Drops
    u'\U000026F1': 2224,  # Umbrella on Ground
    u'\U000026A1': 2225,  # High Voltage
    u'\U00002744': 2226,  # Snowflake
    u'\U00002603': 2227,  # Snowman
    u'\U000026C4': 2228,  # Snowman Without Snow
    u'\U00002604': 2229,  # Comet
    u'\U0001F525': 2230,  # Fire
    u'\U0001F4A7': 2231,  # Droplet
    u'\U0001F30A': 2232,  # Water Wave
    u'\U0001F383': 2233,  # Jack-O-Lantern
    u'\U0001F384': 2234,  # Christmas Tree
    u'\U0001F386': 2235,  # Fireworks
    u'\U0001F387': 2236,  # Sparkler
    u'\U0001F9E8': 2237,  # Firecracker
    u'\U00002728': 2238,  # Sparkles
    u'\U0001F388': 2239,  # Balloon
    u'\U0001F389': 2240,  # Party Popper
    u'\U0001F38A': 2241,  # Confetti Ball
    u'\U0001F38B': 2242,  # Tanabata Tree
    u'\U0001F38D': 2243,  # Pine Decoration
    u'\U0001F38E': 2244,  # Japanese Dolls
    u'\U0001F38F': 2245,  # Carp Streamer
    u'\U0001F390': 2246,  # Wind Chime
    u'\U0001F391': 2247,  # Moon Viewing Ceremony
    u'\U0001F9E7': 2248,  # Red Envelope
    u'\U0001F380': 2249,  # Ribbon
    u'\U0001F381': 2250,  # Wrapped Gift
    u'\U0001F397': 2251,  # Reminder Ribbon
    u'\U0001F39F': 2252,  # Admission Tickets
    u'\U0001F3AB': 2253,  # Ticket
    u'\U0001F396': 2254,  # Military Medal
    u'\U0001F3C6': 2255,  # Trophy
    u'\U0001F3C5': 2256,  # Sports Medal
    u'\U0001F947': 2257,  # 1st Place Medal
    u'\U0001F948': 2258,  # 2nd Place Medal
    u'\U0001F949': 2259,  # 3rd Place Medal
    u'\U000026BD': 2260,  # Soccer Ball
    u'\U000026BE': 2261,  # Baseball
    u'\U0001F94E': 2262,  # Softball
    u'\U0001F3C0': 2263,  # Basketball
    u'\U0001F3D0': 2264,  # Volleyball
    u'\U0001F3C8': 2265,  # American Football
    u'\U0001F3C9': 2266,  # Rugby Football
    u'\U0001F3BE': 2267,  # Tennis
    u'\U0001F94F': 2268,  # Flying Disc
    u'\U0001F3B3': 2269,  # Bowling
    u'\U0001F3CF': 2270,  # Cricket Game
    u'\U0001F3D1': 2271,  # Field Hockey
    u'\U0001F3D2': 2272,  # Ice Hockey
    u'\U0001F94D': 2273,  # Lacrosse
    u'\U0001F3D3': 2274,  # Ping Pong
    u'\U0001F3F8': 2275,  # Badminton
    u'\U0001F94A': 2276,  # Boxing Glove
    u'\U0001F94B': 2277,  # Martial Arts Uniform
    u'\U0001F945': 2278,  # Goal Net
    u'\U000026F3': 2279,  # Flag in Hole
    u'\U000026F8': 2280,  # Ice Skate
    u'\U0001F3A3': 2281,  # Fishing Pole
    u'\U0001F93F': 2282,  # Diving Mask
    u'\U0001F3BD': 2283,  # Running Shirt
    u'\U0001F3BF': 2284,  # Skis
    u'\U0001F6F7': 2285,  # Sled
    u'\U0001F94C': 2286,  # Curling Stone
    u'\U0001F3AF': 2287,  # Direct Hit
    u'\U0001FA80': 2288,  # Yo-Yo
    u'\U0001FA81': 2289,  # Kite
    u'\U0001F3B1': 2290,  # Pool 8 Ball
    u'\U0001F52E': 2291,  # Crystal Ball
    u'\U0001F9FF': 2292,  # Nazar Amulet
    u'\U0001F3AE': 2293,  # Video Game
    u'\U0001F579': 2294,  # Joystick
    u'\U0001F3B0': 2295,  # Slot Machine
    u'\U0001F3B2': 2296,  # Game Die
    u'\U0001F9E9': 2297,  # Puzzle Piece
    u'\U0001F9F8': 2298,  # Teddy Bear
    u'\U00002660': 2299,  # Spade Suit
    u'\U00002665': 2300,  # Heart Suit
    u'\U00002666': 2301,  # Diamond Suit
    u'\U00002663': 2302,  # Club Suit
    u'\U0000265F': 2303,  # Chess Pawn
    u'\U0001F0CF': 2304,  # Joker
    u'\U0001F004': 2305,  # Mahjong Red Dragon
    u'\U0001F3B4': 2306,  # Flower Playing Cards
    u'\U0001F3AD': 2307,  # Performing Arts
    u'\U0001F5BC': 2308,  # Framed Picture
    u'\U0001F3A8': 2309,  # Artist Palette
    u'\U0001F9F5': 2310,  # Thread
    u'\U0001F9F6': 2311,  # Yarn
    u'\U0001F453': 2312,  # Glasses
    u'\U0001F576': 2313,  # Sunglasses
    u'\U0001F97D': 2314,  # Goggles
    u'\U0001F97C': 2315,  # Lab Coat
    u'\U0001F9BA': 2316,  # Safety Vest
    u'\U0001F454': 2317,  # Necktie
    u'\U0001F455': 2318,  # T-Shirt
    u'\U0001F456': 2319,  # Jeans
    u'\U0001F9E3': 2320,  # Scarf
    u'\U0001F9E4': 2321,  # Gloves
    u'\U0001F9E5': 2322,  # Coat
    u'\U0001F9E6': 2323,  # Socks
    u'\U0001F457': 2324,  # Dress
    u'\U0001F458': 2325,  # Kimono
    u'\U0001F97B': 2326,  # Sari
    u'\U0001FA71': 2327,  # One-Piece Swimsuit
    u'\U0001FA72': 2328,  # Briefs
    u'\U0001FA73': 2329,  # Shorts
    u'\U0001F459': 2330,  # Bikini
    u'\U0001F45A': 2331,  # Woman�s Clothes
    u'\U0001F45B': 2332,  # Purse
    u'\U0001F45C': 2333,  # Handbag
    u'\U0001F45D': 2334,  # Clutch Bag
    u'\U0001F6CD': 2335,  # Shopping Bags
    u'\U0001F392': 2336,  # Backpack
    u'\U0001F45E': 2337,  # Man�s Shoe
    u'\U0001F45F': 2338,  # Running Shoe
    u'\U0001F97E': 2339,  # Hiking Boot
    u'\U0001F97F': 2340,  # Flat Shoe
    u'\U0001F460': 2341,  # High-Heeled Shoe
    u'\U0001F461': 2342,  # Woman�s Sandal
    u'\U0001FA70': 2343,  # Ballet Shoes
    u'\U0001F462': 2344,  # Woman�s Boot
    u'\U0001F451': 2345,  # Crown
    u'\U0001F452': 2346,  # Woman�s Hat
    u'\U0001F3A9': 2347,  # Top Hat
    u'\U0001F393': 2348,  # Graduation Cap
    u'\U0001F9E2': 2349,  # Billed Cap
    u'\U000026D1': 2350,  # Rescue Worker�s Helmet
    u'\U0001F4FF': 2351,  # Prayer Beads
    u'\U0001F484': 2352,  # Lipstick
    u'\U0001F48D': 2353,  # Ring
    u'\U0001F48E': 2354,  # Gem Stone
    u'\U0001F507': 2355,  # Muted Speaker
    u'\U0001F508': 2356,  # Speaker Low Volume
    u'\U0001F509': 2357,  # Speaker Medium Volume
    u'\U0001F50A': 2358,  # Speaker High Volume
    u'\U0001F4E2': 2359,  # Loudspeaker
    u'\U0001F4E3': 2360,  # Megaphone
    u'\U0001F4EF': 2361,  # Postal Horn
    u'\U0001F514': 2362,  # Bell
    u'\U0001F515': 2363,  # Bell with Slash
    u'\U0001F3BC': 2364,  # Musical Score
    u'\U0001F3B5': 2365,  # Musical Note
    u'\U0001F3B6': 2366,  # Musical Notes
    u'\U0001F399': 2367,  # Studio Microphone
    u'\U0001F39A': 2368,  # Level Slider
    u'\U0001F39B': 2369,  # Control Knobs
    u'\U0001F3A4': 2370,  # Microphone
    u'\U0001F3A7': 2371,  # Headphone
    u'\U0001F4FB': 2372,  # Radio
    u'\U0001F3B7': 2373,  # Saxophone
    u'\U0001F3B8': 2374,  # Guitar
    u'\U0001F3B9': 2375,  # Musical Keyboard
    u'\U0001F3BA': 2376,  # Trumpet
    u'\U0001F3BB': 2377,  # Violin
    u'\U0001FA95': 2378,  # Banjo
    u'\U0001F941': 2379,  # Drum
    u'\U0001F4F1': 2380,  # Mobile Phone
    u'\U0001F4F2': 2381,  # Mobile Phone with Arrow
    u'\U0000260E': 2382,  # Telephone
    u'\U0001F4DE': 2383,  # Telephone Receiver
    u'\U0001F4DF': 2384,  # Pager
    u'\U0001F4E0': 2385,  # Fax Machine
    u'\U0001F50B': 2386,  # Battery
    u'\U0001F50C': 2387,  # Electric Plug
    u'\U0001F4BB': 2388,  # Laptop
    u'\U0001F5A5': 2389,  # Desktop Computer
    u'\U0001F5A8': 2390,  # Printer
    u'\U00002328': 2391,  # Keyboard
    u'\U0001F5B1': 2392,  # Computer Mouse
    u'\U0001F5B2': 2393,  # Trackball
    u'\U0001F4BD': 2394,  # Computer Disk
    u'\U0001F4BE': 2395,  # Floppy Disk
    u'\U0001F4BF': 2396,  # Optical Disk
    u'\U0001F4C0': 2397,  # DVD
    u'\U0001F9EE': 2398,  # Abacus
    u'\U0001F3A5': 2399,  # Movie Camera
    u'\U0001F39E': 2400,  # Film Frames
    u'\U0001F4FD': 2401,  # Film Projector
    u'\U0001F3AC': 2402,  # Clapper Board
    u'\U0001F4FA': 2403,  # Television
    u'\U0001F4F7': 2404,  # Camera
    u'\U0001F4F8': 2405,  # Camera with Flash
    u'\U0001F4F9': 2406,  # Video Camera
    u'\U0001F4FC': 2407,  # Videocassette
    u'\U0001F50D': 2408,  # Magnifying Glass Tilted Left
    u'\U0001F50E': 2409,  # Magnifying Glass Tilted Right
    u'\U0001F56F': 2410,  # Candle
    u'\U0001F4A1': 2411,  # Light Bulb
    u'\U0001F526': 2412,  # Flashlight
    u'\U0001F3EE': 2413,  # Red Paper Lantern
    u'\U0001FA94': 2414,  # Diya Lamp
    u'\U0001F4D4': 2415,  # Notebook with Decorative Cover
    u'\U0001F4D5': 2416,  # Closed Book
    u'\U0001F4D6': 2417,  # Open Book
    u'\U0001F4D7': 2418,  # Green Book
    u'\U0001F4D8': 2419,  # Blue Book
    u'\U0001F4D9': 2420,  # Orange Book
    u'\U0001F4DA': 2421,  # Books
    u'\U0001F4D3': 2422,  # Notebook
    u'\U0001F4D2': 2423,  # Ledger
    u'\U0001F4C3': 2424,  # Page with Curl
    u'\U0001F4DC': 2425,  # Scroll
    u'\U0001F4C4': 2426,  # Page Facing Up
    u'\U0001F4F0': 2427,  # Newspaper
    u'\U0001F5DE': 2428,  # Rolled-Up Newspaper
    u'\U0001F4D1': 2429,  # Bookmark Tabs
    u'\U0001F516': 2430,  # Bookmark
    u'\U0001F3F7': 2431,  # Label
    u'\U0001F4B0': 2432,  # Money Bag
    u'\U0001F4B4': 2433,  # Yen Banknote
    u'\U0001F4B5': 2434,  # Dollar Banknote
    u'\U0001F4B6': 2435,  # Euro Banknote
    u'\U0001F4B7': 2436,  # Pound Banknote
    u'\U0001F4B8': 2437,  # Money with Wings
    u'\U0001F4B3': 2438,  # Credit Card
    u'\U0001F9FE': 2439,  # Receipt
    u'\U0001F4B9': 2440,  # Chart Increasing with Yen
    u'\U00002709': 2441,  # Envelope
    u'\U0001F4E7': 2442,  # E-Mail
    u'\U0001F4E8': 2443,  # Incoming Envelope
    u'\U0001F4E9': 2444,  # Envelope with Arrow
    u'\U0001F4E4': 2445,  # Outbox Tray
    u'\U0001F4E5': 2446,  # Inbox Tray
    u'\U0001F4E6': 2447,  # Package
    u'\U0001F4EB': 2448,  # Closed Mailbox with Raised Flag
    u'\U0001F4EA': 2449,  # Closed Mailbox with Lowered Flag
    u'\U0001F4EC': 2450,  # Open Mailbox with Raised Flag
    u'\U0001F4ED': 2451,  # Open Mailbox with Lowered Flag
    u'\U0001F4EE': 2452,  # Postbox
    u'\U0001F5F3': 2453,  # Ballot Box with Ballot
    u'\U0000270F': 2454,  # Pencil
    u'\U00002712': 2455,  # Black Nib
    u'\U0001F58B': 2456,  # Fountain Pen
    u'\U0001F58A': 2457,  # Pen
    u'\U0001F58C': 2458,  # Paintbrush
    u'\U0001F58D': 2459,  # Crayon
    u'\U0001F4DD': 2460,  # Memo
    u'\U0001F4BC': 2461,  # Briefcase
    u'\U0001F4C1': 2462,  # File Folder
    u'\U0001F4C2': 2463,  # Open File Folder
    u'\U0001F5C2': 2464,  # Card Index Dividers
    u'\U0001F4C5': 2465,  # Calendar
    u'\U0001F4C6': 2466,  # Tear-Off Calendar
    u'\U0001F5D2': 2467,  # Spiral Notepad
    u'\U0001F5D3': 2468,  # Spiral Calendar
    u'\U0001F4C7': 2469,  # Card Index
    u'\U0001F4C8': 2470,  # Chart Increasing
    u'\U0001F4C9': 2471,  # Chart Decreasing
    u'\U0001F4CA': 2472,  # Bar Chart
    u'\U0001F4CB': 2473,  # Clipboard
    u'\U0001F4CC': 2474,  # Pushpin
    u'\U0001F4CD': 2475,  # Round Pushpin
    u'\U0001F4CE': 2476,  # Paperclip
    u'\U0001F587': 2477,  # Linked Paperclips
    u'\U0001F4CF': 2478,  # Straight Ruler
    u'\U0001F4D0': 2479,  # Triangular Ruler
    u'\U00002702': 2480,  # Scissors
    u'\U0001F5C3': 2481,  # Card File Box
    u'\U0001F5C4': 2482,  # File Cabinet
    u'\U0001F5D1': 2483,  # Wastebasket
    u'\U0001F512': 2484,  # Locked
    u'\U0001F513': 2485,  # Unlocked
    u'\U0001F50F': 2486,  # Locked with Pen
    u'\U0001F510': 2487,  # Locked with Key
    u'\U0001F511': 2488,  # Key
    u'\U0001F5DD': 2489,  # Old Key
    u'\U0001F528': 2490,  # Hammer
    u'\U0001FA93': 2491,  # Axe
    u'\U000026CF': 2492,  # Pick
    u'\U00002692': 2493,  # Hammer and Pick
    u'\U0001F6E0': 2494,  # Hammer and Wrench
    u'\U0001F5E1': 2495,  # Dagger
    u'\U00002694': 2496,  # Crossed Swords
    u'\U0001F52B': 2497,  # Pistol
    u'\U0001F3F9': 2498,  # Bow and Arrow
    u'\U0001F6E1': 2499,  # Shield
    u'\U0001F527': 2500,  # Wrench
    u'\U0001F529': 2501,  # Nut and Bolt
    u'\U00002699': 2502,  # Gear
    u'\U0001F5DC': 2503,  # Clamp
    u'\U00002696': 2504,  # Balance Scale
    u'\U0001F9AF': 2505,  # Probing Cane
    u'\U0001F517': 2506,  # Link
    u'\U000026D3': 2507,  # Chains
    u'\U0001F9F0': 2508,  # Toolbox
    u'\U0001F9F2': 2509,  # Magnet
    u'\U00002697': 2510,  # Alembic
    u'\U0001F9EA': 2511,  # Test Tube
    u'\U0001F9EB': 2512,  # Petri Dish
    u'\U0001F9EC': 2513,  # DNA
    u'\U0001F52C': 2514,  # Microscope
    u'\U0001F52D': 2515,  # Telescope
    u'\U0001F4E1': 2516,  # Satellite Antenna
    u'\U0001F489': 2517,  # Syringe
    u'\U0001FA78': 2518,  # Drop of Blood
    u'\U0001F48A': 2519,  # Pill
    u'\U0001FA79': 2520,  # Adhesive Bandage
    u'\U0001FA7A': 2521,  # Stethoscope
    u'\U0001F6AA': 2522,  # Door
    u'\U0001F6CF': 2523,  # Bed
    u'\U0001F6CB': 2524,  # Couch and Lamp
    u'\U0001FA91': 2525,  # Chair
    u'\U0001F6BD': 2526,  # Toilet
    u'\U0001F6BF': 2527,  # Shower
    u'\U0001F6C1': 2528,  # Bathtub
    u'\U0001FA92': 2529,  # Razor
    u'\U0001F9F4': 2530,  # Lotion Bottle
    u'\U0001F9F7': 2531,  # Safety Pin
    u'\U0001F9F9': 2532,  # Broom
    u'\U0001F9FA': 2533,  # Basket
    u'\U0001F9FB': 2534,  # Roll of Paper
    u'\U0001F9FC': 2535,  # Soap
    u'\U0001F9FD': 2536,  # Sponge
    u'\U0001F9EF': 2537,  # Fire Extinguisher
    u'\U0001F6D2': 2538,  # Shopping Cart
    u'\U0001F6AC': 2539,  # Cigarette
    u'\U000026B0': 2540,  # Coffin
    u'\U000026B1': 2541,  # Funeral Urn
    u'\U0001F5FF': 2542,  # Moai
    u'\U0001F3E7': 2543,  # ATM Sign
    u'\U0001F6AE': 2544,  # Litter in Bin Sign
    u'\U0001F6B0': 2545,  # Potable Water
    u'\U0000267F': 2546,  # Wheelchair Symbol
    u'\U0001F6B9': 2547,  # Men�s Room
    u'\U0001F6BA': 2548,  # Women�s Room
    u'\U0001F6BB': 2549,  # Restroom
    u'\U0001F6BC': 2550,  # Baby Symbol
    u'\U0001F6BE': 2551,  # Water Closet
    u'\U0001F6C2': 2552,  # Passport Control
    u'\U0001F6C3': 2553,  # Customs
    u'\U0001F6C4': 2554,  # Baggage Claim
    u'\U0001F6C5': 2555,  # Left Luggage
    u'\U000026A0': 2556,  # Warning
    u'\U0001F6B8': 2557,  # Children Crossing
    u'\U000026D4': 2558,  # No Entry
    u'\U0001F6AB': 2559,  # Prohibited
    u'\U0001F6B3': 2560,  # No Bicycles
    u'\U0001F6AD': 2561,  # No Smoking
    u'\U0001F6AF': 2562,  # No Littering
    u'\U0001F6B1': 2563,  # Non-Potable Water
    u'\U0001F6B7': 2564,  # No Pedestrians
    u'\U0001F4F5': 2565,  # No Mobile Phones
    u'\U0001F51E': 2566,  # No One Under Eighteen
    u'\U00002622': 2567,  # Radioactive
    u'\U00002623': 2568,  # Biohazard
    u'\U00002B06': 2569,  # Up Arrow
    u'\U00002197': 2570,  # Up-Right Arrow
    u'\U000027A1': 2571,  # Right Arrow
    u'\U00002198': 2572,  # Down-Right Arrow
    u'\U00002B07': 2573,  # Down Arrow
    u'\U00002199': 2574,  # Down-Left Arrow
    u'\U00002B05': 2575,  # Left Arrow
    u'\U00002196': 2576,  # Up-Left Arrow
    u'\U00002195': 2577,  # Up-Down Arrow
    u'\U00002194': 2578,  # Left-Right Arrow
    u'\U000021A9': 2579,  # Right Arrow Curving Left
    u'\U000021AA': 2580,  # Left Arrow Curving Right
    u'\U00002934': 2581,  # Right Arrow Curving Up
    u'\U00002935': 2582,  # Right Arrow Curving Down
    u'\U0001F503': 2583,  # Clockwise Vertical Arrows
    u'\U0001F504': 2584,  # Counterclockwise Arrows Button
    u'\U0001F519': 2585,  # Back Arrow
    u'\U0001F51A': 2586,  # End Arrow
    u'\U0001F51B': 2587,  # On! Arrow
    u'\U0001F51C': 2588,  # Soon Arrow
    u'\U0001F51D': 2589,  # Top Arrow
    u'\U0001F6D0': 2590,  # Place of Worship
    u'\U0000269B': 2591,  # Atom Symbol
    u'\U0001F549': 2592,  # Om
    u'\U00002721': 2593,  # Star of David
    u'\U00002638': 2594,  # Wheel of Dharma
    u'\U0000262F': 2595,  # Yin Yang
    u'\U0000271D': 2596,  # Latin Cross
    u'\U00002626': 2597,  # Orthodox Cross
    u'\U0000262A': 2598,  # Star and Crescent
    u'\U0000262E': 2599,  # Peace Symbol
    u'\U0001F54E': 2600,  # Menorah
    u'\U0001F52F': 2601,  # Dotted Six-Pointed Star
    u'\U00002648': 2602,  # Aries
    u'\U00002649': 2603,  # Taurus
    u'\U0000264A': 2604,  # Gemini
    u'\U0000264B': 2605,  # Cancer
    u'\U0000264C': 2606,  # Leo
    u'\U0000264D': 2607,  # Virgo
    u'\U0000264E': 2608,  # Libra
    u'\U0000264F': 2609,  # Scorpio
    u'\U00002650': 2610,  # Sagittarius
    u'\U00002651': 2611,  # Capricorn
    u'\U00002652': 2612,  # Aquarius
    u'\U00002653': 2613,  # Pisces
    u'\U000026CE': 2614,  # Ophiuchus
    u'\U0001F500': 2615,  # Shuffle Tracks Button
    u'\U0001F501': 2616,  # Repeat Button
    u'\U0001F502': 2617,  # Repeat Single Button
    u'\U000025B6': 2618,  # Play Button
    u'\U000023E9': 2619,  # Fast-Forward Button
    u'\U000023ED': 2620,  # Next Track Button
    u'\U000023EF': 2621,  # Play or Pause Button
    u'\U000025C0': 2622,  # Reverse Button
    u'\U000023EA': 2623,  # Fast Reverse Button
    u'\U000023EE': 2624,  # Last Track Button
    u'\U0001F53C': 2625,  # Upwards Button
    u'\U000023EB': 2626,  # Fast Up Button
    u'\U0001F53D': 2627,  # Downwards Button
    u'\U000023EC': 2628,  # Fast Down Button
    u'\U000023F8': 2629,  # Pause Button
    u'\U000023F9': 2630,  # Stop Button
    u'\U000023FA': 2631,  # Record Button
    u'\U000023CF': 2632,  # Eject Button
    u'\U0001F3A6': 2633,  # Cinema
    u'\U0001F505': 2634,  # Dim Button
    u'\U0001F506': 2635,  # Bright Button
    u'\U0001F4F6': 2636,  # Antenna Bars
    u'\U0001F4F3': 2637,  # Vibration Mode
    u'\U0001F4F4': 2638,  # Mobile Phone Off
    u'\U00002640': 2639,  # Female Sign
    u'\U00002642': 2640,  # Male Sign
    u'\U000026A7': 2641,  # Transgender Symbol
    u'\U00002716': 2642,  # Multiplication Sign
    u'\U00002795': 2643,  # Plus Sign
    u'\U00002796': 2644,  # Minus Sign
    u'\U00002797': 2645,  # Division Sign
    u'\U0000267E': 2646,  # Infinity
    u'\U0000203C': 2647,  # Double Exclamation Mark
    u'\U00002049': 2648,  # Exclamation Question Mark
    u'\U00002753': 2649,  # Question Mark
    u'\U00002754': 2650,  # White Question Mark
    u'\U00002755': 2651,  # White Exclamation Mark
    u'\U00002757': 2652,  # Exclamation Mark
    u'\U00003030': 2653,  # Wavy Dash
    u'\U0001F4B1': 2654,  # Currency Exchange
    u'\U0001F4B2': 2655,  # Heavy Dollar Sign
    u'\U00002695': 2656,  # Medical Symbol
    u'\U0000267B': 2657,  # Recycling Symbol
    u'\U0000269C': 2658,  # Fleur-de-lis
    u'\U0001F531': 2659,  # Trident Emblem
    u'\U0001F4DB': 2660,  # Name Badge
    u'\U0001F530': 2661,  # Japanese Symbol for Beginner
    u'\U00002B55': 2662,  # Hollow Red Circle
    u'\U00002705': 2663,  # Check Mark Button
    u'\U00002611': 2664,  # Check Box with Check
    u'\U00002714': 2665,  # Check Mark
    u'\U0000274C': 2666,  # Cross Mark
    u'\U0000274E': 2667,  # Cross Mark Button
    u'\U000027B0': 2668,  # Curly Loop
    u'\U000027BF': 2669,  # Double Curly Loop
    u'\U0000303D': 2670,  # Part Alternation Mark
    u'\U00002733': 2671,  # Eight-Spoked Asterisk
    u'\U00002734': 2672,  # Eight-Pointed Star
    u'\U00002747': 2673,  # Sparkle
    u'\U000000A9': 2674,  # Copyright
    u'\U000000AE': 2675,  # Registered
    u'\U00002122': 2676,  # Trade Mark
    u'\U00000023\U000020E3': 2677,  # Keycap Number Sign
    u'\U0000002A\U000020E3': 2678,  # Keycap Asterisk
    u'\U00000030\U000020E3': 2679,  # Keycap Digit Zero
    u'\U00000031\U000020E3': 2680,  # Keycap Digit One
    u'\U00000032\U000020E3': 2681,  # Keycap Digit Two
    u'\U00000033\U000020E3': 2682,  # Keycap Digit Three
    u'\U00000034\U000020E3': 2683,  # Keycap Digit Four
    u'\U00000035\U000020E3': 2684,  # Keycap Digit Five
    u'\U00000036\U000020E3': 2685,  # Keycap Digit Six
    u'\U00000037\U000020E3': 2686,  # Keycap Digit Seven
    u'\U00000038\U000020E3': 2687,  # Keycap Digit Eight
    u'\U00000039\U000020E3': 2688,  # Keycap Digit Nine
    u'\U0001F51F': 2689,  # Keycap: 10
    u'\U0001F520': 2690,  # Input Latin Uppercase
    u'\U0001F521': 2691,  # Input Latin Lowercase
    u'\U0001F522': 2692,  # Input Numbers
    u'\U0001F523': 2693,  # Input Symbols
    u'\U0001F524': 2694,  # Input Latin Letters
    u'\U0001F170': 2695,  # A Button (Blood Type)
    u'\U0001F18E': 2696,  # AB Button (Blood Type)
    u'\U0001F171': 2697,  # B Button (Blood Type)
    u'\U0001F191': 2698,  # CL Button
    u'\U0001F192': 2699,  # Cool Button
    u'\U0001F193': 2700,  # Free Button
    u'\U00002139': 2701,  # Information
    u'\U0001F194': 2702,  # ID Button
    u'\U000024C2': 2703,  # Circled M
    u'\U0001F195': 2704,  # New Button
    u'\U0001F196': 2705,  # NG Button
    u'\U0001F17E': 2706,  # O Button (Blood Type)
    u'\U0001F197': 2707,  # OK Button
    u'\U0001F17F': 2708,  # P Button
    u'\U0001F198': 2709,  # SOS Button
    u'\U0001F199': 2710,  # Up! Button
    u'\U0001F19A': 2711,  # Vs Button
    u'\U0001F201': 2712,  # Japanese �Here� Button
    u'\U0001F202': 2713,  # Japanese �Service Charge� Button
    u'\U0001F237': 2714,  # Japanese �Monthly Amount� Button
    u'\U0001F236': 2715,  # Japanese �Not Free of Charge� Button
    u'\U0001F22F': 2716,  # Japanese �Reserved� Button
    u'\U0001F250': 2717,  # Japanese �Bargain� Button
    u'\U0001F239': 2718,  # Japanese �Discount� Button
    u'\U0001F21A': 2719,  # Japanese �Free of Charge� Button
    u'\U0001F232': 2720,  # Japanese �Prohibited� Button
    u'\U0001F251': 2721,  # Japanese �Acceptable� Button
    u'\U0001F238': 2722,  # Japanese �Application� Button
    u'\U0001F234': 2723,  # Japanese �Passing Grade� Button
    u'\U0001F233': 2724,  # Japanese �Vacancy� Button
    u'\U00003297': 2725,  # Japanese �Congratulations� Button
    u'\U00003299': 2726,  # Japanese �Secret� Button
    u'\U0001F23A': 2727,  # Japanese �Open for Business� Button
    u'\U0001F235': 2728,  # Japanese �No Vacancy� Button
    u'\U0001F534': 2729,  # Red Circle
    u'\U0001F7E0': 2730,  # Orange Circle
    u'\U0001F7E1': 2731,  # Yellow Circle
    u'\U0001F7E2': 2732,  # Green Circle
    u'\U0001F535': 2733,  # Blue Circle
    u'\U0001F7E3': 2734,  # Purple Circle
    u'\U0001F7E4': 2735,  # Brown Circle
    u'\U000026AB': 2736,  # Black Circle
    u'\U000026AA': 2737,  # White Circle
    u'\U0001F7E5': 2738,  # Red Square
    u'\U0001F7E7': 2739,  # Orange Square
    u'\U0001F7E8': 2740,  # Yellow Square
    u'\U0001F7E9': 2741,  # Green Square
    u'\U0001F7E6': 2742,  # Blue Square
    u'\U0001F7EA': 2743,  # Purple Square
    u'\U0001F7EB': 2744,  # Brown Square
    u'\U00002B1B': 2745,  # Black Large Square
    u'\U00002B1C': 2746,  # White Large Square
    u'\U000025FC': 2747,  # Black Medium Square
    u'\U000025FB': 2748,  # White Medium Square
    u'\U000025FE': 2749,  # Black Medium-Small Square
    u'\U000025FD': 2750,  # White Medium-Small Square
    u'\U000025AA': 2751,  # Black Small Square
    u'\U000025AB': 2752,  # White Small Square
    u'\U0001F536': 2753,  # Large Orange Diamond
    u'\U0001F537': 2754,  # Large Blue Diamond
    u'\U0001F538': 2755,  # Small Orange Diamond
    u'\U0001F539': 2756,  # Small Blue Diamond
    u'\U0001F53A': 2757,  # Red Triangle Pointed Up
    u'\U0001F53B': 2758,  # Red Triangle Pointed Down
    u'\U0001F4A0': 2759,  # Diamond with a Dot
    u'\U0001F518': 2760,  # Radio Button
    u'\U0001F533': 2761,  # White Square Button
    u'\U0001F532': 2762,  # Black Square Button
    u'\U0001F3C1': 2763,  # Chequered Flag
    u'\U0001F6A9': 2764,  # Triangular Flag
    u'\U0001F38C': 2765,  # Crossed Flags
    u'\U0001F3F4': 2766,  # Black Flag
    u'\U0001F3F3': 2767,  # White Flag
    u'\U0001F3F3\U0000200D\U0001F308': 2768,  # Rainbow Flag
    u'\U0001F3F3\U0000200D\U000026A7': 2769,  # Transgender Flag
    u'\U0001F3F4\U0000200D\U00002620': 2770,  # Pirate Flag
    u'\U0001F1E6\U0001F1E8': 2771,  # Flag: Ascension Island
    u'\U0001F1E6\U0001F1E9': 2772,  # Flag: Andorra
    u'\U0001F1E6\U0001F1EA': 2773,  # Flag: United Arab Emirates
    u'\U0001F1E6\U0001F1EB': 2774,  # Flag: Afghanistan
    u'\U0001F1E6\U0001F1EC': 2775,  # Flag: Antigua & Barbuda
    u'\U0001F1E6\U0001F1EE': 2776,  # Flag: Anguilla
    u'\U0001F1E6\U0001F1F1': 2777,  # Flag: Albania
    u'\U0001F1E6\U0001F1F2': 2778,  # Flag: Armenia
    u'\U0001F1E6\U0001F1F4': 2779,  # Flag: Angola
    u'\U0001F1E6\U0001F1F6': 2780,  # Flag: Antarctica
    u'\U0001F1E6\U0001F1F7': 2781,  # Flag: Argentina
    u'\U0001F1E6\U0001F1F8': 2782,  # Flag: American Samoa
    u'\U0001F1E6\U0001F1F9': 2783,  # Flag: Austria
    u'\U0001F1E6\U0001F1FA': 2784,  # Flag: Australia
    u'\U0001F1E6\U0001F1FC': 2785,  # Flag: Aruba
    u'\U0001F1E6\U0001F1FD': 2786,  # Flag: �land Islands
    u'\U0001F1E6\U0001F1FF': 2787,  # Flag: Azerbaijan
    u'\U0001F1E7\U0001F1E6': 2788,  # Flag: Bosnia & Herzegovina
    u'\U0001F1E7\U0001F1E7': 2789,  # Flag: Barbados
    u'\U0001F1E7\U0001F1E9': 2790,  # Flag: Bangladesh
    u'\U0001F1E7\U0001F1EA': 2791,  # Flag: Belgium
    u'\U0001F1E7\U0001F1EB': 2792,  # Flag: Burkina Faso
    u'\U0001F1E7\U0001F1EC': 2793,  # Flag: Bulgaria
    u'\U0001F1E7\U0001F1ED': 2794,  # Flag: Bahrain
    u'\U0001F1E7\U0001F1EE': 2795,  # Flag: Burundi
    u'\U0001F1E7\U0001F1EF': 2796,  # Flag: Benin
    u'\U0001F1E7\U0001F1F1': 2797,  # Flag: St. Barth�lemy
    u'\U0001F1E7\U0001F1F2': 2798,  # Flag: Bermuda
    u'\U0001F1E7\U0001F1F3': 2799,  # Flag: Brunei
    u'\U0001F1E7\U0001F1F4': 2800,  # Flag: Bolivia
    u'\U0001F1E7\U0001F1F6': 2801,  # Flag: Caribbean Netherlands
    u'\U0001F1E7\U0001F1F7': 2802,  # Flag: Brazil
    u'\U0001F1E7\U0001F1F8': 2803,  # Flag: Bahamas
    u'\U0001F1E7\U0001F1F9': 2804,  # Flag: Bhutan
    u'\U0001F1E7\U0001F1FB': 2805,  # Flag: Bouvet Island
    u'\U0001F1E7\U0001F1FC': 2806,  # Flag: Botswana
    u'\U0001F1E7\U0001F1FE': 2807,  # Flag: Belarus
    u'\U0001F1E7\U0001F1FF': 2808,  # Flag: Belize
    u'\U0001F1E8\U0001F1E6': 2809,  # Flag: Canada
    u'\U0001F1E8\U0001F1E8': 2810,  # Flag: Cocos (Keeling) Islands
    u'\U0001F1E8\U0001F1E9': 2811,  # Flag: Congo - Kinshasa
    u'\U0001F1E8\U0001F1EB': 2812,  # Flag: Central African Republic
    u'\U0001F1E8\U0001F1EC': 2813,  # Flag: Congo - Brazzaville
    u'\U0001F1E8\U0001F1ED': 2814,  # Flag: Switzerland
    u'\U0001F1E8\U0001F1EE': 2815,  # Flag: C�te d�Ivoire
    u'\U0001F1E8\U0001F1F0': 2816,  # Flag: Cook Islands
    u'\U0001F1E8\U0001F1F1': 2817,  # Flag: Chile
    u'\U0001F1E8\U0001F1F2': 2818,  # Flag: Cameroon
    u'\U0001F1E8\U0001F1F3': 2819,  # Flag: China
    u'\U0001F1E8\U0001F1F4': 2820,  # Flag: Colombia
    u'\U0001F1E8\U0001F1F5': 2821,  # Flag: Clipperton Island
    u'\U0001F1E8\U0001F1F7': 2822,  # Flag: Costa Rica
    u'\U0001F1E8\U0001F1FA': 2823,  # Flag: Cuba
    u'\U0001F1E8\U0001F1FB': 2824,  # Flag: Cape Verde
    u'\U0001F1E8\U0001F1FC': 2825,  # Flag: Cura�ao
    u'\U0001F1E8\U0001F1FD': 2826,  # Flag: Christmas Island
    u'\U0001F1E8\U0001F1FE': 2827,  # Flag: Cyprus
    u'\U0001F1E8\U0001F1FF': 2828,  # Flag: Czechia
    u'\U0001F1E9\U0001F1EA': 2829,  # Flag: Germany
    u'\U0001F1E9\U0001F1EC': 2830,  # Flag: Diego Garcia
    u'\U0001F1E9\U0001F1EF': 2831,  # Flag: Djibouti
    u'\U0001F1E9\U0001F1F0': 2832,  # Flag: Denmark
    u'\U0001F1E9\U0001F1F2': 2833,  # Flag: Dominica
    u'\U0001F1E9\U0001F1F4': 2834,  # Flag: Dominican Republic
    u'\U0001F1E9\U0001F1FF': 2835,  # Flag: Algeria
    u'\U0001F1EA\U0001F1E6': 2836,  # Flag: Ceuta & Melilla
    u'\U0001F1EA\U0001F1E8': 2837,  # Flag: Ecuador
    u'\U0001F1EA\U0001F1EA': 2838,  # Flag: Estonia
    u'\U0001F1EA\U0001F1EC': 2839,  # Flag: Egypt
    u'\U0001F1EA\U0001F1ED': 2840,  # Flag: Western Sahara
    u'\U0001F1EA\U0001F1F7': 2841,  # Flag: Eritrea
    u'\U0001F1EA\U0001F1F8': 2842,  # Flag: Spain
    u'\U0001F1EA\U0001F1F9': 2843,  # Flag: Ethiopia
    u'\U0001F1EA\U0001F1FA': 2844,  # Flag: European Union
    u'\U0001F1EB\U0001F1EE': 2845,  # Flag: Finland
    u'\U0001F1EB\U0001F1EF': 2846,  # Flag: Fiji
    u'\U0001F1EB\U0001F1F0': 2847,  # Flag: Falkland Islands
    u'\U0001F1EB\U0001F1F2': 2848,  # Flag: Micronesia
    u'\U0001F1EB\U0001F1F4': 2849,  # Flag: Faroe Islands
    u'\U0001F1EB\U0001F1F7': 2850,  # Flag: France
    u'\U0001F1EC\U0001F1E6': 2851,  # Flag: Gabon
    u'\U0001F1EC\U0001F1E7': 2852,  # Flag: United Kingdom
    u'\U0001F1EC\U0001F1E9': 2853,  # Flag: Grenada
    u'\U0001F1EC\U0001F1EA': 2854,  # Flag: Georgia
    u'\U0001F1EC\U0001F1EB': 2855,  # Flag: French Guiana
    u'\U0001F1EC\U0001F1EC': 2856,  # Flag: Guernsey
    u'\U0001F1EC\U0001F1ED': 2857,  # Flag: Ghana
    u'\U0001F1EC\U0001F1EE': 2858,  # Flag: Gibraltar
    u'\U0001F1EC\U0001F1F1': 2859,  # Flag: Greenland
    u'\U0001F1EC\U0001F1F2': 2860,  # Flag: Gambia
    u'\U0001F1EC\U0001F1F3': 2861,  # Flag: Guinea
    u'\U0001F1EC\U0001F1F5': 2862,  # Flag: Guadeloupe
    u'\U0001F1EC\U0001F1F6': 2863,  # Flag: Equatorial Guinea
    u'\U0001F1EC\U0001F1F7': 2864,  # Flag: Greece
    u'\U0001F1EC\U0001F1F8': 2865,  # Flag: South Georgia & South Sandwich Islands
    u'\U0001F1EC\U0001F1F9': 2866,  # Flag: Guatemala
    u'\U0001F1EC\U0001F1FA': 2867,  # Flag: Guam
    u'\U0001F1EC\U0001F1FC': 2868,  # Flag: Guinea-Bissau
    u'\U0001F1EC\U0001F1FE': 2869,  # Flag: Guyana
    u'\U0001F1ED\U0001F1F0': 2870,  # Flag: Hong Kong SAR China
    u'\U0001F1ED\U0001F1F2': 2871,  # Flag: Heard & McDonald Islands
    u'\U0001F1ED\U0001F1F3': 2872,  # Flag: Honduras
    u'\U0001F1ED\U0001F1F7': 2873,  # Flag: Croatia
    u'\U0001F1ED\U0001F1F9': 2874,  # Flag: Haiti
    u'\U0001F1ED\U0001F1FA': 2875,  # Flag: Hungary
    u'\U0001F1EE\U0001F1E8': 2876,  # Flag: Canary Islands
    u'\U0001F1EE\U0001F1E9': 2877,  # Flag: Indonesia
    u'\U0001F1EE\U0001F1EA': 2878,  # Flag: Ireland
    u'\U0001F1EE\U0001F1F1': 2879,  # Flag: Israel
    u'\U0001F1EE\U0001F1F2': 2880,  # Flag: Isle of Man
    u'\U0001F1EE\U0001F1F3': 2881,  # Flag: India
    u'\U0001F1EE\U0001F1F4': 2882,  # Flag: British Indian Ocean Territory
    u'\U0001F1EE\U0001F1F6': 2883,  # Flag: Iraq
    u'\U0001F1EE\U0001F1F7': 2884,  # Flag: Iran
    u'\U0001F1EE\U0001F1F8': 2885,  # Flag: Iceland
    u'\U0001F1EE\U0001F1F9': 2886,  # Flag: Italy
    u'\U0001F1EF\U0001F1EA': 2887,  # Flag: Jersey
    u'\U0001F1EF\U0001F1F2': 2888,  # Flag: Jamaica
    u'\U0001F1EF\U0001F1F4': 2889,  # Flag: Jordan
    u'\U0001F1EF\U0001F1F5': 2890,  # Flag: Japan
    u'\U0001F1F0\U0001F1EA': 2891,  # Flag: Kenya
    u'\U0001F1F0\U0001F1EC': 2892,  # Flag: Kyrgyzstan
    u'\U0001F1F0\U0001F1ED': 2893,  # Flag: Cambodia
    u'\U0001F1F0\U0001F1EE': 2894,  # Flag: Kiribati
    u'\U0001F1F0\U0001F1F2': 2895,  # Flag: Comoros
    u'\U0001F1F0\U0001F1F3': 2896,  # Flag: St. Kitts & Nevis
    u'\U0001F1F0\U0001F1F5': 2897,  # Flag: North Korea
    u'\U0001F1F0\U0001F1F7': 2898,  # Flag: South Korea
    u'\U0001F1F0\U0001F1FC': 2899,  # Flag: Kuwait
    u'\U0001F1F0\U0001F1FE': 2900,  # Flag: Cayman Islands
    u'\U0001F1F0\U0001F1FF': 2901,  # Flag: Kazakhstan
    u'\U0001F1F1\U0001F1E6': 2902,  # Flag: Laos
    u'\U0001F1F1\U0001F1E7': 2903,  # Flag: Lebanon
    u'\U0001F1F1\U0001F1E8': 2904,  # Flag: St. Lucia
    u'\U0001F1F1\U0001F1EE': 2905,  # Flag: Liechtenstein
    u'\U0001F1F1\U0001F1F0': 2906,  # Flag: Sri Lanka
    u'\U0001F1F1\U0001F1F7': 2907,  # Flag: Liberia
    u'\U0001F1F1\U0001F1F8': 2908,  # Flag: Lesotho
    u'\U0001F1F1\U0001F1F9': 2909,  # Flag: Lithuania
    u'\U0001F1F1\U0001F1FA': 2910,  # Flag: Luxembourg
    u'\U0001F1F1\U0001F1FB': 2911,  # Flag: Latvia
    u'\U0001F1F1\U0001F1FE': 2912,  # Flag: Libya
    u'\U0001F1F2\U0001F1E6': 2913,  # Flag: Morocco
    u'\U0001F1F2\U0001F1E8': 2914,  # Flag: Monaco
    u'\U0001F1F2\U0001F1E9': 2915,  # Flag: Moldova
    u'\U0001F1F2\U0001F1EA': 2916,  # Flag: Montenegro
    u'\U0001F1F2\U0001F1EB': 2917,  # Flag: St. Martin
    u'\U0001F1F2\U0001F1EC': 2918,  # Flag: Madagascar
    u'\U0001F1F2\U0001F1ED': 2919,  # Flag: Marshall Islands
    u'\U0001F1F2\U0001F1F0': 2920,  # Flag: North Macedonia
    u'\U0001F1F2\U0001F1F1': 2921,  # Flag: Mali
    u'\U0001F1F2\U0001F1F2': 2922,  # Flag: Myanmar (Burma)
    u'\U0001F1F2\U0001F1F3': 2923,  # Flag: Mongolia
    u'\U0001F1F2\U0001F1F4': 2924,  # Flag: Macao Sar China
    u'\U0001F1F2\U0001F1F5': 2925,  # Flag: Northern Mariana Islands
    u'\U0001F1F2\U0001F1F6': 2926,  # Flag: Martinique
    u'\U0001F1F2\U0001F1F7': 2927,  # Flag: Mauritania
    u'\U0001F1F2\U0001F1F8': 2928,  # Flag: Montserrat
    u'\U0001F1F2\U0001F1F9': 2929,  # Flag: Malta
    u'\U0001F1F2\U0001F1FA': 2930,  # Flag: Mauritius
    u'\U0001F1F2\U0001F1FB': 2931,  # Flag: Maldives
    u'\U0001F1F2\U0001F1FC': 2932,  # Flag: Malawi
    u'\U0001F1F2\U0001F1FD': 2933,  # Flag: Mexico
    u'\U0001F1F2\U0001F1FE': 2934,  # Flag: Malaysia
    u'\U0001F1F2\U0001F1FF': 2935,  # Flag: Mozambique
    u'\U0001F1F3\U0001F1E6': 2936,  # Flag: Namibia
    u'\U0001F1F3\U0001F1E8': 2937,  # Flag: New Caledonia
    u'\U0001F1F3\U0001F1EA': 2938,  # Flag: Niger
    u'\U0001F1F3\U0001F1EB': 2939,  # Flag: Norfolk Island
    u'\U0001F1F3\U0001F1EC': 2940,  # Flag: Nigeria
    u'\U0001F1F3\U0001F1EE': 2941,  # Flag: Nicaragua
    u'\U0001F1F3\U0001F1F1': 2942,  # Flag: Netherlands
    u'\U0001F1F3\U0001F1F4': 2943,  # Flag: Norway
    u'\U0001F1F3\U0001F1F5': 2944,  # Flag: Nepal
    u'\U0001F1F3\U0001F1F7': 2945,  # Flag: Nauru
    u'\U0001F1F3\U0001F1FA': 2946,  # Flag: Niue
    u'\U0001F1F3\U0001F1FF': 2947,  # Flag: New Zealand
    u'\U0001F1F4\U0001F1F2': 2948,  # Flag: Oman
    u'\U0001F1F5\U0001F1E6': 2949,  # Flag: Panama
    u'\U0001F1F5\U0001F1EA': 2950,  # Flag: Peru
    u'\U0001F1F5\U0001F1EB': 2951,  # Flag: French Polynesia
    u'\U0001F1F5\U0001F1EC': 2952,  # Flag: Papua New Guinea
    u'\U0001F1F5\U0001F1ED': 2953,  # Flag: Philippines
    u'\U0001F1F5\U0001F1F0': 2954,  # Flag: Pakistan
    u'\U0001F1F5\U0001F1F1': 2955,  # Flag: Poland
    u'\U0001F1F5\U0001F1F2': 2956,  # Flag: St. Pierre & Miquelon
    u'\U0001F1F5\U0001F1F3': 2957,  # Flag: Pitcairn Islands
    u'\U0001F1F5\U0001F1F7': 2958,  # Flag: Puerto Rico
    u'\U0001F1F5\U0001F1F8': 2959,  # Flag: Palestinian Territories
    u'\U0001F1F5\U0001F1F9': 2960,  # Flag: Portugal
    u'\U0001F1F5\U0001F1FC': 2961,  # Flag: Palau
    u'\U0001F1F5\U0001F1FE': 2962,  # Flag: Paraguay
    u'\U0001F1F6\U0001F1E6': 2963,  # Flag: Qatar
    u'\U0001F1F7\U0001F1EA': 2964,  # Flag: R�union
    u'\U0001F1F7\U0001F1F4': 2965,  # Flag: Romania
    u'\U0001F1F7\U0001F1F8': 2966,  # Flag: Serbia
    u'\U0001F1F7\U0001F1FA': 2967,  # Flag: Russia
    u'\U0001F1F7\U0001F1FC': 2968,  # Flag: Rwanda
    u'\U0001F1F8\U0001F1E6': 2969,  # Flag: Saudi Arabia
    u'\U0001F1F8\U0001F1E7': 2970,  # Flag: Solomon Islands
    u'\U0001F1F8\U0001F1E8': 2971,  # Flag: Seychelles
    u'\U0001F1F8\U0001F1E9': 2972,  # Flag: Sudan
    u'\U0001F1F8\U0001F1EA': 2973,  # Flag: Sweden
    u'\U0001F1F8\U0001F1EC': 2974,  # Flag: Singapore
    u'\U0001F1F8\U0001F1ED': 2975,  # Flag: St. Helena
    u'\U0001F1F8\U0001F1EE': 2976,  # Flag: Slovenia
    u'\U0001F1F8\U0001F1EF': 2977,  # Flag: Svalbard & Jan Mayen
    u'\U0001F1F8\U0001F1F0': 2978,  # Flag: Slovakia
    u'\U0001F1F8\U0001F1F1': 2979,  # Flag: Sierra Leone
    u'\U0001F1F8\U0001F1F2': 2980,  # Flag: San Marino
    u'\U0001F1F8\U0001F1F3': 2981,  # Flag: Senegal
    u'\U0001F1F8\U0001F1F4': 2982,  # Flag: Somalia
    u'\U0001F1F8\U0001F1F7': 2983,  # Flag: Suriname
    u'\U0001F1F8\U0001F1F8': 2984,  # Flag: South Sudan
    u'\U0001F1F8\U0001F1F9': 2985,  # Flag: S�o Tom� & Pr�ncipe
    u'\U0001F1F8\U0001F1FB': 2986,  # Flag: El Salvador
    u'\U0001F1F8\U0001F1FD': 2987,  # Flag: Sint Maarten
    u'\U0001F1F8\U0001F1FE': 2988,  # Flag: Syria
    u'\U0001F1F8\U0001F1FF': 2989,  # Flag: Eswatini
    u'\U0001F1F9\U0001F1E6': 2990,  # Flag: Tristan Da Cunha
    u'\U0001F1F9\U0001F1E8': 2991,  # Flag: Turks & Caicos Islands
    u'\U0001F1F9\U0001F1E9': 2992,  # Flag: Chad
    u'\U0001F1F9\U0001F1EB': 2993,  # Flag: French Southern Territories
    u'\U0001F1F9\U0001F1EC': 2994,  # Flag: Togo
    u'\U0001F1F9\U0001F1ED': 2995,  # Flag: Thailand
    u'\U0001F1F9\U0001F1EF': 2996,  # Flag: Tajikistan
    u'\U0001F1F9\U0001F1F0': 2997,  # Flag: Tokelau
    u'\U0001F1F9\U0001F1F1': 2998,  # Flag: Timor-Leste
    u'\U0001F1F9\U0001F1F2': 2999,  # Flag: Turkmenistan
    u'\U0001F1F9\U0001F1F3': 3000,  # Flag: Tunisia
    u'\U0001F1F9\U0001F1F4': 3001,  # Flag: Tonga
    u'\U0001F1F9\U0001F1F7': 3002,  # Flag: Turkey
    u'\U0001F1F9\U0001F1F9': 3003,  # Flag: Trinidad & Tobago
    u'\U0001F1F9\U0001F1FB': 3004,  # Flag: Tuvalu
    u'\U0001F1F9\U0001F1FC': 3005,  # Flag: Taiwan
    u'\U0001F1F9\U0001F1FF': 3006,  # Flag: Tanzania
    u'\U0001F1FA\U0001F1E6': 3007,  # Flag: Ukraine
    u'\U0001F1FA\U0001F1EC': 3008,  # Flag: Uganda
    u'\U0001F1FA\U0001F1F2': 3009,  # Flag: U.S. Outlying Islands
    u'\U0001F1FA\U0001F1F3': 3010,  # Flag: United Nations
    u'\U0001F1FA\U0001F1F8': 3011,  # Flag: United States
    u'\U0001F1FA\U0001F1FE': 3012,  # Flag: Uruguay
    u'\U0001F1FA\U0001F1FF': 3013,  # Flag: Uzbekistan
    u'\U0001F1FB\U0001F1E6': 3014,  # Flag: Vatican City
    u'\U0001F1FB\U0001F1E8': 3015,  # Flag: St. Vincent & Grenadines
    u'\U0001F1FB\U0001F1EA': 3016,  # Flag: Venezuela
    u'\U0001F1FB\U0001F1EC': 3017,  # Flag: British Virgin Islands
    u'\U0001F1FB\U0001F1EE': 3018,  # Flag: U.S. Virgin Islands
    u'\U0001F1FB\U0001F1F3': 3019,  # Flag: Vietnam
    u'\U0001F1FB\U0001F1FA': 3020,  # Flag: Vanuatu
    u'\U0001F1FC\U0001F1EB': 3021,  # Flag: Wallis & Futuna
    u'\U0001F1FC\U0001F1F8': 3022,  # Flag: Samoa
    u'\U0001F1FD\U0001F1F0': 3023,  # Flag: Kosovo
    u'\U0001F1FE\U0001F1EA': 3024,  # Flag: Yemen
    u'\U0001F1FE\U0001F1F9': 3025,  # Flag: Mayotte
    u'\U0001F1FF\U0001F1E6': 3026,  # Flag: South Africa
    u'\U0001F1FF\U0001F1F2': 3027,  # Flag: Zambia
    u'\U0001F1FF\U0001F1FC': 3028,  # Flag: Zimbabwe
    u'\U0001F3F4\U0000E0067\U0000E0062\U0000E0065\U0000E006E\U0000E0067\U0000E007F': 3029,  # Flag: England
    u'\U0001F3F4\U0000E0067\U0000E0062\U0000E0073\U0000E0063\U0000E0074\U0000E007F': 3030,  # Flag: Scotland
    u'\U0001F3F4\U0000E0067\U0000E0062\U0000E0077\U0000E006C\U0000E0073\U0000E007F': 3031,  # Flag: Wales
    u'\U0001F3F4\U0000E0075\U0000E0073\U0000E0074\U0000E0078\U0000E007F': 3032,  # Flag for Texas (US-TX)
}

DEMOJI = {f'<Emoji_{v}>': k for k, v in EMOJI.items()}