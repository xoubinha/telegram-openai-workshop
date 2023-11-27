import os
import requests


def get_telegram_file_url(bot_token: str, file_info: dict) -> str:
    """
    Get the Telegram file URL for a given bot token and file information.

    Args:
        bot_token (str): The Telegram bot token.
        file_info (dict): The file information containing 'file_path'.

    Returns:
        str: The complete file URL.
    """
    return f"https://api.telegram.org/file/bot{bot_token}/{file_info.file_path}"


def download_file(file_url: str, savedir: str) -> str:
    """
    Download a file from a given URL and save it to a specified directory.

    Args:
        file_url (str): The URL of the file to download.
        savedir (str): The directory where the downloaded file will be saved.

    Returns:
        str: The path to the saved file.
    """
    if not os.path.exists(savedir):
        os.makedirs(savedir)

    response = requests.get(file_url, allow_redirects=True)
    if response.ok:
        filename = _get_filename_from_url(file_url)
        savepath = os.path.join(savedir, filename)
        with open(savepath, 'wb') as file:
            file.write(response.content)
        return savepath


def download_telegram_file(bot, file_id, savedir: str="../data/audios/"):
    file_info = bot.get_file(file_id)
    audio_url = get_telegram_file_url(bot.token, file_info)
    audio_filepath = download_file(audio_url, savedir)
    return audio_filepath

def _get_filename_from_url(url: str) -> str:
    """
    Extract the filename from a URL.

    Args:
        url (str): The URL from which to extract the filename.

    Returns:
        str: The extracted filename.
    """
    return url.split('/')[-1]
