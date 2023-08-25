from dagster_airbyte import load_assets_from_airbyte_instance, AirbyteResource
import pandas as pd


airbyte_instance = AirbyteResource(
    host="http://20.19.18.134",
    port="80",
)
airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance)

# from dagster import (
#     ScheduleDefinition,
#     define_asset_job,
#     AssetSelection,
#     Definitions,
# )

# # materialize all assets
# run_everything_job = define_asset_job("run_everything", selection="*")

# # only run my_airbyte_connection and downstream assets
# my_etl_job = define_asset_job(
#     "my_etl_job", AssetSelection.groups("my_airbyte_connection").downstream()
# )

# defs = Definitions(
#     assets=[airbyte_assets],
#     schedules=[
#         ScheduleDefinition(
#             job=my_etl_job,
#             cron_schedule="@daily",
#         ),
#         ScheduleDefinition(
#             job=run_everything_job,
#             cron_schedule="@weekly",
#         ),
#     ],
# )
