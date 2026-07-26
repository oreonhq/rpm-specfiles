%global source0_hash 196042a19f3eee02a6754a9e1ef4b40412ffdf3695f8746ef19baec62d2dbeb2

%global		_hardened_build 1

Name:		libdkimpp
Version:	2.0.0
Release:	22%{?dist}
Summary:	Lightweight and portable DKIM (RFC4871) library

License:	LGPL-3.0-or-later
URL:		https://github.com/halonsecurity/libdkimpp
Source0:	https://github.com/halonsecurity/libdkimpp/archive/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	coreutils
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	sed

BuildRequires:	pkgconfig(cppunit)
BuildRequires:	openssl-devel
BuildRequires:	libsodium-devel

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

%files
%license LICENSE
%doc README.md
%{_libdir}/libdkim++.so.*

%files devel
%{_includedir}/libdkim++
%{_libdir}/libdkim++.so
%{_libdir}/pkgconfig/libdkim++.pc

%changelog
%autochangelog
