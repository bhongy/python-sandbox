## Start

```sh
# manually run when Dockerfile changes
docker-compose build
# run one-off command - i.e. `sh`
docker-compose run --rm python_dev sh
```

You will be in the docker container with the isolated python environment.


## TODO:

- configuration to start the dev is currently scattered in 3 places: Dockerfile (`WORKDIR`), docker-compose.yml (`volume:`), docker-compose run command (`python_dev sh`) ... finds a way to organize them better
- think about a better way to "rebuild" and publish the image (maybe just publish the image to dockerhub) - so if Dockerfile changes people don't have to remember to run `docker-compose build`