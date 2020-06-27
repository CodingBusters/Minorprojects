from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("t.mp4")
clip2 = VideoFileClip("t1.mp4")
#clip3 = VideoFileClip("myvideo3.mp4")
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("my_concatenation.mp4")