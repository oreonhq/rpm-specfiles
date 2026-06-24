%global source0_hash none

Summary:	Open audio/video container format library
Name:		libmatroska
Version:	1.7.1
Release:	13%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://www.matroska.org/
Source0:	https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
Patch0:		%{name}-cmake-4.0.patch
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	libebml-devel >= 1.4.4
Requires:	libebml%{_isa} >= 1.4.4

%description
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).


%package	devel
Summary:	Matroska container format library development files
Requires:	%{name}%{_isa} = %{version}-%{release}
Requires:	cmake-filesystem
Requires:	libebml-devel%{_isa} >= 1.4.4
Requires:	pkgconfig

%description	devel
Matroska is an extensible open standard Audio/Video container.  It
aims to become THE standard of multimedia container formats.  Matroska
is usually found as .mkv files (matroska video) and .mka files
(matroska audio).

This package contains the files required to rebuild applications which
will use the Matroska container format.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .cmake4


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.LGPL
%doc NEWS.md README.md
%{_libdir}/%{name}.so.7{,.*}

%files devel
%{_includedir}/matroska/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_libdir}/cmake/Matroska
%{_libdir}/cmake/Matroska/MatroskaConfig.cmake
%{_libdir}/cmake/Matroska/MatroskaConfigVersion.cmake
%{_libdir}/cmake/Matroska/MatroskaTargets-noconfig.cmake
%{_libdir}/cmake/Matroska/MatroskaTargets.cmake


%changelog
%autochangelog

