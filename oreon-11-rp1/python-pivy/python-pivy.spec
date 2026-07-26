%global source0_hash c207f5ed73089b2281356da4a504c38faaab90900b95639c80772d9d25ba0bbc

%global realname pivy
%global githash 46ddb2c
%global gitdate 20191108

Name:           python-pivy
Version:        0.6.9
Release:        7%{?dist}
Summary:        Python binding for Coin

License:        ISC
URL:            https://github.com/FreeCAD/pivy

Source0:        https://github.com/coin3d/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz

BuildRequires:  gcc gcc-c++ cmake swig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  python3-devel
BuildRequires:  Coin4-devel
BuildRequires:  SoQt-devel
BuildRequires:  SIMVoleon-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libEGL-devel

%global _description\
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.\

%description %_description

%package -n python3-pivy
Summary: %summary
%{?python_provide:%python_provide python3-pivy}

%description -n python3-pivy %_description

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

 
%files -n python3-pivy
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python3_sitearch}/pivy/

%files examples
%doc examples

%changelog
%autochangelog
