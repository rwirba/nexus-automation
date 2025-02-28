#!/bin/bash

set -e

NEXUS_URL="http://nexus.kihhuf.org:8081/repository/infra"
SOURCE_FILE="sources.json"

mkdir -p downloads

# Read sources.json to get download URLs
for os_type in $(jq -r 'keys[]' $SOURCE_FILE); do
    for app in $(jq -r ".[\"$os_type\"] | keys[]" $SOURCE_FILE); do
        URL=$(jq -r ".[\"$os_type\"][\"$app\"]" $SOURCE_FILE)
        VERSION=$(cat "new_versions/${app}_latest.txt")

        if [ -n "$VERSION" ]; then
            echo "Downloading $app version $VERSION..."
            curl -L "$URL" -o "downloads/${app}-${VERSION}.tar.gz"
        fi
    done
done
