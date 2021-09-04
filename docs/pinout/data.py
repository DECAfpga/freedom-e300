legend = [
    ("PIN NUMBER", "pinid"),
    ("GROUND/NC", "gnd"),
    ("FPGA PIN", "gpsingle"),
    ("RISC-V JTAG", "pwr"),
    ("GPIO", "gpio"),
    ("IOF0", "analog"),
    ("IOF1", "touch"),
]

# Pin labels
gnd = ("GND", "gnd")
pwr = ("3.3V", "pwr")

##############################
# LHS
lhs_outer_numbered = []

lhs_inner_numbered = []

##############################
# RHS
rhs_outer_numbered = [
    [
        ("2", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("4", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[1]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN0_1", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("6", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[3]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_DQ0", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN0_3", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("8", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[5]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_SCK", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("10", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[7]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_DQ3", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("12", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[9]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_CS2", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("14", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[11]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN2_1", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("16", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[13]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("I2C0_SCL", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN2_3", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("18", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[15]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("20", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[17]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("UART0_TX", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("22", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[19]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN1_0", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("24", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[21]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN1_2", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("26", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[23]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("28", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[25]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("UART1_TX", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("30", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[27]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_DQ0", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("32", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[29]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_SCK", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("34", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[31]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_DQ3", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("36", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("38", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("40", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("42", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("44", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("RISCV_JTAG_TDI", "pwr", {"body": {"width": 120, "height": 20}}),
    ],
    [
        ("46", "pinid", {"body": {"width": 30, "height": 20}}),
        ("R13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("RISCV_JTAG_TMS", "pwr", {"body": {"width": 120, "height": 20}}),
    ],
]

rhs_inner_numbered = [
    [
        ("1", "pinid", {"body": {"width": 30, "height": 20}}),
        ("GND", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("3", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W18", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[0]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN0_0", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("5", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[2]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_CS0", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN0_2", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("7", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AA20", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[4]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_DQ1", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("9", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB21", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[6]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_DQ2", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("11", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB19", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[8]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_CS1", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("13", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[10]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI0_CS3", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN2_0", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("15", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[12]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("I2C0_SDA", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN2_2", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("17", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[14]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("19", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB16", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[16]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("UART0_RX", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("21", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[18]", "gpio", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("23", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[20]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN1_1", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("25", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB14", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[22]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("-", "analog", {"body": {"width": 85, "height": 20}}),
        ("PWN1_3", "touch", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("27", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[24]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("UART1_RX", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("29", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[26]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_CS0", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("31", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[28]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_DQ1", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("33", "pinid", {"body": {"width": 30, "height": 20}}),
        ("AB10", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("GPIO[30]", "gpio", {"body": {"width": 85, "height": 20}}),
        ("SPI1_DQ2", "analog", {"body": {"width": 85, "height": 20}}),
    ],
    [
        ("35", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y11", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("37", "pinid", {"body": {"width": 30, "height": 20}}),
        ("W12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("39", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V12", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("41", "pinid", {"body": {"width": 30, "height": 20}}),
        ("V13", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("NC", "gnd", {"body": {"width": 40, "height": 20}}),
    ],
    [
        ("43", "pinid", {"body": {"width": 30, "height": 20}}),
        ("Y17", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("RISCV_JTAG_TCK", "pwr", {"body": {"width": 120, "height": 20}}),
    ],
    [
        ("45", "pinid", {"body": {"width": 30, "height": 20}}),
        ("U15", "gpsingle", {"body": {"width": 40, "height": 20}}),
        ("RISCV_JTAG_TDO", "pwr", {"body": {"width": 120, "height": 20}}),
    ],
]

# Text
title = "<tspan class='h1'>RISC-V e300 - DECA Pinout</tspan>"

description = "Made with Pinout\n" \
              "For more information please visit\n" \
              "<tspan class='italic strong'>pinout.readthedocs.io</tspan>."

P8 = "<tspan class='h1'>P8 Connector (RISC-V Interface)</tspan>"

