import tempfile


def download_rom(URL):
    """在线下载更新包"""
    response = requests.get(URL)
    with tempfile.TemporaryFile() as temp_file:
        for index, data in enumerate(response.iter_content(1024)):
            temp_file.write(data)
    return temp_file
