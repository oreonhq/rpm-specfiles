%global wayland_min_version 1.4
%global debug_package %{nil}

Name:    plasma-wayland-protocols
Version: 1.20.0
Release: 2%{?dist}
Summary: Plasma Specific Protocols for Wayland

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later AND MIT-CMU
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/* COPYING.LIB
%{_kf6_datadir}/plasma-wayland-protocols/

%files devel
%{_kf6_datadir}/cmake/PlasmaWaylandProtocols/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20.0-2
- Prepare for Oreon 11 (RP1)
