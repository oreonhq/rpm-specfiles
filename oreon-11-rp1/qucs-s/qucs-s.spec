%global source0_hash bf4ccff9e975680129ba850c5045145ad121f4e0f7eef86799398abe2f68eb24
%global name_u qucs_s
Summary:        Qucs circuit simulator which works with SPICE
Name:    qucs-s
Version: 26.1.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://ra3xdh.github.io/
Source0:        https://github.com/ra3xdh/%{name_u}/archive/%{version}/%{name_u}-%{version}.tar.gz
Patch0:  qucs-s-0.0.19-fix-desktop-file.patch
Requires: ngspice
Recommends: %{name}-library
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
%description
Qucs-S is a spin-off of the Qucs cross-platform circuit simulator. "S" letter
indicates SPICE. The purpose of the Qucs-S subproject is to use free SPICE
circuit simulation kernels with the Qucs GUI. It merges the power of SPICE
and the simplicity of the Qucs GUI.

%package library
Summary: Qucs-S library
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description library
Qucs-S library.

%package devel
Summary: Qucs-S development files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Qucs-S development files.

%package examples
Summary: Qucs-S examples
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description examples
Qucs-S examples.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name_u}-%{version} -p1

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.ra3xdh.qucs_s.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n qucs-s-library -f %{oreon_filedir}/qucs-s-library.list
%files -n qucs-s-devel -f %{oreon_filedir}/qucs-s-devel.list
%files -n qucs-s-examples -f %{oreon_filedir}/qucs-s-examples.list

%changelog

%autochangelog
