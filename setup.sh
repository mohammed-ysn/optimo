#!/bin/bash

# Define variables
NS_VERSION="3.40"
NS_ARCHIVE="ns-allinone-$NS_VERSION.tar.bz2"
NS_DIR="ns-allinone-$NS_VERSION"

# ANSI escape codes for colours
GREEN='\033[1;32m' # Bold Green
RED='\033[1;31m'   # Bold Red
NC='\033[0m'       # No Colour

# Step 1: Download and extract ns-3 version 3.40
printf "${GREEN}Step 1: Downloading ns-3 version $NS_VERSION...${NC}\n"
if [ ! -f "$NS_ARCHIVE" ]; then
    wget "https://www.nsnam.org/releases/$NS_ARCHIVE" || { printf "${RED}Error: Failed to download $NS_ARCHIVE${NC}\n"; exit 1; }
fi

printf "${GREEN}Extracting $NS_ARCHIVE...${NC}\n"
if [ ! -d "$NS_DIR" ]; then
    tar xfj "$NS_ARCHIVE" || { printf "${RED}Error: Failed to extract $NS_ARCHIVE${NC}\n"; exit 1; }
fi

# Step 2: Navigate to the ns-3.40 directory and configure the build
printf "${GREEN}Step 2: Navigating to $NS_DIR directory...${NC}\n"
cd "$NS_DIR/ns-$NS_VERSION" || { printf "${RED}Error: Failed to navigate to $NS_DIR${NC}\n"; exit 1; }

printf "${GREEN}Step 3: Configuring the build...${NC}\n"
./ns3 configure --enable-examples --enable-tests || { printf "${RED}Error: Failed to configure the build${NC}\n"; exit 1; }

# Step 3: Build the project
printf "${GREEN}Step 4: Building the project...${NC}\n"
./ns3 || { printf "${RED}Error: Failed to build the project${NC}\n"; exit 1; }

printf "${GREEN}Process completed successfully!${NC}\n"
