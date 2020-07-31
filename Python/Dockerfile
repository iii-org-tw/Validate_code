FROM ubuntu
RUN apt-get update
RUN apt-get install python3.8 -y
RUN apt install python3-pip -y
RUN python3.8 -m pip install cython
RUN apt-get install git -y
WORKDIR /wq
RUN git clone https://github.com/iii-org-tw/numpy --branch weighted_quantile /wq/numpy
RUN cd /wq/numpy && python3.8 ./setup.py build_ext --inplace
ENV PYTHONPATH="${PYTHONPATH}:/wq/numpy"
