"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - ANGRY_WORDS, STRESSED_WORDS, SAD_WORDS, BORED_WORDS, HAPPY_WORDS: mood-specific word lists
  - MOOD_CATEGORIES: dict mapping moods to word lists
  - SAMPLE_POSTS: 102 example posts for evaluation and training
  - TRUE_LABELS: 3-label human labels for activity recommendation:
      * "positive" - keep the good mood going (celebrations, fun, restaurants)
      * "negative_relax" - stressed/angry/frustrated needs calming (yoga, spas, parks)
      * "negative_cheerup" - sad/lonely/depressed needs uplifting (comedy, social, parties)
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
]

# ---------------------------------------------------------------------
# Mood-specific word lists (used by detect_specific_mood)
# ---------------------------------------------------------------------

ANGRY_WORDS = [
    "angry", "furious", "rage", "livid", "mad", "infuriated",
    "irritated", "outraged", "fuming", "seething", "annoyed", "pissed",
]

STRESSED_WORDS = [
    "stressed", "overwhelmed", "anxious", "deadline", "pressure",
    "exhausted", "burnout", "frantic", "worried", "nervous", "tense",
    "overloaded", "swamped",
]

SAD_WORDS = [
    "sad", "depressed", "unhappy", "miserable", "lonely", "heartbroken",
    "down", "hopeless", "gloomy", "grief", "crying", "devastated", "upset",
]

BORED_WORDS = [
    "bored", "boring", "dull", "uninterested", "restless",
    "listless", "monotonous", "tedious", "meh", "aimless",
]

HAPPY_WORDS = [
    "happy", "joyful", "excited", "thrilled", "ecstatic", "elated",
    "great", "wonderful", "amazing", "fantastic", "cheerful", "delighted",
    "content", "pumped", "stoked", "blessed", "grateful",
]

MOOD_CATEGORIES = {
    "angry":   ANGRY_WORDS,
    "stressed": STRESSED_WORDS,
    "sad":     SAD_WORDS,
    "bored":   BORED_WORDS,
    "happy":   HAPPY_WORDS,
}

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    # Original 27 posts
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "This is beautiful",
    "This place is so nice",
    "Feeling like the best version of myself",
    "Feeling down today",
    "I'm a bit anxious",
    "What a horrible day",
    "No negativity, just good vibes",
    "I don't know how I'm feeling today",
    "I think I'm feeling good",
    "I'm either really anxious or really excited 🫠",
    "This is exhilarating",
    "I feel nothing 🫩",
    "What a wonderfully trashy day",
    "I could say I'm feeling good but I'd be lying",
    "Is any day not a good day ",
    "It's aight",
    "I am really happy",
    "I am sad",
    "I am not good",
    "I am not in a bad mood",
    "I am really angry right now",
    # New 25 posts for better mood coverage
    # HAPPY posts (5)
    "Just got promoted and celebrating with my friends 🎉🥳",
    "Life is genuinely amazing right now, no cap fr fr",
    "Woke up feeling grateful for absolutely everything 😊✨",
    "Everything is falling into place and I'm thriving",
    "Can't stop smiling today, the universe is being nice to me 💛",
    # ANGRY posts (5)
    "Oh WONDERFUL, traffic made me 30 minutes late. Just FANTASTIC 😤",
    "I'm literally seething right now, cannot believe they did that",
    "So furious I could punch a wall. People are the worst 🤬",
    "How DARE they disrespect me like that. I'm LIVID",
    "Absolutely LOVE being betrayed by people I trusted 🙃🔥",
    # STRESSED posts (5)
    "Five assignments due tomorrow and I haven't started ANY 💀",
    "My brain is going a million miles per hour and won't stop",
    "Drowning in deadlines and responsibilities rn 😰",
    "Everything is due at once and I'm physically incapable help",
    "Running on 2 hours of sleep, 3 coffees, and pure panic 🤪",
    # SAD posts (5)
    "Yeah everything is cool, totally not breaking inside lol 🙂",
    "Loneliness is hitting different today",
    "Just realized I lost something I can never get back 💔",
    "Nobody gets me and I don't even know why I try anymore",
    "Feeling so empty and hollow, like something's missing",
    # BORED posts (5)
    "Been scrolling for 3 hours and still haven't found anything interesting",
    "Same boring routine, different day. Meh 😐",
    "Is this what life is? Just existing? Where's the excitement",
    "Everything feels so monotonous and pointless lately",
    "Just sitting here with nothing to do and nowhere to be 😴",
    # New 50 simple posts for expanded training
    # NEGATION POSTS (25) - testing negation handling
    "I'm not feeling sad",
    "I'm not feeling happy",
    "Not upset at all",
    "I don't feel mad, I feel furious",
    "I'm not in a good mood",
    "This is not boring",
    "Not excited about anything",
    "I don't feel stressed",
    "I'm not annoyed, I'm livid",
    "I don't feel relaxed",
    "I'm not happy right now",
    "Not sad at all today",
    "I don't have anything interesting to do",
    "I'm not calm",
    "This is not terrible",
    "I'm not just upset, I'm furious",
    "I'm not okay",
    "Not bad at all",
    "I don't feel at ease",
    "I'm not unhappy",
    "Nothing to do, not even one thing",
    "I don't feel down",
    "I'm not just irritated",
    "I'm not in the best place right now",
    "Not feeling negative today",
    # SIMPLE STRAIGHTFORWARD POSTS (25) - basic clear statements
    "I'm feeling great",
    "I feel sad",
    "I'm so angry",
    "I feel stressed",
    "I'm bored",
    "Life is good",
    "Everything is bad",
    "I'm mad",
    "Too much to handle",
    "Nothing interesting",
    "I'm excited",
    "I'm down",
    "I'm furious",
    "I'm overwhelmed",
    "This is dull",
    "I'm joyful",
    "I'm miserable",
    "I'm livid",
    "I'm anxious",
    "I'm restless",
    "Feeling blessed",
    "Feeling lonely",
    "Feeling rage",
    "Feeling pressure",
    "Feeling listless",
]

# Human labels for each post above.
# 3-label system optimized for activity recommendations:
#   - "positive" → keep the good mood going
#   - "negative_relax" → stressed/angry/frustrated needs calming
#   - "negative_cheerup" → sad/lonely/depressed needs uplifting
TRUE_LABELS = [
    # Original 27 posts
    "positive",       # "I love this class so much"
    "negative_cheerup",  # "Today was a terrible day"
    "positive",       # "Feeling tired but kind of hopeful"
    "positive",       # "This is fine"
    "positive",       # "So excited for the weekend"
    "negative_cheerup",  # "I am not happy about this"
    "positive",       # "This is beautiful"
    "positive",       # "This place is so nice"
    "positive",       # "Feeling like the best version of myself"
    "negative_cheerup",  # "Feeling down today"
    "negative_relax", # "I'm a bit anxious"
    "negative_cheerup",  # "What a horrible day"
    "positive",       # "No negativity, just good vibes"
    "positive",       # "I don't know how I'm feeling today"
    "positive",       # "I think I'm feeling good"
    "negative_relax", # "I'm either really anxious or really excited 🫠"
    "positive",       # "This is exhilarating"
    "negative_cheerup",  # "I feel nothing 🫩"
    "negative_relax", # "What a wonderfully trashy day"
    "negative_cheerup",  # "I could say I'm feeling good but I'd be lying"
    "positive",       # "Is any day not a good day"
    "positive",       # "It's aight"
    "positive",       # "I'm really happy"
    "negative_cheerup",  # "I am sad"
    "negative_cheerup",  # "I am not good"
    "positive",       # "I am not in a bad mood"
    "negative_relax", # "I am really angry right now"
    # New 25 complex posts
    "positive",       # "Just got promoted and celebrating with my friends 🎉🥳"
    "positive",       # "Life is genuinely amazing right now, no cap fr fr"
    "positive",       # "Woke up feeling grateful for absolutely everything 😊✨"
    "positive",       # "Everything is falling into place and I'm thriving"
    "positive",       # "Can't stop smiling today, the universe is being nice to me 💛"
    "negative_relax", # "Oh WONDERFUL, traffic made me 30 minutes late. Just FANTASTIC 😤"
    "negative_relax", # "I'm literally seething right now, cannot believe they did that"
    "negative_relax", # "So furious I could punch a wall. People are the worst 🤬"
    "negative_relax", # "How DARE they disrespect me like that. I'm LIVID"
    "negative_relax", # "Absolutely LOVE being betrayed by people I trusted 🙃🔥"
    "negative_relax", # "Five assignments due tomorrow and I haven't started ANY 💀"
    "negative_relax", # "My brain is going a million miles per hour and won't stop"
    "negative_relax", # "Drowning in deadlines and responsibilities rn 😰"
    "negative_relax", # "Everything is due at once and I'm physically incapable help"
    "negative_relax", # "Running on 2 hours of sleep, 3 coffees, and pure panic 🤪"
    "negative_cheerup",  # "Yeah everything is cool, totally not breaking inside lol 🙂"
    "negative_cheerup",  # "Loneliness is hitting different today"
    "negative_cheerup",  # "Just realized I lost something I can never get back 💔"
    "negative_cheerup",  # "Nobody gets me and I don't even know why I try anymore"
    "negative_cheerup",  # "Feeling so empty and hollow, like something's missing"
    "positive",       # "Been scrolling for 3 hours and still haven't found anything interesting"
    "positive",       # "Same boring routine, different day. Meh 😐"
    "positive",       # "Is this what life is? Just existing? Where's the excitement"
    "negative_cheerup",  # "Everything feels so monotonous and pointless lately"
    "positive",       # "Just sitting here with nothing to do and nowhere to be 😴"
    # New 50 simple posts - NEGATION (25)
    "positive",       # "I'm not feeling sad"
    "negative_cheerup",  # "I'm not feeling happy"
    "positive",       # "Not upset at all"
    "negative_relax", # "I don't feel mad, I feel furious"
    "negative_cheerup",  # "I'm not in a good mood"
    "positive",       # "This is not boring"
    "negative_cheerup",  # "Not excited about anything"
    "positive",       # "I don't feel stressed"
    "negative_relax", # "I'm not annoyed, I'm livid"
    "negative_relax", # "I don't feel relaxed"
    "negative_cheerup",  # "I'm not happy right now"
    "positive",       # "Not sad at all today"
    "positive",       # "I don't have anything interesting to do"
    "negative_relax", # "I'm not calm"
    "positive",       # "This is not terrible"
    "negative_relax", # "I'm not just upset, I'm furious"
    "negative_cheerup",  # "I'm not okay"
    "positive",       # "Not bad at all"
    "negative_relax", # "I don't feel at ease"
    "positive",       # "I'm not unhappy"
    "positive",       # "Nothing to do, not even one thing"
    "positive",       # "I don't feel down"
    "negative_relax", # "I'm not just irritated"
    "negative_cheerup",  # "I'm not in the best place right now"
    "positive",       # "Not feeling negative today"
    # New 50 simple posts - STRAIGHTFORWARD (25)
    "positive",       # "I'm feeling great"
    "negative_cheerup",  # "I feel sad"
    "negative_relax", # "I'm so angry"
    "negative_relax", # "I feel stressed"
    "positive",       # "I'm bored"
    "positive",       # "Life is good"
    "negative_cheerup",  # "Everything is bad"
    "negative_relax", # "I'm mad"
    "negative_relax", # "Too much to handle"
    "positive",       # "Nothing interesting"
    "positive",       # "I'm excited"
    "negative_cheerup",  # "I'm down"
    "negative_relax", # "I'm furious"
    "negative_relax", # "I'm overwhelmed"
    "positive",       # "This is dull"
    "positive",       # "I'm joyful"
    "negative_cheerup",  # "I'm miserable"
    "negative_relax", # "I'm livid"
    "negative_relax", # "I'm anxious"
    "positive",       # "I'm restless"
    "positive",       # "Feeling blessed"
    "negative_cheerup",  # "Feeling lonely"
    "negative_relax", # "Feeling rage"
    "negative_relax", # "Feeling pressure"
    "positive",       # "Feeling listless"
]

# Verify dataset integrity
assert len(SAMPLE_POSTS) == len(TRUE_LABELS), \
    f"Length mismatch: SAMPLE_POSTS={len(SAMPLE_POSTS)}, TRUE_LABELS={len(TRUE_LABELS)}"
