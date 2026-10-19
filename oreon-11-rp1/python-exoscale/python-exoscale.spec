%global source0_hash 52fe26d37b693d857519eb0dbdf4c8514c7f3f0fb31008bce914b8a039156b3c
Name:           python-exoscale
Version:        0.16.4
Release:        1%{?dist}
Summary:        Clients for Exoscale IaaS APIs
License:        ISC
URL:            https://github.com/exoscale/python-exoscale
Source0:        https://files.pythonhosted.org/packages/source/e/exoscale/exoscale-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-exoscale = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-exoscale
Summary:        Clients for Exoscale IaaS APIs
# oreon:reqs
Requires:       python3dist(requests) >= 2.22.0
Requires:       python3dist(requests-exoscale-auth) >= 1.1.2
# /oreon:reqs
%description -n python3-exoscale

%prep
%global oreon_srcdir exoscale-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-exoscale usr/lib/python3*/site-packages/exoscale* usr/lib64/python3*/site-packages/exoscale* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/exoscale* usr/lib64/python3*/site-packages/exoscale* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-exoscale -f %{oreon_filedir}/python3-exoscale.list

%changelog

%autochangelog
