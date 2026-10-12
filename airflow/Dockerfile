FROM apache/airflow:2.10.3-python3.12

# PyPI packages install into the "airflow" user's ~/.local (as if --user).
# The image deliberately fails `pip install` when run as root, so stay on the
# default "airflow" user.
COPY requirements.txt /tmp/requirements.txt
COPY airflow/requirements.txt /tmp/airflow-requirements.txt
RUN pip install --no-cache-dir -r /tmp/airflow-requirements.txt