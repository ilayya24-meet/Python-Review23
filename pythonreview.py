def create_youtube_video(title, description):
	video = {
	"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
	return video

def like(yt_video):
	if 'likes' in yt_video:
		yt_video['likes'] += 1
	return yt_video
def dislike(yt_video):
	if 'dislikes' in yt_video:
		yt_video['likes'] += 1
	return yt_video
def add_comment(yt_video, username, comment_text):
	yt_video['comments'][username] = comment_text
	return yt_video


video1 = create_youtube_video("Tal","I am terribly sleep deprived")
video1 = like(video1)
video1 = dislike(video1)
video1 = add_comment(video1, "Tal", "coffee")
print(video1)