import os
imagenet_root = [
    "/home/dataset/ILSVRC2015/Data/CLS-LOC/test/"
][0]

filelist = "/home/lizhaoyang/yfcc100m-entity/data/Artifacts/test.txt"


total = 0
exist = 0
with open(filelist) as f:
    for line in f:
        filename, label, source = line.strip().split(" ")
        if source != "imagenet":
            continue
        total += 1
        if os.path.exists(os.path.join(imagenet_root, filename)):
            exist += 1
            # print(exist, "/", total, filename, label)
        continue

print(exist, "/", total)
