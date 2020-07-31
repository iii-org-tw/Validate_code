FROM ubuntu
RUN apt-get update
RUN apt-get install gnupg -y
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN sh -c 'echo "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/" >> /etc/apt/sources.list'
RUN apt-get install --reinstall ca-certificates -y
RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install r-base -y
RUN apt-get install build-essential libcurl4-gnutls-dev libxml2-dev libssl-dev -y
WORKDIR /wq
COPY ./install.R ./install.R
RUN Rscript install.R
