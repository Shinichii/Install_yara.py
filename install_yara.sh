#!/bin/bash

VERSION="3.7.0"
YARA_VERSION="yara-$VERSION"

apt-get install automake libtool make gcc libssl-dev python-pip
wget -q "https://github.com/VirusTotal/yara/archive/v$VERSION.tar.gz"
tar -xzf v$VERSION.tar.gz
pip install yara-python
cd $YARA_VERSION
./bootstrap.sh
./configure
make
make install
make check
echo "Verification, you should see dummy my_first_rule appear"
echo "rule dummy { condition:true }" > my_first_rule
yara ./my_first_rule ./my_first_rule
