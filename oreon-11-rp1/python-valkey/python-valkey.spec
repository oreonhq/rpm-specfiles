%global source0_hash 0dca8e78701968f59b8c038f4efdfe308da80bd9cdca8dcae784e8d7af69a23c
Name:           python-valkey
Version:        6.1.1
Release:        1%{?dist}
Summary:        The Python interface to the Valkey key-value store
License:        MIT
URL:            https://github.com/valkey-io/valkey-py
Source0:        https://github.com/valkey-io/valkey-py/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         fix-tests-with-version-lower-than-9.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-valkey = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-valkey
Summary:        The Python interface to the Valkey key-value store
%description -n python3-valkey

This is a Python 3 interface to the Valkey key-value store.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n valkey-py-%{version}
# Upstream pins this dependency, but we need to be more flexible.
sed -e '/ocsp/ s/pyopenssl==/pyopenssl>=/' \
    -i setup.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-valkey usr/lib/python3*/site-packages/valkey* usr/lib64/python3*/site-packages/valkey* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/valkey* usr/lib64/python3*/site-packages/valkey* usr/bin/*

%check

echo 'enable-module-command yes' | valkey-server --port 6379 --enable-debug-command yes - &
%pytest -m 'not onlycluster and not redismod and not ssl' -k 'not get_from_cache and not test_cache_decode_response[sentinel_setup0] and not psync and not test_geopos and not geosearch and not georadius'
kill %1
%files
%files -n python3-valkey -f %{oreon_filedir}/python3-valkey.list

%changelog

%autochangelog
