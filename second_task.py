import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на Яндекс.Диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}"}
        params = {"path": file_path, "overwrite": "true"}

        response = requests.get(url, headers=headers, params=params)
        upload_url = response.json()["href"]

        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.put(upload_url, files=files)

        if response.status_code == 201:
            print("Файл успешно загружен на Яндекс.Диск")
        else:
            print("Ошибка при загрузке файла на Яндекс.Диск")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь до файла на компьютере: ")
    token = input("Введите токен Яндекс.Диска: ")

    uploader = YaUploader(token)
    uploader.upload(path_to_file)