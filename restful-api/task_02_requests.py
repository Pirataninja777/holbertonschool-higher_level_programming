#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.

    Sends a GET request to the JSONPlaceholder API to retrieve all posts.
    If the request is successful, prints the title of each post. If not,
    prints an error message.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    # If the request was successful, parse and print the titles
    if response.status_code == 200:
        posts = response.json()  # Parse JSON data
        for post in posts:
            print(post['title'])  # Print the title of each post
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.

    Sends a GET request to the JSONPlaceholder API to retrieve all posts.
    If the request is successful, saves the data (id, title, and body) of
    each post to a CSV file called 'posts.csv'. If not, prints an error
    message.

    Returns:
        None
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # If the request was successful, save the data to a CSV file
    if response.status_code == 200:
        posts = response.json()  # Parse JSON data

        # Prepare list of dictionaries with id, title, and body
        posts_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Write the data to a CSV file using csv.DictWriter
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Write the header
            writer.writerows(posts_data)  # Write all rows

        print("Posts have been saved to posts.csv")
    else:
        print("Failed to retrieve posts.")
