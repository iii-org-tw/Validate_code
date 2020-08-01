# Validate Process
**Python**

1. git clone https://github.com/iii-org-tw/numpy --branch ready_version
2. Install from source according to [numpy tutorial](https://numpy.org/doc/stable/user/building.html).
3. Execute test.py under Validate_code/Python directory

**R**
1. install.packages("devtools")
2. install https://cran.r-project.org/bin/windows/Rtools/
3. library(devtools)
4. install_github("iii-org-tw/Hmisc")
5. Execte test.R script under Validate_code/R directory

**Testing Data**  
For testing, please download HIGGS.csv and put it into data directory



**JAVA**

1. `sudo docker build -t percentile - < Dockerfile`

2. `sudo docker run --name bash --rm -i -t percentile`

3. `cd java-percentile-test`

4. Download 'HIGGS.csv'.

4. `mvn exec:java -D"exec.mainClass"="org.ioxcenter.App"`

5. Input the path to 'HIGGS.csv' and it will start the test.
