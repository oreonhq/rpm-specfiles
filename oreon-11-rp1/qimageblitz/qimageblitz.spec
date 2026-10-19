%global source0_hash 9f102269dec50641440e23a449df215a0db9efef9a3969939d618c5e78a5010f
Summary:        Graphical effect and filter library
Name:    qimageblitz
Version: 0.0.6
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD AND ImageMagick
URL:     http://qimageblitz.sourceforge.net/
Source0:        http://download.kde.org/stable/qimageblitz/qimageblitz-%{version}.tar.bz2
Patch100: qimageblitz-0.0.4-noexecstack.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  qt4-devel
# /oreon:deps
%description
Blitz is a graphical effect and filter library for KDE4 that contains
improvements over KDE 3.x's kdefx library including bugfixes, memory and
speed improvements, and MMX/SSE support.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package examples
Summary: Example programs for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
This package contains the blitztest example program for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P100 -p1
# cmake4 needs an explicit minimum
sed -i '1i cmake_minimum_required(VERSION 3.5)' CMakeLists.txt

%build

%cmake %{?_cmake_skip_rpath} -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion qimageblitz)" = "4.0.0"
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n qimageblitz-devel -f %{oreon_filedir}/qimageblitz-devel.list
%files -n qimageblitz-examples -f %{oreon_filedir}/qimageblitz-examples.list

%changelog

%autochangelog
