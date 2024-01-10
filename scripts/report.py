import asyncio

from fontra.backends import getFileSystemBackend


async def main(path):
    font = getFileSystemBackend(path)
    glyphMap = await font.getGlyphMap()

    unicode_names = [x for x in glyphMap if x.startswith("uni")]

    fully_made_of_components = set()
    mix_contours_components = set()
    fully_made_of_contours = set()
    empty = set()

    green_glyphs = set()
    blue_glyphs = set()
    yellow_glyphs = set()
    orange_glyphs = set()
    red_glyphs = set()

    for name in unicode_names:
        glyph = await font.getGlyph(name)
        status = None
        if glyph.sources:
            status = glyph.sources[0].customData["fontra.development.status"]
        if status == 4:
            green_glyphs.add(name)
        elif status == 3:
            blue_glyphs.add(name)
        elif status == 2:
            yellow_glyphs.add(name)
        elif status == 1:
            orange_glyphs.add(name)
        else:
            red_glyphs.add(name)

        for layer_name, layer_infos in glyph.layers.items():
            components = layer_infos.glyph.components
            contours_coords = layer_infos.glyph.path.coordinates
            if not contours_coords and components:
                fully_made_of_components.add(name)
            elif contours_coords and components:
                mix_contours_components.add(name)
            elif contours_coords and not components:
                fully_made_of_contours.add(name)
            else:
                empty.add(name)


    print(len(green_glyphs), "green_glyphs", "".join([chr(int(x[3:],16)) for x in sorted(list(green_glyphs))]), '\n')
    print(len(blue_glyphs), "blue_glyphs", "".join([chr(int(x[3:],16)) for x in sorted(list(blue_glyphs))]), '\n')
    print(len(yellow_glyphs), "yellow_glyphs", "".join([chr(int(x[3:],16)) for x in sorted(list(yellow_glyphs))]), '\n')
    print(len(orange_glyphs), "orange_glyphs", "".join([chr(int(x[3:],16)) for x in sorted(list(orange_glyphs))]), '\n')
    print(len(red_glyphs), "red_glyphs", "".join([chr(int(x[3:],16)) for x in sorted(list(red_glyphs))]), '\n')
    print("---\n")
    print(len(fully_made_of_components), "fully_made_of_components", "".join([chr(int(x[3:],16)) for x in sorted(list(fully_made_of_components))]), '\n')
    print(len(mix_contours_components), "mix_contours_components", "".join([chr(int(x[3:],16)) for x in sorted(list(mix_contours_components))]), '\n')
    print(len(fully_made_of_contours), "fully_made_of_contours", "".join([chr(int(x[3:],16)) for x in sorted(list(fully_made_of_contours))]), '\n')
    print(len(empty), "empty", "".join([chr(int(x[3:],16)) for x in sorted(list(empty))]), '\n')

    print("total unicode names", len(fully_made_of_components)+len(mix_contours_components)+len(fully_made_of_contours)+len(empty))
    


if __name__ == "__main__":
    path = "notoserifcjkjp.rcjk"
    asyncio.run(main(path))
