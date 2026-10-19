%global source0_hash 5c32bf347956d4252a25c49fc1304d8b0fc9fa1939c143eb37e720e99e6783f5
Name: byebyebios
Version: 1.0
Release:        8%{?dist}
Summary:        Injects a x86 boot sector to inform of UEFI boot requirement
License: MIT-0
Url: https://gitlab.com/berrange/byebyebios
Source0:        https://gitlab.com/berrange/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
ExclusiveArch: x86_64
BuildArch: noarch
# oreon:deps
BuildRequires:  binutils
BuildRequires:  make
BuildRequires:  parted
BuildRequires:  python3-docutils
BuildRequires:  qemu-system-x86-core
# /oreon:deps
%description
The byebyebios package provides an x86 boot sector that should
be copied to any disk image that does not intend to support
use of BIOS firmware. It will display a message to the user,
on the first serial port and VGA console, informing them of
the requirement to boot using UEFI firmware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%__make
%check

%__make test
%install
%make_install \
    DESTDIR=$RPM_BUILD_ROOT \
    bindir=%{_bindir} \
    datadir=%{_datadir} \
    mandir=%{_mandir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
