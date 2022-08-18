from os import listdir, path

from pykeepass import PyKeePass

from config import settings


def list_of_duplicate(keepass_folder_path: str, kepass_main_db_name: str) -> list:
    """
    This function list all duplicates created in case of conflict in dropbox
    """
    duplicates = [
        f
        for f in listdir(keepass_folder_path)
        if path.isfile(path.join(keepass_folder_path, f))
        and f.endswith(".kdbx")
        and f != kepass_main_db_name
    ]
    return duplicates


def confict_highlights():
    """
    Load all conflict entries into the conflict group in the main db
    """
    keepass_folder_path = settings.keepass_folder_path
    kepass_main_db_name = settings.kepass_main_db_name
    keepass_list_duplicate = list_of_duplicate(keepass_folder_path, kepass_main_db_name)

    main_file_path = path.join(keepass_folder_path, kepass_main_db_name)
    main = PyKeePass(main_file_path, settings.password)

    if not main.find_groups(name="conflict", first=True):
        main.add_group(main.root_group, "conflict")
        main.save()

    conflict_group = main.find_groups(name="conflict", first=True)

    for duplicate_file_name in keepass_list_duplicate:
        duplicate_file_path = path.join(keepass_folder_path, duplicate_file_name)
        duplicate = PyKeePass(duplicate_file_path, settings.password)
        for group in duplicate.groups:
            for item in group.entries:
                duplicate_password = item.password
                duplicate_uuid = item.uuid
                duplicate_username = item.username
                duplicate_title = item.title
                if not main.find_entries(
                    uuid=duplicate_uuid, first=True
                ) and not main.find_entries(
                    group=conflict_group, title=duplicate_title, first=True
                ):
                    if duplicate_password and duplicate_title:
                        info = f"load {duplicate_title} from {duplicate_file_name}"
                        print(info)
                        note = f"imported from {duplicate_file_name}"
                        main.add_entry(
                            conflict_group,
                            title=duplicate_title,
                            username=duplicate_username,
                            password=duplicate_password,
                            notes=note,
                        )

    main.save()


if __name__ == "__main__":
    confict_highlights()
