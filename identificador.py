import os
import shutil

def isMusic(file):
    name, ext = os.path.splitext(file)
    if ext in ['.mp3', '.m4a', '.wav', '.mid']:
        return True
    else:
        return False

def isDocument(file):
    name, ext = os.path.splitext(file)
    if ext in ['.doc', '.docx', '.pdf', '.txt', '.csv', '.xml', '.odf', '.dif', '.ppt', '.xls', '.xlsx', '.pps']:
        return True
    else:
        return False

def isPicture(file):
    name, ext = os.path.splitext(file)
    if ext in ['.png', '.jpg', '.jpeg', '.raw', '.gif', '.svg']:
        return True
    else:
        return False

def isZip(file):
    name, ext = os.path.splitext(file)
    if ext in ['.zip', '.rar', '.iso']:
        return True
    else:
        return False

def isDesign(file):
    name, ext = os.path.splitext(file)
    if ext in ['.ai', '.psd', '.xd', '.cdr', '.jsp', '.cfm', '.dwg', '.eps']:
        return True
    else:
        return False

def isWeb(file):
    name, ext = os.path.splitext(file)
    if ext in ['.html']:
        return True
    else:
        return False

def isVideo(file):
    name, ext = os.path.splitext(file)
    if ext in ['.mp4', '.mkv', '.smi', 'mpeg4', '.MP4', '.wmv', '.mov', '.avi']:
        return True
    else:
        return False

def isCode(file):
    name, ext = os.path.splitext(file)
    if ext in ['.py', '.js', '.h', '.c', '.css', '.php', '.dart', '.lua', '.java', '.r', '.aspx', '.sql']:
        return True
    else:
        return False


def create_folder(base_path, name):
    new_path = os.path.join(base_path, name)
    if os.path.exists(new_path):
        print('='*60)
        print(f'\033[1;31mThe folder {name} == this path alread exist\033[m')
    else:
        os.mkdir(new_path)
        print('created a new dir')
    return new_path

def move_to_right_folder(src, dst):
    if os.path.exists(dst):
        print(f'\033[1;31mThis file just exist in {dst}\033[m')
    else:
        shutil.move(src, dst)

def identify(path, base_path, src):

    if isMusic(path):
        dst = os.path.join(create_folder(base_path, "MUSIC"), path)
        move_to_right_folder(src, dst)

    if isCode(path):
        dst = os.path.join(create_folder(base_path, "CODE"), path)
        move_to_right_folder(src, dst)
    
    if isDocument(path):
        dst = os.path.join(create_folder(base_path, "DOCUMENT"), path)
        move_to_right_folder(src, dst)

    if isPicture(path):
        dst = os.path.join(create_folder(base_path, "PICTURE"), path)
        move_to_right_folder(src, dst)

    if isZip(path):
        dst = os.path.join(create_folder(base_path, "ZIP FILES"), path)
        move_to_right_folder(src, dst)

    if isVideo(path):
        dst = os.path.join(create_folder(base_path, "VIDEO"), path)
        move_to_right_folder(src, dst)

    if isDesign(path):
        dst = os.path.join(create_folder(base_path, "DESIGN"), path)
        move_to_right_folder(src, dst)

    if isWeb(path):
        dst = os.path.join(create_folder(base_path, "WEB"), path)
        move_to_right_folder(src, dst)
