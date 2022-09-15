ARG conf_dir="/data/teamcity_agent/conf"
ARG system_dir="/data/teamcity_agent/system"

FROM jetbrains/teamcity-agent:latest

# Add the following environment variables:
ENV SERVER_URL=http://locallinux:8111

# Add the following volumes:
VOLUME ["$conf_dir:/data/teamcity_agent/conf", "$system_dir/data/teamcity_agent/system"]