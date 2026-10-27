
# D:\openclaw-brain\acer_full_inventory.ps1
# OpenClaw 自主硬體完整資料收集 不靠人手動 直接跑不搜尋
# 輸出 D:\openclaw-brain\logs\acer_hardware_full.json + .txt

$ErrorActionPreference = "SilentlyContinue"
$root = "D:\openclaw-brain"
$logDir = "$root\logs"
if (!(Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
$jsonPath = "$logDir\acer_hardware_full.json"
$txtPath = "$logDir\acer_hardware_full.txt"

function Get-Cmd($cmd){ try { Invoke-Expression $cmd 2>&1 | Out-String } catch { "ERROR: $_" } }

$model = (Get-CimInstance Win32_ComputerSystem).Model
$manufacturer = (Get-CimInstance Win32_ComputerSystem).Manufacturer
$cpu = (Get-CimInstance Win32_Processor).Name
$cores = (Get-CimInstance Win32_Processor).NumberOfCores
$threads = (Get-CimInstance Win32_Processor).NumberOfLogicalProcessors
$ramBytes = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory
$ramGB = [math]::Round($ramBytes/1GB,2)
$gpus = (Get-CimInstance Win32_VideoController | ForEach-Object { $_.Name }) -join "; "
$os = (Get-CimInstance Win32_OperatingSystem).Caption + " " + (Get-CimInstance Win32_OperatingSystem).Version
$osBuild = (Get-CimInstance Win32_OperatingSystem).BuildNumber

$disks = Get-CimInstance Win32_LogicalDisk | Select-Object DeviceID, Size, FreeSpace, FileSystem | ForEach-Object {
  @{ DeviceID=$_.DeviceID; SizeGB=[math]::Round($_.Size/1GB,2); FreeGB=[math]::Round($_.FreeSpace/1GB,2); FS=$_.FileSystem }
}

$brainExists = Test-Path "$root"
$brainTree = if ($brainExists) { Get-ChildItem $root -Recurse -Depth 2 | ForEach-Object { $_.FullName } } else { @() }

$python = Get-Cmd "python --version"
$python3 = Get-Cmd "python3 --version"
$node = Get-Cmd "node --version"
$npm = Get-Cmd "npm --version"
$code = Get-Cmd "code --version"
$wsl = Get-Cmd "wsl --version"
$wslStatus = Get-Cmd "wsl --status"
$openclaw = Get-Cmd "openclaw --version"
$git = Get-Cmd "git --version"

$result = @{
  timestamp = (Get-Date -Format "yyyy-MM-dd HH:mm:ss K")
  manufacturer = $manufacturer.Trim()
  model = $model.Trim()
  cpu = $cpu.Trim()
  cores = $cores
  threads = $threads
  ram_bytes = $ramBytes
  ram_gb = $ramGB
  gpu = $gpus
  os = $os
  os_build = $osBuild
  disks = $disks
  brain_exists = $brainExists
  brain_root = $root
  brain_tree_sample = $brainTree | Select-Object -First 50
  versions = @{
    python = $python.Trim()
    python3 = $python3.Trim()
    node = $node.Trim()
    npm = $npm.Trim()
    vscode = $code.Trim()
    wsl = $wsl.Trim()
    wsl_status = $wslStatus.Trim()
    openclaw = $openclaw.Trim()
    git = $git.Trim()
  }
  raw = @{
    systeminfo = Get-Cmd "systeminfo"
  }
}

$result | ConvertTo-Json -Depth 10 | Out-File -Encoding utf8 $jsonPath
$result | Format-List | Out-File -Encoding utf8 $txtPath

Write-Host "=== OpenClaw Acer Full Inventory Done ==="
Write-Host "JSON: $jsonPath"
Write-Host "TXT: $txtPath"
Get-Content $txtPath | Select-Object -First 200
