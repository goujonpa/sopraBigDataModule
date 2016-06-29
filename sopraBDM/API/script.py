import json
import requests

r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 1,
                    "widget":  5,
                    "rating": 5
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 1,
                    "widget":  3,
                    "rating": 2
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 1,
                    "widget":  4,
                    "rating": 1
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 2,
                    "widget":  3,
                    "rating": 4
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 2,
                    "widget":  5,
                    "rating": 1
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 3,
                    "widget":  1,
                    "rating": 2
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 3,
                    "widget":  2,
                    "rating": 5
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 3,
                    "widget":  5,
                    "rating": 1
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 4,
                    "widget":  2,
                    "rating": 3
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 5,
                    "widget":  1,
                    "rating": 2
                }
            }
))
r = requests.post(
        "http://127.0.0.1:8000/api/idb/",
        data=json.dumps({
            "object": "notation",
            "attributes":
                {
                    "employee": 5,
                    "widget":  3,
                    "rating": 3
                }
            }
))

