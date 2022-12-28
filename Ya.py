from pprint import pprint
import requests



class YaUploader:
    files_url = 'https://disk.yandex.ru/client/disk/files/Текст для яндекса.txt'
    upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path=%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0&url=https%3A%2F%2Fdisk.yandex.ru%2Fclient%2Fdisk%2Ffiles%2F%D0%A2%D0%B5%D0%BA%D1%81%D1%82%20%D0%B4%D0%BB%D1%8F%20%D1%8F%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B0.txt'


    def __init__(self, token: str):
        self.token = token


    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f"OAuth {token}"
                  }



    def get_upload_link(self, file_path):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_link, params=params, headers=self.headers)
        pprint(response.json())
        return response.json()



    def upload(self, file_path ):
        href = self.get_upload_link(file_path).get('href')
        if not href:
            return

        with open(file_path, 'rb') as file:
            response = requests.put(href, data=file)
            if response.status_code == 201:
                print('File uploaded successfully')
                return True
            else:
                print('File upload failed', response.status_code)


if __name__ == '__main__':
    path_to_file = 'Текст для яндекса.txt'
    token = 'y0_AgAAAABkPyMuAAjz_AAAAADX-BHtmNnR110HT_aSuRyeSFtWWNjUTf0'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)

