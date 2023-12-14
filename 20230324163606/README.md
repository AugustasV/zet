# Resize Virtualbox vm disk size

1. Resize Virtual Hard Disk in VM
1. **Expand the LVM Partition**:
     ```bash
     sudo lvextend -l+100%FREE /dev/mapper/development--vg-root
     sudo resize2fs /dev/mapper/development--vg-root
     ```
   - Replace `/dev/mapper/development--vg-root` with your actual LVM partition name

4. **Verify the New Size**:

Source: [Resize ubuntu disk in virtualbux](https://devlog.rolandow.com/2021/10/resize-ubuntu-disk-in-virtualbox)
