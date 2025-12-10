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

from setuptools import setup
import os
from pathlib import Path

# Get the absolute path to the repo root (4 levels up from this setup.py)
repo_root = Path(__file__).parent.parent.parent.parent.parent.resolve()

# Manually discover all packages under airflow.providers.cncf.kubernetes
def find_packages():
    """Find all namespace packages manually."""
    packages = []
    base_path = repo_root / "airflow" / "providers" / "cncf" / "kubernetes"

    for root, dirs, files in os.walk(base_path):
        # Skip venv and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('venv')]

        if '__init__.py' in files:
            # Convert path to package name
            rel_path = Path(root).relative_to(repo_root)
            package = str(rel_path).replace(os.sep, '.')
            packages.append(package)

    return packages

setup(
    name="apache-airflow-providers-cncf-kubernetes",
    version="8.3.1.post1+khyaal",
    description="Apache Airflow Providers for CNCF Kubernetes (Khyaal custom build)",
    packages=find_packages(),
    package_dir={"": str(repo_root)},
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
