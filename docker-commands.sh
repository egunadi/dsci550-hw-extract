# Show and Tell model Image Text Captioning
# Used for image captioning
# -----------------------------------------
docker pull uscdatascience/im2txt-rest-tika

# cannot run this simultaneously with inception-rest-tika
# they both use the same port
docker run -d --name im2text -p 8764:8764 uscdatascience/im2txt-rest-tika
# -d (daemon mode) allows container to be managed in Docker Desktop
# to run as an interactive shell, use:
# docker run -it -p 8764:8764 uscdatascience/im2txt-rest-tika

# sample service on port 8764
# http://localhost:8764/inception/v3/caption/image?url=https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Marcus_Thames_Tigers_2007.jpg/1200px-Marcus_Thames_Tigers_2007.jpg

# Inception v4 model Image detection
# Used for detecting objects
# ----------------------------------
docker pull uscdatascience/inception-rest-tika

# cannot run this simultaneously with im2txt-rest-tika
# they both use the same port
docker run -d --name inception -p 8764:8764 uscdatascience/inception-rest-tika
# -d (daemon mode) allows container to be managed in Docker Desktop
# to run as an interactive shell, use:
# docker run -it -p 8764:8764 uscdatascience/inception-rest-tika

# sample service on port 8764
# http://localhost:8764/inception/v4/classify/image?topn=2&min_confidence=0.03&url=https://upload.wikimedia.org/wikipedia/commons/f/f6/Working_Dogs%2C_Handlers_Share_Special_Bond_DVIDS124942.jpg

# for reference, see
# ------------------
# https://github.com/USCDataScience/tika-dockers
# https://hub.docker.com/r/uscdatascience/im2txt-rest-tika
# https://cwiki.apache.org/confluence/display/TIKA/ImageCaption#ImageCaption-a.Usingdocker(Recommended)
