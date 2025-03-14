# Base image with required tools
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl jq unzip \
    bash git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a virtual environment and install Python packages
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install nexus3-cli requests

# Set the virtual environment as default
ENV PATH="/opt/venv/bin:$PATH"
# Install Nexus CLI (nexus3-cli)
RUN pip3 install nexus3-cli requests

# Set working directory
WORKDIR /workspace

# Default command (Harness will override)
CMD ["/bin/bash"]
