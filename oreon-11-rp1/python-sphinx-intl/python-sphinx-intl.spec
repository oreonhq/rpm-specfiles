%global source0_hash f13173bfc4a131f74ea082a5820386e2bcdc020b3003378b029d438f404edbde
Name:           python-sphinx-intl
Version:        2.4.0
Release:        1%{?dist}
Summary:        Sphinx utility that make it easy to translate and to apply translation.
License:        BSD-2-Clause
URL:            https://github.com/sphinx-doc/sphinx-intl
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx_intl/sphinx_intl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-sphinx-intl = %{version}-%{release}
# /oreon:deps
%package -n       python3-sphinx-intl+test
Summary:        Metapackage for python3-sphinx-intl test extras
Requires:       python3-sphinx-intl = %{version}-%{release}
Requires:       python3dist(pytest) >= 8.3.5
Provides:       python3dist(sphinx-intl[test]) = %{version}-%{release}

%description -n python3-sphinx-intl+test
Metapackage for python3-sphinx-intl test extras.

%description

%package -n     python3-sphinx-intl
Summary:        Sphinx utility that make it easy to translate and to apply translation.
# oreon:reqs
Requires:       python3dist(babel) >= 2.9.0
Requires:       python3dist(click) >= 8.0.0
# /oreon:reqs
%description -n python3-sphinx-intl

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sphinx_intl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sphinx-intl usr/lib/python3*/site-packages/sphinx_intl* usr/lib64/python3*/site-packages/sphinx_intl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sphinx_intl* usr/lib64/python3*/site-packages/sphinx_intl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sphinx-intl -f %{oreon_filedir}/python3-sphinx-intl.list

%changelog

%autochangelog
