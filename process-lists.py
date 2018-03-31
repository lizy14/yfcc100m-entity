filelist = "/home/justin/s/datasets/yfcc100m-entity/data/{domain}/{which_set}.txt"

expected_url_prefix = "https://multimedia-commons.s3-us-west-2.amazonaws.com/data/images/"

urls_filename = "urls-{domain}-{which_set}.txt"

synsets_filename = "synsets-{domain}-{which_set}.txt"

def main():
    for domain in ['Artifacts', 'Species-I', 'Species-Y', 'Sports']:
        for which_set in ['dev', 'full', 'test']:
            with open(urls_filename.format_map({'domain': domain, 'which_set': which_set}), "w") as yfccof:
                with open(synsets_filename.format_map({'domain': domain, 'which_set': which_set}), "w") as imagenetof:
                
                    total = 0
                    exist = [0, 0]
                    with open(filelist.format_map({'domain': domain, 'which_set': which_set})) as f:
                        for line in f:
                            filename, label, source = line.strip().split(" ")
                            total += 1
                            if source == "imagenet":
                                    exist[0] += 1
                                    actual_filename = filename.split('/')[-1].split('.')[0]
                                    # ImageNet Synset
                                    print(actual_filename.split('_')[0], file=imagenetof)

                            elif source == "yfcc100m":
                                splits = filename.split('/')
                                expected_filename_prefix = (splits[-3] + splits[-2])
                                if filename.startswith(expected_url_prefix) and splits[-1].startswith(expected_filename_prefix):
                                    exist[1] += 1
                                    # YFCC100M url
                                    print(filename, file=yfccof)
                                else:
                                    print("unexpected url: ", filename)
                            else:
                                print("unknown source: ", source)
                            continue

            print(domain, which_set, ':' , exist, "/", total)

if __name__ == "__main__":
    main()
