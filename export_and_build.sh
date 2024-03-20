#!/bin/sh

set -e  # make sure to abort on error
set -x  # echo commands


mkdir -p build
mkdir -p build/fontra
mkdir -p build/ufo
mkdir -p build/glyf-1
mkdir -p build/ttf

fontra-copy notosanscjksc.rcjk build/fontra/notosanscjksc.fontra
fontra-copy notoserifcjkjp.rcjk build/fontra/notoserifcjkjp.fontra

fontra-copy notosanscjksc.rcjk build/ufo/notosanscjksc.designspace
fontra-copy notoserifcjkjp.rcjk build/ufo/notoserifcjkjp.designspace

fontra-compile notosanscjksc.rcjk build/glyf-1/notosanscjksc-glyf1.ttf
fontra-compile notoserifcjkjp.rcjk build/glyf-1/notoserifcjkjp-glyf1.ttf

# fontra-workflow notosanscjksc.yaml --output-dir build/ttf
fontra-workflow notoserifcjkjp.yaml --output-dir build/ttf
