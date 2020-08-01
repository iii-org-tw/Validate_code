FROM ubuntu

# install java8
RUN apt-get update && apt-get install openjdk-8-jdk -y

# install maven
RUN apt install maven -y

# install git
RUN apt-get install git -y

# set path
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH $PATH:$JAVA_HOME/bin

# clone common-math
WORKDIR /wq/commons-math
RUN git clone https://github.com/apache/commons-math.git /wq/commons-math

# install common-math to local repository
RUN mvn install
# clone test project
WORKDIR /wq/java-percentile-test
RUN git clone https://github.com/iii-org-tw/java-percentile-test.git /wq/java-percentile-test
