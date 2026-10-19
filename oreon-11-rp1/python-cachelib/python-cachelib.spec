%global source0_hash f3c7dc8d3c1132ab699681ffdf8a52d341d9425ac1401c538cf0b1d87b1677c8
Name:           python-cachelib
Version:        0.17.0
Release:        1%{?dist}
Summary:        A collection of cache libraries in the same API interface.
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/cachelib/
Source0:        https://files.pythonhosted.org/packages/source/c/cachelib/cachelib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-cachelib = %{version}-%{release}
# /oreon:deps
%package -n       python3-cachelib+dynamodb
Summary:        Metapackage for python3-cachelib dynamodb extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.43.4
Provides:       python3dist(cachelib[dynamodb]) = %{version}-%{release}

%description -n python3-cachelib+dynamodb
Metapackage for python3-cachelib dynamodb extras.

%package -n       python3-cachelib+memcached
Summary:        Metapackage for python3-cachelib memcached extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(pylibmc) >= 1.6.3
Provides:       python3dist(cachelib[memcached]) = %{version}-%{release}

%description -n python3-cachelib+memcached
Metapackage for python3-cachelib memcached extras.

%package -n       python3-cachelib+mongodb
Summary:        Metapackage for python3-cachelib mongodb extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(pymongo) >= 4.11
Provides:       python3dist(cachelib[mongodb]) = %{version}-%{release}

%description -n python3-cachelib+mongodb
Metapackage for python3-cachelib mongodb extras.

%package -n       python3-cachelib+redis
Summary:        Metapackage for python3-cachelib redis extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(redis) >= 6.0.0
Provides:       python3dist(cachelib[redis]) = %{version}-%{release}

%description -n python3-cachelib+redis
Metapackage for python3-cachelib redis extras.

%package -n       python3-cachelib+valkey
Summary:        Metapackage for python3-cachelib valkey extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(valkey) >= 6.1.0
Provides:       python3dist(cachelib[valkey]) = %{version}-%{release}

%description -n python3-cachelib+valkey
Metapackage for python3-cachelib valkey extras.

%package -n       python3-cachelib+uwsgi
Summary:        Metapackage for python3-cachelib uwsgi extras
Requires:       python3-cachelib = %{version}-%{release}
Requires:       python3dist(uwsgi) >= 2.0.28
Provides:       python3dist(cachelib[uwsgi]) = %{version}-%{release}

%description -n python3-cachelib+uwsgi
Metapackage for python3-cachelib uwsgi extras.

%description

%package -n     python3-cachelib
Summary:        A collection of cache libraries in the same API interface.
%description -n python3-cachelib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir cachelib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-cachelib usr/lib/python3*/site-packages/cachelib* usr/lib64/python3*/site-packages/cachelib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/cachelib* usr/lib64/python3*/site-packages/cachelib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-cachelib -f %{oreon_filedir}/python3-cachelib.list

%changelog

%autochangelog
