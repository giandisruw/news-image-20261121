#!/usr/bin/env python3
"""Draw the front page for Saturday 21 November 2026.

Self-contained: reads nothing but the story text below, uses only the
standard library plus Pillow, touches no network, no clock and no
randomness, so running it twice produces identical bytes. Writes
entry.png next to this file (or to the path in --out).
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

PAGE_W = 1024
PAGE_H = 1024
SIDE = 36
COL_W = PAGE_W - 2 * SIDE  # 952

PAPER = (248, 244, 232)
INK = (17, 17, 17)
ACCENT = (138, 20, 20)
MUTED = (98, 92, 82)
BAND = (26, 26, 26)
BAND_TEXT = (241, 239, 231)

LIB = "/usr/share/fonts/truetype/liberation"


def load(name, size):
    return ImageFont.truetype(os.path.join(LIB, name), size)


SERIF_BOLD = "LiberationSerif-Bold.ttf"
SERIF_REG = "LiberationSerif-Regular.ttf"
SERIF_ITAL = "LiberationSerif-Italic.ttf"
SANS_BOLD = "LiberationSans-Bold.ttf"
SANS_REG = "LiberationSans-Regular.ttf"

F_NAMEPLATE = load(SERIF_BOLD, 80)
F_DATELINE = load(SANS_BOLD, 26)
F_STRAP = load(SANS_REG, 14)
F_LABEL = load(SANS_BOLD, 19)
F_TOP_HEAD = load(SERIF_BOLD, 48)
F_TOP_DEK = load(SERIF_ITAL, 22)
F_TOP_TEXT = load(SERIF_REG, 16)
F_STRIP = load(SANS_BOLD, 14)
F_HEAD = load(SERIF_BOLD, 29)
F_HEAD_SMALL = load(SERIF_BOLD, 23)
F_TEXT = load(SERIF_REG, 16)
F_TEXT_SMALL = load(SERIF_REG, 15)
F_TAPE = load(SANS_BOLD, 15)
F_FOOT = load(SANS_REG, 13)


def fit_lines(draw, text, face, width):
    """Greedy wrap of one paragraph into lines no wider than width."""
    out = []
    for chunk in text.split("\n"):
        words = chunk.split()
        if not words:
            out.append("")
            continue
        line = words[0]
        for word in words[1:]:
            test = line + " " + word
            if draw.textlength(test, font=face) <= width:
                line = test
            else:
                out.append(line)
                line = word
        out.append(line)
    return out


def draw_para(draw, x, y, width, text, face, step, colour=INK):
    for line in fit_lines(draw, text, face, width):
        draw.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def hline(draw, y, weight=2, x0=None, x1=None):
    x0 = SIDE if x0 is None else x0
    x1 = PAGE_W - SIDE if x1 is None else x1
    draw.line([(x0, y), (x1, y)], fill=INK, width=weight)
    return y + weight


def double_hline(draw, y):
    hline(draw, y, 3)
    hline(draw, y + 6, 1)
    return y + 10


def draw_label(draw, x, y, text):
    draw.text((x, y), text, font=F_LABEL, fill=ACCENT)
    return y + 26


def draw_story(draw, x, y, width, label, headline, body,
               head_face, head_step, body_face=F_TEXT, body_step=20):
    y = draw_label(draw, x, y, label)
    for line in fit_lines(draw, headline, head_face, width):
        draw.text((x, y), line, font=head_face, fill=INK)
        y += head_step
    y += 2
    return draw_para(draw, x, y, width, body, body_face, body_step)


# ---------------------------------------------------------------- stories

TOP_LABEL = "POLAND  \u2014  NATO'S EASTERN FLANK"
TOP_HEAD = "RUSSIAN MISSILES LAND IN POLAND"
TOP_DEK = ("Warsaw calls the overnight incursion an intentional provocation "
           "as NATO jets scramble \u2014 and Ukraine endures one of the "
           "war's biggest attacks.")
TOP_LEFT = ("NOWY LIPOWIEC \u2014 Two Russian missiles and a suspected "
            "jet-powered drone came down in south-east Poland on Friday, "
            "during a huge overnight attack on Ukraine. A Kh-101 cruise "
            "missile fell near Nowy Lipowiec, about 50 km from the border.")
TOP_RIGHT = ("No one in Poland was hurt. Prime Minister Donald Tusk called "
             "it an \u201cintentional provocation\u201d, and NATO chief Mark "
             "Rutte called it a \u201cgrave violation\u201d of Polish "
             "airspace. In Ukraine, eight people were killed.")
TOP_STRIP = ("3 OBJECTS CROSSED  \u00b7  KH-101 CRUISE MISSILE  \u00b7  "
             "NO INJURIES IN POLAND  \u00b7  400+ DRONES, 110 MISSILES AT UKRAINE")

PAIR_A = [
    ("NEW YORK",
     "WALL ST SLUMPS INTO CORRECTION",
     "The S&P 500 fell 3.7% on Friday and the Dow 1.9%, both now more "
     "than 10% below their peaks. The Nasdaq sank 5.3% and is down for "
     "the year, as an AI sell-off led by Nvidia, down 14%, erased 2026's "
     "gains."),
    ("ODISHA",
     "AKVAN COMES ASHORE",
     "Cyclone Akvan made landfall near Gopalpur on Friday morning, with "
     "winds of 70\u201380 km/h. About 370,000 people had moved to "
     "shelters; officials reported no major damage and no loss of life."),
]

TRIO = [
    ("COPENHAGEN",
     "DENMARK FOILS \u2018HIT\u2019 PLOT",
     "Police say they stopped a Russian plot to kill the rapper "
     "Kyivstoner at a concert in September. Two Danes were charged on "
     "Friday; Denmark is expelling Russia's defence attach\u00e9."),
    ("STRAIT OF HORMUZ",
     "TANKER HIT, AFIRE",
     "A tanker was struck by an unknown projectile eight nautical miles "
     "north of Oman's Khasab on Friday and caught fire. No casualties "
     "were reported; Iran said the ship hit a mine."),
    ("BRUSSELS",
     "UK AND EU SEAL RESET",
     "Britain and the EU agreed deals on food trade, carbon markets and "
     "youth travel on Friday. Each side will take in 100,000 young "
     "people a year; PM Burnham called it a \u201cwin-win\u201d."),
]

PAIR_B = [
    ("HEALTH",
     "PANCREATIC CANCER PILL SHRINKS TUMOURS",
     "Erasca's pill ERAS-0015 shrank tumours in 44% of 25 pancreatic "
     "cancer patients in an early trial, results showed on Friday. In "
     "the two most common gene variants, the response rate was 69%."),
    ("LOS ANGELES",
     "PALISADES FIRE ARSON VERDICT",
     "Jonathan Rinderknecht, 30, was found guilty on Friday of starting "
     "the fire that became the Palisades Fire, which killed 12 people "
     "and destroyed about 6,800 structures. He faces sentencing in "
     "March."),
]

TAPE_LINES = [
    "VIRGINIA \u00b7 First measles death of 2026 \u2014 a child aged 0\u20134 "
    "\u00b7 220 cases in the state this year",
    "RIYADH \u00b7 Saudi coalition says it shot down three Houthi "
    "missiles and struck Hodeidah",
    "UKRAINE \u00b7 Trump dials into allies' meeting after Putin\u2013Xi "
    "talks  \u00b7  ANTHROPIC \u00b7 Shares fall 9% to $88 after record IPO",
]


def render():
    img = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- nameplate -----------------------------------------------------
    y = 20
    name = "THE WORLD"
    nw = d.textlength(name, font=F_NAMEPLATE)
    d.text(((PAGE_W - nw) / 2, y), name, font=F_NAMEPLATE, fill=INK)
    y += 86
    dateline = "SATURDAY  21  NOVEMBER  2026"
    dw = d.textlength(dateline, font=F_DATELINE)
    d.text(((PAGE_W - dw) / 2, y), dateline, font=F_DATELINE, fill=ACCENT)
    y += 34
    strap = "THE DAY\u2019S WORLD NEWS IN ONE PAGE"
    sw = d.textlength(strap, font=F_STRAP)
    d.text(((PAGE_W - sw) / 2, y), strap, font=F_STRAP, fill=MUTED)
    y += 18
    y = double_hline(d, y)
    y += 4

    # ---- top story -----------------------------------------------------
    y = draw_label(d, SIDE, y, TOP_LABEL)
    for line in fit_lines(d, TOP_HEAD, F_TOP_HEAD, COL_W):
        d.text((SIDE, y), line, font=F_TOP_HEAD, fill=INK)
        y += 54
    y += 2
    y = draw_para(d, SIDE, y, COL_W, TOP_DEK, F_TOP_DEK, 27)
    y += 6
    half = (COL_W - 24) // 2
    end_l = draw_para(d, SIDE, y, half, TOP_LEFT, F_TOP_TEXT, 20)
    end_r = draw_para(d, SIDE + half + 24, y, half, TOP_RIGHT, F_TOP_TEXT, 20)
    y = max(end_l, end_r) + 5
    sw = d.textlength(TOP_STRIP, font=F_STRIP)
    d.text(((PAGE_W - sw) / 2, y), TOP_STRIP, font=F_STRIP, fill=ACCENT)
    y += 20
    y = hline(d, y, 2)
    y += 6

    # ---- pair A: two stories ------------------------------------------
    half = (COL_W - 28) // 2
    e1 = draw_story(d, SIDE, y, half, PAIR_A[0][0], PAIR_A[0][1],
                    PAIR_A[0][2], F_HEAD, 33)
    e2 = draw_story(d, SIDE + half + 28, y, half, PAIR_A[1][0],
                    PAIR_A[1][1], PAIR_A[1][2], F_HEAD, 33)
    y = max(e1, e2) + 3
    y = hline(d, y, 1)
    y += 6

    # ---- trio: three stories ------------------------------------------
    third = (COL_W - 2 * 24) // 3
    ends = []
    for i, (label, head, body) in enumerate(TRIO):
        x = SIDE + i * (third + 24)
        ends.append(draw_story(d, x, y, third, label, head, body,
                               F_HEAD_SMALL, 27, F_TEXT_SMALL, 18))
    y = max(ends) + 3
    y = hline(d, y, 1)
    y += 6

    # ---- pair B: two stories ------------------------------------------
    half = (COL_W - 28) // 2
    e1 = draw_story(d, SIDE, y, half, PAIR_B[0][0], PAIR_B[0][1],
                    PAIR_B[0][2], F_HEAD, 33, F_TEXT, 19)
    e2 = draw_story(d, SIDE + half + 28, y, half, PAIR_B[1][0],
                    PAIR_B[1][1], PAIR_B[1][2], F_HEAD, 33, F_TEXT, 19)
    y = max(e1, e2) + 4

    # ---- news tape ------------------------------------------------------
    band_top = y
    band_h = 84
    d.rectangle([(SIDE, band_top), (PAGE_W - SIDE, band_top + band_h)],
                fill=BAND)
    ty = band_top + 8
    for line in TAPE_LINES:
        for seg in fit_lines(d, line, F_TAPE, COL_W - 20):
            d.text((SIDE + 10, ty), seg, font=F_TAPE, fill=BAND_TEXT)
            ty += 20
    y = band_top + band_h + 6

    # ---- footer: what the page covers and where it comes from ----------
    foot = ("REPORTED 20\u201321 NOVEMBER 2026  \u00b7  SOURCES: REUTERS, AP, "
            "INDIA METEOROLOGICAL DEPARTMENT, UKMTO, VIRGINIA DEPT. OF HEALTH")
    fw = d.textlength(foot, font=F_FOOT)
    d.text(((PAGE_W - fw) / 2, y), foot, font=F_FOOT, fill=MUTED)
    y += 14

    if y > PAGE_H - 8:
        raise SystemExit("layout overflow: content ends at y=%d" % y)
    return img


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    out = args.out or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img = render()
    img.save(out, format="PNG", optimize=True)
    print("wrote %s (%dx%d)" % (out, PAGE_W, PAGE_H))
    return 0


if __name__ == "__main__":
    sys.exit(main())
