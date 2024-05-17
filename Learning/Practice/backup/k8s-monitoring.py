#

import kubernetes
import time
import logging
import json
import os
from kubernetes.client import (
    CoreV1Api,
    AppsV1Api,
    BatchV1Api,
    NetworkingV1Api,
    CustomObjectsApi,
)

logging.basicConfig(level=logging.INFO)


def get_k8s_api_client():
    config.load_kube_config()
    return kubernetes.client.ApiClient()


def get_pod_list(api_client):
    v1 = CoreV1Api(api_client)
    return v1.list_namespaced_pod("default")


def get_service_list(api_client):
    v1 = CoreV1Api(api_client)
    return v1.list_namespaced_service("default")


def get_deployment_list(api_client):
    apps = AppsV1Api(api_client)
    return apps.list_namespaced_deployment("default")


def get_pod_status(api_client, pod_name):
    v1 = CoreV1Api(api_client)
    pod = v1.read_namespaced_pod(pod_name, "default")
    return pod.status.phase


def get_service_status(api_client, service_name):
    v1 = CoreV1Api(api_client)
    service = v1.read_namespaced_service(service_name, "default")
    return service.status.load_balancer.ingress


def get_deployment_status(api_client, deployment_name):
    apps = AppsV1Api(api_client)
    deployment = apps.read_namespaced_deployment(deployment_name, "default")
    return deployment.status.replicas, deployment.status.available_replicas


def write_to_log_file(log_message, log_file_path):
    with open(log_file_path, "a") as f:
        f.write(log_message + "\n")


def monitor_k8s_cluster():
    api_client = get_k8s_api_client()
    log_file_path = "k8s_monitor.log"
    log_file_count = 1
    while True:
        time.sleep(60)
        pod_list = get_pod_list(api_client)
        service_list = get_service_list(api_client)
        deployment_list = get_deployment_list(api_client)
        for pod in pod_list.items:
            if pod.status.phase != "Running":
                log_message = f"Pod {pod.metadata.name} is not running"
                write_to_log_file(log_message, log_file_path)
        for service in service_list.items:
            if not service.status.load_balancer.ingress:
                log_message = f"Service {service.metadata.name} is not accessible"
                write_to_log_file(log_message, log_file_path)
        for deployment in deployment_list.items:
            replicas, available_replicas = get_deployment_status(
                api_client, deployment.metadata.name
            )
            if replicas != available_replicas:
                log_message = f"Deployment {deployment.metadata.name} is not in sync"
                write_to_log_file(log_message, log_file_path)
        print("Monitoring completed")
        # Check if log file size is over 5MB
        if os.path.getsize(log_file_path) > 5 * 1024 * 1024:
            # Rename log file and increment log file count
            file_name, file_ext = os.path.splitext(log_file_path)
            new_log_file_path = file_name + f"_{log_file_count}" + file_ext
            os.rename(log_file_path, new_log_file_path)
            log_file_path = new_log_file_path
            log_file_count += 1
            # Clear previous log file
            with open(log_file_path, "w") as f:
                f.write("")


if __name__ == "__main__":
    monitor_k8s_cluster()


# 打开“任务计划程序”（可以通过搜索框查找“任务计划程序”）。
# 在左侧面板中，右键单击“创建基本任务”。
# 输入任务名称和描述，然后单击“下一步”。
# 选择“创建基本任务”选项，单击“下一步”。
# 在“操作”部分，选择“启动程序”。
# 在“程序或脚本”中输入Python解释器的路径（例如，“C:\Python38\python.exe”），然后在“添加参数”中输入监控脚本的完整路径（例如，“C:\Monitor\monitor_k8s_cluster.py”）。
# 单击“下一步”并选择“立即开始”，然后单击“完成”。
