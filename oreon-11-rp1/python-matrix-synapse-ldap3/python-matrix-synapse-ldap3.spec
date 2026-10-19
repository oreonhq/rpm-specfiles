%global source0_hash cff52ba780170de5e6e8af42863d2648ee23f3bf0a9fea6db52372f9fc00be2b
Name:           python-matrix-synapse-ldap3
Version:        0.4.0
Release:        1%{?dist}
Summary:        An LDAP3 auth provider for Synapse
License:        ...
URL:            https://github.com/matrix-org/matrix-synapse-ldap3
Source0:        https://files.pythonhosted.org/packages/source/m/matrix_synapse_ldap3/matrix_synapse_ldap3-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 39.2.0
Requires:       python3-matrix-synapse-ldap3 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-matrix-synapse-ldap3
Summary:        An LDAP3 auth provider for Synapse
%description -n python3-matrix-synapse-ldap3

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir matrix_synapse_ldap3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-matrix-synapse-ldap3 usr/lib/python3*/site-packages/matrix_synapse_ldap3* usr/lib64/python3*/site-packages/matrix_synapse_ldap3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/matrix_synapse_ldap3* usr/lib64/python3*/site-packages/matrix_synapse_ldap3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-matrix-synapse-ldap3 -f %{oreon_filedir}/python3-matrix-synapse-ldap3.list

%changelog

%autochangelog
