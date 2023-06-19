# build stage 
FROM python:3.10 AS builder

# install PDM -> plus Version 
RUN pip install pdm==2.6.1

# COPY . /workdir
COPY pyproject.toml pdm.lock /workdir/
COPY src/ /workdir/src

WORKDIR /workdir 

RUN mkdir -p __pypackages__ && pdm sync --prod --no-editable

# run stage 
FROM python:3.10-alpine

# retrieve packages from build stage
EXPOSE 8000

RUN mkdir -p /workdir/__pypackages__ 
RUN apk add curl

COPY --from=builder /workdir/__pypackages__/3.10/lib /workdir/__pypackages__/lib
COPY --from=builder /workdir/__pypackages__/3.10/bin /workdir/__pypackages__/bin

ENV PATH=$PATH:/workdir/__pypackages__/bin
ENV PYTHONPATH=/workdir/__pypackages__/lib:/workdir/__pypackages__/lib/coffee

# CMD ["pdm", "run", "start"]
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]

