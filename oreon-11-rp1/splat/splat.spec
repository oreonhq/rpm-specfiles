%global source0_hash 39b0b314e2e927bdf00d1eda4b9865efd128ba850305f987aec049c4fd58a29c

Name:		splat
Version:	1.4.2
Release:	25%{?dist}
Summary:	Analyze point-to-point terrestrial RF communication links
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later

URL:		http://www.qsl.net/kd2bd/%{name}.html
Source0:	http://www.qsl.net/kd2bd/%{name}-%{version}.tar.bz2

# Man pages for utilities, generated from utils README file
Source1:	citydecoder.man
Source2:	srtm2sdf.man
Source3:	usgs2sdf.man
Source4:	bearing.man
Source5:	postdownload.1
Source6:        splat.1

# Configuration parameters
Source7:        std-parms.h
Source8:        hd-parms.h

# Build flags patch
Patch0:		%{name}-%{version}-build_flags.patch

BuildRequires:	gcc-c++
BuildRequires:	bzip2-devel
BuildRequires:	groff
BuildRequires:	zlib-devel

%description
SPLAT! is a Surface Path Length And Terrain analysis application written for
Linux and Unix workstations. SPLAT! analyzes point-to-point terrestrial RF 
communication links, and provides information useful to communication system
designers and site engineers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

install -p %{SOURCE7} .
%ifarch x86_64
install -p %{SOURCE8} .
%endif

# Fix end of line encoding
sed -i 's/\r//' utils/fips.txt

%build
# Uses custom build scripts
./build all

%install
# Build additional man pages
mkdir -p %{buildroot}%{_mandir}/man1/
groff -e -T ascii -man %{SOURCE1} > %{buildroot}%{_mandir}/man1/citydecoder.1
groff -e -T ascii -man %{SOURCE2} > %{buildroot}%{_mandir}/man1/srtm2sdf.1
groff -e -T ascii -man %{SOURCE3} > %{buildroot}%{_mandir}/man1/usgs2sdf.1
groff -e -T ascii -man %{SOURCE4} > %{buildroot}%{_mandir}/man1/bearing.1
install -pm 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/postdownload.1
install -pm 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/splat.1
install -D -pm 0644 docs/spanish/man/%{name}.1 %{buildroot}%{_mandir}/es/man1/splat.1

# Manual install, easier than patching upstream custom install script
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%ifarch x86_64
install -D -m 0755 %{name}-hd %{buildroot}%{_bindir}/%{name}-hd
%endif

# Install utils
install -D -m 0755 utils/citydecoder %{buildroot}%{_bindir}/citydecoder
install -D -m 0755 utils/bearing %{buildroot}%{_bindir}/bearing
install -D -m 0755 utils/postdownload %{buildroot}%{_bindir}/postdownload
install -D -m 0755 utils/usgs2sdf %{buildroot}%{_bindir}/usgs2sdf
install -D -m 0755 utils/srtm2sdf %{buildroot}%{_bindir}/srtm2sdf

# Rename this to avoid conflict with main readme
mv utils/README utils/README-utils

%files
%license COPYING
%doc CHANGES README utils/README-utils utils/fips.txt
%doc sample_data
%{_bindir}/*
%{_mandir}/es/man1/*
%{_mandir}/man1/*

%changelog
%autochangelog
