"""
2. 想办法在程序里拿到页面源代码
3. 写正则. 提取到playinfo中的内容
4. 转化成字典. 提取下载url(video, audio)
5. 下载视频和音频
6. 合并起来.
"""
import requests   # 提前安装requests模块  pip install requests
import re
import json
import os


# 想办法在程序里拿到页面源代码
url = "https://www.bilibili.com/video/BV15u41167Ch?spm_id_from=333.999.0.0&vd_source=47c7ffb06df7e09e7d93c63150e1ae60"

headers = {
    # 对网站最基本的尊重
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
# print(resp.text)  # 页面源代码

# 写正则. 提取到playinfo中的内容
play_info_re = re.compile(r"window.__playinfo__=(?P<play_info>.*?)</script>")
play_info = play_info_re.search(resp.text).group("play_info")
# print(play_info)  # 有用的

dic = json.loads(play_info)
# print(dic)

video_url = dic['data']['dash']["video"][0]['baseUrl']
audio_url = dic['data']['dash']["audio"][0]['baseUrl']

# print(video_url)
# print(audio_url)

headers['Referer'] = url  # 对上referer

# 下载视频和音频
# 发请求. 保存成文件
v_resp = requests.get(video_url, headers=headers)
with open("video.m4s", mode="wb") as f:
    f.write(v_resp.content)

a_resp = requests.get(audio_url, headers=headers)
with open("audio.m4s", mode="wb") as f:
    f.write(a_resp.content)

# 合并起来
# 借助专业工具来合并视频. 剪映, PR. FFMPEG
# FFMPEG, 下载之后. 解压缩. 把bin目录添加到环境变量.
# mac的同学特别简单. 百度一下.

# 执行一条命令
os.system("ffmpeg -i audio.m4s -i video.m4s -acodec copy -vcodec copy good.mp4")
