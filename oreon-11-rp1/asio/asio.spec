%global source0_hash c04e0e66ac29741faad763a56f3c50196421d4b968009fc237c53314769bf8ad

# asio only ships headers, so no debuginfo package is needed
%global debug_package %{nil}

Name:           asio
Version:        1.38.2
Release:        %autorelease
Summary:        A cross-platform C++ library for network programming

License:        BSL-1.0
URL:            https://think-async.com
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl-generators

%description
The asio package contains a cross-platform C++ library for network programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary:        Header files for asio
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
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
%autosetup

%build
autoreconf --install
%configure
%make_build

%install
%make_install

%files devel
%license LICENSE_1_0.txt
%{_includedir}/asio/
%{_includedir}/asio.hpp

%files doc
%doc doc/*

%changelog
%autochangelog
