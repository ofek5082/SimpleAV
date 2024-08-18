#!/bin/bash

#// Set filenames and corresponding download URLs 
declare -A cert_links=(
["cert1.txt"]="https://www.eicar.org/download/eicar.com"
["cert2.txt"]="https://www.avast.com/eicar-test-file"
["cert3.txt"]="https://media.kaspersky.com/virus-advisories/EICAR.com"
["cert4.txt"]="https://download.bitdefender.com/testfile/eicar.com"
["cert5.txt"]="https://files.trendmicro.com/solutions/eicar.com"
)

#// Get the current dir
current_dir=$(dirname "$0")

#// Download the certification files
for cert_file in "${!cert_links[@]}"; do
    url="${cert_links[$cert_file]}"
    file_path="$current_dir/$cert_file"

    if [ -f "$file_path" ]; then
      echo "$cert_file Already exists. It will be overwritten."
    fi

    echo "Downloading $cert_file from $url..."

#// Use curl to download and overwrite data 
curl -o "$file_path" "$url"

if [ $? -eq 0 ]; then
    echo "$cert_file Downloaded and overwritten successfully."
else
    echo "Failed to download cert_file."
fi
done
