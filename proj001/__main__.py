from .gui import getRepoPaths
from .pdf import read

# First, grab necessary paths

repo_path = getRepoPaths.get_repo_paths()

pdf_name = 'test.pdf'
pdf_path = repo_path['pdf'] / pdf_name

print('*** End of program. ***')
