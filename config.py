import re
from os import getenv
import os

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(os.getenv("API_ID", "5282591")) 
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(os.getenv("LOGGER_ID", "1002435647179"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 1356469075))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/aa29b3dd2e10a746d9e2e-4d50fc10e45d842d80.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/9d62e65e6b6dfabf2d5ec-2663c09d9549c5a99e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/e93edf5fecc1fcf45649d-8a76d5d69048ede0fd.jpg"
STATS_IMG_URL = "https://graph.org/file/f037167ffd754757b9200-78a41f1418a569dce8.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/34a3df5b22ecd9523a9d4-8f8992fd7da4964282.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f45508f4814c65d434de5-5261b118fd7fe93479.jpg"
STREAM_IMG_URL = "https://graph.org/file/abb6d4d2c21112c8a6e3c-9a3b89cc6a258e4f69.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/d60c787ee00830a2159ab-2d4e9ce6fa014e1764.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/aec571747beb6e8dada7e-ae0394c012d07881e1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/8b2a5d789d0557a01e095-6d3a4bbff8e20e7cd4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/aa29b3dd2e10a746d9e2e-4d50fc10e45d842d80.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/aa29b3dd2e10a746d9e2e-4d50fc10e45d842d80.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
