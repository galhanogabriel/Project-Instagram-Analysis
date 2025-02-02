from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parents[2]

DATA_FOLDER = PROJECT_FOLDER / "data"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
ORIGINAL_DATA = DATA_FOLDER / "Instagram engagement.xlsx"