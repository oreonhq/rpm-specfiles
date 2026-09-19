%global source0_hash ad556772f3e06345f1ce503fc118ef5bd54cdd0469a990ea1f2d7cd9946d1fb2

Name:           python-pysubnettree
Version:        0.38.1
Release:        %autorelease
Summary:        Python Module for CIDR Lookups

# BSD-4-Clause is coming from include/patricia.h
License:        BSD-3-Clause-LBNL and BSD-4-Clause
URL:            https://github.com/zeek/pysubnettree
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# btest config file for RPM build environment
Source1:        btest.cfg

Provides:       pysubnettree = %{version}-%{release}
Obsoletes:      pysubnettree < 0.35-16

BuildRequires:  python3-devel
BuildRequires:  gcc-c++
BuildRequires:  zeek-btest

%global _description %{expand:
The PySubnetTree package provides a Python data structure SubnetTree which maps
subnets given in CIDR notation (incl. corresponding IPv6 versions) to Python
objects. Lookups are performed by longest-prefix matching.}

%description %{_description}

%package -n python3-pysubnettree
Summary:        %{summary}

%description -n python3-pysubnettree %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pysubnettree-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l SubnetTree _SubnetTree

%check
%pyproject_check_import
cd testing
cp %{SOURCE1} btest.cfg
PYTHONPATH="%{buildroot}%{python3_sitearch}:$PWD/Scripts" btest -c btest.cfg -d

%files -n python3-pysubnettree -f %{pyproject_files}
%doc CHANGES README

%changelog
%autochangelog
