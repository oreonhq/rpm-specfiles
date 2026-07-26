%global source0_hash 7602e37c6715fbf4cec3f0ded1e860157796423dc79da062a0e5ccb1226dc8e6

%global realname urdfdom_headers

Name:		urdfdom-headers
Version:	1.1.2
Release:	3%{?dist}
Summary:	The URDF (U-Robot Description Format) headers

License:	BSD-3-Clause
URL:		http://ros.org/wiki/urdf
Source0:	https://github.com/ros/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch

# Install configs to arch independent paths
# https://github.com/ros/urdfdom_headers/issues/27
Patch0:		urdfdom-headers-1.1.2-fedora.patch

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake

%description
%{summary}

%package devel
Summary: The URDF (U-Robot Description Format) headers
Requires: pkgconfig
BuildArch: noarch
Provides: %{name}-static = %{version}-%{release}

%description devel
The URDF (U-Robot Description Format) headers provides core data structure
headers for URDF.

For now, the details of the URDF specifications reside on
http://ros.org/wiki/urdf

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -Sgendiff -p1 -n %{realname}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/urdfdom_headers
%{_datadir}/pkgconfig/*.pc
%{_datadir}/%{realname}

%changelog
%autochangelog
