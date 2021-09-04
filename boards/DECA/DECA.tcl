#============================================================
# Build by Raetro Board Tools v0.1.0
#============================================================
set_global_assignment -name DEVICE 10M50DAF484C6GES
set_global_assignment -name DEVICE_FILTER_PACKAGE FBGA
set_global_assignment -name DEVICE_FILTER_PIN_COUNT 484
set_global_assignment -name DEVICE_FILTER_SPEED_GRADE 6
#============================================================
# Disable config pin so bank8 can use 1.2V
#============================================================
set_global_assignment -name AUTO_RESTART_CONFIGURATION ON
set_global_assignment -name ENABLE_CONFIGURATION_PINS OFF
set_global_assignment -name ENABLE_BOOT_SEL_PIN OFF
#============================================================
# Clocks
#============================================================
set_instance_assignment -name IO_STANDARD "2.5 V" -to ADC_CLK_10
set_instance_assignment -name IO_STANDARD "2.5 V" -to MAX10_CLK1_50
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to MAX10_CLK2_50
set_location_assignment PIN_M9 -to ADC_CLK_10
set_location_assignment PIN_M8 -to MAX10_CLK1_50
set_location_assignment PIN_P11 -to MAX10_CLK2_50

#============================================================
# KEY
#============================================================
set_instance_assignment -name IO_STANDARD "1.5 V Schmitt Trigger" -to KEY[0]
set_instance_assignment -name IO_STANDARD "1.5 V Schmitt Trigger" -to KEY[1]
set_location_assignment PIN_H21 -to KEY[0]
set_location_assignment PIN_H22 -to KEY[1]

#============================================================
# SW
#============================================================
set_instance_assignment -name IO_STANDARD "1.5 V Schmitt Trigger" -to SW[0]
set_instance_assignment -name IO_STANDARD "1.5 V Schmitt Trigger" -to SW[1]
set_location_assignment PIN_J21 -to SW[0]
set_location_assignment PIN_J22 -to SW[1]

#============================================================
# LED
#============================================================
set_instance_assignment -name IO_STANDARD "1.2 V" -to LED[0]
set_instance_assignment -name IO_STANDARD "1.2 V" -to LED[1]
set_instance_assignment -name IO_STANDARD "1.2 V" -to LED[2]
set_instance_assignment -name IO_STANDARD "1.2 V" -to LED[3]
set_location_assignment PIN_C7 -to LED[0]
set_location_assignment PIN_C8 -to LED[1]
set_location_assignment PIN_A6 -to LED[2]
set_location_assignment PIN_B7 -to LED[3]

#============================================================
# GPIO
#============================================================
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[0]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[1]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[2]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[3]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[4]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[5]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[6]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[7]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[8]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[9]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[10]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[11]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[12]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[13]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[14]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[15]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[16]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[17]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[18]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[19]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[20]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[21]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[22]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[23]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[24]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[25]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[26]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[27]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[28]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[29]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[30]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to GPIO[31]
set_location_assignment PIN_W18 -to GPIO[0]
set_location_assignment PIN_Y18 -to GPIO[1]
set_location_assignment PIN_Y19 -to GPIO[2]
set_location_assignment PIN_AA17 -to GPIO[3]
set_location_assignment PIN_AA20 -to GPIO[4]
set_location_assignment PIN_AA19 -to GPIO[5]
set_location_assignment PIN_AB21 -to GPIO[6]
set_location_assignment PIN_AB20 -to GPIO[7]
set_location_assignment PIN_AB19 -to GPIO[8]
set_location_assignment PIN_Y16 -to GPIO[9]
set_location_assignment PIN_V16 -to GPIO[10]
set_location_assignment PIN_AB18 -to GPIO[11]
set_location_assignment PIN_V15 -to GPIO[12]
set_location_assignment PIN_W17 -to GPIO[13]
set_location_assignment PIN_AB17 -to GPIO[14]
set_location_assignment PIN_AA16 -to GPIO[15]
set_location_assignment PIN_AB16 -to GPIO[16]
set_location_assignment PIN_W16 -to GPIO[17]
set_location_assignment PIN_AB15 -to GPIO[18]
set_location_assignment PIN_W15 -to GPIO[19]
set_location_assignment PIN_Y14 -to GPIO[20]
set_location_assignment PIN_AA15 -to GPIO[21]
set_location_assignment PIN_AB14 -to GPIO[22]
set_location_assignment PIN_AA14 -to GPIO[23]
set_location_assignment PIN_AB13 -to GPIO[24]
set_location_assignment PIN_AA13 -to GPIO[25]
set_location_assignment PIN_AB12 -to GPIO[26]
set_location_assignment PIN_AA12 -to GPIO[27]
set_location_assignment PIN_AB11 -to GPIO[28]
set_location_assignment PIN_AA11 -to GPIO[29]
set_location_assignment PIN_AB10 -to GPIO[30]
set_location_assignment PIN_Y13 -to GPIO[31]

#============================================================
# QSPI
#============================================================
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_DATA[0]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_DATA[1]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_DATA[2]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_DATA[3]
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_SCLK
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_CE_n
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to QSPI_FLASH_RESET_n
set_location_assignment PIN_P12 -to QSPI_FLASH_DATA[0]
set_location_assignment PIN_V4 -to QSPI_FLASH_DATA[1]
set_location_assignment PIN_V5 -to QSPI_FLASH_DATA[2]
set_location_assignment PIN_P10 -to QSPI_FLASH_DATA[3]
set_location_assignment PIN_R12 -to QSPI_FLASH_SCLK
set_location_assignment PIN_R10 -to QSPI_FLASH_CE_n
set_location_assignment PIN_W10 -to QSPI_FLASH_RESET_n

#============================================================
# RISC-V JTAG
#============================================================
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to RISCV_JTAG_TCK
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to RISCV_JTAG_TDI
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to RISCV_JTAG_TDO
set_instance_assignment -name IO_STANDARD "3.3-V LVTTL" -to RISCV_JTAG_TMS
set_location_assignment PIN_Y17 -to RISCV_JTAG_TCK
set_location_assignment PIN_W14 -to RISCV_JTAG_TDI
set_location_assignment PIN_U15 -to RISCV_JTAG_TDO
set_location_assignment PIN_R13 -to RISCV_JTAG_TMS
