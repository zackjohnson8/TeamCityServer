ARG data_dir="/home/locallinux/teamcity/server/data"
ARG logs_dir="/home/locallinux/teamcity/server/logs"

# Grab the initial layer jetbrains/teamcity-server:latest and use it as the base image for the new image.
FROM jetbrains/teamcity-server:latest

# Add the following environment variables:
ENV TEAMCITY_SERVER_MEM_OPTS="-Xmx3g -XX:MaxPermSize=270m -XX:ReservedCodeCacheSize=450m"

# Add the following volumes:
VOLUME ["$data_dir:/data/teamcity_server/datadir", "$logs_dir:/opt/teamcity/logs"]