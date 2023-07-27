FROM docker.io/library/openjdk:20-ea-jdk-buster as build

WORKDIR /app
COPY WelcomeGrads.java /app

RUN javac --release 17 WelcomeGrads.java


FROM docker.io/jasaz/distroless-jre:wolfi-jre17-one-amd64 as runner

COPY --from=build /app/WelcomeGrads.class /app/
CMD ["WelcomeGrads"]