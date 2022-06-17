from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "ocp_deploy_2-0617075716",
}

dag = DAG(
    "ocp_deploy_2-0617075716",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using ocp_deploy_2.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_94ce2428_d9d1_4824_8c17_0b50ed1063f3 = NotebookOp(
    name="get_artifact",
    namespace="ml-workshop",
    task_id="get_artifact",
    notebook="ml-workshop-improved/airflow/deploy_model/ocp/get-artifact.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="ocp_deploy_2-0617075716",
    cos_dependencies_archive="get-artifact-94ce2428-d9d1-4824-8c17-0b50ed1063f3.tar.gz",
    pipeline_outputs=[
        "model.pkl",
        "requirements.txt",
        "CustomerChurnOrdinalEncoder.pkl",
        "CustomerChurnOneHotEncoder.pkl",
    ],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "u29",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_94ce2428_d9d1_4824_8c17_0b50ed1063f3.image_pull_policy = "IfNotPresent"


notebook_op_89caab6f_9738_4a08_9205_19edf4ead6ab = NotebookOp(
    name="build_container",
    namespace="ml-workshop",
    task_id="build_container",
    notebook="ml-workshop-improved/airflow/deploy_model/ocp/build-container.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="ocp_deploy_2-0617075716",
    cos_dependencies_archive="build-container-89caab6f-9738-4a08-9205-19edf4ead6ab.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "CustomerChurnOrdinalEncoder.pkl",
        "model.pkl",
        "requirements.txt",
        "CustomerChurnOneHotEncoder.pkl",
    ],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "u29",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_89caab6f_9738_4a08_9205_19edf4ead6ab.image_pull_policy = "IfNotPresent"

(
    notebook_op_89caab6f_9738_4a08_9205_19edf4ead6ab
    << notebook_op_94ce2428_d9d1_4824_8c17_0b50ed1063f3
)


notebook_op_f623f6a5_fd57_47fd_8b64_c0032ca9ac15 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="ml-workshop-improved/airflow/deploy_model/ocp/deploy-model.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="ocp_deploy_2-0617075716",
    cos_dependencies_archive="deploy-model-f623f6a5-fd57-47fd-8b64-c0032ca9ac15.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[
        "CustomerChurnOrdinalEncoder.pkl",
        "model.pkl",
        "requirements.txt",
        "CustomerChurnOneHotEncoder.pkl",
    ],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "u29",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_f623f6a5_fd57_47fd_8b64_c0032ca9ac15.image_pull_policy = "IfNotPresent"

(
    notebook_op_f623f6a5_fd57_47fd_8b64_c0032ca9ac15
    << notebook_op_89caab6f_9738_4a08_9205_19edf4ead6ab
)
