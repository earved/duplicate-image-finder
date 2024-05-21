'''
Simple python script to search for similar or identical images using cross-correlation. All possible rotations of the images are considerd.
'''
#import modules
import os
import numpy
from PIL import Image
import matplotlib.pyplot as plt
import time

### USER SETTINGS
# specify the directory path
path = "D:/Test/Testfolder"

corr_threshold = 0.95

delete_files_switch = False # True or False to automatically duplicate images

### Main Code
# === preallocation ====================================================================================================
# list files in img directory
files = os.listdir(path)

counter_delfiles = 0
counter_unique = 0

N_img = len(files) #number of images
file1_counter = -1

#using a set as delete_list to avoid duplicates in the list
delete_list = set()

corrcoef_list=[]
results = []

#function definiton
def sortcorreff(val):
    return val[2]

# === comparing images =================================================================================================
print(str(N_img) + " files: starting process...")
tic = time.time()
for file1 in files:
    # make sure file is an image
    if file1.endswith(('.jpg', '.JPG', '.jpeg')):

        img1_path = path + "/" + file1
        img1 = Image.open(img1_path).convert("L")
        img1_metadata = img1.getexif()
        #print("checking " + file1)

        file1_counter += 1 #increment file 1 counter
        file2_counter = 0  #reset file 2 counter

        for file2 in files[file1_counter:N_img - 1]:
            if file2.endswith(('.jpg', '.JPG', '.jpeg')):

                file2_counter += 1
                img2_path = path + "/" + file2
                img2 = Image.open(img2_path).convert("L")
                img2_metadata = img2.getexif()

                # === 1st step: compare metadata to check if these are seperate pictures ===============================
                # use continue to proceed to next picture if metadata is identical
                if img2_path == img1_path: #check if path & photo name are identical
                    continue #filenames are identical and therefore its the same pic

                #check if pictures were recorded with same hardware
                if img1_metadata.get(272) and img2_metadata.get(272):
                    if img1_metadata.get(272) != img2_metadata.get(272):
                        #print("img1 was recorded with " + img1_metadata.get(272) + \
                        # " while img2 recorded with " + img2_metadata.get(272))
                        #continue if different hardware was used
                        continue

                #check if pictures have different resolution
                # if not img1.size[0] in img2.size or not img1.size[1] in img2.size:
                #     print("\r pictures have different pixel sizes")
                #     continue

                # === 2nd step: re-interpolate and calculate correlation to check if pictures are identical ============
                img_size=100
                img1resize = img1.resize((img_size, img_size))
                img2resize = img2.resize((img_size, img_size))

                img1resize_arr = numpy.array(img1resize)
                img2resize_arr = numpy.array(img2resize)

                # calculate correlation with all 4 possible rotations of picture 2
                img2resize_rotated = img2resize_arr
                corrcoef = [0] * 4
                for ii in [0,1,2,3]:
                    img2resize_rotated = numpy.rot90(img2resize_rotated)
                    corrcoef[ii] = numpy.corrcoef(img1resize_arr.flatten(),img2resize_rotated.flatten())[0,1]
                    if corrcoef[ii] > corr_threshold:
                        break

                corrcoef_list.append(round(max(corrcoef),3))
                #print("\r correlation: "+str(round(max(corrcoef),3))+" with "+file2)
                results.append((file1, file2, round(max(corrcoef),3)))

                if max(corrcoef) > corr_threshold:
                    counter_delfiles += 1
                    print("-->" + file1 + " AND " + file2 + "--> correlation: " + str(max(corrcoef)))
                    if sorted(img1.size)[0] <= sorted(img2.size)[0] and sorted(img1.size)[1] <= sorted(img2.size)[1]:
                        delete_list.add(img1_path)
                        #print("---> file 1 has lower or equal resolution and is put to kill-list")
                    else:
                        delete_list.add(img2_path)
                        #print("file 2 has lower resolution and is put to kill-list")

                    if 0: #enable to plot similar pictures
                        ind = corrcoef.index(max(corrcoef))
                        img2resize_rotated = img2resize_arr
                        for jj in range(0, ind+1):
                            img2resize_rotated = numpy.rot90(img2resize_rotated)

                        plt.figure()
                        plt.subplot(121)
                        plt.imshow(img1resize_arr, cmap='gray')
                        plt.subplot(122)
                        plt.imshow(img2resize_rotated, cmap='gray')
                        plt.show()

        print(str(file1_counter+1) + " checked / " + str(counter_delfiles) + " duplicates")

# === print summary ====================================================================================================
print("summary: " + str(N_img) + " files checked / " + str(counter_delfiles) + " files duplicates")
print("=== highest corrcoeff values ===")
#print out 10 highest correlations
for ii in sorted(results,key=sortcorreff,reverse=True)[0:9]:
    print("corrcoeff: " + str(ii[2]) + " -->"+ ii[0] + " AND " + ii[1]  )

for del_file in delete_list:
    if delete_files_switch:
        os.remove(del_file)
        print(del_file + "  deleted")
    else:
        print(del_file + "  can potentially be deleted")

toc = time.time()
print(f"Runtime: {toc - tic:0.4f} seconds")
print("-->process finished")