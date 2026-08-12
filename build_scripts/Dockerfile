# Use Python 3.12 as base image from Aliyun mirror
FROM luochen2025/dataengineer-agent:0.1.5a4

RUN pip uninstall -y dataengineer-agent

RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dataengineer-agent==0.1.8


WORKDIR /app

# Keep the container running
CMD ["tail", "-f", "/dev/null"]


