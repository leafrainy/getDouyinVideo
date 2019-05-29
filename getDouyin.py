#coding:utf8
#下载抖音无水印视频小助手
#leafrainy
#leafrainy.cc

from bs4 import BeautifulSoup as bs
import requests
import sys


#get请求
def get(url,isMobile=0):

	if isMobile==0:#解析原始连接
		header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
		isRedirects = 1

	if isMobile==1:#获取最终视频连接
		header ={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'}
		isRedirects = 0

	res = requests.get(url,headers=header,allow_redirects=isRedirects)

	return res

#解析网页
def getContent(data):

	scriptStr = bs(data.content,'lxml').find_all("script")[-1].get_text()

	videoUrl = "https:"+scriptStr.split(",")[3].split(":")[2].replace('"','')
	
	coverUrl = scriptStr.split(",")[4].split('"')[1]#获取封面，有需要的自取

	return videoUrl

#获取最终视频连接
def getVideo(videoData):

	videoDownloadUrl = videoData.headers['Location']

	return videoDownloadUrl

#下载文件
def downloadFile(url,mp4Name):

	res = requests.get(url)

	with open(mp4Name, "wb") as code:
		code.write(res.content)
	print("下载完成")


if __name__ == '__main__':
	
	shareUrl=sys.argv[1]
	mp4Name=sys.argv[2]

	getContentData = get(shareUrl,0)

	videoUrl = getContent(getContentData)

	videoData = get(videoUrl,1)

	videoDownloadUrl = getVideo(videoData)

	downloadFile(videoDownloadUrl,mp4Name)

