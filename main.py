from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    """
    获取YouTube视频字幕
    :param video_id: YouTube视频ID
    :return: 字幕文本
    """
    try:
        # 从视频ID中移除额外的参数（如果有）
        video_id = video_id.split('&')[0]
        
        # 获取字幕
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-CN', 'zh', 'en'])
        
        # 格式化字幕输出
        formatted_transcript = ""
        for entry in transcript_list:
            time = entry['start']
            minutes = int(time // 60)
            seconds = int(time % 60)
            text = entry['text']
            formatted_transcript += f"[{minutes:02d}:{seconds:02d}] {text}\n"
        
        return formatted_transcript
    except Exception as e:
        return f"获取字幕时出错: {str(e)}"

def main():
    # 获取用户输入的视频ID
    print("请输入YouTube视频ID或完整URL")
    print("例如: https://www.youtube.com/watch?v=VIDEO_ID 或直接输入 VIDEO_ID")
    user_input = input("> ")
    
    # 从URL中提取视频ID（如果输入的是URL）
    if "youtube.com" in user_input or "youtu.be" in user_input:
        if "v=" in user_input:
            video_id = user_input.split("v=")[1].split("&")[0]
        else:
            video_id = user_input.split("/")[-1].split("&")[0]
    else:
        video_id = user_input
    
    # 获取并打印字幕
    print("\n正在获取字幕...")
    transcript = get_transcript(video_id)
    print("\n获取到的字幕内容：")
    print("-" * 50)
    print(transcript)
    print("-" * 50)

if __name__ == "__main__":
    main() 