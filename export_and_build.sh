#!/bin/sh

set -e  # make sure to abort on error
set -x  # echo commands


mkdir -p build
mkdir -p build/sources/fontra
mkdir -p build/sources/ufo
mkdir -p build/fonts/otf-varc
mkdir -p build/fonts/ttf-varc
mkdir -p build/fonts/otf
mkdir -p build/fonts/ttf

fontra-copy notosanscjksc.rcjk build/sources/fontra/notosanscjksc.fontra
fontra-copy notoserifcjkjp.rcjk build/sources/fontra/notoserifcjkjp.fontra

fontra-copy notosanscjksc.rcjk build/sources/ufo/notosanscjksc.designspace
fontra-copy notoserifcjkjp.rcjk build/sources/ufo/notoserifcjkjp.designspace

fontra-workflow notosanscjksc.yaml --output-dir build/fonts --continue-on-error
fontra-workflow notoserifcjkjp.yaml --output-dir build/fonts --continue-on-error
