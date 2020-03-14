#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"
find ../src -iname '*.pkg.tar.xz' -exec mv '{}' . \;

