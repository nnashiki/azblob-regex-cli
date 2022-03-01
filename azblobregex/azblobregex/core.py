import re
import os
from azure.storage.blob import ContainerClient
from tqdm import tqdm

def get_match_blobs(container_client: ContainerClient, filter_pattern):
    items = [item for item in container_client.walk_blobs() if re.match(filter_pattern, item.name)]
    return items


def download_blobs(container_client: ContainerClient, items, dl_target_dir):
    if not os.path.exists(dl_target_dir):
        os.mkdir(dl_target_dir)

    for item in tqdm(items):
        with open(F"{dl_target_dir}/{item.name}", "wb") as my_blob:
            my_blob.write(container_client.download_blob(item).readall())

def delete_blobs(container_client: ContainerClient, items):
    for item in tqdm(items):
        container_client.delete_blob(item.name)
