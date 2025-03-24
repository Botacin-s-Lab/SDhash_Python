FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    software-properties-common \
    apt-transport-https \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH

RUN apt-get update && \
    apt-get install -y maven

RUN java -version
RUN mvn -version

WORKDIR /usr/src/app

RUN apt-get install -y vim
RUN apt-get install -y python3
RUN apt-get update
RUN apt install -y python3-pip
RUN apt install -y python3.12-venv
RUN apt install -y libfuzzy-dev
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# RUN wget https://github.com/Botacin-s-Lab/SDHash/releases/download/1.0.0/SDhash -O SDhash
# # Make SDhash executable
# RUN chmod +x SDhash

# # Optionally move SDhash to a global bin location (e.g., /usr/local/bin) to run it anywhere
# RUN mv SDhash /usr/local/bin/sdhash

# Copy the current directory contents into the container
# COPY *.py /usr/src/app/
# COPY utils utils
# COPY augmented_predictor augmented_predictor

# Run the application
CMD ["bash"]
