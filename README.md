# noto-cjk-varco

Initial sources origin: https://github.com/notofonts/noto-cjk

This repository is meant to demonstrate the usage of Variable Components as a design tool, with Fontra as source editor in CJK fonts.

https://fontra.xyz

There are 2 subsets of the typefaces `Noto Sans CJK SC` and `Noto Serif CJK JP`.

The goal is to make 2 fonts with 1000 Character Glyphs each using the minimal quantity of Variable Components (details in the .txt files).

We notice significant binary font file size savings (currently based on the `glyf v1` implementation):

- Noto Serif JP: 60,9% of file size savings
  - VarCo VF: 276 kb
  - Trad VF: 706 kb

- Noto Sans SC: 39,6% of file size savings
  - VarCo VF: 194 kb
  - Trad VF: 321 kb
    
## Variable Component Design and Precision

https://github.com/notofonts/noto-cjk-varco/assets/13123463/b9b41496-310e-4178-a88b-e854589c912b

The goal is to remaster the Noto CJK fonts truthfully to the original typeface design, but not to match 100%. In addition, designing with Variable Components may level up the overall glyph consistency throughout the typeface.
The images below illustrate to fact that we do not try to match pixel perfect the original, it is a remastering of the typeface that is true to the original design while being more consistent over all radicals usage.

![900](https://github.com/notofonts/noto-cjk-varco/assets/13123463/143eb6c2-30f2-448a-a20d-a2bf0e576ff7)
![200](https://github.com/notofonts/noto-cjk-varco/assets/13123463/6b250302-20d2-4dfe-bd29-7eed37c3cc5f)

