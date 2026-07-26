%global source0_hash df106300a7b1d4a9e35fe122dfca3432ffd02249e65043f429da5dadc5284382

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

Name:           libnest2d
%global commit  da4782500da4eb8cb6e38e5e3f10164ec5a59778
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Version:        0.4^20200805git%{shortcommit}
Release:        %autorelease
Summary:        Library for the 2D bin packaging problem
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/tamasmeszaros/libnest2d
Source:         %{url}/archive/%{commit}/libnest2d-%{shortcommit}.tar.gz

# Add disallowed areas
Patch0:         %{url}/pull/18.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  polyclipping-devel
BuildRequires:  pkgconfig(nlopt)

# This is a header only library
%global debug_package %{nil}

%description
A library and framework for the 2D bin packaging problem.

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       boost-devel
Requires:       polyclipping-devel
Requires:       pkgconfig(nlopt)

%description devel
A library and framework for the 2D bin packaging problem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1
sed -i -e "s/ lib\([^n]\)/ "%{_lib}"\1/" CMakeLists.txt

%build
%cmake -DLIBNEST2D_HEADER_ONLY=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/libnest2d/
%{_libdir}/cmake/Libnest2D/

%changelog
%autochangelog
