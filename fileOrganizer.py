#! python 3
# file organizer.py 
# aranges file automatically for you 

from pathlib import Path
import shutil


def sort(directory, foldernames=['txt_folder', 'pdf_folder', '.jpg_folder', 'png_folders', 'doc_folder'],
                file_extentions=['.txt', '.pdf', '.jpg', '.png', '.docx']):

    """ specify the directory you would like to sort
        file_extention are list of file extention you would like to sort
        foldernames are the list of folder you would like 
        to sort your files in """

    directory = Path(directory)
    for i in range(len(foldernames)):
        try:
            newFolder = (directory / foldernames[i])
            newFolder.mkdir()
        except FileExistsError:
            pass
        
        for moveFiles in directory.glob(f'*{file_extentions[i]}'):
            shutil.move(f'{moveFiles}', f'{(directory / foldernames[i])}')

