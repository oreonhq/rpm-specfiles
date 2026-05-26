# asio only ships headers, so no debuginfo package is needed
%global debug_package %{nil}

Name:           asio
Version:        1.30.2
Release:        %autorelease
Summary:        A cross-platform C++ library for network programming

License:        BSL-1.0
URL:            https://think-async.com
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 9f12cef05c0477eace9c68ccabd19f9e3a04b875d4768c323714cbd3a5fa3c2b
%global source0_file asio-1.30.2.tar.bz2
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/asio-1.30.2.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9f12cef05c0477eace9c68ccabd19f9e3a04b875d4768c323714cbd3a5fa3c2b" || { echo "oreon: Source0 SHA256 mismatch for asio-1.30.2.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
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
%{_libdir}/pkgconfig/asio.pc

%files doc
%doc doc/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.30.2-1
- Prepare for Oreon 11 (RP1)
