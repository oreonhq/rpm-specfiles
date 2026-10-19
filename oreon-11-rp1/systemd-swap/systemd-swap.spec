%global source0_hash efafcf8dcd67af8237ca269cddb487f4be8101e039f6ee94f7f7ad92a3cdbd4e
Name: systemd-swap
Summary:        Creating hybrid swap space from zram swaps, swap files and swap partitions
Version: 4.4.0
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://github.com/Nefelim4ag/%{name}
Source0:        https://github.com/Nefelim4ag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: %{url}/commit/9f843c41a185b8972470e8ce828cadffea936b59.patch
BuildArch: noarch
%{?systemd_requires}
Requires: util-linux
Requires: kmod
Requires: kmod(zram.ko)
# oreon:deps
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  systemd-units
# /oreon:deps
%description
Manage swap on:
    zswap - Enable/Configure
    zram - Autoconfigurating
    files - (sparse files for saving space, support btrfs)
    block devices - auto find and do swapon
It is configurable in /etc/systemd/swap.conf

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n%{name}-%{version}
# preserve timestamps
sed -i -r 's:install -:\0p -:' Makefile

%build

%install
%make_install PREFIX=%{buildroot}
pushd %{buildroot}
install -d .%{_unitdir}
find . -name '*.service' -print -exec mv '{}' .%{_unitdir} \;
install -d .%{_mandir}/man1
help2man -o .%{_mandir}/man1/%{name}.1 .%{_bindir}/%{name}
%oreon_autofiles main

%post

%systemd_post mkzram.service
%preun

%systemd_preun mkzram.service
%postun

%systemd_postun_with_restart mkzram.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
