%global source0_hash a3937021808846a07b4566966ec7e71efd97f4c90eb26ab33678629f6148f92e
%global pkgname nmrglue
%global pkgsum Python module for processing NMR data
Name:		python-%{pkgname}
Version:	0.12
Release:        1%{?dist}
Summary:        Python module for processing NMR data
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jjhelmus/%{pkgname}
Source0:        https://github.com/jjhelmus/%{pkgname}/archive/v%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy
BuildRequires:  python3-setuptools
# /oreon:deps
%description
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%package -n python3-%{pkgname}
Summary:	%{pkgsum}
%{?python_provide:%python_provide python3-%{pkgname}}
Requires:	python3-numpy
Requires:	python3-scipy
%description -n python3-%{pkgname}
nmrglue is a module for working with NMR data in Python. When used with the 
numpy, scipy, and matplotlib packages nmrglue provides a robust interpreted 
environment for processing, analyzing, and inspecting NMR data.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}

# disable tests bundling
sed -i '/nmrglue.fileio.tests/d' setup.py
sed -i '/package_data/d' setup.py
sed -i '/fileio\/tests\/data\//d' setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd nmrglue/fileio/tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{__python3} test_pipe.py
popd
%files -f %{oreon_filedir}/main.list
%files -n python3-nmrglue -f %{oreon_filedir}/python3-nmrglue.list

%changelog

%autochangelog
