%global source0_hash 781cfa9a42de8f33c52aff857fd0a04e483de4fd1c53eaaa9a6aeac62bad11de
Name:           python-tablib
Version:        3.10.0
Release:        1%{?dist}
Summary:        Format agnostic tabular data library _XLS, JSON, YAML, CSV, etc._
License:        MIT
URL:            https://tablib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/t/tablib/tablib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 58
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-tablib = %{version}-%{release}
# /oreon:deps
%package -n       python3-tablib+all
Summary:        Metapackage for python3-tablib all extras
Requires:       python3-tablib = %{version}-%{release}
Requires:       python3dist(openpyxl) >= 2.6.0
Provides:       python3dist(tablib[all]) = %{version}-%{release}

%description -n python3-tablib+all
Metapackage for python3-tablib all extras.

%package -n       python3-tablib+cli
Summary:        Metapackage for python3-tablib cli extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[cli]) = %{version}-%{release}

%description -n python3-tablib+cli
Metapackage for python3-tablib cli extras.

%package -n       python3-tablib+html
Summary:        Metapackage for python3-tablib html extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[html]) = %{version}-%{release}

%description -n python3-tablib+html
Metapackage for python3-tablib html extras.

%package -n       python3-tablib+ods
Summary:        Metapackage for python3-tablib ods extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[ods]) = %{version}-%{release}

%description -n python3-tablib+ods
Metapackage for python3-tablib ods extras.

%package -n       python3-tablib+pandas
Summary:        Metapackage for python3-tablib pandas extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[pandas]) = %{version}-%{release}

%description -n python3-tablib+pandas
Metapackage for python3-tablib pandas extras.

%package -n       python3-tablib+xls
Summary:        Metapackage for python3-tablib xls extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[xls]) = %{version}-%{release}

%description -n python3-tablib+xls
Metapackage for python3-tablib xls extras.

%package -n       python3-tablib+xlsx
Summary:        Metapackage for python3-tablib xlsx extras
Requires:       python3-tablib = %{version}-%{release}
Requires:       python3dist(openpyxl) >= 2.6.0
Provides:       python3dist(tablib[xlsx]) = %{version}-%{release}

%description -n python3-tablib+xlsx
Metapackage for python3-tablib xlsx extras.

%package -n       python3-tablib+yaml
Summary:        Metapackage for python3-tablib yaml extras
Requires:       python3-tablib = %{version}-%{release}
Provides:       python3dist(tablib[yaml]) = %{version}-%{release}

%description -n python3-tablib+yaml
Metapackage for python3-tablib yaml extras.

%description

%package -n     python3-tablib
Summary:        Format agnostic tabular data library _XLS, JSON, YAML, CSV, etc._
%description -n python3-tablib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir tablib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tablib usr/lib/python3*/site-packages/tablib* usr/lib64/python3*/site-packages/tablib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tablib* usr/lib64/python3*/site-packages/tablib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-tablib -f %{oreon_filedir}/python3-tablib.list

%changelog

%autochangelog
