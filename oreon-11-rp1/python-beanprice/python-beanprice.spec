%global source0_hash d90d26641f7baed8443cdfdb5545c38f8d01f97604ed4ad4173b023598982b13
Name:           python-beanprice
Version:        2.1.0
Release:        1%{?dist}
Summary:        Price quotes fetcher for Beancount
License:        ...
URL:            https://github.com/beancount/beanprice
Source0:        https://files.pythonhosted.org/packages/source/b/beanprice/beanprice-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-beanprice = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-beanprice
Summary:        Price quotes fetcher for Beancount
# oreon:reqs
Requires:       python3dist(beancount) >= 3.0.0
Requires:       python3dist(curl-cffi) >= 0.6.5
Requires:       python3dist(diskcache) >= 5.6.3
Requires:       python3dist(python-dateutil) >= 2.6.0
Requires:       python3dist(requests) >= 2.0
# /oreon:reqs
%description -n python3-beanprice

%prep
%global oreon_srcdir beanprice-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-beanprice usr/lib/python3*/site-packages/beanprice* usr/lib64/python3*/site-packages/beanprice* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/beanprice* usr/lib64/python3*/site-packages/beanprice* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-beanprice -f %{oreon_filedir}/python3-beanprice.list

%changelog

%autochangelog
