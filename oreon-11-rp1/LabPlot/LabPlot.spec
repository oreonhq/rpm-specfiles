%global source0_hash e28155bfddf40e5b6f7c4791313556d1e48138044f216f210d515b9f6d6c106a
%global genname labplot
%ifarch s390x
%bcond libcerf 0
%else
%bcond libcerf 1
%endif
Name:           LabPlot
Version:        2.12.1%{?gitdate:~%{gitdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Data Analysis and Visualization
License:        GPL-2.0-or-later
URL:            https://labplot.kde.org/
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Source0:        https://download.kde.org/stable/labplot/labplot-%{version}.tar.xz
Patch0:         labplot-fix-build-against-qt-6-10.patch
%if %{with cerf}
%endif
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if %{undefined flatpak}
Requires:       electronics-menu
%endif
# oreon:deps
BuildRequires:  QXlsx-devel
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cantor-devel
BuildRequires:  cfitsio-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Mqtt)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(qtadvanceddocking-qt6)
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libixion-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  liborcus-devel
BuildRequires:  liborigin-devel
BuildRequires:  libspectre-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  matio-devel
BuildRequires:  netcdf-devel
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  readstat-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
LabPlot is a FREE, open source and cross-platform Data Visualization and
Analysis software accessible to everyone.

- High-quality Data Visualization and Plotting with just a few clicks
- Reliable and easy Data Analysis and Statistics, no coding required!
- Intuitive and fast Computing with Interactive Notebooks
- Effortless Data Extraction from plots and support for Live Data
- Smooth Data Import and Export to and from multiple formats
- Available for Windows, macOS, Linux and FreeBSD

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Widgets)
%description devel
This package contains the LabPlot Software Development Kit.

%prep

%autosetup -p1 -n %{genname}-%{!?gitcommit:%{version}}%{?gitcommit}

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{genname} --all-name --with-html --with-man
%oreon_autofiles LabPlot-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%files -f %{oreon_filedir}/main.list
%files -n LabPlot-devel -f %{oreon_filedir}/LabPlot-devel.list

%changelog

%autochangelog
