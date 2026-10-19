%global source0_hash 0be289da7f43b1892575f14b27860af5d1e1f6961eae11653d64e625fd7924b7
Name:           libclaw
Version:        1.7.4
Release:        45%{?dist}
Summary:        C++ Library of various utility functions
License:        LicenseRef-Callaway-LGPLv2
URL:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         libclaw-1.6.1-nostrip.patch
Patch1:         libclaw-1.7.4-libdir.patch
Patch2:         libclaw-1.7.4-gcc62.patch
Patch3:         libclaw-1.7.4-noarch.patch
Patch4:         libclaw-1.7.4-gcc7.patch
Patch5:         libclaw-c++20-no-concept-keyword.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Claw (C++ Library Absolutely Wonderful) is a C++ library of various utility
functions. In doesn't have a particular objective but being useful to
anyone.

%package devel
Summary:        Development files for Claw library
Requires:       %{name} = %{version}-%{release}
Requires:       cmake
Requires:       boost-devel%{?_isa}
Requires:       libjpeg-devel%{?_isa}
Requires:       libpng-devel%{?_isa}
%description devel
This package contains files needed to develop and build software against
Claw (C++ Library Absolutely Wonderful).

%package doc
Summary:        Documentation for Claw library
BuildArch:      noarch
%description doc
This package contains documentation for Claw (C++ Library Absolutely
Wonderful).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done
%install
%cmake_install
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libclaw-devel -f %{oreon_filedir}/libclaw-devel.list
%files -n libclaw-doc -f %{oreon_filedir}/libclaw-doc.list

%changelog

%autochangelog
