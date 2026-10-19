%global source0_hash d144a1c26ab13a197d72929081ca72a5b017bbfcb53bd93c8bea25bf85c8dec8
Name:           docparser
Version:        1.0.26
Release:        1%{?dist}
Summary:        A document parser library ported from document2html
License:        LGPL-3.0-or-later AND CC-BY-4.0 AND CC0-1.0 AND MIT
URL:            https://github.com/linuxdeepin/docparser
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
This file content analysis library is provided for the full-text search function
of document management.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
sed -i 's|Debug|RelWithDebInfo|' CMakeLists.txt

%build

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_bindir}/{docparser_test,docparser_autotest}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/tests/docparser_autotest
%files -f %{oreon_filedir}/main.list
%files -n docparser-devel -f %{oreon_filedir}/docparser-devel.list

%changelog

%autochangelog
