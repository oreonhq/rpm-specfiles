%global source0_hash 79b72d5ac5143992d1836ad78f4d8e65666061dd44e220548caab3723089826b
Name:           python-requests-cache
Version:        1.3.3
Release:        1%{?dist}
Summary:        A persistent cache for python requests
License:        BSD-2-Clause
URL:            https://github.com/requests-cache/requests-cache
Source0:        https://files.pythonhosted.org/packages/source/r/requests_cache/requests_cache-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.0.0
Requires:       python3-requests-cache = %{version}-%{release}
# /oreon:deps
%package -n       python3-requests-cache+dynamodb
Summary:        Metapackage for python3-requests-cache dynamodb extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.15
Requires:       python3dist(botocore) >= 1.18
Provides:       python3dist(requests-cache[dynamodb]) = %{version}-%{release}

%description -n python3-requests-cache+dynamodb
Metapackage for python3-requests-cache dynamodb extras.

%package -n       python3-requests-cache+mongodb
Summary:        Metapackage for python3-requests-cache mongodb extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(pymongo) >= 3
Provides:       python3dist(requests-cache[mongodb]) = %{version}-%{release}

%description -n python3-requests-cache+mongodb
Metapackage for python3-requests-cache mongodb extras.

%package -n       python3-requests-cache+redis
Summary:        Metapackage for python3-requests-cache redis extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(redis) >= 3
Provides:       python3dist(requests-cache[redis]) = %{version}-%{release}

%description -n python3-requests-cache+redis
Metapackage for python3-requests-cache redis extras.

%package -n       python3-requests-cache+security
Summary:        Metapackage for python3-requests-cache security extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(itsdangerous) >= 2.0
Provides:       python3dist(requests-cache[security]) = %{version}-%{release}

%description -n python3-requests-cache+security
Metapackage for python3-requests-cache security extras.

%package -n       python3-requests-cache+yaml
Summary:        Metapackage for python3-requests-cache yaml extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(pyyaml) >= 6.0.1
Provides:       python3dist(requests-cache[yaml]) = %{version}-%{release}

%description -n python3-requests-cache+yaml
Metapackage for python3-requests-cache yaml extras.

%package -n       python3-requests-cache+all
Summary:        Metapackage for python3-requests-cache all extras
Requires:       python3-requests-cache = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.15
Requires:       python3dist(botocore) >= 1.18
Requires:       python3dist(itsdangerous) >= 2.0
Requires:       python3dist(orjson) >= 3.0
Requires:       python3dist(pymongo) >= 3
Requires:       python3dist(pyyaml) >= 6.0.1
Requires:       python3dist(redis) >= 3
Requires:       python3dist(ujson) >= 5.4
Provides:       python3dist(requests-cache[all]) = %{version}-%{release}

%description -n python3-requests-cache+all
Metapackage for python3-requests-cache all extras.

%description

%package -n     python3-requests-cache
Summary:        A persistent cache for python requests
# oreon:reqs
Requires:       python3dist(attrs) >= 21.2
Requires:       python3dist(cattrs) >= 22.2
Requires:       python3dist(platformdirs) >= 2.5
Requires:       python3dist(requests) >= 2.22
Requires:       python3dist(url-normalize) >= 2.0
Requires:       python3dist(urllib3) >= 1.25.5
# /oreon:reqs
%description -n python3-requests-cache

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir requests_cache-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requests-cache usr/lib/python3*/site-packages/requests_cache* usr/lib64/python3*/site-packages/requests_cache* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requests_cache* usr/lib64/python3*/site-packages/requests_cache* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-requests-cache -f %{oreon_filedir}/python3-requests-cache.list

%changelog

%autochangelog
