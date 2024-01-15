import pathlib
from collections import defaultdict
from drawbot_skia.drawbot import *

RED_COLOR = (1, 0, 0, 1)
ORANGE_COLOR = (1, 0.5, 0, 1)
YELLOW_COLOR = (1, 1, 0, 1)
BLUE_COLOR = (0, 0.5, 1, 1)
GREEN_COLOR = (0, 1, 0.5, 1)


def make_page(text_infos, number_of_days_untile_deadline, number_of_glyphs, ends_date, title):
    dates = []
    reds = []
    oranges = []
    yellows = []
    blues = []
    greens = []

    for l in text_infos:
        date, red, orange, yellow, blue, green = l.strip().split(",")
        dates.append(date)
        reds.append(int(red))
        oranges.append(int(orange))
        yellows.append(int(yellow))
        blues.append(int(blue))
        greens.append(int(green))

    number_of_days = len(dates)

    pageWidth = 842
    pageHeight = 595
    margin = 50

    if number_of_days > 1:

        reds_list = reds
        oranges_list = oranges
        yellows_list = yellows
        blues_list = blues
        greens_list = greens

        maximumValue = sum(
            [
                reds_list[-1],
                oranges_list[-1],
                yellows_list[-1],
                blues_list[-1],
                greens_list[-1],
            ]
        )
        xWidth = pageWidth - 2 * margin
        yHeight = pageHeight - 2 * margin

        xstep = xWidth / (number_of_days_untile_deadline-1)
        ystep = yHeight / int(number_of_glyphs)

        newPage(pageWidth, pageHeight)

        fill(0.1)
        rect(0, 0, pageWidth, pageHeight)
        translate(margin, margin)
        stroke(1)
        line((0, 0), (xWidth, 0))
        line((0, 0), (0, yHeight))
        with savedState():
            stroke(1)
            strokeWidth(1)
            line((-10, yHeight), (0, yHeight))
            stroke(None)
            fill(1)
            font("Helvetica", 5)
            text(str(number_of_glyphs), (-15, yHeight-1), align = "right")

        for i in range(6):
            y = (int(maximumValue) / 5) * i
            stroke(1)
            strokeWidth(1)
            line((-10, y * ystep), (0, y * ystep))
            stroke(0.2, 0.2, 0.2, 1)
            strokeWidth(0.5)
            stroke(None)
            fill(1)
            font("Helvetica", 5)
            text(str(int(y)), (-15, y * ystep - 1), align="right")

        strokeWidth(2)

        pol = [
            (
                0 * xstep,
                int(
                    reds_list[0]
                    + oranges_list[0]
                    + yellows_list[0]
                    + greens_list[0]
                    + blues_list[0]
                )
                * ystep,
            )
        ]
        fill(*RED_COLOR)
        for i, red in enumerate(reds_list[1:]):
            pol.append(
                (
                    (i + 1) * xstep,
                    int(
                        reds_list[i + 1]
                        + oranges_list[i + 1]
                        + yellows_list[i + 1]
                        + greens_list[i + 1]
                        + blues_list[i + 1]
                    )
                    * ystep,
                )
            )
        pol.append(((len(reds_list) - 1) * xstep, 0))
        pol.append((0, 0))
        polygon(*pol)
        stroke(None)

        value = int(reds_list[i + 1])
        if value:
            font("Helvetica", 5)
            text(
                str(value),
                (
                    (i + 1) * xstep + 5,
                    int(
                        reds_list[i + 1]
                        + oranges_list[i + 1]
                        + yellows_list[i + 1]
                        + greens_list[i + 1]
                        + blues_list[i + 1]
                    )
                    * ystep,
                ),
                align="left",
            )

        pol = [
            (
                0 * xstep,
                int(oranges_list[0] + yellows_list[0] + greens_list[0] + blues_list[0])
                * ystep,
            )
        ]
        fill(*ORANGE_COLOR)
        for i, red in enumerate(oranges_list[1:]):
            pol.append(
                (
                    (i + 1) * xstep,
                    int(
                        oranges_list[i + 1]
                        + yellows_list[i + 1]
                        + greens_list[i + 1]
                        + blues_list[i + 1]
                    )
                    * ystep,
                )
            )
        pol.append(((len(oranges_list) - 1) * xstep, 0))
        pol.append((0, 0))
        polygon(*pol)
        stroke(None)

        value = int(oranges_list[i + 1])
        if value:
            font("Helvetica", 5)
            text(
                str(value),
                (
                    (i + 1) * xstep + 5,
                    int(
                        oranges_list[i + 1]
                        + yellows_list[i + 1]
                        + greens_list[i + 1]
                        + blues_list[i + 1]
                    )
                    * ystep + 4 * (value < 200),
                ),
                align="left",
            )

        pol = [(0 * xstep, int(yellows_list[0] + greens_list[0] + blues_list[0]) * ystep)]
        fill(*YELLOW_COLOR)
        for i, red in enumerate(yellows_list[1:]):
            pol.append(
                (
                    (i + 1) * xstep,
                    int(yellows_list[i + 1] + greens_list[i + 1] + blues_list[i + 1])
                    * ystep,
                )
            )
        pol.append(((len(yellows_list) - 1) * xstep, 0))
        pol.append((0, 0))
        polygon(*pol)
        stroke(None)

        value = int(yellows_list[i + 1])
        if value:
            font("Helvetica", 5)
            text(
                str(value),
                (
                    (i + 1) * xstep + 5,
                    int(yellows_list[i + 1] + greens_list[i + 1] + blues_list[i + 1])
                    * ystep + 4 * (value < 200),
                ),
                align="left",
            )

        pol = [(0 * xstep, int(greens_list[0] + blues_list[0]) * ystep)]
        fill(*BLUE_COLOR)
        for i, red in enumerate(blues_list[1:]):
            pol.append(
                ((i + 1) * xstep, int(greens_list[i + 1] + blues_list[i + 1]) * ystep)
            )
        pol.append(((len(blues_list) - 1) * xstep, 0))
        pol.append((0, 0))
        polygon(*pol)
        stroke(None)

        value = int(blues_list[i + 1])
        if value:
            font("Helvetica", 5)
            text(
                str(value),
                ((i + 1) * xstep + 5, int(greens_list[i + 1] + blues_list[i + 1]) * ystep + 4 * (value < 200)),
                align="left",
            )

        pol = [(0 * xstep, int(greens_list[0]) * ystep)]
        fill(*GREEN_COLOR)
        for i, red in enumerate(greens_list[1:]):
            pol.append(((i + 1) * xstep, int(greens_list[i + 1]) * ystep))
        pol.append(((len(greens_list) - 1) * xstep, 0))
        pol.append((0, 0))
        polygon(*pol)
        stroke(None)
        # fill(1)
        value = int(greens_list[i + 1])
        if value:
            font("Helvetica", 5)
            text(
                str(value),
                ((i + 1) * xstep + 5, int(greens_list[i + 1]) * ystep ),
                align="left",
            )

        stroke(1)
        line((0, 0), (xWidth, yHeight))

        with savedState():
            stroke(None)
            fill(1)
            font("Helvetica", 5)
            with savedState():
                rotate(45, (xWidth, -20))
                text(ends_date, (xWidth, -20), align="center")
            # restore()
            stroke(1)
            strokeWidth(1)
            line((xWidth, 0), (xWidth, -10))

        for i, date in enumerate(dates):
            j = 5
            if number_of_days > j:
                v = i % (number_of_days // j)
                if v:
                    continue
            stroke(None)
            fill(1)
            font("Helvetica", 5)
            with savedState():
                rotate(45, (i * xstep, -20))
                text(date, (i * xstep, -20), align="center")
            # restore()
            stroke(1)
            strokeWidth(1)
            line((i * xstep, 0), (i * xstep, -10))

        fontSize(16)
        text(title, (xWidth * 0.5, yHeight + 20), align="center")




if __name__ == "__main__":
    prooferDir = pathlib.Path(__file__).resolve().parent
    repoDir = prooferDir.parent
    reportDir = repoDir / "scripts" / "resources"
    reportDir.mkdir(parents=True, exist_ok=True)

    projects_names = ["notoserifcjkjp", "notosanscjksc"]
    for project_name in projects_names:
        newDrawing()
        colors_evolution_path = reportDir / f"{project_name}_evolution_character_glyphs.csv"
        with open(colors_evolution_path, "r", encoding="utf-8") as file:
            colorEvolutionCGText = file.readlines()

        # get number of glyphs from last csv line
        last_line = colorEvolutionCGText[-1].strip().split(",")
        number_of_glyphs = sum([int(x) for x in last_line[1:]])
        
        make_page(colorEvolutionCGText, number_of_days_untile_deadline = 62, number_of_glyphs = number_of_glyphs, ends_date = "2024-03-11", title = "CG")

        saveImage(reportDir / f"{project_name}-progress.pdf")
