from .gui import getRepoPaths
from .pdf import read

repo_paths = getRepoPaths.get_repo_paths()

pdf_name = 'CapCall_MSOFLP_17Aug2018 (CD).PDF'
pdf_path = repo_paths['pdf'] / pdf_name

pdf_info = read.get_info(pdf_path)

print(pdf_info['/Author'])
