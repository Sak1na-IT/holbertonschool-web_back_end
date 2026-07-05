#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def main():
    """Display Nginx log statistics."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method,
            collection.count_documents({"method": method})
        ))

    print("{} status check".format(
        collection.count_documents({
            "method": "GET",
            "path": "/status"
        })
    ))


if __name__ == "__main__":
    main()
