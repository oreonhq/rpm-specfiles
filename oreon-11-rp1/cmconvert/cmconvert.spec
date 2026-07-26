%global source0_hash 8f79d26cd4a8b4e70053bee0d53cfdbc93c1e6e1a5cb95e0fbc643dfe1313076

Name: cmconvert
Summary: CacheMate import file converter 
Version: 1.9.6
Release: 35%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.smittyware.com/palm/cachemate/tools.php
Source0: http://www.smittyware.com/download/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: expat-devel
BuildRequires: zziplib-devel
BuildRequires: zlib-devel
BuildRequires: make

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

%files 
%doc ChangeLog README
%license COPYING
%{_bindir}/cmconvert
%{_mandir}/man1/cmconvert.1*

%changelog
%autochangelog
