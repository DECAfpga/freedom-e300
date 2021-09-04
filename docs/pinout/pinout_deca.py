###########################################
# Script to build pinout diagram.
# Build from cmd:
# >>> python3 -m pinout.manager --export pinout_deca pinout_deca.png
###########################################

from pinout.components import leaderline as lline
from pinout.components.layout import Diagram, Panel
from pinout.components.legend import Legend
from pinout.components.pinlabel import PinLabelGroup
from pinout.components.text import TextBlock
from pinout.core import Group, Image

# Import data for the diagram
import data

# Create a new diagram
diagram = Diagram(1588, 920, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a layout
content = diagram.add(
    Panel(
        width=1550,
        height=800,
        inset=(2, 2, 2, 2),
    )
)

# Board Pinout Diagram
panel_main = content.add(
    Panel(
        x=40,
        width=content.inset_width,
        height=content.inset_height,
        inset=(0, 0, 2, 0),
        tag="panel--main",
    )
)

# Board Pinout Legend
panel_info = content.add(
    Panel(
        x=0,
        y=panel_main.height,
        width=panel_main.width + 38,
        height=content.inset_height - panel_main.height,
        inset=(0, 2, 0, 2),
        tag="panel--info",
    )
)

# Create a group to hold the pinout-diagram components.
graphic = panel_main.add(Group(0, 20))

# Add and embed an image
hardware_img = graphic.add(
    Image("./board_deca.png", width=652, height=1462, embed=True)
)

# Right hand side double-header P8 connector
############################################

# P8 connector text label
P8_connector: object = panel_main.add(
    TextBlock(
        data.P8,
        x=690,
        y=70,
        line_height=10,
        tag="panel P8_connector",
    )
)

# Create pin label on the outer side
graphic.add(
    PinLabelGroup(
        x=626,
        y=85,
        body={"width": 200, "height": 20},
        pin_pitch=(0, 28),
        label_start=(420, 0),
        label_pitch=(0, 28),
        scale=(1, 1),
        labels=data.rhs_outer_numbered,
    )
)

# Create pin label on the inner side
graphic.add(
    PinLabelGroup(
        x=600,
        y=85,
        body={"width": 200, "height": 20},
        pin_pitch=(0, 28),
        label_start=(60, 0),  # 15 to Offset
        label_pitch=(0, -28),
        scale=(1, -1),
        labels=data.rhs_inner_numbered,
        leaderline=lline.Curved(direction="vh"),
    )
)

############################################
# Create a title and a text-block
title_block = panel_info.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)

panel_info.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=panel_info.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = panel_info.add(
    Legend(
        data.legend,
        x=400,
        y=8,
        max_height=136,
    )
)
