%global source0_hash dc31ee7d52b8525223b041cb69a084816f092ffaae039cfa0c6f40f85024ab78
Name:		open-amp
Version:	2026.04.0
Release:        1%{?dist}
Summary:        Open Asymmetric Multi Processing (OpenAMP) framework project
License:	BSD-3-Clause OR BSD-2-Clause
URL:		https://github.com/OpenAMP/open-amp/
Source0:        https://github.com/OpenAMP/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libmetal-devel
BuildRequires:  libsysfs-devel
# /oreon:deps
%description
The OpenAMP framework provides software components that enable development of
software applications for Asymmetric Multiprocessing (AMP) systems.

%package libs
Summary:	Libaries for OpenAMP
Obsoletes:	open-amp <= 2025.04.0
Provides:	open-amp
%description libs
Libaries for OpenAMP baremetal, and RTOS environments.

%package devel
Summary:	Development files for OpenAMP
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development file for OpenAMP
baremetal, and RTOS environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DWITH_STATIC_LIB=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n open-amp-libs -f %{oreon_filedir}/open-amp-libs.list
%files -n open-amp-devel -f %{oreon_filedir}/open-amp-devel.list

%changelog

%autochangelog
