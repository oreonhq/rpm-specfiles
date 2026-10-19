%global source0_hash f76c36a46e801ebd6e1f53d06987f148e70c1a4b288da5aba0dce1b3c7b2bf0f
Name:		lsvpd
Version:	1.7.17
Release:        1%{?dist}
Summary:        VPD/hardware inventory utilities for Linux
License:	GPL-2.0-or-later
URL:    https://github.com/power-ras/%{name}/releases
Source0:        https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires(post): %{_sbindir}/vpdupdate
ExclusiveArch:	%{power64}
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  libvpd-devel
BuildRequires:  make
BuildRequires:  sg3_utils-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The lsvpd package contains all of the lsvpd, lscfg and lsmcode
commands. These commands, along with a scanning program
called vpdupdate, constitute a hardware inventory
system. The lsvpd command provides Vital Product Data (VPD) about
hardware components to higher-level serviceability tools. The lscfg
command provides a more human-readable format of the VPD, as well as
some system-specific information.  lsmcode lists microcode and
firmware levels.  lsvio lists virtual devices, usually only found
on POWER PC based systems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./bootstrap.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%post

%{_sbindir}/vpdupdate &
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
