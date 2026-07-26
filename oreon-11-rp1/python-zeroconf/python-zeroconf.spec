%global source0_hash 57f044f1c4c24c1c1c658b257cf4b8174af49a8d9082533be085efc8edb52f95

Name:           python-zeroconf
Version:        0.118.0
Release:        %autorelease
Summary:        Pure Python Multicast DNS Service Discovery Library

License:        LGPL-2.1-or-later
URL:            https://github.com/jstasiak/python-zeroconf
Source0:        %{url}/archive/%{version}/zeroconf-%{version}.tar.gz

# Fixup the Cython declaration of zeroconf._handlers.record_manager.async_updates_complete to match the Python type
# Partially cherry-picked from https://github.com/python-zeroconf/python-zeroconf/commit/9eac0a12
Patch:          cython-3.2.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio

%description
A pure Python implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%package -n     python3-zeroconf
Summary:        %{summary}

%description -n python3-zeroconf
A pure Python 3 implementation of multicast DNS service discovery
supporting Bonjour/Avahi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Upstream requires this for https://github.com/python-poetry/poetry/issues/7505
# But it's not relevant for the RPM package
sed -i 's/poetry-core>=1.5.2/poetry-core/' pyproject.toml
# We don't measure coverage in tests
sed -Ei 's/--cov(-|=)[^ "]+//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
# Explicitly choose to compile the Cython extensions
export REQUIRE_CYTHON=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zeroconf

%check
# IPv6 tests fail in Koji/mock, test_sending_unicast uses IPv6
%pytest -v -k "not test_sending_unicast and not test_integration_with_listener_ipv6"

%files -n python3-zeroconf -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
