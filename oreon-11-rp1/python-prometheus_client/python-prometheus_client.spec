%global source0_hash 04a91bcf94e2cf74a44a1a874d651a2e853ed354b6e822f3b7487751465d5c2b
Name:           python-prometheus-client
Version:        0.26.0
Release:        1%{?dist}
Summary:        Python client for the Prometheus monitoring system.
License:        Apache-2.0 AND BSD-2-Clause
URL:            https://github.com/prometheus/client_python
Source0:        https://files.pythonhosted.org/packages/source/p/prometheus_client/prometheus_client-%{version}.tar.gz
BuildArch:      noarch
Patch0001:      0001-Remove-the-bundled-decorator-package.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-prometheus-client = %{version}-%{release}
# /oreon:deps
%package -n       python3-prometheus-client+twisted
Summary:        Metapackage for python3-prometheus-client twisted extras
Requires:       python3-prometheus-client = %{version}-%{release}
Provides:       python3dist(prometheus-client[twisted]) = %{version}-%{release}

%description -n python3-prometheus-client+twisted
Metapackage for python3-prometheus-client twisted extras.

%package -n       python3-prometheus-client+aiohttp
Summary:        Metapackage for python3-prometheus-client aiohttp extras
Requires:       python3-prometheus-client = %{version}-%{release}
Provides:       python3dist(prometheus-client[aiohttp]) = %{version}-%{release}

%description -n python3-prometheus-client+aiohttp
Metapackage for python3-prometheus-client aiohttp extras.

%package -n       python3-prometheus-client+django
Summary:        Metapackage for python3-prometheus-client django extras
Requires:       python3-prometheus-client = %{version}-%{release}
Provides:       python3dist(prometheus-client[django]) = %{version}-%{release}

%description -n python3-prometheus-client+django
Metapackage for python3-prometheus-client django extras.

%description

%package -n     python3-prometheus-client
Summary:        Python client for the Prometheus monitoring system.
%description -n python3-prometheus-client

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir prometheus_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-prometheus-client usr/lib/python3*/site-packages/prometheus_client* usr/lib64/python3*/site-packages/prometheus_client* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/prometheus_client* usr/lib64/python3*/site-packages/prometheus_client* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-prometheus-client -f %{oreon_filedir}/python3-prometheus-client.list

%changelog

%autochangelog
