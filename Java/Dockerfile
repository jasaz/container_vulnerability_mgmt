FROM docker.io/library/openjdk:20-ea-jdk-buster

WORKDIR /app

COPY WelcomeGrads.java /app

RUN javac WelcomeGrads.java

ENTRYPOINT [ "java", "WelcomeGrads","tail", "-f", "/dev/null"]
