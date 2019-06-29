#coding:utf8
#下载抖音无水印视频小助手
#leafrainy
#leafrainy.cc

from bs4 import BeautifulSoup as bs
import requests
import time
import json
import sys

#核心api
api = "https://aweme.snssdk.com/aweme/v1/aweme/detail/?retry_type=no_retry&iid=74655440239&device_id=57318346369&ac=wifi&channel=wandoujia&aid=1128&app_name=aweme&version_code=140&version_name=1.4.0&device_platform=android&ssmix=a&device_type=MI+8&device_brand=xiaomi&os_api=22&os_version=5.1.1&uuid=865166029463703&openudid=ec6d541a2f7350cd&manifest_version_code=140&resolution=1080*1920&dpi=1080&update_version_code=1400&ts=1560245644&as=a125372f1c487cb50f&cp=728dcc5bc7f4f558e1&aweme_id="
awemeId = ""
url = ""

#请求&数据处理
def get(url,isGetId=0,awemeId=awemeId,api=api):

	if isGetId==1:#获取id
		
		header ={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'}
		
		res = requests.get(url,headers=header)

		awemeId=bs(res.content,'lxml').find_all("script")[-9].get_text().split(",")[3].split(":")[1].split('"')[1]

		return awemeId

	if isGetId==0:#获取数据
		
		header = {'accept-encoding': 'utf-8','cookie': '','user-agent':'okhttp/3.10.0.1'}

		timeStr = str(int(time.time()))
		
		_rticket = timeStr+'139'
		
		res = requests.get(api+awemeId+"&ts="+timeStr+"&_rticket="+_rticket,headers=header)

		resArr = json.loads(res.content)

		return resArr

if __name__ == '__main__':

	#分享链接
	#shareUrl="http://v.douyin.com/huW3PD/"
	shareUrl=sys.argv[1]

	#获取id
	awemeId = get(shareUrl,1)
	
	#获取数据
	getAllDataArr = get(url,0,awemeId)
	

	#使用数据	
	print("标题："+getAllDataArr['aweme_detail']['share_info']['share_title'])
	print("所属用户："+getAllDataArr['aweme_detail']['author']['nickname'])
	print("音乐名称："+getAllDataArr['aweme_detail']['music']['title'])
	print("音乐连接："+getAllDataArr['aweme_detail']['music']['play_url']['url_list'][0])
	print("封面："+getAllDataArr['aweme_detail']['video']['cover']['url_list'][0])

	print("无水印视频连接1："+getAllDataArr['aweme_detail']['video']['play_addr']['url_list'][0])
	print("无水印视频连接2："+getAllDataArr['aweme_detail']['video']['play_addr']['url_list'][1])
	print("带水印视频连接1："+getAllDataArr['aweme_detail']['video']['download_addr']['url_list'][0])
	print("带水印视频连接2："+getAllDataArr['aweme_detail']['video']['download_addr']['url_list'][1])
	


	