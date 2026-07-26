%global source0_hash 7330700c6aef16f4bf9c620d3b785e0d9218c00be84e08df22c166404f94f3fd

#global snapdate 20160508
#global snaphash 42c2f64d41863a002a14911410a121a5ecb1df1a

Name:           fluid
Summary:        Library for fluid and dynamic applications development with QtQuick
Version:        0.8.0
Release:        25%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://liri.io
Source0:        https://github.com/hawaii-desktop/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%description
Library for fluid and dynamic applications development with QtQuick.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.LGPLv21
%doc AUTHORS.md README.md
%{_kf5_qmldir}/Fluid/

%changelog
%autochangelog
