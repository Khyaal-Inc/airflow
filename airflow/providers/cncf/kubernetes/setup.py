# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_namespace_packages

setup(
    name="apache-airflow-providers-cncf-kubernetes",
    version="8.3.1.post1+khyaal",
    description="Apache Airflow Providers for CNCF Kubernetes (Khyaal custom build)",
    packages=find_namespace_packages(where="../../../..", include=["airflow.providers.cncf.kubernetes*"]),
    package_dir={"": "../../../.."},
    include_package_data=True,
    install_requires=[
        "aiofiles>=23.2.0",
        "apache-airflow>=2.7.0",
        "asgiref>=3.5.2",
        "cryptography>=41.0.0",
        "kubernetes>=28.1.0,<=29.0.0",
        "kubernetes_asyncio>=28.1.0,<=29.0.0",
    ],
    entry_points={
        "apache_airflow_provider": [
            "provider_info=airflow.providers.cncf.kubernetes:get_provider_info",
        ],
    },
    python_requires="~=3.8",
    zip_safe=False,
)
