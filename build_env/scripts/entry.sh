#!/bin/bash
set -x
set -e
#cp -r /build /build_copy
chown builder -R /build
cd /build/src
su builder -c "python3 build_n_install_in_order.py order"
cd /build/built_pkgs
#./collect.sh
#rm -rf /output/*
#cp -r /build_copy /output/
