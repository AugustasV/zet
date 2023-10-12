# Linux KVM minikube fix network issues

Had to check if libvirt reports no errors:

`virt-host-validate`
in grub boot file had to add those boot parameters:
GRUB_CMDLINE_LINUX_DEFAULT="intel_iommu=on systemd.unified_cgroup_hierarchy=0"

Now `virt-host-validate` command report no issues, works as expected
