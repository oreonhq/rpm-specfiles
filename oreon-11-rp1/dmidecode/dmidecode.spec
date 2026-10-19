%global source0_hash 2c3aed12c85a1e6a9410d406d5e417c455466dc1bc7c89278bb32cf7cad91e8a
Summary:        Tool to analyse BIOS DMI data
Name:           dmidecode
Version:        3.7
Release:        1%{?dist}
Epoch:          1
License:        GPL-2.0-or-later
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
URL:            https://www.nongnu.org/dmidecode/
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64 riscv64
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/dmidecode
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
dmidecode reports information about x86 & ia64 hardware as described in the
system BIOS according to the SMBIOS/DMI standard. This information
typically includes system manufacturer, model name, serial number,
BIOS version, asset tag as well as a lot of other details of varying
level of interest and reliability depending on the manufacturer.

This will often include usage status for the CPU sockets, expansion
slots (e.g. AGP, PCI, ISA) and memory module slots, and the list of
I/O ports (e.g. serial, parallel, USB).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"
%install
%make_install %{?_smp_mflags} prefix=%{_prefix} sbindir=%{_sbindir} install-bin install-man
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
