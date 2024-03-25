#!/bin/bash

# Define variables
NS_VERSION="3.40"
NS_ARCHIVE="ns-allinone-$NS_VERSION.tar.bz2"
NS_DIR="ns-allinone-$NS_VERSION"

# ANSI escape codes for colours
GREEN='\033[1;32m'  # Bold Green
RED='\033[1;31m'    # Bold Red
ORANGE='\033[1;33m' # Bold Orange
NC='\033[0m'        # No Colour

# Define function to print with prefix
print_step() {
    local prefix="${ORANGE}[OPTIMO SETUP $1/$2]${NC}"
    local message="$3"
    printf "${prefix} ${GREEN}${message}${NC}\n"
}

# Define function to print error messages
print_error() {
    local prefix="${ORANGE}[OPTIMO SETUP $1/$2]${NC}"
    local message="$3"
    printf "${prefix} ${RED}${message}${NC}\n" >&2
}

print_step 1 5 "Downloading ns-3 version $NS_VERSION..."
if [ ! -f "$NS_ARCHIVE" ]; then
    wget "https://www.nsnam.org/releases/$NS_ARCHIVE" || { print_error 1 5 "Error: Failed to download $NS_ARCHIVE"; exit 1; }
fi

print_step 2 5 "Extracting $NS_ARCHIVE..."
if [ ! -d "$NS_DIR" ]; then
    tar xfj "$NS_ARCHIVE" || { print_error 2 5 "Error: Failed to extract $NS_ARCHIVE"; exit 1; }
fi

print_step 3 5 "Navigating to $NS_DIR directory..."
cd "$NS_DIR/ns-$NS_VERSION" || { print_error 3 5 "Error: Failed to navigate to $NS_DIR"; exit 1; }

print_step 4 5 "Configuring the build..."
./ns3 configure --enable-examples --enable-tests || { print_error 4 5 "Error: Failed to configure the build"; exit 1; }

print_step 5 5 "Building the project..."
./ns3 || { print_error 5 5 "Error: Failed to build the project"; exit 1; }

printf "${ORANGE}[OPTIMO SETUP]${NC} ${GREEN}Setup completed successfully!${NC}\n"
