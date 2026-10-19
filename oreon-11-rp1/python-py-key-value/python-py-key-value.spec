%global source0_hash 9f0fbd55b9040f9de5444c9ae7fe54ea137fd321156747e71636cefeb74ed7bd
%global extras disk,elasticsearch,keyring,memory,pydantic,redis
Name:           python-py-key-value
Version:        0.3.0
Release:        1%{?dist}
Summary:        Key-Value Store Project
License:        Apache-2.0
BuildArch:      noarch
URL:            https://github.com/strawgate/py-key-value
Source0:        https://github.com/strawgate/py-key-value/archive/%{version}/py-key-value-%{version}.tar.gz
Patch:          0001-Fedora-dependency-adjustments.patch
Patch1:         0002-Drop-the-docker-setup-from-redis-store-tests.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.9.0
BuildRequires:  python3dist(uv-build) >= 0.8.2
Requires:       python3-py-key-value = %{version}-%{release}
# /oreon:deps
%package -n       python3-py-key-value+memory
Summary:        Metapackage for python3-py-key-value memory extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(cachetools) >= 5.0.0
Provides:       python3dist(py-key-value[memory]) = %{version}-%{release}

%description -n python3-py-key-value+memory
Metapackage for python3-py-key-value memory extras.

%package -n       python3-py-key-value+disk
Summary:        Metapackage for python3-py-key-value disk extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(diskcache) >= 5.0.0
Requires:       python3dist(pathvalidate) >= 3.3.1
Provides:       python3dist(py-key-value[disk]) = %{version}-%{release}

%description -n python3-py-key-value+disk
Metapackage for python3-py-key-value disk extras.

%package -n       python3-py-key-value+filetree
Summary:        Metapackage for python3-py-key-value filetree extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(aiofile) >= 3.5.0
Requires:       python3dist(anyio) >= 4.4.0
Provides:       python3dist(py-key-value[filetree]) = %{version}-%{release}

%description -n python3-py-key-value+filetree
Metapackage for python3-py-key-value filetree extras.

%package -n       python3-py-key-value+redis
Summary:        Metapackage for python3-py-key-value redis extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(redis) >= 4.3.0
Provides:       python3dist(py-key-value[redis]) = %{version}-%{release}

%description -n python3-py-key-value+redis
Metapackage for python3-py-key-value redis extras.

%package -n       python3-py-key-value+mongodb
Summary:        Metapackage for python3-py-key-value mongodb extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(pymongo) >= 4.0.0
Provides:       python3dist(py-key-value[mongodb]) = %{version}-%{release}

%description -n python3-py-key-value+mongodb
Metapackage for python3-py-key-value mongodb extras.

%package -n       python3-py-key-value+valkey
Summary:        Metapackage for python3-py-key-value valkey extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(valkey-glide) >= 2.1.0
Provides:       python3dist(py-key-value[valkey]) = %{version}-%{release}

%description -n python3-py-key-value+valkey
Metapackage for python3-py-key-value valkey extras.

%package -n       python3-py-key-value+vault
Summary:        Metapackage for python3-py-key-value vault extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(hvac) >= 2.3.0
Requires:       python3dist(types-hvac) >= 2.3.0
Provides:       python3dist(py-key-value[vault]) = %{version}-%{release}

%description -n python3-py-key-value+vault
Metapackage for python3-py-key-value vault extras.

%package -n       python3-py-key-value+memcached
Summary:        Metapackage for python3-py-key-value memcached extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(aiomcache) >= 0.8.0
Provides:       python3dist(py-key-value[memcached]) = %{version}-%{release}

%description -n python3-py-key-value+memcached
Metapackage for python3-py-key-value memcached extras.

%package -n       python3-py-key-value+elasticsearch
Summary:        Metapackage for python3-py-key-value elasticsearch extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(elasticsearch) >= 8.0.0
Requires:       python3dist(aiohttp) >= 3.12
Provides:       python3dist(py-key-value[elasticsearch]) = %{version}-%{release}

%description -n python3-py-key-value+elasticsearch
Metapackage for python3-py-key-value elasticsearch extras.

%package -n       python3-py-key-value+dynamodb
Summary:        Metapackage for python3-py-key-value dynamodb extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(aioboto3) >= 13.3.0
Requires:       python3dist(types-aiobotocore-dynamodb) >= 2.16.0
Provides:       python3dist(py-key-value[dynamodb]) = %{version}-%{release}

%description -n python3-py-key-value+dynamodb
Metapackage for python3-py-key-value dynamodb extras.

%package -n       python3-py-key-value+keyring
Summary:        Metapackage for python3-py-key-value keyring extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(keyring) >= 25.6.0
Provides:       python3dist(py-key-value[keyring]) = %{version}-%{release}

%description -n python3-py-key-value+keyring
Metapackage for python3-py-key-value keyring extras.

%package -n       python3-py-key-value+keyring-linux
Summary:        Metapackage for python3-py-key-value keyring-linux extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(keyring) >= 25.6.0
Requires:       python3dist(dbus-python) >= 1.4.0
Provides:       python3dist(py-key-value[keyring-linux]) = %{version}-%{release}

%description -n python3-py-key-value+keyring-linux
Metapackage for python3-py-key-value keyring-linux extras.

%package -n       python3-py-key-value+pydantic
Summary:        Metapackage for python3-py-key-value pydantic extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(pydantic) >= 2.11.9
Provides:       python3dist(py-key-value[pydantic]) = %{version}-%{release}

%description -n python3-py-key-value+pydantic
Metapackage for python3-py-key-value pydantic extras.

%package -n       python3-py-key-value+rocksdb
Summary:        Metapackage for python3-py-key-value rocksdb extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(rocksdict) >= 0.3.24
Requires:       python3dist(rocksdict) >= 0.3.2
Provides:       python3dist(py-key-value[rocksdb]) = %{version}-%{release}

%description -n python3-py-key-value+rocksdb
Metapackage for python3-py-key-value rocksdb extras.

%package -n       python3-py-key-value+duckdb
Summary:        Metapackage for python3-py-key-value duckdb extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(duckdb) >= 1.1.1
Requires:       python3dist(pytz) >= 2025.2
Provides:       python3dist(py-key-value[duckdb]) = %{version}-%{release}

%description -n python3-py-key-value+duckdb
Metapackage for python3-py-key-value duckdb extras.

%package -n       python3-py-key-value+wrappers-encryption
Summary:        Metapackage for python3-py-key-value wrappers-encryption extras
Requires:       python3-py-key-value = %{version}-%{release}
Requires:       python3dist(cryptography) >= 45.0.0
Provides:       python3dist(py-key-value[wrappers-encryption]) = %{version}-%{release}

%description -n python3-py-key-value+wrappers-encryption
Metapackage for python3-py-key-value wrappers-encryption extras.

%description

%package -n python3-py-key-value-shared
Summary:        Shared Key-Value
%description -n python3-py-key-value-shared

This package provides the key_value.shared importable module.

%package -n python3-py-key-value-aio
Summary:        Async Key-Value
%description -n python3-py-key-value-aio

This package provides the key_value.aio importable module.

# The upstream monorepo also includes a key_value.sync module, but that is
# described as "under development".  For now we'll leave that out, but it can
# be added later as another subpackage if needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir py-key-value-%{version}
%oreon_prep
%build

cd key-value/key-value-shared-test
%pyproject_wheel
cd ../key-value-shared
%pyproject_wheel
cd ../key-value-aio
%pyproject_wheel
%install
cd key-value/key-value-shared-test
%pyproject_install
cd ../key-value-shared
%pyproject_install
cd ../key-value-aio
%pyproject_install
%oreon_autofiles python3-py-key-value-shared usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-py-key-value-aio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd key-value/key-value-shared
%pytest
cd ../key-value-aio
%{_bindir}/valkey-server --bind 127.0.0.1 --port 6380 &
VALKEY_SERVER_PID=$!
%pytest \
    --ignore tests/stores/duckdb \
    --ignore tests/stores/dynamodb \
    --ignore tests/stores/filetree \
    --ignore tests/stores/memcached \
    --ignore tests/stores/mongodb \
    --ignore tests/stores/rocksdb \
    --ignore tests/stores/vault \
    --ignore tests/stores/windows_registry
kill $VALKEY_SERVER_PID
%files
%files -n python3-py-key-value-shared -f %{oreon_filedir}/python3-py-key-value-shared.list
%files -n python3-py-key-value-aio -f %{oreon_filedir}/python3-py-key-value-aio.list

%changelog

%autochangelog
