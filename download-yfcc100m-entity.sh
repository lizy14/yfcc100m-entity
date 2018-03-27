# split url list
split --lines=5000 urls.txt urls.txt.

# spawn downloaders
for i in ../urls/urls.txt.*;
    do (wget --no-clobber --no-verbose --input-file="$i" &);
done

# check image integrity
mkdir corrupted/
for i in *; do 
    (identify "$i" || (echo "$i"; mv "$i" corrupted/))
done
