%global source0_hash e41fb5a97c74a7e9c7d012e864a622096e819180bec504069e34664f6a360531

Name:           minipro
Version:        0.7.4
Release:        2%{?dist}
Summary:        Utility for MiniPro TL866A/TL866/CS programmer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gitlab.com/DavidGriffith/minipro
Source0:        https://gitlab.com/DavidGriffith/minipro/-/archive/%{version}/minipro-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-udev
Requires:       systemd-udev
# for dump-alg-minipro.bash
Requires:       bsdtar
Requires:       coreutils
Requires:       curl

%description
Programming utility compatible with Minipro TL866CS and Minipro TL866A
programmers.

Supports programming more than 16000 kinds of devices (including AVRs,
PICs, GALs and EPROMs) as well as testing logic devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{make_build} PREFIX=%{_prefix} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
%{make_install} PREFIX=%{_prefix} COMPLETIONS_DIR=%{_datadir}/bash-completion/completions
# This is obsolete; we just keep the uaccess rule
rm %{buildroot}%{_udevrulesdir}/61-minipro-plugdev.rules

%files
%license LICENSE
%{_datadir}/bash-completion/completions
%{_bindir}/minipro
%{_bindir}/dump-alg-minipro.bash
%{_udevrulesdir}/60-minipro.rules
%{_udevrulesdir}/61-minipro-uaccess.rules
%{_datadir}/%{name}/infoic.xml
%{_datadir}/%{name}/logicic.xml
%{_mandir}/man1/minipro.1*

%changelog
%autochangelog
