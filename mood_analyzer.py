# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

from typing import List, Dict, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS, MOOD_CATEGORIES


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.
        """
        cleaned  = text.strip().lower()
        tokens = cleaned.split()
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: List[str]) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        score = 0
        mixed = False

        positive_words_weight = {
                "happy": 0.1,
                "great": 0.2,
                "good":  0.1,
                "love":  0.3,
                "excited": 0.3,
                "awesome": 0.2,
                "fun": 0.2,
                "chill": 0.1,
                "relaxed": 0.1,
                "amazing": 0.3
        }
        negative_words_weight = {
              "sad": -0.1,
              "bad": -0.1,
              "terrible": -0.2,
              "awful": -0.2,
              "angry": -0.2,
              "upset": -0.1,
              "tired": -0.1,
              "stressed": -0.2,
              "hate": -0.1,
              "boring": -0.05
        }
        mixed_words = {
            "but",
            "however", 
            "although",
            "despite",  
            "regardless" 
        }
        booster_words = {
           "very": 1.1,
           "really": 1.1,
           "extremely": 1.3,
           "utterly": 1.3,
           "so" : 1.2
        }
        # implement a stack to evaluate negation
        def scorer(text):
           negation = 1
           boost = 1
           score = 0
           for i in text:
              if i == 'not':
                negation *= -1
              if i in booster_words:
                 boost *= booster_words[i]
              if i in self.positive_words:
                score += negation * boost * positive_words_weight[i]
                negation *= -1
                boost = 1
              if i in self.negative_words:
                score += negation * boost * negative_words_weight[i]
                negation *= -1
                boost = 1
                 
           return score


        # check if text has a mixed word in it
        def mixed_word_checker(text):
          for w in text:
            if w in mixed_words: 
              return True
          return False
        
        score = scorer(text)
             
        mixed = mixed_word_checker(text)# If there is a mixed word -> true, else -> false    
        return (score, mixed)

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        processed_text = self.preprocess(text)
        score = self.score_text(processed_text)[0]
        mixed = self.score_text(processed_text)[1]
        if -0.2 <= score <= 0.2 and mixed:
           return "mixed"
        elif score == 0 and not mixed:
           return "neutral"
        if score < 0:
           return "negative"
        if score > 0:
           return "positive"
      

    def detect_specific_mood(self, text: str) -> str:
        """
        Classify text into one of: angry, stressed, sad, bored, happy.

        Counts mood-keyword hits from MOOD_CATEGORIES with basic negation
        handling. Falls back to mapping predict_label() when no keywords match.
        """
        tokens = self.preprocess(text)
        scores = {mood: 0 for mood in MOOD_CATEGORIES}
        negation_words = {"not", "never", "don't", "dont", "no"}

        for i, token in enumerate(tokens):
            negated = i > 0 and tokens[i - 1] in negation_words
            if negated:
                continue
            for mood, word_list in MOOD_CATEGORIES.items():
                if token in word_list:
                    scores[mood] += 1

        best_mood = max(scores, key=scores.get)
        if scores[best_mood] == 0:
            fallback = {
                "positive": "happy",
                "negative": "sad",
                "neutral":  "bored",
                "mixed":    "stressed",
            }
            broad = self.predict_label(text)
            return fallback.get(broad, "happy")

        return best_mood

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        return "Explanation not yet implemented!"

