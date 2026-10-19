%global source0_hash 0a380ab72853487ea2764c5df772f35026b4219868fc3eba68e193c9aea230ac
Name:           python-oracledb
Version:        4.0.2
Release:        1%{?dist}
Summary:        Python interface to Oracle Database
License:        UPL-1.0 OR Apache-2.0
URL:            https://oracle.github.io/python-oracledb
Source0:        https://files.pythonhosted.org/packages/source/o/oracledb/oracledb-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.2
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-oracledb = %{version}-%{release}
# /oreon:deps
%package -n       python3-oracledb+test
Summary:        Metapackage for python3-oracledb test extras
Requires:       python3-oracledb = %{version}-%{release}
Provides:       python3dist(oracledb[test]) = %{version}-%{release}

%description -n python3-oracledb+test
Metapackage for python3-oracledb test extras.

%package -n       python3-oracledb+oci_config
Summary:        Metapackage for python3-oracledb oci_config extras
Requires:       python3-oracledb = %{version}-%{release}
Provides:       python3dist(oracledb[oci_config]) = %{version}-%{release}

%description -n python3-oracledb+oci_config
Metapackage for python3-oracledb oci_config extras.

%package -n       python3-oracledb+oci_auth
Summary:        Metapackage for python3-oracledb oci_auth extras
Requires:       python3-oracledb = %{version}-%{release}
Requires:       python3dist(requests) >= 2.33
Provides:       python3dist(oracledb[oci_auth]) = %{version}-%{release}

%description -n python3-oracledb+oci_auth
Metapackage for python3-oracledb oci_auth extras.

%package -n       python3-oracledb+azure_config
Summary:        Metapackage for python3-oracledb azure_config extras
Requires:       python3-oracledb = %{version}-%{release}
Provides:       python3dist(oracledb[azure_config]) = %{version}-%{release}

%description -n python3-oracledb+azure_config
Metapackage for python3-oracledb azure_config extras.

%package -n       python3-oracledb+azure_auth
Summary:        Metapackage for python3-oracledb azure_auth extras
Requires:       python3-oracledb = %{version}-%{release}
Provides:       python3dist(oracledb[azure_auth]) = %{version}-%{release}

%description -n python3-oracledb+azure_auth
Metapackage for python3-oracledb azure_auth extras.

%description

%package -n     python3-oracledb
Summary:        Python interface to Oracle Database
# oreon:reqs
Requires:       python3dist(cryptography) >= 3.2.1
Requires:       python3dist(typing-extensions) >= 4.14.0
# /oreon:reqs
%description -n python3-oracledb

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir oracledb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-oracledb usr/lib/python3*/site-packages/oracledb* usr/lib64/python3*/site-packages/oracledb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oracledb* usr/lib64/python3*/site-packages/oracledb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-oracledb -f %{oreon_filedir}/python3-oracledb.list

%changelog

%autochangelog
