%global source0_hash d5b288529782e536ae171866df3ca9dc4f6cbfb3cc2f18e6f837fbb90dbc262b
Name:           python-pymysql
Version:        1.2.3
Release:        1%{?dist}
Summary:        Pure Python MySQL Driver
License:        MIT
URL:            https://github.com/PyMySQL/PyMySQL
Source0:        https://files.pythonhosted.org/packages/source/p/pymysql/pymysql-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pymysql = %{version}-%{release}
# /oreon:deps
%package -n       python3-pymysql+rsa
Summary:        Metapackage for python3-pymysql rsa extras
Requires:       python3-pymysql = %{version}-%{release}
Requires:       python3dist(cryptography) >= 46.0.7
Provides:       python3dist(pymysql[rsa]) = %{version}-%{release}

%description -n python3-pymysql+rsa
Metapackage for python3-pymysql rsa extras.

%package -n       python3-pymysql+ed25519
Summary:        Metapackage for python3-pymysql ed25519 extras
Requires:       python3-pymysql = %{version}-%{release}
Requires:       python3dist(pynacl) >= 1.6.2
Provides:       python3dist(pymysql[ed25519]) = %{version}-%{release}

%description -n python3-pymysql+ed25519
Metapackage for python3-pymysql ed25519 extras.

%description

%package -n     python3-pymysql
Summary:        Pure Python MySQL Driver
%description -n python3-pymysql

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pymysql-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymysql usr/lib/python3*/site-packages/pymysql* usr/lib64/python3*/site-packages/pymysql* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymysql* usr/lib64/python3*/site-packages/pymysql* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymysql -f %{oreon_filedir}/python3-pymysql.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-3
- Prepare for Oreon 11 (RP1)
