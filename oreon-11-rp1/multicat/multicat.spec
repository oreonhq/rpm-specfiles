%global source0_hash 59d91045965104a882aaa7e96a4b23c56b4017f49de6883722039f3a9d31e9d9
Name:           multicat
Version:        2.4
Release:        1%{?dist}
Summary:        Simple and efficient multicast and transport stream manipulation
License:        GPL-2.0-or-later
URL:            https://www.videolan.org/projects/multicat.html
Source0:        https://download.videolan.org/multicat/%{version}/multicat-%{version}.tar.bz2
# oreon:deps
BuildRequires:  bitstream-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Simple and efficient multicast and transport stream manipulation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e 's|-O3|%{optflags}|' Makefile

%build

%make_build
%install
%make_install PREFIX=%{_prefix}
chmod -x %{buildroot}%{_mandir}/man1/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
