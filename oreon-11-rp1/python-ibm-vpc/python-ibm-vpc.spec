%global source0_hash d8e8fd434f67852fa03cf8e1de2b0f4350d1602bf56b18d17fcb8c1af9412629
Name:           python-ibm-vpc
Version:        0.35.1
Release:        1%{?dist}
Summary:        Python client library for IBM Cloud ibm-vpc Services
License:        ...
URL:            https://github.com/IBM/vpc-python-sdk
Source0:        https://files.pythonhosted.org/packages/source/i/ibm_vpc/ibm_vpc-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.7.2
Requires:       python3-ibm-vpc = %{version}-%{release}
# /oreon:deps
%package -n       python3-ibm-vpc+dev
Summary:        Metapackage for python3-ibm-vpc dev extras
Requires:       python3-ibm-vpc = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.9.0
Requires:       python3dist(coverage) < 8.0.0
Requires:       python3dist(pylint) >= 3.3.7
Requires:       python3dist(pylint) < 4.0.0
Requires:       python3dist(pytest) >= 7.4.4
Requires:       python3dist(pytest) < 8.0.0
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(pytest-cov) < 5.0.0
Requires:       python3dist(responses) >= 0.25.7
Requires:       python3dist(responses) < 1.0.0
Requires:       python3dist(black) >= 25.0.0
Requires:       python3dist(black) < 26.0.0
Requires:       python3dist(pytest-rerunfailures) >= 12.0
Requires:       python3dist(tox) >= 4.12.0
Requires:       python3dist(tox) < 4.23.2
Provides:       python3dist(ibm-vpc[dev]) = %{version}-%{release}

%description -n python3-ibm-vpc+dev
Metapackage for python3-ibm-vpc dev extras.

%package -n       python3-ibm-vpc+publish
Summary:        Metapackage for python3-ibm-vpc publish extras
Requires:       python3-ibm-vpc = %{version}-%{release}
Provides:       python3dist(ibm-vpc[publish]) = %{version}-%{release}

%description -n python3-ibm-vpc+publish
Metapackage for python3-ibm-vpc publish extras.

%description

%package -n     python3-ibm-vpc
Summary:        Python client library for IBM Cloud ibm-vpc Services
# oreon:reqs
Requires:       python3dist(ibm-cloud-sdk-core) < 4.0.0
Requires:       python3dist(ibm-cloud-sdk-core) >= 3.26.0
Requires:       python3dist(python-dateutil) < 3.0.0
Requires:       python3dist(python-dateutil) >= 2.5.3
# /oreon:reqs
%description -n python3-ibm-vpc

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ibm_vpc-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ibm-vpc usr/lib/python3*/site-packages/ibm_vpc* usr/lib64/python3*/site-packages/ibm_vpc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ibm_vpc* usr/lib64/python3*/site-packages/ibm_vpc* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ibm-vpc -f %{oreon_filedir}/python3-ibm-vpc.list

%changelog

%autochangelog
