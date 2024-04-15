ARG VARIANT="3.10-buster"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel pip

ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi
