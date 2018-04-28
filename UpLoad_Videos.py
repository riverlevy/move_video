import subprocess
class UpLoad_Video(object):
    def upload_to_youtube(self,file_name,file_exp):
        full_name='"'+file_name.split("\\")[-1].split(".")[0]+"."+file_exp+'"'
        command_str='''python ../youtube-upload-master\\bin\\youtube-upload --client-secrets=../youtube-upload-master\client_secret.json --title="'''+file_name.split('\\')[-1]+'''" '''+full_name
        print(command_str)
        upload_file=subprocess.run(command_str, stdout=subprocess.PIPE)
        return upload_file.stdout.decode("utf-8")
