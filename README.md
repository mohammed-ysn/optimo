# Optimo

## Prerequisites

Before getting started, make you have the following installed on your machine:

- g++ or clang++
- python3 (recommended version 3.12)
- CMake
- Ccache (optional but recommended for faster builds)

## Setup

1. Clone the repository and navigate to the root directory

```bash
git clone https://github.com/mohammed-ysn/optimo.git
cd optimo
```

2. Install Python dependencies (it is recommended to use a virtual environment)

```bash
pip install -r requirements.txt
```

3. Download and extract [ns-3 version 3.40](https://www.nsnam.org/releases/ns-3-40/)

```bash
wget https://www.nsnam.org/releases/ns-allinone-3.40.tar.bz2
tar xfj ns-allinone-3.40.tar.bz2
```

4. Navigate to the `ns-3.40` directory and configure the build

```bash
cd ns-allinone-3.40/ns-3.40
./ns3 configure --enable-examples --enable-tests
```

5. Build the project

```bash
./ns3 build
```
