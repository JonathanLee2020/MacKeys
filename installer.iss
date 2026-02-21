; Inno Setup Script for MacKeys
; This creates a Windows installer (.exe) for easy distribution
; Download Inno Setup from: https://jrsoftware.org/isdl.php

#define MyAppName "MacKeys"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "JonathanLee2020"
#define MyAppURL "https://github.com/JonathanLee2020/MacKeys"
#define MyAppExeName "MacShortcuts.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
AppId={{8B7F5A3C-9E2D-4F1A-A8B6-3C9D7E2F1A4B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}/issues
AppUpdatesURL={#MyAppURL}/releases
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=installer_output
OutputBaseFilename=MacKeys-Setup-v{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin
ArchitecturesInstallIn64BitMode=x64

; Modern look (commented out to avoid file not found errors on GitHub Actions)
; WizardImageFile=compiler:WizModernImage-IS.bmp
; WizardSmallImageFile=compiler:WizModernSmallImage-IS.bmp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "startupicon"; Description: "Run at Windows startup (recommended)"; GroupDescription: "Auto-start:"

[Files]
Source: "dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
; Add more files here if needed

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
; Run the app after installation
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent runascurrentuser

[Registry]
; Auto-start registry entry
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "{#MyAppName}"; ValueData: """{app}\{#MyAppExeName}"""; Flags: uninsdeletevalue; Tasks: startupicon

[Code]
// Custom message during installation
procedure InitializeWizard();
begin
  WizardForm.WelcomeLabel2.Caption :=
    'This will install MacKeys on your computer.' + #13#10 + #13#10 +
    'MacKeys brings Mac-style keyboard shortcuts to Windows:' + #13#10 +
    '  • Alt + Backspace: Delete line' + #13#10 +
    '  • Win + Backspace: Delete word' + #13#10 +
    '  • Alt + `: Switch app instances' + #13#10 +
    '  • Alt + C/V/X/Z: Mac-style shortcuts' + #13#10 + #13#10 +
    'Click Next to continue.';
end;

// Show info after installation
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    MsgBox('Installation complete!' + #13#10 + #13#10 +
           'MacKeys will appear in your system tray.' + #13#10 +
           'Right-click the tray icon to enable/disable shortcuts.' + #13#10 + #13#10 +
           'Note: The app requires administrator privileges to work properly.',
           mbInformation, MB_OK);
  end;
end;
