%global source0_hash 959f1276c1d8b99fc5a17b5da850ca7dee43010d932dca8d5d3460727b0f8835
%global gitcommit_full f47ec3d7e72ad4b8bc163a515b6e66bd94a6b02e
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20221013
Name:           co2mon
Version:        2.1.1
Release:        1%{?dist}
Summary:        CO2 monitor software
License:        GPL-3.0-or-later
URL:            https://github.com/dmage/co2mon
Source0:        https://github.com/dmage/%{name}/tarball/%{gitcommit_full}
Requires:       udev
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)
# /oreon:deps
%description
Software for USB CO2 Monitor devices.

%package        devel
Summary:        Include files for CO2 monitor software
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for USB CO2 Monitor devices.

%prep

%autosetup -n dmage-%{name}-%{gitcommit}

%build

%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 644 udevrules/99-%{name}.rules %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r graph %{buildroot}%{_datadir}/%{name}/
%oreon_autofiles co2mon-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n co2mon-devel -f %{oreon_filedir}/co2mon-devel.list

%changelog

%autochangelog
