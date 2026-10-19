%global source0_hash 4ad5b7279da14f6aa16fa3e6dcd2ecc06b558b22a69d044c4cedd258bd7e0c3e
Name:           openarm-can
Version:        1.4.0
Release:        1%{?dist}
Summary:        OpenArm CAN control library
License:        Apache-2.0
URL:            https://docs.openarm.dev/software/can
Source0:        https://github.com/enactic/openarm_can/archive/%{version}/openarm_can-%{version}.tar.gz
Provides:       openarm_can = %{version}-%{release}
Obsoletes:      openarm_can <= 1.1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
A C++ library for CAN communication with OpenArm robotic hardware,
supporting Damiao motors over CAN/CAN-FD interfaces. This library
is a part of OpenArm.

%package devel
Summary:   Development files for OpenARM CAN control library
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and development libraries for OpenARM CAN control library.

%package utils
Summary: Setup and configuration utility scripts
%description utils
Setup and configuration utility scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir openarm_can-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openarm-can-devel -f %{oreon_filedir}/openarm-can-devel.list
%files -n openarm-can-utils -f %{oreon_filedir}/openarm-can-utils.list

%changelog

%autochangelog
