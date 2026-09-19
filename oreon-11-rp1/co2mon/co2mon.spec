%global source0_hash none

%global gitcommit_full f47ec3d7e72ad4b8bc163a515b6e66bd94a6b02e
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20221013

Name:           co2mon
Version:        2.1.1
Release:        18.%{date}git%{gitcommit}%{?dist}
Summary:        CO2 monitor software

License:        GPL-3.0-or-later
URL:            https://github.com/dmage/co2mon
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hidapi-libusb)
BuildRequires:  pkgconfig(udev)

Requires:       udev

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

%files
%doc README.md
%license LICENSE
%{_bindir}/co2mond
%{_datadir}/%{name}
%{_libdir}/*.so.1*
%{_udevrulesdir}/99-%{name}.rules

%files devel
%{_libdir}/*.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
