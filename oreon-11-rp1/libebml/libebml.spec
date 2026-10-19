%global source0_hash 5b08214f929ee54c6187c370f84235fc9d0f2a2258c4d320d68eae6e2bdfd3f7
Summary:        Extensible Binary Meta Language library
Name:       libebml
Version:    1.4.7
Release:        1%{?dist}
License:    LGPL-2.1-or-later
URL:        https://www.matroska.org/
Source0:        https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
Patch0:     %{name}-use-system-utf8cpp.patch
Patch1:     %{name}-cmake-4.0.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  utf8cpp-devel
# /oreon:deps
%description
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.

%package    devel
Summary:    Development files for the Extensible Binary Meta Language library
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   cmake-filesystem
Requires:   pkgconfig
%description devel
Extensible Binary Meta Language access library A library for reading
and writing files with the Extensible Binary Meta Language, a binary
pendant to XML.

This package contains the files required to rebuild applications which
will use the Extensible Binary Meta Language library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .utf8cpp
%patch 1 -p1 -b .cmake4
rm -r src/lib/utf8-cpp

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libebml-devel -f %{oreon_filedir}/libebml-devel.list

%changelog

%autochangelog

