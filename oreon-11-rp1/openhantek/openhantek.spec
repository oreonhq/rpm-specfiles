%global source0_hash 38641e6bdd82638d9852662eda955e49ad2055960ddf3694617151821812e6a5
Name:           openhantek
Version:        3.4~rc3
Release:        5%{?dist}
Summary:        Hantek and compatible USB digital signal oscilloscope
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/OpenHantek/OpenHantek6022
Source0:        https://github.com/OpenHantek/OpenHantek6022/archive/3.4-rc3/OpenHantek6022-3.4-rc3.tar.gz
Requires:       hicolor-icon-theme
Requires:       udev
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  pkgconfig(udev)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttranslations
# /oreon:deps
%description
OpenHantek is a free software for Hantek and compatible
(Voltcraft/Darkwire/Protek/Acetech) USB digital signal oscilloscopes.
Supported devices: 6022BE/BL.

%prep
%global oreon_srcdir OpenHantek6022-3.4-rc3
%oreon_prep
%build

export VERSION=%{version}
%cmake3
%cmake3_build
%install
%cmake3_install
mkdir -p %{buildroot}%{_udevrulesdir}
rm %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/OpenHantek.png
rm %{buildroot}%{_datadir}/doc/%{name}/*
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/OpenHantek.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
