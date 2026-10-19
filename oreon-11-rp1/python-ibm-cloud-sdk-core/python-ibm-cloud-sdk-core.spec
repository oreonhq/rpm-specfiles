%global source0_hash f1ba689371392e9a71ead7d6fcc700b065832a4be7d56641e816a0b72b14e2a3
Name:           python-ibm-cloud-sdk-core
Version:        3.26.1
Release:        1%{?dist}
Summary:        Core library used by SDKs for IBM Cloud Services
License:        ...
URL:            https://github.com/IBM/python-sdk-core
Source0:        https://files.pythonhosted.org/packages/source/i/ibm_cloud_sdk_core/ibm_cloud_sdk_core-%{version}.tar.gz
BuildArch:      noarch
Patch0:         fix-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 67.7.2
Requires:       python3-ibm-cloud-sdk-core = %{version}-%{release}
# /oreon:deps
%package -n       python3-ibm-cloud-sdk-core+dev
Summary:        Metapackage for python3-ibm-cloud-sdk-core dev extras
Requires:       python3-ibm-cloud-sdk-core = %{version}-%{release}
Requires:       python3dist(coverage) >= 7.9.0
Requires:       python3dist(coverage) < 8.0.0
Requires:       python3dist(pylint) >= 4.0.7
Requires:       python3dist(pylint) < 4.1.0
Requires:       python3dist(pytest) >= 9.1.1
Requires:       python3dist(pytest) < 9.2.0
Requires:       python3dist(pytest-cov) >= 7.1.0
Requires:       python3dist(pytest-cov) < 7.2.0
Requires:       python3dist(responses) >= 0.25.7
Requires:       python3dist(responses) < 1.0.0
Requires:       python3dist(black) >= 26.5.1
Requires:       python3dist(black) < 26.6.0
Provides:       python3dist(ibm-cloud-sdk-core[dev]) = %{version}-%{release}

%description -n python3-ibm-cloud-sdk-core+dev
Metapackage for python3-ibm-cloud-sdk-core dev extras.

%package -n       python3-ibm-cloud-sdk-core+publish
Summary:        Metapackage for python3-ibm-cloud-sdk-core publish extras
Requires:       python3-ibm-cloud-sdk-core = %{version}-%{release}
Provides:       python3dist(ibm-cloud-sdk-core[publish]) = %{version}-%{release}

%description -n python3-ibm-cloud-sdk-core+publish
Metapackage for python3-ibm-cloud-sdk-core publish extras.

%description

%package -n     python3-ibm-cloud-sdk-core
Summary:        Core library used by SDKs for IBM Cloud Services
# oreon:reqs
Requires:       python3dist(pyjwt) < 3.0.0
Requires:       python3dist(pyjwt) >= 2.11.0
Requires:       python3dist(python-dateutil) < 3.0.0
Requires:       python3dist(python-dateutil) >= 2.9.0
Requires:       python3dist(requests) < 3.0.0
Requires:       python3dist(requests) >= 2.32.4
Requires:       python3dist(urllib3) < 3.0.0
Requires:       python3dist(urllib3) >= 2.4.0
# /oreon:reqs
%description -n python3-ibm-cloud-sdk-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ibm_cloud_sdk_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ibm-cloud-sdk-core usr/lib/python3*/site-packages/ibm_cloud_sdk_core* usr/lib64/python3*/site-packages/ibm_cloud_sdk_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ibm_cloud_sdk_core* usr/lib64/python3*/site-packages/ibm_cloud_sdk_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ibm-cloud-sdk-core -f %{oreon_filedir}/python3-ibm-cloud-sdk-core.list

%changelog

%autochangelog
