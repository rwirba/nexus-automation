# Base image with required tools
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    curl jq unzip \
    bash git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Nexus CLI (nexus3-cli)
RUN pip3 install nexus3-cli requests

# Set working directory
WORKDIR /workspace

# Default command (Harness will override)
CMD ["/bin/bash"]
