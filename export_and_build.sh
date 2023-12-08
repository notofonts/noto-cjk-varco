#!/bin/sh

set -e  # make sure to abort on error
set -x  # echo commands


mkdir -p build
mkdir -p build/fontra
mkdir -p build/fonts

fontra-copy notosanscjksc.rcjk build/fontra/notosanscjksc.fontra
fontra-copy notoserifcjkjp.rcjk build/fontra/notoserifcjkjp.fontra

fontra-compile notosanscjksc.rcjk build/fonts/notosanscjksc-glyf1.ttf
fontra-compile notoserifcjkjp.rcjk build/fonts/notoserifcjkjp-glyf1.ttf
