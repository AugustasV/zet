# Linux environment on virtualbox with windows

**Objective:**
Set up Linux on VirtualBox with Windows for SSH access, avoiding resource-intensive alternatives like WSL2.

**Procedure:**

1. **VirtualBox Installation:**
   - Download and install Virtualbox on Windows `winget install Oracle.VirtualBox'

2. **Linux Installation:**
   - Install Linux on VirtualBox and add your public SSH key.

3. **Network Configuration:**
   - Choose NAT as the network setting.
   - In advanced settings, set up port forwarding:
     - Host Port: Choose a port (e.g., 3022)
     - System Port: 22

4. **SSH Connection:**
   - Open a Windows terminal and SSH into the virtual machine:
     ```bash
     ssh augustas@127.0.0.1 -p 3022
     ```

**Note:** Avoid WSL2 for resource considerations. Adjust port numbers as needed.
I would use VMware player if I would have option.

