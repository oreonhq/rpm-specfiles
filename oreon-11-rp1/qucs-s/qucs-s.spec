%global source0_hash 2354beab1642c60b02cb9c51adb2bde4998aeaba4fa5c1121eebc22546f96639

%global name_u qucs_s

Summary: Qucs circuit simulator which works with SPICE
Name:    qucs-s
Version: 25.2.0
Release: 2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://ra3xdh.github.io/

Source0: https://github.com/ra3xdh/qucs_s/archive/%{version}/%{name_u}-%{version}.tar.gz

# Desktop file categories must terminate with a semicolon, bug #1424234
Patch0:  qucs-s-0.0.19-fix-desktop-file.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: bison
BuildRequires: desktop-file-utils
# for "appstream-util validate-relax"
BuildRequires: libappstream-glib
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-linguist
BuildRequires: qt6-qtsvg-devel
BuildRequires: qt6-qtcharts-devel
BuildRequires: qt6-qttools-devel
Requires: ngspice
Recommends: %{name}-library

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.ra3xdh.qucs_s.metainfo.xml

%files
%license COPYING
%doc AUTHORS NEWS.md README.md THANKS TODO
%exclude %{_datadir}/%{name}/examples
%exclude %{_datadir}/%{name}/library
%exclude %{_datadir}/%{name}/xspice_cmlib
%{_bindir}/qucs*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/icons/hicolor/*
%{_metainfodir}/io.github.ra3xdh.qucs_s.metainfo.xml

%files library
%{_datadir}/%{name}/library

%files devel
%{_datadir}/%{name}/xspice_cmlib

%files examples
%{_datadir}/%{name}/examples

%changelog
%autochangelog
