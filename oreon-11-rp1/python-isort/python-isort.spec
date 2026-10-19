%global source0_hash ba23db109e3e93ef1999f7209a651214994cd807801addd16ac485982eb4edd7
Name:           python-isort
Version:        9.0.1
Release:        1%{?dist}
Summary:        A Python utility / library to sort Python imports.
License:        MIT
URL:            https://isort.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/i/isort/isort-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-isort = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-isort
Summary:        A Python utility / library to sort Python imports.
# oreon:reqs
Requires:       python3dist(black) >= 24.3.0
Requires:       python3dist(isort) >= 5.13.2
# /oreon:reqs
%description -n python3-isort

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir isort-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-isort usr/lib/python3*/site-packages/isort* usr/lib64/python3*/site-packages/isort* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/isort* usr/lib64/python3*/site-packages/isort* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-isort -f %{oreon_filedir}/python3-isort.list

%changelog

%autochangelog
