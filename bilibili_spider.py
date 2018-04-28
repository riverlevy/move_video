#encoding=utf-8
import requests
import Html_Downloader
import Url_Manager
import DownloadVideos
import Bilibili_Ranking_Html_Parser
bilibili_rank_url='''https://www.bilibili.com/ranking'''
bilibili_country_rank_url="https://www.bilibili.com/ranking/all/3/0/1"
html_downloader=Html_Downloader.HtmlDownloader()
html_praser=Bilibili_Ranking_Html_Parser.Bilibili_Ranking_Html_Parser()
urls=html_praser.parse_from_html(html_downloader.download(bilibili_rank_url))
url_manager=Url_Manager.Url_Manager()
url_manager.add_new_urls(urls)
download_videos=DownloadVideos.DownloadVideos(5)
# download_videos.download_single_video('''https://www.bilibili.com/video/av22147952/''',"E:\Code\Python\\bilibili_spider")
download_videos.download_multipule_videos(urls,"E:\code\python\\bilibili_spider")
url_manager.save_all()
