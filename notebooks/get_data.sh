
urls=("https://g-f332be.7a577b.6fbd.data.globus.org/tutorial-collection/lens2-subset.tar.gz")
for url in "${urls[@]}"; do
  # Download the tar file
  wget --quiet https://g-f332be.7a577b.6fbd.data.globus.org/tutorial-collection/lens2-subset.tar.gz -O ../data.tar.gz

  mkdir ../data
  # Unzip the tar file
  tar -xzf ../data.tar.gz -C ../data

  # Clean up by removing the tar file
  rm ../data.tar.gz
done