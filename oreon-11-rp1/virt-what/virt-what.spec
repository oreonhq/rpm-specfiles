Name:           virt-what
Version:        1.27
Release:        5%{?dist}
Summary:        Detect if we are running in a virtual machine
License:        GPL-2.0-or-later

URL:            http://people.redhat.com/~rjones/virt-what/
Source0:        http://people.redhat.com/~rjones/virt-what/files/%{name}-%{version}.tar.gz
Source1:        http://people.redhat.com/~rjones/virt-what/files/%{name}-%{version}.tar.gz.sig

# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring

# Maintainer script which helps with handling patches.
Source3:        copy-patches.sh

# Add detection of systemd-nspawn (upstream)
Patch:          0001-virt-what-detect-systemd-nspawn.patch
# Add detection of WSL2 (upstream)
Patch:          0002-Add-support-for-WSL2.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git
BuildRequires:  autoconf, automake, libtool
BuildRequires:  /usr/bin/pod2man

# Required to verify tarball signature.
BuildRequires: gnupg2

# Required at build time in order to do 'make check' (for getopt).
BuildRequires:  util-linux

# virt-what script uses dmidecode and getopt (from util-linux).
# RPM cannot detect this so make the dependencies explicit here.
%ifarch aarch64 %{ix86} x86_64
Requires:       dmidecode
%endif
Requires:       util-linux

# Runs the 'which' program to find the helper.
Requires:       which


%description
virt-what is a shell script which can be used to detect if the program
is running in a virtual machine.

The program prints out a list of "facts" about the virtual machine,
derived from heuristics.  One fact is printed per line.

If nothing is printed and the script exits with code 0 (no error),
then it can mean either that the program is running on bare-metal or
the program is running inside a type of virtual machine which we don't
know about or can't detect.

Current types of virtualization detected:

 - alibaba_cloud      Alibaba cloud
 - alibaba_cloud-ebm
 - aws                Amazon Web Services
 - bhyve              FreeBSD hypervisor
 - docker             Docker container
 - google_cloud       Google cloud
 - hyperv             Microsoft Hyper-V
 - ibm_power-kvm      IBM POWER KVM
 - ibm_power-lpar_shared IBM POWER LPAR (hardware partition)
 - ibm_power-lpar_dedicated
 - ibm_systemz-*      IBM SystemZ Direct / LPAR / z/VM / KVM
 - illumos-lx         Illumos with Linux syscall emulation
 - ldoms              Oracle VM Server for SPARC Logical Domains
 - linux_vserver      Linux VServer container
 - lxc                Linux LXC container
 - kvm                Linux Kernel Virtual Machine (KVM)
 - lkvm               LKVM / kvmtool
 - nutanix_ahv        Nutanix Acropolis Hypervisor (AHV)
 - openvz             OpenVZ or Virtuozzo
 - ovirt              oVirt node
 - parallels          Parallels Virtual Platform
 - podman             Podman container
 - powervm_lx86       IBM PowerVM Lx86 Linux/x86 emulator
 - qemu               QEMU (unaccelerated)
 - redhat             Red Hat hypervisor
 - rhev               Red Hat Enterprise Virtualization
 - uml                User-Mode Linux (UML)
 - virtage            Hitachi Virtualization Manager (HVM) Virtage LPAR
 - virtualbox         VirtualBox
 - virtualpc          Microsoft VirtualPC
 - vmm                vmm OpenBSD hypervisor
 - vmware             VMware
 - xen                Xen
 - xen-dom0           Xen dom0 (privileged domain)
 - xen-domU           Xen domU (paravirtualized guest domain)
 - xen-hvm            Xen guest fully virtualized (HVM)


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git

# Always rebuild upstream autotools files.
autoreconf -i


%build
%configure || { cat config.log; exit 1; }
make


%install
%make_install


%check
if ! make -k check ; then
    find -name test-suite.log -exec cat {} \;
    exit 1
fi

%files
%doc README COPYING
%{_sbindir}/virt-what
%{_sbindir}/virt-what-cvm
%{_libexecdir}/virt-what-cpuid-helper
%{_mandir}/man1/*.1*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27-5
- Import
