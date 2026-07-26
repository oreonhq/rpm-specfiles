%global source0_hash 8cee8787e841b520596d0b20b16e72afebf3d0c05c4d629bc1a6a3279b0d282f

%bcond check 0

%global forgeurl https://github.com/jbagg/QtZeroConf
%global commit d13a7eb4be3723e843758fa86182e99ea3f92d79

Name:			qtzeroconf
Version:		0.1.0

%forgemeta

Release:		%{autorelease}
Summary:		A Qt wrapper class for ZeroConf libraries across various platforms

# LGPL-3.0-or-later: this project
# LGPL-2.1-or-later: headers derived from avahi
License:		LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:			%{forgeurl}
Source0:		%{forgesource}

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)

BuildRequires:	avahi-devel

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++

%description
QZeroConf is a Qt wrapper class for ZeroConf libraries across various platforms.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libQtZeroConf.so.0*

%files devel
%{_includedir}/QtZeroConf/
%{_libdir}/libQtZeroConf.so
%{_libdir}/cmake/QtZeroConf/

%changelog
%autochangelog
