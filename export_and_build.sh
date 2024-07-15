#!/bin/sh

set -e  # make sure to abort on error
set -x  # echo commands


mkdir -p build
mkdir -p build/fontra
mkdir -p build/ufo
mkdir -p build/otf-varco
mkdir -p build/ttf-varco
mkdir -p build/otf
mkdir -p build/ttf

fontra-copy notosanscjksc.rcjk build/fontra/notosanscjksc.fontra
fontra-copy notoserifcjkjp.rcjk build/fontra/notoserifcjkjp.fontra

fontra-copy notosanscjksc.rcjk build/ufo/notosanscjksc.designspace
fontra-copy notoserifcjkjp.rcjk build/ufo/notoserifcjkjp.designspace

fontra-workflow notosanscjksc.yaml --output-dir build --continue-on-error
fontra-workflow notoserifcjkjp.yaml --output-dir build --continue-on-error
