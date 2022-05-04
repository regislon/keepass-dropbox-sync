import os
import dropbox
from pykeepass import PyKeePass

ACCESS_TOKEN = '...'
dbx = dropbox.Dropbox(ACCESS_TOKEN)


def download_dropbox_file(dropbox_file_path: str, local_path: str):
    """
    Download file from dropbox
    """
    dbx.files_download_to_file(local_path, dropbox_file_path)


def upload_dropbox_file(dropbox_file_path: str, local_path: str):
    """
    Upload file to dropbox
    """
    with open(local_path, "rb") as f:
        response = dbx.files_upload(f.read(), dropbox_file_path)
    print(response)


def list_files_dropbox_folder(dropbox_folder_path):
    """
    List of file in a dropbox folder
    """
    list_folder_results = dbx.files_list_folder(dropbox_folder_path)
    files_name = list()
    for i in list_folder_results.entries:
        files_name.append(i.name)
    return files_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dropbox_folder_path = "/KeepPass"
    # files_name = list_files_dropbox_folder(dropbox_folder_path)
    # for name in files_name :
    #     dropbox_file_path = f"{dropbox_folder_path}/{name}"
    #     local_path = os.path.join("C:\\Users\\regis\\Desktop\\test",name)
    #     download_dropbox_file(dropbox_file_path, local_path)

    local_path = "C://Users//regis//Desktop//test//database_test.kdbx"

    # local_path = "C:\\Users\\regis\\Desktop\\test\\database.kdbx"
    #
    # dropbox_file_path = "/KeepPass/database.kdbx"
    #
    # download_dropbox_file(dropbox_file_path,local_path)
    #
    #
    # upload_dropbox_file(dropbox_file_path,local_path)
