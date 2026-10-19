%global source0_hash fe0942a80434cfe9136d385035b3eec3dc08e84b1826bf26bf033c663ad5299b
Name:           python-pynest2d
Version:        5.2.0
Release:        1%{?dist}
Summary:        Python bindings for libnest2d
License:        LGPL-3.0-only
URL:            https://github.com/Ultimaker/pynest2d
Source0:        https://github.com/Ultimaker/pynest2d/archive/%{version}/pynest2d-%{version}.tar.gz
Patch0:         pynest2d-PyQt5.sip.patch
Patch1:         Retrieve-required-flags-from-Libnest2D-target.patch
Requires:       python3-pyqt5-sip
# oreon:deps
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libnest2d-static
BuildRequires:  python3-devel
BuildRequires:  python3-pyqt5-sip
BuildRequires:  python3-sip-devel
# /oreon:deps
%description
Binding allowing libnest2d to be called from Python using NumPy.

%package -n python3-pynest2d
Summary:        Python bindings for libnest2d
%description -n python3-pynest2d
Binding allowing libnest2d to be called from Python using NumPy.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pynest2d-%{version} -p1

# Boost 1.75+ needs C++14, upstream: https://github.com/Ultimaker/pynest2d/pull/7
sed -i 's/CMAKE_CXX_STANDARD 11/CMAKE_CXX_STANDARD 14/' CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles python3-pynest2d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pynest2d -f %{oreon_filedir}/python3-pynest2d.list

%changelog

%autochangelog
