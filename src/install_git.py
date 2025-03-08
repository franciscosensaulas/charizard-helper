# URL for Git for Windows

import os
import urllib.request
import urllib.request

from rich.progress import Progress


# Function to download with progress
def download_file(url, dest_path):
    # Start the download and show the progress bar
    with Progress() as progress:
        task = progress.add_task("[cyan]Downloading...", total=100)

        # Define the download function with progress update
        def report_hook(count, block_size, total_size):
            downloaded = count * block_size
            progress.update(task, completed=downloaded, total=total_size)

        # Download the file with the progress callback
        print("Downloading Git installer...")
        urllib.request.urlretrieve(url, dest_path, reporthook=report_hook)

    print("Download complete.")


def run(install_silent: bool):
    # URL for Git for Windows
    git_installer_url = "https://github.com/git-for-windows/git/releases/download/v2.48.1.windows.1/Git-2.48.1-64-bit.exe"
    # Define the path to save the installer
    installer_path = "git-installer.exe"

    # Run the download
    download_file(git_installer_url, installer_path)

    # Run the installer
    print("Running the installer...")
    if install_silent:
        os.system(f"{installer_path} /VERYSILENT /NORESTART")
    else:
        os.system(f"{installer_path}")

    # Optional: Delete the installer after installation
    os.remove(installer_path)

    print("Git has been installed successfully!")
