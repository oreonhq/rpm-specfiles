%global source0_hash 6d6338f3b5e4d2bef66ad37a94e292d5acaefacfad32652d0cf3245465fba7e9
Summary:        Command-line program to read and set MPEG-4 tags compatible with iPod/iTunes
URL:       http://atomicparsley.sourceforge.net/
Name:      AtomicParsley
Version:   20240608.083822.1ed9031
Release:        1%{?dist}
License:   GPL-2.0-or-later
Source0:        https://bitbucket.org/wez/atomicparsley/overview/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
# /oreon:deps
%description
AtomicParsley is a command line program for reading, parsing and setting
tags and meta-data into MPEG-4 files supporting these styles of meta-data:

* iTunes-style meta-data into .mp4, .m4a, .m4p, .m4v, .m4b files
* 3gp-style assets (3GPP TS 26.444 version 6.4.0 Release 6 specification
  conforming) in 3GPP, 3GPP2, MobileMP4 & derivatives
* ISO copyright notices at movie & track level for MPEG-4 & derivative files
* uuid private user extension text & file embedding for MPEG-4 & derivative
  files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./autogen.sh
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make install install DESTDIR=%{buildroot} BINDIR=%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
