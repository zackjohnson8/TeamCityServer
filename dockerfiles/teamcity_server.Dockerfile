ARG data_dir="/teamcity/data"
ARG logs_dir="/teamcity/logs"

# Grab the initial layer jetbrains/teamcity-server:latest and use it as the base image for the new image.
FROM jetbrains/teamcity-server:latest

# Add the following environment variables:
ENV TEAMCITY_SERVER_MEM_OPTS="-Xmx3g -XX:MaxPermSize=270m -XX:ReservedCodeCacheSize=450m"

# Add the following volumes:
VOLUME ["$data_dir:/data/teamcity_server/datadir", "$logs_dir:/opt/teamcity/logs"]

# Add the following ports:
EXPOSE 8111

# Add the following command:
CMD ["/opt/teamcity/bin/run.sh"]