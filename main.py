from youtube_stat import YTstats


API_KEY = 'AIzaSyBYcraWvyE6HXPS6bQ_j_jBmb9_Ua5axxk'
channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'

yt = YTstats(API_KEY, channel_id)
# yt.get_channel_statistics()
# yt.dump()
yt.get_channel_video_data()