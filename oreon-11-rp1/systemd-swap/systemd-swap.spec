%global source0_hash 61e59919778a96880f0bff414cdd09f6c336bb3e60e5979630645dc739041b20

Name: systemd-swap
Summary: Creating hybrid swap space from zram swaps, swap files and swap partitions
Version: 3.3.0
Release: 19%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://github.com/Nefelim4ag/%{name}
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Not schred swapfc file on ext4
Patch0: %{url}/commit/9f843c41a185b8972470e8ce828cadffea936b59.patch

BuildArch: noarch

BuildRequires: make
%if 0%{?fedora} >= 31
BuildRequires: systemd-rpm-macros
%else
BuildRequires: systemd-units
%endif
%{?systemd_requires}

BuildRequires: help2man

# support for zram
Requires: util-linux
Requires: kmod

# need Linux kernel version 2.6.37.1 or better to use zram
#Requires: kernel >= 2.6.37.1
Requires: kmod(zram.ko)

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
# nothing

%install
%make_install PREFIX=%{buildroot}
pushd %{buildroot}
install -d .%{_unitdir}
find . -name '*.service' -print -exec mv '{}' .%{_unitdir} \;
install -d .%{_mandir}/man1
help2man -o .%{_mandir}/man1/%{name}.1 .%{_bindir}/%{name}

%post
%systemd_post mkzram.service

%preun
%systemd_preun mkzram.service

%postun
%systemd_postun_with_restart mkzram.service

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/systemd/swap.conf
%{_unitdir}/*.service
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
