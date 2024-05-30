#!/usr/bin/python3
"""
Write a basic Python script to fetch posts
from JSONPlaceholder using requests.get().
"""

import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        post_data = []

        for post in posts:
            post_dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            post_data.append(post_dict)

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in post_data:
                writer.writerow(post)
