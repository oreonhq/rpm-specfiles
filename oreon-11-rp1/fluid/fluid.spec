%global source0_hash 7330700c6aef16f4bf9c620d3b785e0d9218c00be84e08df22c166404f94f3fd
Name:           fluid
Summary:        Library for fluid and dynamic applications development with QtQuick
Version:        0.8.0
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://liri.io
Source0:        https://github.com/hawaii-desktop/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
# /oreon:deps
%description
Library for fluid and dynamic applications development with QtQuick.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}

%build

%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
