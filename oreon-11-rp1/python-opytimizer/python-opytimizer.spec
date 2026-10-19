%global source0_hash 4fa27087166c1a74e2cb6a1dd7c298827c62de98ba1364c37171d8f9f28c0204
Name:           python-opytimizer
Version:        4.1.0
Release:        1%{?dist}
Summary:        Nature-Inspired Python Optimizer
License:        ...
URL:            https://github.com/recogna-lab/opytimizer
Source0:        https://files.pythonhosted.org/packages/source/o/opytimizer/opytimizer-%{version}.tar.gz
BuildArch:      noarch
Patch:          remove-ci-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opytimizer = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opytimizer
Summary:        Nature-Inspired Python Optimizer
%description -n python3-opytimizer

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir opytimizer-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opytimizer usr/lib/python3*/site-packages/opytimizer* usr/lib64/python3*/site-packages/opytimizer* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opytimizer* usr/lib64/python3*/site-packages/opytimizer* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-opytimizer -f %{oreon_filedir}/python3-opytimizer.list

%changelog

%autochangelog
