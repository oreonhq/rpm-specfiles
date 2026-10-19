%global source0_hash e41fb5a97c74a7e9c7d012e864a622096e819180bec504069e34664f6a360531
Name:           minipro
Version:        0.7.4
Release:        2%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer
License:        GPL-3.0-or-later
URL:            https://gitlab.com/DavidGriffith/minipro
Source0:        https://gitlab.com/DavidGriffith/minipro/-/archive/%{version}/minipro-%{version}.tar.gz
Requires:       systemd-udev
Requires:       bsdtar
Requires:       coreutils
Requires:       curl
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-udev
# /oreon:deps
%description
Programming utility compatible with Minipro TL866CS and Minipro TL866A
programmers.

Supports programming more than 16000 kinds of devices (including AVRs,
PICs, GALs and EPROMs) as well as testing logic devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{make_build} PREFIX=%{_prefix} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"
%install
%{make_install} PREFIX=%{_prefix} COMPLETIONS_DIR=%{_datadir}/bash-completion/completions
rm %{buildroot}%{_udevrulesdir}/61-minipro-plugdev.rules
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
