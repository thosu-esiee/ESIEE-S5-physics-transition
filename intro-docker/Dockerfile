FROM ubuntu:24.04
LABEL version="0.1" maintainer="thosu"
RUN apt-get update && apt-get upgrade -y
WORKDIR /hello-dir
COPY hello.sh .
RUN chmod +x hello.sh
ENTRYPOINT ["./hello.sh"]

