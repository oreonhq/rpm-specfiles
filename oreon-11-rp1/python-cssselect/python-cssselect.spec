%global source0_hash 3cbe82dd7acbee9ba9e5723b5f9e4749826912f1fb31cd7f92aabed5fde15b15
Name:           python-cssselect
Version:        1.5.0
Release:        1%{?dist}
Summary:        cssselect parses CSS3 Selectors and translates them to XPath 1.0
License:        BSD-3-Clause
URL:            https://github.com/scrapy/cssselect
Source0:        https://files.pythonhosted.org/packages/source/c/cssselect/cssselect-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-cssselect = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-cssselect
Summary:        cssselect parses CSS3 Selectors and translates them to XPath 1.0
%description -n python3-cssselect

%prep
%global oreon_srcdir cssselect-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cssselect usr/lib/python3*/site-packages/cssselect* usr/lib64/python3*/site-packages/cssselect* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cssselect* usr/lib64/python3*/site-packages/cssselect* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cssselect -f %{oreon_filedir}/python3-cssselect.list

%changelog

%autochangelog
