import asyncio
import pathlib
import csv
from datetime import datetime

from fontra.backends import getFileSystemBackend


async def main(path):
    font = getFileSystemBackend(path)
    glyphMap = await font.getGlyphMap()

    unicode_names = [x for x in glyphMap if x.startswith("uni")]

    fully_made_of_components = set()
    mix_contours_components = set()
    fully_made_of_contours = set()
    empty_glyphs = set()

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
                empty_glyphs.add(name)

    return dict(
        green_glyphs=green_glyphs,
        blue_glyphs=blue_glyphs,
        yellow_glyphs=yellow_glyphs,
        orange_glyphs=orange_glyphs,
        red_glyphs=red_glyphs,
        fully_made_of_components=fully_made_of_components,
        mix_contours_components=mix_contours_components,
        fully_made_of_contours=fully_made_of_contours,
        empty_glyphs=empty_glyphs,
    )


def export_csv_characters_colors_evolution(report, reportDir, project_name):
    evolution_character_glyphs_color_path = (
        reportDir / f"{project_name}_evolution_character_glyphs.csv"
    )

    fieldnames = ["dates", "red", "orange", "yellow", "blue", "green"]
    row = {
        "dates": str(datetime.now()).split(" ")[0],
        "red": len(report["red_glyphs"]),
        "orange": len(report["orange_glyphs"]),
        "yellow": len(report["yellow_glyphs"]),
        "blue": len(report["blue_glyphs"]),
        "green": len(report["green_glyphs"]),
    }
    # create a CSV file if it does not already exist
    if not evolution_character_glyphs_color_path.is_file():
        with open(evolution_character_glyphs_color_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(row)
    else:
        with open(
            evolution_character_glyphs_color_path, "r", encoding="utf-8"
        ) as csvfile:
            txt = csvfile.readlines()
            # looking for the latest stored date, to avoid restore it
            latest_date = txt[-1].strip().split("\r")[0].split(",")[0]

        with open(evolution_character_glyphs_color_path, "a", newline="") as csvfile:
            if latest_date != str(datetime.now()).split(" ")[0]:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(row)


def _glyphnames_to_chars(glyphnames_list):
    return "".join([chr(int(x[3:], 16)) for x in sorted(list(glyphnames_list))])


def export_txt_report_file(report, reportDir, project_name):
    evolution_character_glyphs_color_path = (
        reportDir / f"{project_name}_evolution_character_glyphs.txt"
    )

    txt = "COLORS\n\n\n"
    txt += f"{len(report['green_glyphs'])} green glyphs\n"
    txt += f"{_glyphnames_to_chars(report['green_glyphs'])}\n\n"
    txt += f"{len(report['blue_glyphs'])} blue glyphs\n"
    txt += f"{_glyphnames_to_chars(report['blue_glyphs'])}\n\n"
    txt += f"{len(report['yellow_glyphs'])} yellow glyphs\n"
    txt += f"{_glyphnames_to_chars(report['yellow_glyphs'])}\n\n"
    txt += f"{len(report['orange_glyphs'])} orange glyphs\n"
    txt += f"{_glyphnames_to_chars(report['orange_glyphs'])}\n\n"
    txt += f"{len(report['red_glyphs'])} red glyphs\n"
    txt += f"{_glyphnames_to_chars(report['red_glyphs'])}\n\n\n"
    txt += "STRUCTURES\n\n\n"
    txt += f"{len(report['fully_made_of_components'])} fully made of components\n"
    txt += f"{_glyphnames_to_chars(report['fully_made_of_components'])}\n\n"
    txt += f"{len(report['mix_contours_components'])} mix contours / components\n"
    txt += f"{_glyphnames_to_chars(report['mix_contours_components'])}\n\n"
    txt += f"{len(report['fully_made_of_contours'])} fully made of contours\n"
    txt += f"{_glyphnames_to_chars(report['fully_made_of_contours'])}\n\n"
    txt += f"{len(report['empty_glyphs'])} empty glyphs\n"
    txt += f"{_glyphnames_to_chars(report['empty_glyphs'])}\n\n"

    with open(evolution_character_glyphs_color_path, "w", encoding="utf-8") as file:
        file.write(txt)


if __name__ == "__main__":
    prooferDir = pathlib.Path(__file__).resolve().parent
    repoDir = prooferDir.parent
    reportDir = repoDir / "scripts" / "resources"
    reportDir.mkdir(parents=True, exist_ok=True)

    projects_names = ["notoserifcjkjp", "notosanscjksc"]

    for project_name in projects_names:
        path = f"{project_name}.rcjk"

        report = asyncio.run(main(path))

        export_csv_characters_colors_evolution(report, reportDir, project_name)

        export_txt_report_file(report, reportDir, project_name)
