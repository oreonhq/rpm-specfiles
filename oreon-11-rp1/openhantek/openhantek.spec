%global source0_hash none

Name:           openhantek
Version:        3.4~rc3
Release:        5%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/OpenHantek/OpenHantek6022
#Source0:        %{url}/archive/%{version}/OpenHantek6022-%{version}.tar.gz
Source0:        %{url}/archive/3.4-rc3/OpenHantek6022-3.4-rc3.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fftw-devel
BuildRequires:  libusbx-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  binutils-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  pkgconfig(udev)

Requires:       hicolor-icon-theme
Requires:       udev

%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: 6022BE/BL.

%prep
%autosetup -p1 -n OpenHantek6022-3.4-rc3

%build
export VERSION=%{version}
%cmake3
%cmake3_build

%install
%cmake3_install
mkdir -p %{buildroot}%{_udevrulesdir}
rm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/OpenHantek.png
rm %{buildroot}%{_datadir}/doc/%{name}/*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/OpenHantek.desktop

%files
%license LICENSE
%doc README.md CHANGELOG docs/OpenHantek6022_User_Manual.pdf CODE_OF_CONDUCT
%{_bindir}/OpenHantek
%{_datadir}/applications/OpenHantek.desktop
%{_datadir}/icons/hicolor/scalable/apps/OpenHantek.svg
%{_udevrulesdir}/60-openhantek.rules

%changelog
%autochangelog
