# Importation de flow
from prefect import flow

# Importation des dependances de airbyte 
from prefect_airbyte.server import AirbyteServer
from prefect_airbyte.connections import AirbyteConnection
from prefect_airbyte.flows import run_connection_sync

# Importation des dependances de DBT 
from prefect_dbt.cli import DbtCliProfile, DbtCoreOperation

# Import les dependances pour deployer et schedules notre code
from prefect.deployments import run_deployment
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule
from prefect.filesystems import Azure





server = AirbyteServer.load("airbyte-server")

airbyte_connection_bordeaux = AirbyteConnection.load("airbyte-connection-bordeaux",validate=False)
airbyte_connection_montreal = AirbyteConnection.load("airbyte-connection-montreal",validate=False)
airbyte_connection_paris = AirbyteConnection.load("airbyte-connection-paris",validate=False)
airbyte_connection_rennes = AirbyteConnection.load("airbyte-connection-rennes",validate=False)

@flow(name="flow_airbyte")
def airbyte_syncs():
    run_connection_sync(airbyte_connection_bordeaux)

    run_connection_sync(airbyte_connection_montreal)

    run_connection_sync(airbyte_connection_paris)

    run_connection_sync(airbyte_connection_rennes)

storage = Azure.load("azure-blob") # load a pre-defined block

# @flow(name="flow_dbt")
# def flow_dbt() -> str:
#     result = DbtCoreOperation(
#         commands=["dbt run --models onepointbordeaux onepointmontreal onepointparis onepointrennes --target dev"],#,"dbt run --models weathergold --target gold"
#         project_dir=".",
#         profiles_dir="."
#     )
#     return result.run()


# deploiement_dbt = Deployment.build_from_flow(
#     flow= flow_dbt,
#     name= "cron_dbt",
#     storage=storage,
#     schedule=(CronSchedule(cron="* * * * *", timezone="Europe/Paris"))
# )


# deploiement_dbt.apply()

# def main_dbt():
#     run_deployment(name="flow_dbt/cron_dbt")

# @flow
# def trigger_dbt_flow():
#     dbt_cli_profile = DbtCliProfile.load("DBT-CORE-OPERATION-BLOCK-NAME-PLACEHOLDER")
#     with DbtCoreOperation(
#         commands=["dbt debug", "dbt run"],
#         project_dir="PROJECT-DIRECTORY-PLACEHOLDER",
#         profiles_dir="PROFILES-DIRECTORY-PLACEHOLDER",
#         dbt_cli_profile=dbt_cli_profile,
#     ) as dbt_operation:
#         dbt_process = dbt_op.trigger()
#         # do other things before waiting for completion
#         dbt_process.wait_for_completion()
#         result = dbt_process.fetch_result()
#     return result

# trigger_dbt_flow()

deploiement_airbyte = Deployment.build_from_flow(
    flow= airbyte_syncs,
    name= "cron_airflow",
    work_queue_name="default",
    path = './',
    work_pool_name="workpool-onepoint",
    schedule=(CronSchedule(cron="* * * * *", timezone="Europe/Paris"))
)
deploiement_airbyte.apply()

def main_airflow():
    run_deployment(name="flow_airbyte/cron_airflow")


if __name__ == "__main__":
    main_airflow()
    # airbyte_syncs()
    # main_dbt()


