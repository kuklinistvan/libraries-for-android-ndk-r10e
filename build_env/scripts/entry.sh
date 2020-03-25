#!/bin/bash
set -x
set -e
cp -r /build /build_copy
chown builder -R /build_copy
cd /build_copy/src
su builder -c python3 build_n_install_in_order.py order
cd /build_copy/built_pkgs
./collect.sh
cp -r /build_copy /output/
