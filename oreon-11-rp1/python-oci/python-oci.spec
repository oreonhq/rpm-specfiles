%global source0_hash d8c75fb73bddaadcf3835b07b584f80c785686aa3c8a66ae4e4062ac63757c58
Name:           python-oci
Version:        2.186.0
Release:        1%{?dist}
Summary:        Oracle Cloud Infrastructure Python SDK
License:        ...
URL:            https://docs.oracle.com/en-us/iaas/tools/python/latest/index.html
Source0:        https://files.pythonhosted.org/packages/source/o/oci/oci-%{version}.tar.gz
BuildArch:      noarch
Patch0:         https://patch-diff.githubusercontent.com/raw/oracle/oci-python-sdk/pull/253.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(pbr) == 4.1.0
BuildRequires:  python3dist(pbr) == 7.0.3
BuildRequires:  python3dist(setuptools) < 84
BuildRequires:  python3dist(setuptools) == 59.6.0
BuildRequires:  python3dist(setuptools) == 68.0.0
BuildRequires:  python3dist(setuptools) == 75.3.2
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-oci = %{version}-%{release}
# /oreon:deps
%package -n       python3-oci+adk
Summary:        Metapackage for python3-oci adk extras
Requires:       python3-oci = %{version}-%{release}
Requires:       python3dist(docstring-parser) >= 0.16
Requires:       python3dist(pydantic) >= 2.10.6
Requires:       python3dist(pydantic) < 3
Requires:       python3dist(rich) >= 13.9.4
Requires:       python3dist(mcp) >= 1.9.0
Provides:       python3dist(oci[adk]) = %{version}-%{release}

%description -n python3-oci+adk
Metapackage for python3-oci adk extras.

%description

%package -n     python3-oci
Summary:        Oracle Cloud Infrastructure Python SDK
# oreon:reqs
Requires:       python3dist(aiohttp) < 3.11
Requires:       python3dist(aiohttp) < 3.9
Requires:       python3dist(aiohttp) < 4
Requires:       python3dist(aiohttp) >= 3.10.11
Requires:       python3dist(aiohttp) >= 3.8.3
Requires:       python3dist(aiohttp) >= 3.8.6
Requires:       python3dist(circuitbreaker) < 2.0.0
Requires:       python3dist(circuitbreaker) < 3.0.0
Requires:       python3dist(circuitbreaker) >= 1.3.1
Requires:       python3dist(configparser) == 4.0.2
Requires:       python3dist(crc32c) == 2.5
Requires:       python3dist(crc32c) == 2.8.0
Requires:       python3dist(cryptography) < 51.0.0
Requires:       python3dist(cryptography) <= 37.0.2
Requires:       python3dist(cryptography) >= 3.2.1
Requires:       python3dist(pyjwt) == 2.4.0
Requires:       python3dist(pyjwt) >= 2.12.0
Requires:       python3dist(pyopenssl) < 22.0.0
Requires:       python3dist(pyopenssl) < 27.0.0
Requires:       python3dist(pyopenssl) >= 17.5.0
Requires:       python3dist(pyopenssl) >= 26.2.0
Requires:       python3dist(python-dateutil) < 3.0.0
Requires:       python3dist(python-dateutil) >= 2.5.3
Requires:       python3dist(pytz) >= 2016.10
Requires:       python3dist(urllib3) == 1.26.20
Requires:       python3dist(urllib3) >= 2.6.3
# /oreon:reqs
%description -n python3-oci

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir oci-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oci usr/lib/python3*/site-packages/oci* usr/lib64/python3*/site-packages/oci* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oci* usr/lib64/python3*/site-packages/oci* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oci -f %{oreon_filedir}/python3-oci.list

%changelog

%autochangelog
