%global source0_hash e900e7b59a4781f63d9e935e88f6ec50c4d60be3f4adf9c63b51ed39d578fe08
Name:           python-avro
Version:        1.12.2
Release:        1%{?dist}
Summary:        Avro is a serialization and RPC framework.
License:        ...
URL:            https://avro.apache.org/
Source0:        https://files.pythonhosted.org/packages/source/a/avro/avro-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-remove-ipc-tests-as-they-require-internet-connection.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78.1.0
Requires:       python3-avro = %{version}-%{release}
# /oreon:deps
%package -n       python3-avro+snappy
Summary:        Metapackage for python3-avro snappy extras
Requires:       python3-avro = %{version}-%{release}
Provides:       python3dist(avro[snappy]) = %{version}-%{release}

%description -n python3-avro+snappy
Metapackage for python3-avro snappy extras.

%package -n       python3-avro+zstandard
Summary:        Metapackage for python3-avro zstandard extras
Requires:       python3-avro = %{version}-%{release}
Provides:       python3dist(avro[zstandard]) = %{version}-%{release}

%description -n python3-avro+zstandard
Metapackage for python3-avro zstandard extras.

%description

%package -n     python3-avro
Summary:        Avro is a serialization and RPC framework.
%description -n python3-avro

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir avro-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-avro usr/lib/python3*/site-packages/avro* usr/lib64/python3*/site-packages/avro* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/avro* usr/lib64/python3*/site-packages/avro* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-avro -f %{oreon_filedir}/python3-avro.list

%changelog

%autochangelog
