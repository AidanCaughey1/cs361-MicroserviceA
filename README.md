# cs361-MicroserviceA
cs361-Microservice A

This microservice allows other programs to verify whether a given media URL is valid and retrieve basic metadata about the file (file name, type, and size).

**How to Programmatically REQUEST Data**
To request data from the microservice, send a POST request to the following endpoint: **http://localhost:5000/verify**
The request must include a JSON body with the following parameter: url
Example Request:
import requests

response = requests.post(
    "http://localhost:5000/verify",
    json={"url": "https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4"}
)

**How to Programmatically RECEIVE Data**
The microservice will respond with a JSON object. The response will vary depending on whether the link is valid or not.
Example Response (valid):
{
  "valid": true,
  "file_name": "example.mp4",
  "content_type": "video/mp4",
  "file_size": "1585939"
}

Example Response (invalid):
{
  "valid": false,
  "error": "URL not reachable",
  "error_code": 404
}

(UML.png)
