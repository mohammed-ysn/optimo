#!/bin/bash

NS_VERSION="3.40"
NS_ARCHIVE="ns-allinone-$NS_VERSION.tar.bz2"
NS_DIR="ns-allinone-$NS_VERSION"

# Step 1: Download and extract ns-3 version 3.40
echo "Step 1: Downloading ns-3 version $NS_VERSION..."
if [ ! -f "$NS_ARCHIVE" ]; then
    wget "https://www.nsnam.org/releases/$NS_ARCHIVE" || { echo "Error: Failed to download $NS_ARCHIVE"; exit 1; }
fi

echo "Extracting $NS_ARCHIVE..."
if [ ! -d "$NS_DIR" ]; then
    tar xfj "$NS_ARCHIVE" || { echo "Error: Failed to extract $NS_ARCHIVE"; exit 1; }
fi

# Step 2: Navigate to the ns-3.40 directory and configure the build
echo "Step 2: Navigating to $NS_DIR directory..."
cd "$NS_DIR/ns-$NS_VERSION" || { echo "Error: Failed to navigate to $NS_DIR"; exit 1; }

echo "Step 3: Configuring the build..."
./ns3 configure --enable-examples --enable-tests || { echo "Error: Failed to configure the build"; exit 1; }

# Step 3: Build the project
echo "Step 4: Building the project..."
./ns3 || { echo "Error: Failed to build the project"; exit 1; }

echo "Process completed successfully!"
