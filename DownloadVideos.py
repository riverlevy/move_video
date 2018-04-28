import os
import time
import threading
import Url_Manager
import subprocess
import UpLoad_Videos
class DownloadVideos(object):
    def __init__(self,thread_num):
        self.max_threads=thread_num
        self.threads_num=0
        self.url_manager=Url_Manager.Url_Manager()
    def download_single_video(self,url,path,other_command):
        try:
            if not self.url_manager.contain(url):
                if not (url.startswith("http://") or url.startswith("https://")) and url.startswith("//"):
                    url="http:"+url
                elif not url.startswith("http:") or not url.startswith("https:"):
                    url="http://"+url
                # subprocess.run("you-get -o "+path+" "+url,stdout=subprocess.PIPE)
                os.system("you-get -o "+path+" "+other_command+" "+url)
                download_file=subprocess.run("you-get -i "+url,stdout=subprocess.PIPE)
                str=download_file.stdout.decode("UTF-8")
                # print("------------------------------\n")
                # print(str)
                str_lines=str.split('\n')
                file_name=str_lines[1].split(':')[1].lstrip()[:-1]
                file_exp=str_lines[4].split(':')[1].strip()
                if not file_exp == "xml":
                    upload_videos=UpLoad_Videos.UpLoad_Video()
                    res=upload_videos.upload_to_youtube((path+"\\"+file_name),file_exp)
                    print(res)
            #To Do
            #make an log to mysql
        except IOError:
            self.threads_num=self.threads_num-1
            return "Download Error"
        else:
            self.threads_num=self.threads_num-1
            return True
    def download_multipule_videos(self,urls,path,other_command):
        # threads_num=1
        for url in urls:
            # self.download_single_video(url,path)
            # time.sleep(100)
            while self.threads_num>=self.max_threads:
                time.sleep(1)
            try:
                self.threads_num=self.threads_num+1
                t=threading.Thread(target=self.download_single_video,args=(url,path,other_command,))
                t.start()
                # t.join()
            except Exception:
                print("下载错误")
                # return ""
        return True



