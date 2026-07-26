%global source0_hash 7ed70e903082bfa6045e3b2be2f4396cb57d985d59f567ec06ca5b93d894ba42

Name:           libzrtpcpp
Version:        4.6.6
Release:        24%{?dist}
Summary:        ZRTP support library for the GNU ccRTP stack

License:        GPL-3.0-or-later
URL:            https://github.com/wernerd/ZRTPCPP
Source0:        https://github.com/wernerd/ZRTPCPP/archive/V%{version}/%{name}-%{version}.tar.gz
# Look. Don't put #warning statements in header files that every application
# needs to include. Most modern things treat warnings as errors, causing every
# dependent build to fail, even if its not even calling zrtp_getSasType
Patch0:         libzrtpcpp-4.4.0-no-warning.patch
# Fix build with gcc15
Patch1:         libzrtpcpp-gcc15.patch
# Increase minimum cmake version
Patch2:         libzrtpcpp_cmakever.patch
# Fix invalid variable expansion in cmake file
Patch3:         libzrtpcpp_cmakesyntax.patch

BuildRequires:  ccrtp-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel

%description
This package provides a library that adds ZRTP support to the GNU
ccRTP stack. Phil Zimmermann developed ZRTP to allow ad-hoc, easy to
use key negotiation to setup Secure RTP (SRTP) sessions. GNU ZRTP
together with GNU ccRTP (1.5.0 or later) provides a ZRTP
implementation that can be directly embedded into client and server
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ZRTPCPP-%{version}
# Make the NEWS.md file non executable
chmod 644 NEWS.md

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md AUTHORS NEWS.md
%license COPYING
%{_libdir}/libzrtpcpp.so.4*

%files devel
%{_includedir}/libzrtpcpp/
%{_libdir}/libzrtpcpp.so
%{_libdir}/pkgconfig/libzrtpcpp.pc

%changelog
%autochangelog
