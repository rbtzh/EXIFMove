import fileprocess
import os

EXTEND_PHOTO_TUPLE = ("nef", "jpg", "jpeg")

# relative directory, select which folder contains all the photos. leave it "" to specify current folder.
PHOTO_ROOT_DIR = os.getcwd() + "/photos"
PHOTO_ROOT_DIR = "/media/yan/Storage2T2d/Photography"
if __name__ == '__main__':

    filepaths = fileprocess.get_all_filename_in_a_directory(PHOTO_ROOT_DIR, EXTEND_PHOTO_TUPLE)

    for filepath in filepaths:
        try:
            CreatedDate = fileprocess.get_created_date(filepath)

            destpath = os.path.join(
                PHOTO_ROOT_DIR,
                CreatedDate.year,
                CreatedDate.year+"-"+CreatedDate.month,
                CreatedDate.year+"-"+CreatedDate.month+"-"+CreatedDate.day,
                os.path.basename(filepath).split('/')[-1]
            )

            os.makedirs(os.path.dirname(destpath), exist_ok=True)

            os.rename(
                filepath,
                destpath
            )

        except all:
            pass

