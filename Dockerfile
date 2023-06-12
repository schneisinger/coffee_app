# build stage 
FROM python:3.10 AS builder

# install PDM 
RUN pip install pdm

COPY . /workdir

WORKDIR /workdir 

RUN mkdir -p __pypackages__ && pdm sync --prod --no-editable

#run stage 
# FROM python:3.10

# retrieve packages from build stage
# ENV PYTHONPATH=/project/pkgs
# COPY --from=builder /workdir/__pypackages__/3.10/lib /project/pkgs

# set command/entrypoint, adapt to fit your needs
CMD ["pdm", "run", "start"]


