# setup.py
from setuptools import setup, find_packages

setup(
    name="dooray-api-client",  # 패키지 이름
    version="0.1.0",  # 버전 번호
    packages=find_packages(),  # 자동으로 서브패키지 포함
    install_requires=[  # 의존성 라이브러리
        "requests>=2.25.1",
    ],
    author="Mr21percent",
    author_email="mr21percent@gmail.com",
    description="A Python client for interacting with Dooray! API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dooray-api-client",  # GitHub에서 호스팅되는 주소
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 지원하는 Python 버전
)
