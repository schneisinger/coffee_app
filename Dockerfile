# build stage 
FROM python:3.10 AS builder

# install PDM 
RUN pip install pdm uvicorn[standard]

# COPY . /workdir
COPY pyproject.toml pdm.lock /workdir/
COPY src/ /workdir/src

WORKDIR /workdir 

RUN mkdir -p __pypackages__ && pdm build && pdm sync --prod --no-editable

#run stage 
FROM python:3.10

# retrieve packages from build stage
EXPOSE 8000
ENV PATH=$PATH:/workdir/pkgs

RUN mkdir -p /workdir/pkgs

COPY --from=builder /workdir/__pypackages__/3.10/lib /workdir/pkgs

CMD ["pdm", "run", "start"]
# CMD ["uvicorn", "main:app"]

