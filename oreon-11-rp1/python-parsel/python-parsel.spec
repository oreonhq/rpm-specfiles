%global source0_hash 5925fe087eb16fc404a7ed91e31e2c1e2a9b230da4b64f34d81358c0d0e27e88
Name:           python-parsel
Version:        1.11.0
Release:        1%{?dist}
Summary:        Parsel is a library to extract data from HTML and XML using XPath and CSS selectors
License:        BSD-3-Clause
URL:            https://github.com/scrapy/parsel
Source0:        https://files.pythonhosted.org/packages/source/p/parsel/parsel-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-parsel = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-parsel
Summary:        Parsel is a library to extract data from HTML and XML using XPath and CSS selectors
# oreon:reqs
Requires:       python3dist(cssselect) >= 1.2.0
Requires:       python3dist(jmespath) >= 1.0.0
Requires:       python3dist(lxml) >= 5.1.0
Requires:       python3dist(packaging) >= 23.0
Requires:       python3dist(w3lib) >= 1.19.0
# /oreon:reqs
%description -n python3-parsel

%prep
%global oreon_srcdir parsel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-parsel usr/lib/python3*/site-packages/parsel* usr/lib64/python3*/site-packages/parsel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/parsel* usr/lib64/python3*/site-packages/parsel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-parsel -f %{oreon_filedir}/python3-parsel.list

%changelog

%autochangelog
