%global source0_hash 88ff004544ce44e61269cc6f8735f7837d12e09bb77619fc94fbb26b72e5d137
Name:           python-protego
Version:        0.6.2
Release:        1%{?dist}
Summary:        Pure-Python robots.txt parser with support for modern conventions
License:        BSD-3-Clause
URL:            https://github.com/scrapy/protego
Source0:        https://files.pythonhosted.org/packages/source/p/protego/protego-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-protego = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-protego
Summary:        Pure-Python robots.txt parser with support for modern conventions
%description -n python3-protego

%prep
%global oreon_srcdir protego-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-protego usr/lib/python3*/site-packages/protego* usr/lib64/python3*/site-packages/protego* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/protego* usr/lib64/python3*/site-packages/protego* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-protego -f %{oreon_filedir}/python3-protego.list

%changelog

%autochangelog
