from pathlib import Path

DEFAULT_PDF_REPO_PATH = Path('data')
DEFAULT_RES_REPO_PATH = Path('res')


def get_repo_paths():
    """Return a dictionary containing path information"""

    pdf_repo_path_inp = input(
        'Path to .pdf folder (leave blank to use default): '
    )
    res_repo_path_inp = input(
        'Path to result folder (leave blank to use default): '
    )

    pdf_repo_path = DEFAULT_PDF_REPO_PATH \
        if pdf_repo_path_inp == '' else Path(pdf_repo_path_inp)
    res_repo_path = DEFAULT_RES_REPO_PATH \
        if res_repo_path_inp == '' else Path(res_repo_path_inp)

    return {
        'pdf': pdf_repo_path,
        'res': res_repo_path,
    }
