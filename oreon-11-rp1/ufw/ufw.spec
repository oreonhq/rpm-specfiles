%global source0_hash 662f865bc83bf8aa1a40a6fe578bc2ce796ff60a1be2c1103def7db1b91f8509
Name:           ufw
Version:        0.36.2
Release:        1%{?dist}
Summary:        Uncomplicated Firewall
License:        GPL-3.0-only
URL:            https://launchpad.net/%{name}
Source0:        https://launchpad.net/%{name}/%{version}/%{version}/+download/ufw-%{version}.tar.gz
Source1:        ufw.service
Patch0:         ufw-0.35-trans-dir.patch
Patch1:         ufw-0.35-libexec-dir.patch
Patch2:         ufw-0.34~rc-default-enabled.patch
Patch3:         ufw-0.34~rc-default-allow-ssh.patch
Patch4:         ufw-0.34~rc-multicast.patch
Patch5:         ufw-0.34~rc-additional-profiles.patch
Patch6:         ufw-0.35-python36.patch
Patch7:         ufw-0.35-permissions.patch
Patch8:         ufw-0.35-no-pointless-env.patch
Patch9:         ufw-0.35-distutils-setuptools.patch
BuildArch:      noarch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:       systemd
Requires:       iptables
# oreon:deps
BuildRequires:  gettext
BuildRequires:  iptables
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd
# /oreon:deps
%description
The Uncomplicated Firewall(ufw) is a front-end for netfilter, which
aims to make it easier for people unfamiliar with firewall concepts.
Ufw provides a framework for managing netfilter as well as
manipulating the firewall.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .trans-dir
%patch -P1 -p1 -b .libexec-dir
%patch -P2 -p1 -b .default-enabled
%patch -P3 -p1 -b .default-allow-ssh
%patch -P4 -p1 -b .multicast
rm -f profiles/*.multicast
%patch -P5 -p1 -b .additional-profiles
rm -f profiles/*.additional-profiles
%patch -P6 -p1 -b .python36
%patch -P7 -p1 -b .permissions
%patch -P8 -p1 -b .no-pointless-env
%patch -P9 -p1 -b .distutils-setuptools

%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
sed -e "s/'sbin'/'bin'/" -i setup.py
%endif

%build

%py3_build
%install
%py3_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/ufw.service
%find_lang %{name}
%oreon_autofiles main

%post

%systemd_post ufw.service
%preun

%systemd_preun ufw.service
%postun

%systemd_postun_with_restart ufw.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
