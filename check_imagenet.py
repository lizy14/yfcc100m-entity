import os
import time
import subprocess

imagenet_root = "/home/dataset/ILSVRC2015/Data/CLS-LOC/train/"

filelist = "/home/justin/o/yfcc100m-entity/data/{domain}/full.txt"

expected_url_prefix = "https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/"

urls_filename = "urls.txt"
with open(urls_filename, "w") as of:
    for domain in ['Artifacts', 'Species-I', 'Species-Y', 'Sports']:
        if domain != 'Sports':
            continue
        total = 0
        exist = [0, 0, 0]
        with open(filelist.format_map({'domain': domain})) as f:
            for line in f:
                filename, label, source = line.strip().split(" ")
                total += 1
                if source == "imagenet":
                    if os.path.exists(os.path.join(imagenet_root, filename)):
                        exist[0] += 1
                    else:
                        exist[1] += 1
                        pass # print("not found in imagenet: ", filename)
                    # TODO: 
                elif source == "yfcc100m":
                    splits = filename.split('/')
                    expected_filename_prefix = (splits[-3] + splits[-2])
                    if filename.startswith(expected_url_prefix) and splits[-1].startswith(expected_filename_prefix):
                        exist[2] += 1
                        print(filename, file=of)
                    else:   
                        print("unexpected url: ", filename)
                else:
                    print("unknown source: ", source)
                continue

        print(domain, ':' , exist, "/", total)
        subprocess.call([
            'wget',
            '--no-clobber',
            '--input-file={}'.format(urls_filename)
        ])
