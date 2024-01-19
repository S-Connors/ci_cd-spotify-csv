## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clone the repository:
    git clone 

2. Install dependencies
    pip install requirements.txt

## Configuration

Before running the project you will need to set up the following enviroment variables in you .env file

Spotify

client_id = ** your spotify app client id **
 client_secret = ** your soptify client secret **
url = 'https://accounts.spotify.com/api/token'
base_url = 'https://api.spotify.com/v1/'
artist_id = ** artist id **
output_file_path = ** your file path **

Spotify has some great documentation on how to create an app to find your  client id, secret and artist ID
(https://developer.spotify.com/documentation/web-api/tutorials/getting-started)

AWS

You will have to attach a role with access to your s3 bucket, EC2 instance and IAM.

access_key = ** your aws access key **
secret_access_key = ** your aws secret key **
source_path = 
bucket = 
destination = 


## Usage

This project will connect to spotify and grab all of the specificed artists song information and album titles. It will then convert and save it to a csv file. 

## Acknowledgements

This was inspired by Steven Morse (https://stmorse.github.io/journal/spotify-api.html) and WeCloudData


https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli