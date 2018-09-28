## Start

```sh
# manually run when Dockerfile changes
docker-compose build
docker-compose run --rm python_dev
```

You will be in the docker container with the isolated python environment.

## TODO:

- think about a better way to "rebuild" and publish the image (maybe just publish the image to dockerhub) - so if Dockerfile changes people don't have to remember to run `docker-compose build`

## Notes

- use `apk add --no-cache` to do `--update` (update index) and avoid shipping image with local apk cache (better alternative than doing `apk add --update ... && rm -rf /var/cache/apk/*`: faster-less work, avoid cache path)
- (not sure this is needed) use `apk add --virtual <dir> ...` such as `apk add --virtual .build-dependencies package1 package2` to group package installation into a group for easy clean up like `apk del .build-dependencies `