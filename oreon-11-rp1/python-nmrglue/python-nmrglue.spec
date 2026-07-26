%global source0_hash fa721dd9b5675ca0101288727a55af8d8870f7f01a83251798057c1020cb24c3

%global pkgname nmrglue
%global pkgsum Python module for processing NMR data

Name:		python-%{pkgname}
Version:	0.9
Release:	%autorelease
Summary:	%{pkgsum}

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jjhelmus/%{pkgname}
Source0:	https://github.com/jjhelmus/%{pkgname}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
# these are required for tests
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy

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

%check

pushd nmrglue/fileio/tests

#python3 tests
PYTHONPATH="%{buildroot}%{python3_sitelib}" %{__python3} test_pipe.py

popd

%files -n python3-%{pkgname}
%license LICENSE.txt
%doc README.rst TODO.txt
%{python3_sitelib}/*

%changelog
%autochangelog
