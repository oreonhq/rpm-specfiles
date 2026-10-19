%global source0_hash 584925f0eafd57293fa7af62cc3820e47e3889a60d00543b0969716b808d0a8b
Name:     libirc
Version:  0.2.2
Release:        1%{?dist}
Summary:        IRC client library for C
License:  GPL-3.0-only
URL:      https://github.com/n0la/libirc
Source0:        https://github.com/n0la/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:   i686
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  libcmocka-devel
BuildRequires:  pkgconf
# /oreon:deps
%description
%{summary}.

%package devel
Summary:   Development headers for the libirc library
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers for the libric library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libirc-devel -f %{oreon_filedir}/libirc-devel.list

%changelog

%autochangelog
