import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)

    return raw_tweets


def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """

    clean_list = []
    fixed = 0
    removed = 0

    for tweet in tweets:

        # Remove tweet if Text is missing
        if tweet["Text"].strip() == "":
            removed += 1
            continue

        # Replace empty Likes with 0
        if tweet["Likes"].strip() == "":
            tweet["Likes"] = "0"
            fixed += 1

        # Replace empty Retweets with 0
        if tweet["Retweets"].strip() == "":
            tweet["Retweets"] = "0"
            fixed += 1

        clean_list.append(tweet)

    print("Data Cleaning Report")
    print("--------------------")
    print("Rows Fixed:", fixed)
    print("Rows Removed:", removed)
    print()

    return clean_list


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """

    highest = tweets[0]

    for tweet in tweets:
        if int(tweet["Likes"]) > int(highest["Likes"]):
            highest = tweet

    print("Most Viral Tweet")
    print("----------------")
    print("Username:", highest["Username"])
    print("Likes:", highest["Likes"])
    print("Text:", highest["Text"])
    print()


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list
    by 'Likes' in descending order. NO .sort() allowed!
    """

    n = len(tweets)

    for i in range(n):

        for j in range(n - i - 1):

            if int(tweets[j]["Likes"]) < int(tweets[j + 1]["Likes"]):

                temp = tweets[j]
                tweets[j] = tweets[j + 1]
                tweets[j + 1] = temp

    return tweets


def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """

    results = []

    for tweet in tweets:

        if keyword.lower() in tweet["Text"].lower():
            results.append(tweet)

    print("Search Results")
    print("--------------")
    print("Found", len(results), "matching tweets.\n")

    for tweet in results:
        print("Username:", tweet["Username"])
        print("Likes:", tweet["Likes"])
        print("Text:", tweet["Text"])
        print()


if __name__ == "__main__":

    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")

    # Quest 1
    clean_dataset = clean_data(dataset)

    # Quest 2
    find_viral_tweet(clean_dataset)

    # Quest 3
    sorted_dataset = custom_sort_by_likes(clean_dataset)

    print("Top 10 Most Liked Tweets")
    print("------------------------")

    top = 10
    if len(sorted_dataset) < 10:
        top = len(sorted_dataset)

    for i in range(top):
        print(
            i + 1,
            sorted_dataset[i]["Username"],
            sorted_dataset[i]["Likes"],
            sorted_dataset[i]["Text"]
        )

    print()

    # Quest 4
    word = input("Enter a keyword to search: ")
    search_tweets(sorted_dataset, word)