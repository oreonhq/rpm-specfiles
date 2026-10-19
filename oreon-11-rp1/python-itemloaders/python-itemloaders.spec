%global source0_hash b5338308a819098f43525b7afc5f7d46ba338ba4710f5ebe7a21b3b47bb29929
Name:           python-itemloaders
Version:        1.4.0
Release:        1%{?dist}
Summary:        Base library for scrapy_s ItemLoader
License:        BSD-3-Clause
URL:            https://github.com/scrapy/itemloaders
Source0:        https://files.pythonhosted.org/packages/source/i/itemloaders/itemloaders-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-itemloaders = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-itemloaders
Summary:        Base library for scrapy_s ItemLoader
# oreon:reqs
Requires:       python3dist(itemadapter) >= 0.1.0
Requires:       python3dist(jmespath) >= 0.9.5
Requires:       python3dist(parsel) >= 1.5.0
# /oreon:reqs
%description -n python3-itemloaders

%prep
%global oreon_srcdir itemloaders-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-itemloaders usr/lib/python3*/site-packages/itemloaders* usr/lib64/python3*/site-packages/itemloaders* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/itemloaders* usr/lib64/python3*/site-packages/itemloaders* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-itemloaders -f %{oreon_filedir}/python3-itemloaders.list

%changelog

%autochangelog
