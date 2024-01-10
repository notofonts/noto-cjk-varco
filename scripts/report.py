import asyncio

from fontra.backends import getFileSystemBackend


async def main(path):
    font = getFileSystemBackend(path)
    glyphMap = await font.getGlyphMap()

    unicode_names = [x for x in glyphMap if x.startswith("uni")]

    fully_made_of_components = []
    mix_contours_components = []
    fully_made_of_contours = []
    empty = []

    for name in unicode_names:
        glyph = await font.getGlyph(name)
        status = None
        if glyph.sources:
            status = glyph.sources[0].customData["fontra.development.status"]

        for layer_name, layer_infos in glyph.layers.items():
            components = layer_infos.glyph.components
            contours_coords = layer_infos.glyph.path.coordinates
            if not contours_coords and components:
                fully_made_of_components.append(name)
            elif contours_coords and components:
                mix_contours_components.append(name)
            elif contours_coords and not components:
                fully_made_of_contours.append(name)
            else:
                empty.append(name)

    print("fully_made_of_components", fully_made_of_components)
    print("mix_contours_components", mix_contours_components)
    print("fully_made_of_contours", fully_made_of_contours)
    print("empty", empty)


if __name__ == "__main__":
    path = "notoserifcjkjp.rcjk"
    asyncio.run(main(path))
