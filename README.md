# Validate Process  
**Testing Data**  
1. Enter data directory

    `cd data`

2. Run the download script.

    `bash download.sh`  
    
**Python**

1. Enter Python directory
    
    `cd Python`

2. Build the image.

    `sudo docker build -t python-numpy .`

3. Create a container and run it.

    `sudo docker run --name bash --rm -i -t python-numpy`
    
4. For validation, please see the README.md inside Python directory.

**R**  

1. Enter R directory
    
    `cd R`

2. Build the image.

    `sudo docker build -t R-wq .`

3. Create a container and run it.

    `sudo docker run --name bash --rm -i -t R-wq`
    
4. For validation, please see the README.md inside R directory.

**JAVA**

1. Build the image.

    `sudo docker build -t percentile - < Dockerfile`

2. Create a container and run it.

    `sudo docker run --name bash --rm -i -t percentile`

3. Download 'HIGGS.csv'. and put it into `/wq/java-percentile-test`

4. Compile and run the test.

    `mvn exec:java -D"exec.mainClass"="org.ioxcenter.App"`

6. Input the path `/wq/java-percentile-test/HIGGS.csv` to start the test.
