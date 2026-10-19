%global source0_hash bcf27c6ccab787cb41ee2af430d271b4b483319529978e4e2b1770f14db5627b
%global debug_package %{nil}
Name:           simpleini
Version:        4.27
Release:        1%{?dist}
Summary:        Cross-platform C++ library to read and write INI-style configuration files
License:        MIT
URL:            https://github.com/brofield/simpleini
Source0:        https://github.com/brofield/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
# /oreon:deps
%description
simpleini is a cross-platform library that provides a simple API to read and
write INI-style configuration files. It supports data files in ASCII, MBCS and
Unicode. It is designed explicitly to be portable to any platform and has been
tested on Windows, WinCE and Linux. Released as open-source and free using the
MIT licence.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DSIMPLEINI_USE_SYSTEM_GTEST=ON
%cmake_build
%install
%cmake_install
install -pDm644 ConvertUTF.h %{buildroot}%{_includedir}/ConvertUTF.h
install -pDm644 ConvertUTF.c %{buildroot}%{_includedir}/ConvertUTF.c
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n simpleini-devel -f %{oreon_filedir}/simpleini-devel.list

%changelog

%autochangelog
