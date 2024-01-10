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

    for name in unicode_names:
        glyph = await font.getGlyph(name)
        status = None
        if glyph.sources:
            status = glyph.sources[0].customData["fontra.development.status"]

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

    print(len(fully_made_of_components), "fully_made_of_components", "".join([chr(int(x[3:],16)) for x in sorted(list(fully_made_of_components))]))
    print(len(mix_contours_components), "mix_contours_components", "".join([chr(int(x[3:],16)) for x in sorted(list(mix_contours_components))]))
    print(len(fully_made_of_contours), "fully_made_of_contours", "".join([chr(int(x[3:],16)) for x in sorted(list(fully_made_of_contours))]))
    print(len(empty), "empty", "".join([chr(int(x[3:],16)) for x in sorted(list(empty))]))

    print("total unicode names", len(fully_made_of_components)+len(mix_contours_components)+len(fully_made_of_contours)+len(empty))
    


if __name__ == "__main__":
    path = "notoserifcjkjp.rcjk"
    asyncio.run(main(path))
