import kafka
import json
import time
from datetime import datetime

# 创建Kafka客户端实例，连接到Kafka集群
def create_kafka_client(username, password, ssl_truststore_location, ssl_truststore_type, ssl_truststore_password, ssl_endpoint_identification_algorithm, sasl_jaas_config):
    return kafka.KafkaProducer(bootstrap_servers='localhost:9092', security_protocol='SASL_SSL', ssl_context='adhoc', sasl_mechanism='PLAIN', sasl_plain_username=username, sasl_plain_password=password, ssl_truststore_location=ssl_truststore_location, ssl_truststore_type=ssl_truststore_type, ssl_truststore_password=ssl_truststore_password, ssl_endpoint_identification_algorithm=ssl_endpoint_identification_algorithm, sasl_jaas_config=sasl_jaas_config)

# 定义主题名称生成器函数
def topic_name_generator(name):
    return f"{name}_data"
# 创建文件，用于存储最近传输的数据
data_file = "data.txt"
# 创建文件，用于存储异常日志
error_file = "error.log"
# 定义获取所有包含某个字符串的topic列表的函数
def get_topics_with_string(username, password, string):
    client = create_kafka_client(username, password)
    topic_names = []
    for topic in client.topics():
        if string in topic:
            topic_names.append(topic)
    return topic_names
if __name__ == '__main__':
    # 获取所有包含字符串'test'的topic列表
    topic_names = get_topics_with_string('user', 'password', 'test')
    # 遍历所有主题并获取状态信息
    for topic_name in topic_names:
        # 获取主题的状态信息
        client = create_kafka_client('user', 'password', './confluent-truststore.jks', 'JKS', 'confluenttruststorepass', 'https', 'org.apache.kafka.common.security.plain.PlainLoginModule required username="vsXXXX" password="XXXXX";')
        topic = client.topics()
        for topic_info in topic:
            if topic_info == topic_name:
                # 写入数据文件
                data = client.send(topic_name, json.dumps({"name": topic_name, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})).get()
                with open(data_file, "a") as f:
                    f.write(f"{data.payload.decode()}
)
                # 如果状态为异常，写入异常日志文件
                if topic_info not in topic:
                    with open(error_file, "a") as f:
                        f.write(f"{topic_info} is not defined
")
        # 检查Kafka集群的状态
        if client.cluster:
            print(f"{topic_name} is online")
        else:
            print(f"{topic_name} is offline")
        # 等待一段时间后再次检查主题状态
        time.sleep(10)

