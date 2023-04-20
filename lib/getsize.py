import os

class getsize():
    
    def file_size(file_path):
        """
        this function will return the file size
        """
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            # print(file_info.st_size)
            num=file_info.st_size

        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0
    
            # return convert_bytes(file_info.st_size)
        return num
    