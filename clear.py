import os


def delete_contents_of_directory():
    directory_path = "qrcode_img"
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            os.unlink(item_path)
    print(f"Содержимое папки '{directory_path}' удалено.")
