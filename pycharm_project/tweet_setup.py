import ffmpy
import tweepy
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

        :return:
        """
        api = self.connect_to_twitter()
        tweet, text = self.find_tweet(api)
        print("Found tweet.")

        wav_name = "sound1.wav"
        mp4_name = "video.mp4"
        image_file = "image.jpg"
        self.text_control.convert_text_to_wav(text, wav_name)
        print("Converted text to .wav.")

        # convert wav to mp4
        ff = ffmpy.FFmpeg(executable='ffmpeg/ffmpeg.exe', inputs={wav_name: None},
                          outputs={mp4_name: ["-filter:a", "atempo=0.5"]})
        ff.run()
        print("Converted .wav to .mp4.")

        self.upload_tweet(api, mp4_name)
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
        :param api:
        :return: The tweet information.
        :return: The text extracted from the retrieved tweet.
        """
        tweet = api.search_tweets(q="-filter:links -filter:retweets", tweet_mode="extended", lang="en", count=1)
        text = str(tweet.text)
        print(f"{text}")
        return tweet, text

    def upload_tweet(self, api, video_name):
        """
        :param api:
        :param video_name: The video file name
        :return:
        """
        api.media_upload(video_name)
        # self.connect_to_twitter().update_status(media_ids, attachment_url=tweet_url)