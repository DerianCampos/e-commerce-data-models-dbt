"""Daily dbt build scheduled by Airflow (BashOperator).

Runs `dbt build` (models + data tests in dependency order).
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

DBT_PROJECT = "/usr/app/e-commerce-dbt-core"


# Alerts: enable later (e.g. SMTP or a webhook).
# Uncomment once you have a notification channel configured.
#
# def notify_failure(context):
#     """Stub — replace with email/webhook/chat notification."""
#     print(f"FAILED: {context['task_instance']}")
#
# We do NOT turn Airflow into the only source of truth for running dbt — by
# default tasks retry once, then surface in the Airflow UI on failure.
with DAG(
    dag_id="dbt_daily_build",
    schedule="0 5 * * *",                    # daily at 05:00 local time
    start_date=datetime(2026, 1, 1),
    catchup=False,                           # never backfire past runs after downtime
    max_active_runs=1,                       # no overlapping runs
    tags=["dbt", "e-commerce"],
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    doc_md=__doc__,
) as dag:
    dbt_deps = BashOperator(
        task_id="dbt_deps",
        bash_command=f"cd {DBT_PROJECT} && dbt deps",
        # deps is a no-op after the first run (dbt_packages/ persists in the mount)
    )

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command=f"cd {DBT_PROJECT} && dbt build",
    )

    # Uncomment when alerting is wired up:
    # dbt_build.on_failure_callback = notify_failure

    dbt_deps >> dbt_build