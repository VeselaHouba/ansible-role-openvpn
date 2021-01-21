#!/usr/bin/env bash
if [ "${MOLECULE_IMAGE_SERVER}" == "" ]; then
  echo "Variable MOLECULE_IMAGE_SERVER not set, using default"
fi

if [ "${MOLECULE_IMAGE_CLIENT}" == "" ]; then
  echo "Variable MOLECULE_IMAGE_CLIENT not set, using default"
fi

docker \
  run \
  --rm \
  -it \
  -v "$(pwd):/tmp/role" \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -w /tmp/role \
  -e MOLECULE_NO_LOG=false \
  -e MOLECULE_IMAGE_CLIENT \
  -e MOLECULE_IMAGE_SERVER \
  -e MOLECULE_DOCKER_COMMAND \
  veselahouba/molecule  bash -c "
  shellcheck_wrapper && \
  flake8 && \
  yamllint . && \
  ansible-lint && \
  molecule ${*}"
