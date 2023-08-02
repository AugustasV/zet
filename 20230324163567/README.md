# Windows Subsystem for Linux (WSL) not responding fix

I have to use WSL on my Windows machine, and very often WSL/Podman become not responding at all, `wsl --shutdown` command doesn't make any difference
`taskkill /f /im wslservice.exe` worked like a charm.
Source: [https://github.com/microsoft/WSL/issues/8529#issuecomment-1263463528]
