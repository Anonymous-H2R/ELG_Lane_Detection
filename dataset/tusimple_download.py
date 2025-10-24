# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("manideep1108/tusimple")
#
# print("Path to dataset files:", path)
import os,glob
import kagglehub
import shutil

# Download latest version
path = kagglehub.dataset_download("rangalamahesh/preprocessed-1")

print("Path to dataset files:", path)



for root, dirs, files in os.walk(path):
    if files:
        for f in files[:10]:
            print(os.path.join(root, f))
        break

# Change path of the folders where you downloaded the dataset below path won't work on your system
# src_folder = r"\kagglehub\datasets\rangalamahesh\preprocessed-1\versions\1\training\kaggle\working\tusimple_preprocessed\training\frames"
# dst_folder = r"ELG_Lane_Detection\dataset\tusimple"
#
# shutil.move(src_folder, dst_folder)
# print("Moved dataset successfully.")

# AFter moving the dataset to tusimple folder check if its correctly moved add your own path below path won't work on your system
# sample_folder = r"ELG_Lane_Detection\dataset\tusimple\frames"
# imgs = sorted(glob.glob(os.path.join(sample_folder, "*.jpg")))
# print("Found images:", len(imgs))
# print("First 5:", imgs[:5])
