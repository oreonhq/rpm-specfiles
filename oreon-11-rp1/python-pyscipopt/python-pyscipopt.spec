%global source0_hash 9c511bd3dc6767f08c430c3be18af9e900d5bc939d9d1b44379dd0f760da167e
Name:           python-pyscipopt
Version:        6.2.1
Release:        1%{?dist}
Summary:        Python interface and modeling environment for SCIP
License:        MIT AND WTFNMFPL
URL:            https://github.com/scipopt/PySCIPOpt
Source0:        https://github.com/scipopt/PySCIPOpt/archive/v%{version}/PySCIPOpt-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global common_description %{expand:
This project provides an interface from Python to the SCIP Optimization Suite.}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libscip-devel
BuildRequires:  python3dist(pytest)
# /oreon:deps
%description %{common_description}

%package -n python3-pyscipopt
Summary:        Python interface and modeling environment for SCIP
License:        MIT
%description -n python3-pyscipopt %{common_description}

%package examples
Summary:        Examples for PySCIPOpt
BuildArch:      noarch
%description examples
%{summary}.

%prep

%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_beware_of_rpath
sed -r -i 's/^([[:blank:]]*)(.*-Wl,-rpath)/\1# \2/' setup.py

%build -p

export CFLAGS="${CFLAGS} -I/usr/include/scip"
%install
%pyproject_install
%oreon_autofiles python3-pyscipopt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-pyscipopt -f %{oreon_filedir}/python3-pyscipopt.list
%files -n python-pyscipopt-examples -f %{oreon_filedir}/python-pyscipopt-examples.list

%changelog

%autochangelog
