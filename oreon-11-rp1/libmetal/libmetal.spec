%global source0_hash 9d7488915db9710b0d394c7a3e6f2af998b7ae2e8a04cfcf7360f0d614f5c8ae
Name:		libmetal
Version:	2026.04.0
Release:        1%{?dist}
Summary:        An abstraction layer across user-space Linux, baremetal, and RTOS environments
License:	BSD-3-Clause OR Apache-2.0 OR GPL-2.0-only
URL:		https://github.com/OpenAMP/libmetal/
Source0:        https://github.com/OpenAMP/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libmetal-add-additional-arches.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libsysfs-devel
# /oreon:deps
%description
An abstraction layer across user-space Linux, baremetal, and RTOS environments.

%package devel
Summary: 	Development files for libmetal
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.

%package doc
Summary:	Documentation files for libmetal
BuildArch:	noarch
%description doc
Documentation file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DWITH_STATIC_LIB=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmetal-devel -f %{oreon_filedir}/libmetal-devel.list
%files -n libmetal-doc -f %{oreon_filedir}/libmetal-doc.list

%changelog

%autochangelog
