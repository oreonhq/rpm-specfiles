%global source0_hash 88945b5abc11d8f4cea2bb7028e545024a6e060650bd65527a29bc9400daead8
Summary:        Library for interfacing Music Player Daemon
Name:          libmpdclient
Version:       2.27
Release:        1%{?dist}
License:       BSD-2-Clause OR BSD-3-Clause
URL:           https://www.musicpd.org/
Source0:        https://www.musicpd.org/download/%{name}/2/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson
# /oreon:deps
%package devel
Summary: Header files for developing programs with %{name}
Requires: %{name} = %{version}-%{release}
%description
A stable, documented, asynchronous API library for interfacing MPD
in the C, C++ & Objective C languages.

%description devel
%{name}-devel is a sub-package which contains header files and
libraries for developing programs with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -D documentation=true
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-devel
mv %{buildroot}%{_defaultdocdir}/%{name}/html %{buildroot}%{_defaultdocdir}/%{name}-devel
rm %{buildroot}%{_defaultdocdir}/%{name}/BSD-[23]-Clause.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmpdclient-devel -f %{oreon_filedir}/libmpdclient-devel.list

%changelog

%autochangelog
