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
    local prefix="${ORANGE}[OPTIMO SETUP]${NC}"
    local message="$1"
    printf "${prefix} ${GREEN}${message}${NC}\n"
}

# Define function to print error messages
print_error() {
    local prefix="${ORANGE}[OPTIMO SETUP]${NC}"
    local message="$1"
    printf "${prefix} ${RED}${message}${NC}\n" >&2
}

# Check if ns3 folder exists
if [ ! -d "$NS_DIR" ]; then
    print_step "Downloading ns-3 version $NS_VERSION..."
    # Check if archive file exists
    if [ ! -f "$NS_ARCHIVE" ]; then
        wget "https://www.nsnam.org/releases/$NS_ARCHIVE" || { print_error "Error: Failed to download $NS_ARCHIVE"; exit 1; }
    fi
    print_step "Extracting $NS_ARCHIVE..."
    tar xfj "$NS_ARCHIVE" || { print_error "Error: Failed to extract $NS_ARCHIVE"; exit 1; }
    rm "$NS_ARCHIVE"
fi

print_step "Navigating to $NS_DIR directory..."
cd "$NS_DIR/ns-$NS_VERSION" || { print_error "Error: Failed to navigate to $NS_DIR"; exit 1; }

print_step "Configuring the build..."
./ns3 configure --enable-examples --enable-tests || { print_error "Error: Failed to configure the build"; exit 1; }

print_step "Building the project..."
./ns3 || { print_error "Error: Failed to build the project"; exit 1; }

printf "${ORANGE}[OPTIMO SETUP]${NC} ${GREEN}Setup completed successfully!${NC}\n"
