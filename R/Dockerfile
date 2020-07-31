FROM ubuntu
RUN apt-get update
RUN sh -c 'echo "deb https://cloud.r-project.org/bin/linux/ubuntu trusty-cran35/" >> /etc/apt/sources.list'
RUN apt-get install gnupg -y
RUN apt-get install --reinstall ca-certificates -y
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN apt-get update
RUN apt-get upgrade -y
WORKDIR /wq
COPY ./install.R ./install.R
RUN DEBIAN_FRONTEND="noninteractive" apt upgrade r-base r-base-dev -y
RUN apt-get install libcurl4-openssl-dev libssl-dev
RUN Rscript install.R
