# build stage 
FROM python:3.10 AS builder

# install PDM 
RUN pip install pdm

COPY . /workdir

WORKDIR /workdir 

RUN mkdir -p __pypackages__ && pdm sync --prod --no-editable

#run stage 
FROM python:3.10

# retrieve packages from build stage
ENV PATH=$PATH:/workdir/pkgs
COPY --from=builder /workdir/__pypackages__/3.10/lib /workdir/pkgs

# CMD ["pdm", "run", "start"]
CMD ["uvicorn", "main:app"]

