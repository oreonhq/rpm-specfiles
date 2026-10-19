%global source0_hash 00f208ac43f65a5b1b2c33c69d491b49200e0563f27e43840d239d3893f3f76b
%global commit 522d2e64f938bf32b758d5a18e1d0a712ecf7b3c
%global gitdate 20251229
Name:           digikam-gmic-qt
Version:        0^%{gitdate}git%{sub %{commit} 1 7}
Release:        1%{?dist}
Summary:        DigiKam G'MIC plugin
License:        CECILL-2.1 AND CECILL-C AND GPL-2.0-or-later
URL:            https://github.com/cgilles/digikam-gmic-qt
Source0:        https://github.com/cgilles/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          qtplugindir.patch
ExclusiveArch:  %{qt6_qtwebengine_arches}
Provides:  bundled(CImg) = 3.6.0
Provides:  bundled(gmic) = 3.6.0
# oreon:deps
BuildRequires:  cmake(DigikamCore)
BuildRequires:  cmake(DigikamDatabase)
BuildRequires:  cmake(DigikamGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
This provide the port of G'MIC-Qt plugin as a digiKam/Showfoto Image Editor tool.

%prep

%autosetup -n %{name}-%{commit} -p1

%build

%cmake \
  -DGMIC_QT_HOST=digikam \
  -DBUILD_WITH_QT6=ON \
  -DQT_PLUGINS_DIR=%{_qt6_plugindir} \
  -DENABLE_ASAN=OFF \
  -DENABLE_SYSTEM_GMIC=OFF \
  -DENABLE_FFTW3=ON \
  -DENABLE_CURL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
