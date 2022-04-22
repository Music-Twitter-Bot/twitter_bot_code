import ffmpy
import tweepy
import time
from text_control import TextControl


class BotTweet:
    def __init__(self, API_key, API_secret, access_token, access_secret):
        """
        Initializes the authentication keys
        :param API_key: the account API key
        :param API_secret: the account API key secret
        :param access_token: the account access token
        :param access_secret: the account access token secret
        """
        self.API_key = API_key
        self.API_secret = API_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.text_control = TextControl(440, 44100, 20, "a")

    def generate_tweet(self):
        """
        Generates the tweet.
        :return: None.
        """
        api = self.connect_to_twitter()
        tweet, text = self.find_tweet(api)
        print("Found tweet.")

        wav_name = "sound2.wav"
        mp4_name = "video1.mp4"
        image_file = "pythonprofilepic.jpg"
        self.text_control.convert_text_to_wav(text, wav_name)
        print("Converted text to .wav.")

        # convert wav to mp4
        ff = ffmpy.FFmpeg(executable='ffmpeg/ffmpeg.exe', inputs={wav_name: None, image_file: None},
                          outputs={mp4_name: ["-filter:a", "atempo=1"]})
        ff.run()
        print("Converted .wav to .mp4.")

        self.upload_tweet(api, mp4_name, text)
        print("Tweet generated!")

    def connect_to_twitter(self):
        """
        Connects to the Twitter account based on the specified keys.
        :return: Authorization for the Twitter API.
        """
        auth = tweepy.OAuth1UserHandler(self.API_key, self.API_secret, self.access_token, self.access_secret)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            print("Authenticated.")
        except:
            print("Error during authentication.")
        return api

    def find_tweet(self, api):
        """
        Searches for a tweet.
        :param api:
        :return: The tweet information.
        :return: The text extracted from the retrieved tweet.
        """
        search_results = api.search_tweets(q="hello -filter:links -filter:retweets", lang="en", count=1)
        for i in search_results:
            tweet = i
            text = tweet.text
            print(f"{text}")
        return tweet, text

    def upload_tweet(self, api, video_name, text):
        """
        Uploads the tweet with media.
        :param api:
        :param video_name: The video file name
        :param text:
        :return: None.
        """
        #reformat the text so that it is a tweet from the music bot
        text = f"Beep boop. I am a 2140 music bot. I've converted the following tweet into music, mapping it to a major scale centering around 440 Hz:\n\n{text}"
        video = api.media_upload(video_name, chunked=True, media_category="tweet_video")
        time.sleep(5)
        api.update_status(status=text, media_ids=[video.media_id_string])