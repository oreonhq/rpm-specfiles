%global source0_hash c5d78292f553cf0229746bb8a6d23085c6a75bf282bc36c0e3539e7499005bbc
%global		_hardened_build 1
Name:		libdkimpp
Version:	2.4.1
Release:        1%{?dist}
Summary:        Lightweight and portable DKIM (RFC4871) library
License:	LGPL-3.0-or-later
URL:		https://github.com/halonsecurity/libdkimpp
Source0:        https://github.com/halonsecurity/libdkimpp/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  sed
# /oreon:deps
%description
libdkim++ is a lightweight and portable DKIM (RFC4871) library for *NIX,
supporting both signing and DMARC/SDID/ADSP verification, sponsored and
used by Halon Security. libdkim++ has extensive unit test coverage and
aims to fully comply with the current RFC.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and libraries for developing
with %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# avoid invalid path
sed -i 's|/usr/local/lib|%{_libdir}|g' CMakeLists.txt

%build

%cmake
%cmake_build
%check

%ctest
%install
%cmake_install
chmod +x $RPM_BUILD_ROOT/%{_libdir}/*.so*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdkimpp-devel -f %{oreon_filedir}/libdkimpp-devel.list

%changelog

%autochangelog
