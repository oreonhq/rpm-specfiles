%global source0_hash f3e4d406daf7f1399962c43940e4a87de089474d5bcfbf2e6ca516e98bb87cfc
Summary:        Open audio/video container format library
Name:		libmatroska
Version:	1.7.2
Release:        1%{?dist}
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://www.matroska.org/
Source0:        https://dl.matroska.org/downloads/%{name}/%{name}-%{version}.tar.xz
Patch0:		%{name}-cmake-4.0.patch
Requires:	libebml%{_isa} >= 1.4.4
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libebml-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmatroska-devel -f %{oreon_filedir}/libmatroska-devel.list

%changelog

%autochangelog

