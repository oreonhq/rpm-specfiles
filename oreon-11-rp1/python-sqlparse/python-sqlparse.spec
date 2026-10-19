%global source0_hash 113c35c75365ab9cc9c7231d68c6428fb11c085fc8e9eb1ad659b7ddbf6cd2b9
Name:           python-sqlparse
Version:        0.6.0
Release:        1%{?dist}
Summary:        A non-validating SQL parser.
License:        ...
URL:            https://github.com/andialbrecht/sqlparse
Source0:        https://files.pythonhosted.org/packages/source/s/sqlparse/sqlparse-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sqlparse = %{version}-%{release}
# /oreon:deps
%package -n       python3-sqlparse+dev
Summary:        Metapackage for python3-sqlparse dev extras
Requires:       python3-sqlparse = %{version}-%{release}
Provides:       python3dist(sqlparse[dev]) = %{version}-%{release}

%description -n python3-sqlparse+dev
Metapackage for python3-sqlparse dev extras.

%package -n       python3-sqlparse+doc
Summary:        Metapackage for python3-sqlparse doc extras
Requires:       python3-sqlparse = %{version}-%{release}
Provides:       python3dist(sqlparse[doc]) = %{version}-%{release}

%description -n python3-sqlparse+doc
Metapackage for python3-sqlparse doc extras.

%description

%package -n     python3-sqlparse
Summary:        A non-validating SQL parser.
%description -n python3-sqlparse

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlparse-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlparse usr/lib/python3*/site-packages/sqlparse* usr/lib64/python3*/site-packages/sqlparse* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlparse* usr/lib64/python3*/site-packages/sqlparse* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlparse -f %{oreon_filedir}/python3-sqlparse.list

%changelog

%autochangelog
