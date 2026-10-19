%global source0_hash e080377d98957beec053580d38ae54fcdf7c470fb78670ba4bf8b5f9d5cad2a9
Name:           python-parsimonious
Version:        0.11.0
Release:        1%{?dist}
Summary:        _Soon to be_ the fastest pure-Python PEG parser I could muster
License:        MIT
URL:            https://github.com/erikrose/parsimonious
Source0:        https://files.pythonhosted.org/packages/source/p/parsimonious/parsimonious-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-parsimonious = %{version}-%{release}
# /oreon:deps
%package -n       python3-parsimonious+testing
Summary:        Metapackage for python3-parsimonious testing extras
Requires:       python3-parsimonious = %{version}-%{release}
Provides:       python3dist(parsimonious[testing]) = %{version}-%{release}

%description -n python3-parsimonious+testing
Metapackage for python3-parsimonious testing extras.

%description

%package -n     python3-parsimonious
Summary:        _Soon to be_ the fastest pure-Python PEG parser I could muster
# oreon:reqs
Requires:       python3dist(regex) >= 2022.3.15
# /oreon:reqs
%description -n python3-parsimonious

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir parsimonious-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-parsimonious usr/lib/python3*/site-packages/parsimonious* usr/lib64/python3*/site-packages/parsimonious* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/parsimonious* usr/lib64/python3*/site-packages/parsimonious* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-parsimonious -f %{oreon_filedir}/python3-parsimonious.list

%changelog

%autochangelog
