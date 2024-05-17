import logging
import os
from datetime import datetime, timedelta
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from prometheus_client import start_http_server, Summary
from threading import Thread
from typing import List
from urllib.parse import urlparse


# 记录错误并将其写入日志文件中
def write_to_log_file(log_message: str, log_file_path: str):
    # 创建一个日志记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file_path)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(log_message)


# 定义用于监控Kubernetes集群的函数
def monitor_k8s_cluster(api_client: client.CoreV1Api, log_file_path: str):
    # 创建一个用于记录监控时间的Summary对象
    monitor_time = Summary(
        "monitor_k8s_cluster_seconds", "Time spent monitoring the K8s cluster"
    )
    # 定义用于监控的Pod对象列表
    monitored_pods: List[client.V1Pod] = []
    # 获取当前时间
    start_time = datetime.now()
    # 获取Pods列表
    try:
        monitored_pods = api_client.list_namespaced_pod("default", watch=False).items
    except ApiException as e:
        write_to_log_file(f"Error occurred while retrieving pods: {e}", log_file_path)
        return
    # 检查Pods状态
    for pod in monitored_pods:
        if pod.status.phase == "Running":
            write_to_log_file(f"Pod {pod.metadata.name} is Running", log_file_path)
        else:
            write_to_log_file(f"Pod {pod.metadata.name} is not Running", log_file_path)
    # 计算监控时间
    end_time = datetime.now()
    monitor_time.observe((end_time - start_time).total_seconds())
    # 检查日志文件大小
    if os.path.getsize(log_file_path) > 5 * 1024 * 1024:
        # 清空日志文件
        with open(log_file_path, "w") as f:
            f.write("")
        # 重命名日志文件
        file_name, file_ext = os.path.splitext(log_file_path)
        new_log_file_path = file_name + "_new" + file_ext
        os.rename(log_file_path, new_log_file_path)
        log_file_path = new_log_file_path


# 定义用于启动监控脚本的函数
def start_monitoring_kubernetes_cluster(
    api_client: client.CoreV1Api, log_file_path: str
):
    # 开启监控脚本
    monitor_thread = Thread(
        target=monitor_k8s_cluster, args=(api_client, log_file_path)
    )
    monitor_thread.start()
    monitor_thread.join()


# 定义用于获取Kubernetes API客户端的函数
def get_k8s_api_client():
    # 获取Kubernetes API客户端
    config.load_kube_config()
    api_client = client.CoreV1Api()
    return api_client


# 定义用于启动监控脚本的函数
def start_k8s_monitoring():
    # 获取Kubernetes API客户端
    api_client = get_k8s_api_client()
    # 创建一个日志文件路径
    log_file_path = "k8s_monitor.log"
    # 定义监控脚本的运行频率
    monitor_frequency = timedelta(minutes=2)
    # 定义监控脚本的运行周期
    monitor_cycle = timedelta(minutes=1)
    # 开始监控脚本
    while True:
        # 开始监控
        start_monitoring_kubernetes_cluster(api_client, log_file_path)
        # 等待一段时间继续监控
        time.sleep(monitor_frequency.total_seconds())


# 定义主函数
def main():
    # 启动监控脚本
    start_k8s_monitoring()


# 运行主函数
if __name__ == "__main__":
    main()
