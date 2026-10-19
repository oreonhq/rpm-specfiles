%global source0_hash cefd7554c877e1bc76987d2b96b23f7699a2e5340c254454f61b6e0dae370aa7
Name:          udpcast
Summary:        UDP broadcast file distribution and installation
Version:       20250223
Release:        1%{?dist}
License:       GPL-2.0-or-later AND BSD-2-Clause-first-lines AND MPL-1.1
URL:           http://udpcast.linux.lu/
Source0:        https://www.udpcast.linux.lu/download/%{name}-%{version}.tar.gz
Patch1:        udpcast-20200328-read-warn.patch
Patch2:        udpcast-20211207-makefile-in.patch
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}
%description devel
Command-line client for UDP sender and receiver.  Udpcast is an
application for multicasting data to multiple targets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
rm -rf $RPM_BUILD_ROOT
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n udpcast-devel -f %{oreon_filedir}/udpcast-devel.list

%changelog

%autochangelog
