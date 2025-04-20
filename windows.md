## errol intune
powershell in administrator
 
 allow powershell to run scripts
 powershell -ep bypass

 run script
  get-windowsautopilotinfo -online -grouptag "tmp" -assignedcomputername "TAD-PC-N006"

  output
  1 devices imported successfully. Elapsed time to complete import: 187 seconds
  Waiting for 0 of 1 to be synced
  All devices synced. Elapsed time to complete sync: 1 seconds

## system info
powershell
get-ciminstance win32_bios
 output 
  SMBIOSBIOSVersion:N21 Ver. 02.14
  Manufacturer: HP
  Name: Default System BIOS
  SerialNumber: AUD6250HT8
  Version: HPQOEM - 0

hostname
 output
  TAD-PC-N006