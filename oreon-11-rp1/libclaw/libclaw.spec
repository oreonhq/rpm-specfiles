%global source0_hash 0be289da7f43b1892575f14b27860af5d1e1f6961eae11653d64e625fd7924b7

Name:           libclaw
Version:        1.7.4
Release:        45%{?dist}
Summary:        C++ Library of various utility functions
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://libclaw.sourceforge.net/
Source0:        http://dl.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         libclaw-1.6.1-nostrip.patch
Patch1:         libclaw-1.7.4-libdir.patch
Patch2:         libclaw-1.7.4-gcc62.patch
# Make documentation the same on different arches
Patch3:         libclaw-1.7.4-noarch.patch
# Fix errors found by GCC 7 (and Clang)
Patch4:         libclaw-1.7.4-gcc7.patch
# Fix example build with C++20 by avoiding reserved keyword 'concept' 
Patch5:         libclaw-c++20-no-concept-keyword.patch

BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  boost-devel

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

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2380711)
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

%files -f %{name}.lang
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/claw-config
%{_includedir}/claw
%{_libdir}/cmake/%{name}
%{_libdir}/*.so
%exclude %{_libdir}/*.a

%files doc
%license COPYING
%doc %{_datadir}/doc/libclaw1
%doc examples

%changelog
%autochangelog
