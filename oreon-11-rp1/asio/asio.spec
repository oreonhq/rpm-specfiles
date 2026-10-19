%global source0_hash c04e0e66ac29741faad763a56f3c50196421d4b968009fc237c53314769bf8ad
%global debug_package %{nil}
Name:           asio
Version:        1.38.2
Release:        1%{?dist}
Summary:        A cross-platform C++ library for network programming
License:        BSL-1.0
URL:            https://think-async.com
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary:        Header files for asio
Provides:       %{name}-static = %{version}-%{release}
Requires:       openssl-devel
Requires:       boost-devel
%description devel
Header files you can use to develop applications with asio.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package doc
Summary:        Documentation for asio
BuildArch:      noarch
%description doc
Detailed documentation of the asio library.

The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --install
%configure
%make_build
%install
%make_install
%oreon_autofiles asio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles asio-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n asio-devel -f %{oreon_filedir}/asio-devel.list
%files -n asio-doc -f %{oreon_filedir}/asio-doc.list

%changelog

%autochangelog
