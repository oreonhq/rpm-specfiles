%global source0_hash none

Summary:    Extensible Binary Meta Language library
Name:       libebml
Version:    1.4.5
Release:    6%{?dist}
License:    LGPL-2.1-or-later
URL:        https://www.matroska.org/
Source:     https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
Patch0:     %{name}-use-system-utf8cpp.patch
Patch1:     %{name}-cmake-4.0.patch
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: utf8cpp-devel

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


%files
%license LICENSE.LGPL
%doc NEWS.md
%{_libdir}/%{name}.so.5{,.*}

%files devel
%{_includedir}/ebml/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/EBML
%{_libdir}/cmake/EBML/EBMLConfig.cmake
%{_libdir}/cmake/EBML/EBMLConfigVersion.cmake
%{_libdir}/cmake/EBML/EBMLTargets-noconfig.cmake
%{_libdir}/cmake/EBML/EBMLTargets.cmake


%changelog
%autochangelog

