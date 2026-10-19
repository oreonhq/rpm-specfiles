%global source0_hash 78f79bd7d1ce7e8140ceba4b1220136ea1f14b4403b1e463c59fa892feed961e
%global realname pivy
%global githash 46ddb2c
%global gitdate 20191108
Name:           python-pivy
Version:        0.6.11
Release:        1%{?dist}
Summary:        Python binding for Coin
License:        ISC
URL:            https://github.com/FreeCAD/pivy
Source0:        https://github.com/coin3d/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  Coin4-devel
BuildRequires:  SIMVoleon-devel
BuildRequires:  SoQt-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  swig
# /oreon:deps
%description

%package -n python3-pivy
Summary: %summary
%{?python_provide:%python_provide python3-pivy}
%description -n python3-pivy

%package examples
Summary: Pivy example files
%description examples
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

# Examples in the docs folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;

%build

%cmake
%cmake_build
%install
%cmake_install
chmod +x %{buildroot}%{python3_sitearch}/pivy/sogui.py
find %{buildroot}%{python3_sitearch} -name "*.py" -exec sed -i "s|#!/usr/bin/env python|#!%{__python3}|" {} \;
%oreon_autofiles python3-pivy usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pivy -f %{oreon_filedir}/python3-pivy.list
%files -n python-pivy-examples -f %{oreon_filedir}/python-pivy-examples.list

%changelog

%autochangelog
