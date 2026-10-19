%global source0_hash 512a82320cf5418ed70416b96cd49aa51a5ae418e96482144683cad6609add2e
Name:           fpart
Version:        1.7.1
Release:        1%{?dist}
Summary:        Helps you sort file trees and pack them into bags
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://fpart.org
Source0:        https://github.com/martymac/fpart/archive/fpart-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Fpart is a Filesystem partitioner.  It helps you sort file trees and pack them
into bags (called "partitions").  It is developed in C and available under the
BSD license.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fpart-fpart-%{version}
%oreon_prep
%build

autoreconf --install
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
