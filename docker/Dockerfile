# The image every Prometheus pool's check runs in: Python and the pinned dependencies, installed
# into the image's own site-packages, outside /work. Thinkpool mounts the contribution's copy at /work,
# read-write, with a read-only root, so nothing in /work can replace what is installed here.
FROM python:3.12.11-slim
RUN pip install --no-cache-dir sympy==1.14.0 python-flint==0.9.0 numpy==2.3.4 pytest==8.4.2 \
 && useradd -m -u 1000 checker
USER 1000:1000
