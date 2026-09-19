%global source0_hash 9f102269dec50641440e23a449df215a0db9efef9a3969939d618c5e78a5010f

Summary: Graphical effect and filter library
Name:    qimageblitz
Version: 0.0.6
Release: 35%{?dist}

# Automatically converted from old format: BSD and ImageMagick - review is highly recommended.
License: LicenseRef-Callaway-BSD AND ImageMagick
URL:     http://qimageblitz.sourceforge.net/
Source0: http://download.kde.org/stable/qimageblitz/qimageblitz-%{version}.tar.bz2

# upstreamed to kdesupport
# r1204248 | rdieter | 2010-12-06 08:05:09 -0600 (Mon, 06 Dec 2010) | 2 lines
Patch100: qimageblitz-0.0.4-noexecstack.patch

BuildRequires: cmake
BuildRequires: qt4-devel

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

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion qimageblitz)" = "4.0.0"

%ldconfig_scriptlets

%files
%doc Changelog README* COPYING
%{_libdir}/libqimageblitz.so.4*

%files devel
%{_libdir}/libqimageblitz.so
%{_libdir}/pkgconfig/qimageblitz.pc
%{_includedir}/qimageblitz/

%files examples
%{_bindir}/blitztest

%changelog
%autochangelog
