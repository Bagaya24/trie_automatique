from pathlib import Path

chemin = Path.home() / "Downloads"

tries = {
    ".jpg": "Image",
    ".png": "Image",
    ".bmp": "Image",
    ".jpeg": "Image",
    ".avi": "Video",
    ".mkv": "Video",
    ".mp4": "Video",
    ".gif": "Video",
    ".mp3": "Musique",
    ".waw": "Musique",
    ".flac": "Musique",
    ".exe": "Logiciel",
    ".msi": "Logiciel",
    ".txt": "Document",
    ".csv": "Document",
    ".pptx": "Document",
    ".xls": "Document",
    ".pdf": "Document",
    ".zip": "Archive",
    ".rar": "Archive",
    ".xs": "Archive",
    ".tar": "Archive",
    ".py": "Python",
    ".vsix": "Archive",
    ".xz": "Archive",
    ".themepack": "Archive",
    ".java": "Java",
    ".iso": "systeme",
    ".svg": "image"
}

for fichier in chemin.iterdir():
    if fichier.is_file():
        for extension, dossier in tries.items():
            chemin = chemin / dossier
            chemin.mkdir(exist_ok=True)

            if fichier.suffix == extension:
                fichier.rename(chemin / fichier.name)
            chemin = chemin.parent

if __name__ == '__main__':
    print("Bonjour le monde")