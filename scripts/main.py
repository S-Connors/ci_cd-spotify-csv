import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def post_response(url):
    # POST with cridentials
    response = requests.post(
        url,
        {
            "grant_type": "client_credentials",
            "client_id": os.getenv("client_id"),
            "client_secret": os.getenv("client_secret"),
        },
    )

    print(f"Post response: {response}")

    return response


def get_headers(response):
    # convert the response to JSON
    response_data = response.json()

    # save the access token
    access_token = response_data["access_token"]
    print("Access token saved")

    # save headers
    headers = {"Authorization": f"Bearer {access_token}"}

    return headers


def get_artist_albums(headers):
    # get Billy Eilish album info
    resp = requests.get(
        os.getenv("base_url") + "artists/" + os.getenv("artist_id") + "/albums",
        headers=headers,
    )

    print(os.getenv("base_url") + "artists/" + os.getenv("artist_id") + "/albums")
    print(f"Artist album response: {resp}")
    # print(f'Response Content: {resp.text}')

    # change to json
    artist_albums = resp.json()

    # check albums and relase date
    for album in artist_albums["items"]:
        print(album["release_date"], " : ", album["name"])

    return artist_albums


def get_album_tacks(headers, artist_albums):
    data = []

    for album in artist_albums["items"]:
        # get all track info for each album
        r = requests.get(
            os.getenv("base_url") + "albums/" + album["id"] + "/tracks", headers=headers
        )
        tracks = r.json()["items"]

        # get all audio features for every tack id
        for track in tracks:
            f = requests.get(
                os.getenv("base_url") + "audio-features/" + track["id"], headers=headers
            )
            f = f.json()

            # add the album info to the track info
            f.update(
                {
                    "track_name": track["name"],
                    "album_name": album["name"],
                    "release_date": album["release_date"],
                    "album_id": album["id"],
                }
            )

            data.append(f)

    # save as data frame
    df = pd.DataFrame(data)

    # save the dataframe to a csv file locally first
    df.to_csv(os.getenv("output_file_path"), index=False)
    print(f"Datafrme saved to local file {os.getenv('output_file_path')}")


# read secret_access_key of AWS form the .env file
# print("uploading to AWS S3...")
# load_dotenv()
# access_key = os.getenv("access_key")
# secret_access_key = os.getenv("secret_access_key")

# s3_client = boto3.client(
#    "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key
#    )
# s3_client.upload_file(source_path, bucket, destination)
# print("File uploading Done!")

if __name__ == "__main__":
    url = os.getenv("url")

    response = post_response(url)
    headers = get_headers(response)
    artist_albums = get_artist_albums(headers)
    get_album_tacks(headers, artist_albums)
