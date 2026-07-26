%global source0_hash 7ebc1cf881a8686dcbf7a382e47caecd70fbd6e1eb975ce8a4d41b53ef485ab7

# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python-pynest2d
Version:        4.8.0
Release:        %autorelease
Summary:        Python bindings for libnest2d
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/Ultimaker/pynest2d
Source:         %{url}/archive/%{version}/pynest2d-%{version}.tar.gz
# Downstream patch: add PyQt5 namespace
Patch0:         pynest2d-PyQt5.sip.patch
# Retrieve required flags from Libnest2D target
# https://github.com/Ultimaker/pynest2d/pull/3
Patch1:         Retrieve-required-flags-from-Libnest2D-target.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libnest2d-static
BuildRequires:  python3-devel
BuildRequires:  python3-sip-devel < 5
BuildRequires:  python3-pyqt5-sip
Requires:       python3-pyqt5-sip

# we add a dependency on setuptools to provide the distutils module
# upstream already removed the distutils usage in version 5+
BuildRequires:  (python3-setuptools if python3-devel >= 3.12)

%description
Binding allowing libnest2d to be called from Python using NumPy.

%package -n python3-pynest2d
Summary:        %{summary}

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

%files -n python3-pynest2d
%license LICENSE
%doc README.md
%{python3_sitearch}/pynest2d.so

%changelog
%autochangelog
