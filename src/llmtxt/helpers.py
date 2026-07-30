import requests
import os
from pathlib import Path


def get_folder_file_tree(repo_folder: str) -> str:
    """
    Returns the list of all files in a Python repository.
    Args:
        repo_folder (str): Path to the Python repository.
    Returns:
        str: text will all file paths relative to the repo_folder, one for each line
    """
    root = Path(repo_folder)
    files = []
    for file_path in root.glob("*"):
        if file_path.is_dir() and file_path.name in [".", ".venv", ".git", ".idea"]:
            continue
        files += [str(file) for file in file_path.rglob("*") if file.is_file() and file.suffix == ".py"]
    print(f"Found {len(files)} Python files")
    return '\n'.join(sorted(files))


def get_folder_file_content(repo_folder: str, file_path: str) -> str:
    """Get specific file content from a root folder."""
    root = Path(repo_folder)
    file_path = root / file_path
    with open(file_path, "r") as f:
        return f.read()


def gather_repository_info(repo_folder):
    """Gather all necessary repository information."""
    file_tree = get_folder_file_tree(repo_folder)
    readme_content = get_folder_file_content(repo_folder, "README.md")

    # Get key package files
    package_files = []
    for file_path in ["pyproject.toml", "setup.py", "requirements.txt", "package.json"]:
        try:
            content = get_folder_file_content(repo_folder, file_path)
            if "Could not fetch" not in content:
                package_files.append(f"=== {file_path} ===\n{content}")
        except:
            continue

    package_files_content = "\n\n".join(package_files)

    return file_tree, readme_content, package_files_content
