%global source0_hash e16a2cad818da8aa66c8a0d80cfaf540105ba065d27b027c05d0134e8afedb96

Name:		python-pyownet
Version:	0.10.0.post1
Release:	10%{?dist}
Summary:	Pure python client library for accessing OWFS via owserver protocol

License:	LGPL-3.0-or-later
URL:		https://github.com/miccoli/pyownet
Source0:	%{pypi_source pyownet}
# from https://github.com/miccoli/pyownet/commit/1b2e8d10c6b4b3553b7c80eafbc35871658ddec1
Patch0:		python-pyownet-001-declarative-build.patch
Patch1:		python-pyownet-002-remove-www.google.com-from-tests.patch
# from https://github.com/onkelbeh/HomeAssistantRepository/tree/master/dev-python/pyownet/files
# temporary before 0.11.0 is released
# setup.py chunk manualy removed
Patch2:		python-pyownet-003-2to3.patch
Patch3:		python-pyownet-004-pyproject-remove-pin-on-setuptools.patch

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-pytest
BuildRequires:	python3-wheel
%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
Pyownet is a pure python package that allows network client access to the OWFS
1-Wire File System via an owserver and the owserver network protocol.}

%description %_description

%package -n python3-pyownet
Summary:	Pure python client library for accessing OWFS via owserver protocol

%description -n python3-pyownet %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyownet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-pyownet
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/pyownet/
%{python3_sitelib}/pyownet-%{version}.dist-info/

%changelog
%autochangelog
