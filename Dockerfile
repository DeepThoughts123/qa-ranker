FROM 143926955519.dkr.ecr.us-east-1.amazonaws.com/docker-hub/python:3.8-slim

# Required to install packages from private aritifactory
# It will be passed from command line
ARG PIP_INDEX_URL

# Derived from Sagemaker container structure can be used for ML Flow
# https://docs.aws.amazon.com/sagemaker/latest/dg/amazon-sagemaker-toolkits.html
ENV WORKDIR=/opt/ml/code
ENV USER=app

# Working directory for running below mentioned commands
WORKDIR ${WORKDIR}

# Configure user for running the code
RUN useradd ${USER}
RUN mkdir /home/${USER}
RUN chown -R ${USER}:${USER} ${WORKDIR} && \
    chown -R ${USER}:${USER} /home/${USER} && \
    chown -R ${USER}:${USER} /tmp

# Pumpkinpy Server Environment
ENV SERVER_PORT 3000

# Installing linux dependencies
COPY bin/install_linux_dependencies.sh ${WORKDIR}/bin/install_linux_dependencies.sh
RUN bash ${WORKDIR}/bin/install_linux_dependencies.sh

# Upgrade pip
RUN python -m pip install --upgrade pip

# To avoid installing dependencies without changes
COPY requirements.txt ${WORKDIR}
RUN python -m pip install -r ${WORKDIR}/requirements.txt

# Copy your project and compile the code
COPY --chown=app:app . ${WORKDIR}
RUN python -m pip install ${WORKDIR} --no-deps

# Makes `isc shell` and `isc console` pick up the env variables
COPY ./bin/app /etc/default/app
RUN chmod +x /etc/default/app && \
    chmod +x ${WORKDIR}/bin/console

# Click CLI entrypoint
ENTRYPOINT ["bash", "/opt/ml/code/bin/entrypoint.sh"]
CMD ["serve"]
