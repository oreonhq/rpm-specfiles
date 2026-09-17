%global source0_hash e5f82dd90001ed53200b2383bcfd520b1d8ee06d6a2a75b39d37d68daef20c88

Name:           fpart
Version:        1.7.0
Release:        %autorelease
Summary:        Helps you sort file trees and pack them into bags
# main source is BSD-2-Clause
# src/fts.c and src/fts.h are BSD-3-Clause
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://fpart.org
Source:         https://github.com/martymac/fpart/archive/fpart-%{version}.tar.gz

BuildRequires:  gcc autoconf automake
BuildRequires:  make

%description
Fpart is a Filesystem partitioner.  It helps you sort file trees and pack them
into bags (called "partitions").  It is developed in C and available under the
BSD license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n fpart-fpart-%{version}

%build
autoreconf --install
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc docs/www.fpart.org/docs/changelog.md README.md
%{_mandir}/man1/fpart.1*
%{_mandir}/man1/fpsync.1*
%{_bindir}/fpart
%{_bindir}/fpsync

%changelog
%autochangelog
