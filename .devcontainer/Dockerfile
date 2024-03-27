FROM continuumio/miniconda3:latest

RUN apt-get update && apt-get install -y git

ENV CONDA_PREFIX=/langchain_env
ENV CONDA_DEFAULT_ENV=$CONDA_PREFIX
ENV PATH=$CONDA_PREFIX/bin:$PATH

COPY conda.yml .
RUN conda env create -p $CONDA_PREFIX -f conda.yml -q && \
    rm conda.yml && \
    conda run -p $CONDA_PREFIX pip cache purge && \
    conda clean -a -y

RUN useradd -ms /bin/bash devuser
WORKDIR /home/devuser
USER devuser