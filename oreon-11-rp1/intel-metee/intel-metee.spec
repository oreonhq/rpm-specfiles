%global source0_hash 1ec21e30fd068e52009832ab8d2b5451cfd482db2b3a1ca5b910026632ab94f8
%global upstream_name metee
Name:		intel-metee
Version:	6.1.0
Release:        1%{?dist}
Summary:        Cross-platform access library for Intel CSME HECI interface
License:	Apache-2.0 AND BSD-3-Clause AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause)
URL:		https://github.com/intel/metee
Source0:        https://github.com/intel/%{upstream_name}/archive/%{version}/%{upstream_name}-%{version}.tar.gz
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
Cross-platform access library for Intel CSME HECI interface.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via an mei
interface.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%package	doc
Summary:	Documentation files for %{name}
BuildArch:	noarch
%description	doc
The %{name}-doc package contains documentation files for %{name}.
ME TEE Library is a C library to access CSE/CSME/GSC firmware via a mei
interface.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{version}

%build

%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DBUILD_SHARED_LIBS=ON \
   -DBUILD_DOCS=YES
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n intel-metee-devel -f %{oreon_filedir}/intel-metee-devel.list
%files -n intel-metee-doc -f %{oreon_filedir}/intel-metee-doc.list

%changelog

%autochangelog
