## Start

```sh
docker-compose run --rm python_dev sh
```

You will be in the docker container with the isolated python environment.


## TODO:

- configuration to start the dev is currently scattered in 3 places: Dockerfile (`WORKDIR`), docker-compose.yml (`volume:`), docker-compose run command (`python_dev sh`) ... finds a way to organize them better