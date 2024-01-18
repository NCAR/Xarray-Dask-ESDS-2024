urls=("https://docs.google.com/uc?export=download&id=1rpWJJlMSwt7-seeh8kCn-CkOh2FbcwGA" "https://docs.google.com/uc?export=download&id=15rCwQUxxpH6angDhpXzlvbe1nGetYHrf")

for url in "${urls[@]}"; do
  filename="$(basename $url)"
  
  # Download the tar file
  #wget $url -O ../data.tar.gz
  
  FILEID="1sXCEmC9-k2_O8XA780xfodaMdM_yKKC9"
  echo $FILEID
  FILENAME=data.tar.gz
  mkdir .tmp
  echo "Downloading https://docs.google.com/uc?export=download&id=$FILEID"



  wget --no-check-certificate -r 'https://docs.google.com/uc?export=download&id=$FILEID' -O FILENAME

  #wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILEID" -O $FILENAME
  #wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=FILEID" -O FILENAME
  #wget --quiet --load-cookies .tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=FILEID' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FILEID" -O $FILENAME

  # Unzip the tar file
  tar -xvzf ../data.tar.gz -C ../data

  # Clean up by removing the tar file
  rm ../data.tar.gz
done