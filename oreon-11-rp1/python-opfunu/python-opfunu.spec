%global source0_hash 1ae4e83f435c155d6a6ad28f6118d78df8c73d6827a59323167637d6a1d3bf07
Name:           python-opfunu
Version:        1.0.4
Release:        1%{?dist}
Summary:        Opfunu: An Open-source Python Library for Optimization Benchmark Functions
License:        ...
URL:            https://github.com/thieu1995/opfunu
Source0:        https://files.pythonhosted.org/packages/source/o/opfunu/opfunu-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-do-not-package-tests-examples.patch
Patch:          %{url}/pull/12.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opfunu = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opfunu
Summary:        Opfunu: An Open-source Python Library for Optimization Benchmark Functions
%description -n python3-opfunu

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir opfunu-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opfunu usr/lib/python3*/site-packages/opfunu* usr/lib64/python3*/site-packages/opfunu* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opfunu* usr/lib64/python3*/site-packages/opfunu* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opfunu -f %{oreon_filedir}/python3-opfunu.list

%changelog

%autochangelog
