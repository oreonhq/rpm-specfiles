%global source0_hash 5c32bf347956d4252a25c49fc1304d8b0fc9fa1939c143eb37e720e99e6783f5

Name: byebyebios
Version: 1.0
Release: 8%{?dist}
Summary: Injects a x86 boot sector to inform of UEFI boot requirement
License: MIT-0
Url: https://gitlab.com/berrange/byebyebios
Source: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
ExclusiveArch: x86_64
BuildArch: noarch

BuildRequires: make
BuildRequires: python3-docutils
BuildRequires: binutils
BuildRequires: qemu-system-x86-core
BuildRequires: parted

%description
The byebyebios package provides an x86 boot sector that should
be copied to any disk image that does not intend to support
use of BIOS firmware. It will display a message to the user,
on the first serial port and VGA console, informing them of
the requirement to boot using UEFI firmware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

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

%files
%license LICENSES/MIT-0.txt
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/nouefi.txt
%{_datadir}/%{name}/bootstub.bin
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
