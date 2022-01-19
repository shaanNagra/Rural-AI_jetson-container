# syntax=docker/dockerfile:1

# nividia ml image, tensorflow and most ml python libraires etc.
FROM nvcr.io/nvidia/l4t-ml:r32.6.1-py3
#FROM jetyolo:latest

#-------------------APT-PACKAGES-------------------
RUN apt-get update && apt-get install -y \
    #python3-tk is required by tqdm
    python3-tk \
    #for editing files if needed
    nano

#-------------------SET WORK DIR-------------------
# change the directory to /usr/src/app
WORKDIR /app

#--------------------PYTHON------------------------
# copy the requirements.txt into /usr/src/app
COPY requirements.txt ./
# install all modules mentioned in requriements.txt
# requirments main two python libraires are funcx and funcx-endpoints
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt


#-----------------SETUP DIRECTORIES ----------
# funcx looks for token at root/.funcx
#COPY ~/.funcx/ /root/.funcx 
#COPY ~/JetsonYolo/ ./JetsonYolo
#COPY sensor-sim/ ./sensor-sim

#VOLUME ~/output:/app/output/
#VOLUME ~/sensor-sim:/app/sensor-sim/

#set env to use utf-8 over ascii as python issues arise otherwise
ENV LC_ALL C.UTF-8

#    funcx-endpoint start default && \
#    /bin/bash


ENTRYPOINT funcx-endpoint start default && \ 
           /bin/bash
