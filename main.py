#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformAsset, AssetType
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.lambda_function import LambdaFunction
from cdktf_cdktf_provider_aws.lambda_event_source_mapping import LambdaEventSourceMapping
from cdktf_cdktf_provider_aws.data_aws_caller_identity import DataAwsCallerIdentity
from cdktf_cdktf_provider_aws.scheduler_schedule import SchedulerSchedule, SchedulerScheduleFlexibleTimeWindow, SchedulerScheduleTarget
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket
from cdktf_cdktf_provider_aws.dynamodb_table import DynamodbTable,DynamodbTableAttribute,DynamodbTableGlobalSecondaryIndex

class LambdaStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        AwsProvider(self, "AWS", region="us-east-1")
        account_id = DataAwsCallerIdentity(self, "account_id").account_id

        # bucket = S3Bucket(
        #     self, "s3_bucket",
        #     bucket_prefix = "my-cdtf-test-bucket-yan",
        #     acl="private",
        #     force_destroy=True,
        #     versioning={"enabled":True}
        #     )

        dynamodb = DynamodbTable(
            self, "DynamodDB-table",
            name="user_score",
            hash_key="PK",
            range_key="SK",
            attribute=[
                DynamodbTableAttribute(name="PK",type="S" ),
                DynamodbTableAttribute(name="SK",type="S" )
            ],
            billing_mode="PROVISIONED",
            read_capacity=5,
            write_capacity=5,
            global_secondary_index=[
                DynamodbTableGlobalSecondaryIndex(
                    name="InvertedIndex",
                    hash_key="SK",
                    range_key="PK",
                    projection_type="ALL",
                    write_capacity=5,
                    read_capacity=5
                )
            ]
        )


app = App()
LambdaStack(app, "S3")
app.synth()