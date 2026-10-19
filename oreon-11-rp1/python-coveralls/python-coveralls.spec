%global source0_hash dab364025ba80cbb95ce56c6fc62cd9172d7fd637060ea235dde99d9b46a4494
Name:           python-coveralls
Version:        4.1.0
Release:        1%{?dist}
Summary:        Show coverage stats online via coveralls.io
License:        MIT
URL:            https://github.com/TheKevJames/coveralls-python
Source0:        https://files.pythonhosted.org/packages/source/c/coveralls/coveralls-%{version}.tar.gz
BuildArch:      noarch
Patch0001:      0001-pyproject.toml-Allow-building-with-python-3.13.patch
Patch0002:      0002-pyproject-Use-docopt-ng-on-Fedora.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-coveralls = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-coveralls
Summary:        Show coverage stats online via coveralls.io
%description -n python3-coveralls

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir coveralls-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-coveralls usr/lib/python3*/site-packages/coveralls* usr/lib64/python3*/site-packages/coveralls* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/coveralls* usr/lib64/python3*/site-packages/coveralls* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-coveralls -f %{oreon_filedir}/python3-coveralls.list

%changelog

%autochangelog
