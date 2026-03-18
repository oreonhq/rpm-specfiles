Summary:        Tool to analyse BIOS DMI data
Name:           dmidecode
Version:        3.6
Release:        9%{?dist}
Epoch:          1
License:        GPL-2.0-or-later
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
URL:            https://www.nongnu.org/dmidecode/
BuildRequires:  gcc make
BuildRequires:  pkgconfig(bash-completion)
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64 riscv64

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/dmidecode
%endif

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
%autosetup

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"

%install
%make_install %{?_smp_mflags} prefix=%{_prefix} sbindir=%{_sbindir} install-bin install-man

%files
%doc AUTHORS NEWS README
%license LICENSE
%{_sbindir}/dmidecode
%ifnarch ia64 aarch64 riscv64
%{_sbindir}/vpddecode
%{_sbindir}/ownership
%{_sbindir}/biosdecode
%{bash_completions_dir}/vpddecode
%{bash_completions_dir}/ownership
%{bash_completions_dir}/biosdecode
%endif
%{_mandir}/man8/*
%{bash_completions_dir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6-9
- Prepare for Oreon 11 (RP1)
