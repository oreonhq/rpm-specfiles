%global source0_hash 439217116152244369caf3d9f1caf2f9fe29b03bd79e88d2928c8e718c95d680
Name:           python-prettytable
Version:        3.18.0
Release:        1%{?dist}
Summary:        A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
License:        BSD-3-Clause
URL:            https://github.com/prettytable/prettytable
Source0:        https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
Requires:       python3-prettytable = %{version}-%{release}
# /oreon:deps
%package -n       python3-prettytable+tests
Summary:        Metapackage for python3-prettytable tests extras
Requires:       python3-prettytable = %{version}-%{release}
Requires:       python3dist(pytest) >= 9
Provides:       python3dist(prettytable[tests]) = %{version}-%{release}

%description -n python3-prettytable+tests
Metapackage for python3-prettytable tests extras.

%description

%package -n     python3-prettytable
Summary:        A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
# oreon:reqs
Requires:       python3dist(wcwidth) >= 0.3.5
# /oreon:reqs
%description -n python3-prettytable

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir prettytable-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-prettytable usr/lib/python3*/site-packages/prettytable* usr/lib64/python3*/site-packages/prettytable* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/prettytable* usr/lib64/python3*/site-packages/prettytable* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-prettytable -f %{oreon_filedir}/python3-prettytable.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.0-1
- Prepare for Oreon 11 (RP1)
