## About The Project
TeamCityServer is a project for creating a dockerized Teamcity server, agents, and external database. Speeding up and 
reducing the complexity of having CI/CD for the home user.

## Getting Started
As of currently this is a work around solution for static IP addresses. From what I can find, docker swarm does not have
 an easy way to assign static IP addresses to containers. This will be updated in the future.
* Run the 'setup.py' python script to create the necessary files and folders for the projects.
* Run the 'start.py' python scripts to start the docker containers. (This will take a while the first time)
* As of now, using the bash script below is how you can retrieve the TeamCity server's IP address under ['Peers']['IP']. 
This will be changed in the future.
```bash
docker network inspect local-teamcity_teamcity-network 
```
```json
"Peers":
{
    "Name": "8d19fca9528d",
    "IP": "10.0.0.194" <-- This IP is the TeamCity servers IP
}
"3d9498516176de878cc669b02d9350b7859386413ce27ac3851d67b961094ea0": 
{
    "Name": "local-teamcity_postgres.1.rmagycqv7767hixrvkbn49bdx",
    "EndpointID": "7137e7162bca04c4891b1dcfe9e5598e002a00019f1cb49b8f92ffa33cf67d1b",
    "IPv4Address": "172.20.0.6/24", <-- This IP is the postgres database
    "IPv6Address": ""
}
```
* Go to the above IP address with port :8111 -> 10.0.0.194:8111
* At the 'Database connection setup' page
  * Select 'PostgreSQL' as the database type
  * Download the JDBC drivers for postgres
  * Input the database IP from above and port :5432
  * Input teamcity as the database name and username
  * Password is defaulted to mysecretpassword (This will be changed in the future)
* Accept the license agreement
* Create an admin account
* You should now be able to login to the TeamCity server

## Usage
TODO: Add usage instructions

## Roadmap
- [x] Create dockerfiles for TeamCity server, agents, and postgres
- [x] Create docker-compose file for TeamCity server, agents, and postgres
- [ ] Create more scripts to make the setup and removal of the project easier

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

    Fork the Project
    Create your Feature Branch (git checkout -b [name_of_your_new_branch])
    Commit your Changes (git commit -m 'Add some awesome feature')
    Push to the Branch (git push origin [name_of_your_new_branch])
    Open a Pull Request

## License
Distributed under the MIT License. See the `LICENSE` file for more information.

## Contact
Zachary Johnson - @zackjohnson8 - zackjohnson8@gmail.com