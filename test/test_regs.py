from config import *

wb.open()
regs = wb.regs
###
regs.ethphy_crg_reset.write(1)
print("sysid     : 0x%04x" %regs.identifier_sysid.read())
print("revision  : 0x%04x" %regs.identifier_revision.read())
print("frequency : %d MHz" %(regs.identifier_frequency.read()/1000000))
###
wb.close()
