%global source0_hash c145011f4609d841805b69a9300099fc02fed8f5bb9e5bcef77d97aea97b7761
Name:           python-sphinx-last-updated-by-git
Version:        0.3.8
Release:        1%{?dist}
Summary:        Get the _last updated_ time for each Sphinx page from Git
License:        BSD-2-Clause
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_last_updated_by_git/sphinx_last_updated_by_git-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.8.0
Requires:       python3-sphinx-last-updated-by-git = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sphinx-last-updated-by-git
Summary:        Get the _last updated_ time for each Sphinx page from Git
%description -n python3-sphinx-last-updated-by-git

%prep
%global oreon_srcdir sphinx_last_updated_by_git-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-last-updated-by-git usr/lib/python3*/site-packages/sphinx_last_updated_by_git* usr/lib64/python3*/site-packages/sphinx_last_updated_by_git* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_last_updated_by_git* usr/lib64/python3*/site-packages/sphinx_last_updated_by_git* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-last-updated-by-git -f %{oreon_filedir}/python3-sphinx-last-updated-by-git.list

%changelog

%autochangelog
