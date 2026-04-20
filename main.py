"""
Entry point for the Mood Machine. Choose between rule-based or ML model.
"""

from typing import List, Union, Tuple

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from mood_analyzer import MoodAnalyzer
from dataset import SAMPLE_POSTS, TRUE_LABELS
from activity_recommender import get_activities, format_response


def evaluate_rule_based(posts: List[str], labels: List[str]) -> float:
    """
    Evaluate the rule based MoodAnalyzer on a labeled dataset using 5-mood classification.

    Prints each text with its predicted label and the true label,
    then returns the overall accuracy as a float between 0 and 1.
    """
    analyzer = MoodAnalyzer()
    correct = 0
    total = len(posts)

    print("=== Rule Based Evaluation on SAMPLE_POSTS (5-mood system) ===")
    for text, true_label in zip(posts, labels):
        predicted_label = analyzer.detect_specific_mood(text)
        is_correct = predicted_label == true_label
        if is_correct:
            correct += 1

        print(f'"{text}" -> predicted={predicted_label}, true={true_label}')

    if total == 0:
        print("\nNo labeled examples to evaluate.")
        return 0.0

    accuracy = correct / total
    print(f"\nRule based accuracy on SAMPLE_POSTS: {accuracy:.2f}")
    return accuracy


def run_batch_demo() -> None:
    """
    Run the MoodAnalyzer on the sample posts and print 5-mood predictions.

    This is a quick way to see how the mood detection behaves
    on the full dataset.
    """
    analyzer = MoodAnalyzer()
    print("\n=== Batch Demo on SAMPLE_POSTS (rule based, 5-mood) ===")
    for text in SAMPLE_POSTS:
        label = analyzer.detect_specific_mood(text)
        print(f'"{text}" -> {label}')


def train_ml_model(texts: List[str], labels: List[str]) -> Tuple[CountVectorizer, LogisticRegression]:
    """Train a simple ML classifier on the dataset."""
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression(max_iter=1000)
    model.fit(X, labels)
    return vectorizer, model


def evaluate_ml_model(posts: List[str], labels: List[str]) -> float:
    """Evaluate the ML model on a labeled dataset."""
    vectorizer, model = train_ml_model(posts, labels)
    correct = 0
    total = len(posts)

    print("=== ML Model Evaluation on SAMPLE_POSTS (5-mood system) ===")
    for text, true_label in zip(posts, labels):
        X = vectorizer.transform([text])
        predicted_label = model.predict(X)[0]
        is_correct = predicted_label == true_label
        if is_correct:
            correct += 1
        print(f'"{text}" -> predicted={predicted_label}, true={true_label}')

    accuracy = correct / total if total > 0 else 0.0
    print(f"\nML model accuracy on SAMPLE_POSTS: {accuracy:.2f}")
    return accuracy


def run_batch_demo_ml() -> None:
    """Run ML model on sample posts and print predictions."""
    vectorizer, model = train_ml_model(SAMPLE_POSTS, TRUE_LABELS)
    print("\n=== Batch Demo on SAMPLE_POSTS (ML model, 5-mood) ===")
    for text in SAMPLE_POSTS:
        X = vectorizer.transform([text])
        label = model.predict(X)[0]
        print(f'"{text}" -> {label}')


def run_interactive_loop(use_ml: bool = False) -> None:
    """
    Ask how the user is feeling, detect their specific mood, then suggest
    nearby activities using the Foursquare Places API.

    Args:
        use_ml: If True, use ML model. If False, use rule-based analyzer.

    Type 'quit' or press Enter on an empty line to exit.
    """
    if use_ml:
        vectorizer, model = train_ml_model(SAMPLE_POSTS, TRUE_LABELS)
        model_type = "ML"
    else:
        analyzer = MoodAnalyzer()
        model_type = "Rule-Based"

    print(f"\n=== Interactive Mood Machine ({model_type}) ===")
    print("Type 'quit' or press Enter on an empty line to exit.\n")

    while True:
        user_input = input("How are you feeling today? ").strip()
        if user_input == "" or user_input.lower() == "quit":
            print("Goodbye from the Mood Machine.")
            break

        # Get mood prediction based on chosen model
        if use_ml:
            X = vectorizer.transform([user_input])
            mood = model.predict(X)[0]
        else:
            mood = analyzer.detect_specific_mood(user_input)

        print(f"\nDetected mood: {mood}")

        location = input("What's your location? (e.g. Austin TX): ").strip()
        if not location:
            print("No location provided — skipping activity search.\n")
            continue

        print("\nSearching for activities...\n")
        activities = get_activities(mood, location)
        print(format_response(mood, activities))
        print()


def choose_analyzer() -> bool:
    """
    Let user choose between rule-based and ML model.
    Returns True for ML, False for rule-based.
    """
    print("\n" + "="*50)
    print("      MOOD MACHINE - CHOOSE YOUR ANALYZER")
    print("="*50)
    print("\n1. Rule-Based Analyzer (Hand-crafted rules)")
    print("2. ML Model (Machine Learning with scikit-learn)\n")

    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            return False
        elif choice == "2":
            return True
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    use_ml = choose_analyzer()

    if use_ml:
         print("\n>>> Running with ML Model <<<\n")
         evaluate_ml_model(SAMPLE_POSTS, TRUE_LABELS)
         run_batch_demo_ml()
    else:
         print("\n>>> Running with Rule-Based Analyzer <<<\n")
         evaluate_rule_based(SAMPLE_POSTS, TRUE_LABELS)
         run_batch_demo()

    run_interactive_loop(use_ml=use_ml)
