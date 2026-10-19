%global source0_hash 7813654c4a41999f2cf2d456fe73d30fe31c11656d12d2c5483d199df01ba9eb
Name: cmconvert
Summary:        CacheMate import file converter
Version: 1.9.6
Release:        35%{?dist}
License: GPL-2.0-or-later
URL: http://www.smittyware.com/palm/cachemate/tools.php
Source0:        http://www.smittyware.com/download/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
# /oreon:deps
%description 
This program is used to convert EasyGPS XML file formats (LOC and GPX) to
a format that can be installed onto a Palm OS device and imported into
CacheMate.  Options are also available to list waypoints contained in an
XML file, and selectively convert specified waypoints.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

%build 

%configure
make %{?_smp_mflags}
%install 
rm -fr %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
