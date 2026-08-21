FROM python:3.12-slim

WORKDIR /usr/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    "dbt-core>=1.9,<2.0" \
    "dbt-postgres>=1.9,<2.0"

COPY profiles.yml /root/.dbt/profiles.yml
COPY dbt_project.yml .
COPY packages.yml .
COPY models/ models/

ENTRYPOINT ["dbt"]
