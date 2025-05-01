@echo off
title WinGo - by TheYali1
chcp 65001 >nul
setlocal enabledelayedexpansion
:start
echo.
echo                                      [38;2;0;255;0m██╗    ██╗██╗███╗   ██╗ ██████╗  ██████╗ ██╗[0m
echo                                      [38;2;51;255;0m██║    ██║██║████╗  ██║██╔════╝ ██╔═══██╗██║[0m
echo                                      [38;2;102;255;0m██║ █╗ ██║██║██╔██╗ ██║██║  ███╗██║   ██║██║[0m
echo                                      [38;2;153;255;0m██║███╗██║██║██║╚██╗██║██║   ██║██║   ██║╚═╝[0m
echo                                      [38;2;204;255;0m╚███╔███╔╝██║██║ ╚████║╚██████╔╝╚██████╔╝██╗[0m
echo                                      [38;2;255;255;0m ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝[0m
echo.
for /f "tokens=2,*" %%a in ('systeminfo ^| findstr /C:"OS Name"') do set OSName=%%b
echo                                     [38;2;0;255;0m╔[38;2;51;255;0m════════════════════════════════════════════[38;2;0;255;0m╗[0m
echo                                     [38;2;0;255;0m║[0m [38;2;0;255;0mYou Are running: %OSName%[38;2;0;255;0m ║[0m
echo                                     [38;2;255;255;0m╚[38;2;204;255;0m════════════════════════════════════════════[38;2;255;255;0m╝[0m
echo.
echo                                [38;2;0;255;0m╔[38;2;51;255;0m════════════════════════════════════════════════════════[38;2;0;255;0m╗[0m
echo                                [38;2;0;255;0m║[0m [38;2;0;255;0m1. Pro                   ^| 6. Home Country Specific    [38;2;0;255;0m║[0m
echo                                [38;2;51;255;0m║[0m [38;2;0;255;0m2. Pro N                 ^| 7. Enterprise               [38;2;51;255;0m║[0m
echo                                [38;2;102;255;0m║[0m [38;2;0;255;0m3. Home                  ^| 8. Enterprise N             [38;2;102;255;0m║[0m
echo                                [38;2;153;255;0m║[0m [38;2;0;255;0m4. Home N                ^| 9. Education                [38;2;153;255;0m║[0m
echo                                [38;2;204;255;0m║[0m [38;2;0;255;0m5. Home Single Language  ^| 10. Education N             [38;2;204;255;0m║[0m
echo                                [38;2;255;255;0m╚[38;2;204;255;0m════════════════════════════════════════════════════════[38;2;255;255;0m╝[0m
set /p windowsver=[38;2;0;255;0m%username%^> [0m
if %windowsver%==1 (
    slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX >nul
    slmgr /skms kms8.msguides.com >nul
    slmgr /ato >nul
    powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
    shutdown -r
) else (
    if %windowsver%==2 (
        slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9 >nul
        slmgr /skms kms8.msguides.com >nul
        slmgr /ato >nul
        powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
        shutdown -r
    ) else (
        if %windowsver%==3 (
            slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 >nul
            slmgr /skms kms8.msguides.com >nul
            slmgr /ato >nul
            powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
            shutdown -r
        ) else (
            if %windowsver%==4 (
                slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM >nul
                slmgr /skms kms8.msguides.com >nul
                slmgr /ato >nul
                powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                shutdown -r
            ) else (
                if %windowsver%==5 (
                    slmgr /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH >nul
                    slmgr /skms kms8.msguides.com >nul
                    slmgr /ato >nul
                    powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                    shutdown -r
                ) else (
                    if %windowsver%==6 (
                        slmgr /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR >nul
                        slmgr /skms kms8.msguides.com >nul
                        slmgr /ato >nul
                        powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                        shutdown -r
                    ) else (
                        if %windowsver%==7 (
                            slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43 >nul
                            slmgr /skms kms8.msguides.com >nul
                            slmgr /ato >nul
                            powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                            shutdown -r
                        ) else (
                            if %windowsver%==8 (
                                slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 >nul
                                slmgr /skms kms8.msguides.com >nul
                                slmgr /ato >nul
                                powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                                shutdown -r
                            ) else (
                                if %windowsver%==9 (
                                    slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 >nul
                                    slmgr /skms kms8.msguides.com >nul
                                    slmgr /ato >nul
                                    powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                                    shutdown -r
                                ) else (
                                    if %windowsver%==10 (
                                        slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ >nul
                                        slmgr /skms kms8.msguides.com >nul
                                        slmgr /ato >nul
                                        powershell -Command "Add-Type -AssemblyName System.Windows.Forms; [void][System.Windows.Forms.MessageBox]::Show('Your PC is activate windows successfully!','Success','OK','Information')"
                                        shutdown -r
                                    ) else (
                                        cls
                                        goto start
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)
pause