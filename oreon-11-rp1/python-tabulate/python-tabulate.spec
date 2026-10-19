%global source0_hash e2cfde8f79420f6deeffdeda9aaec3b6bc5abce947655d17ac662b126e48a60d
Name:           python-tabulate
Version:        0.10.0
Release:        1%{?dist}
Summary:        Pretty-print tabular data
License:        MIT
URL:            https://github.com/astanin/python-tabulate
Source0:        https://files.pythonhosted.org/packages/source/t/tabulate/tabulate-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-tabulate = %{version}-%{release}
# /oreon:deps
%package -n       python3-tabulate+widechars
Summary:        Metapackage for python3-tabulate widechars extras
Requires:       python3-tabulate = %{version}-%{release}
Provides:       python3dist(tabulate[widechars]) = %{version}-%{release}

%description -n python3-tabulate+widechars
Metapackage for python3-tabulate widechars extras.

%description

%package -n     python3-tabulate
Summary:        Pretty-print tabular data
%description -n python3-tabulate

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tabulate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tabulate usr/lib/python3*/site-packages/tabulate* usr/lib64/python3*/site-packages/tabulate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tabulate* usr/lib64/python3*/site-packages/tabulate* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tabulate -f %{oreon_filedir}/python3-tabulate.list

%changelog

%autochangelog
