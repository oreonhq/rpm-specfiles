%global source0_hash c9107fea58ea8ab8b9a29de3c34e0b4b2421a85bedc8a4900c91f1eed081bcc5
%global sum A Modbus Protocol Stack in Python
%global desc Pymodbus is a full Modbus protocol implementation using twisted for its \
asynchronous communications core. \
\
The library currently supports the following: \
\
Client Features \
\
    * Full read/write protocol on discrete and register \
    * Most of the extended protocol (diagnostic/file/pipe/setting/information) \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Payload builder/decoder utilities \
\
Server Features \
\
    * Can function as a fully implemented Modbus server \
    * TCP, UDP, Serial ASCII, Serial RTU, and Serial Binary \
    * asynchronous(powered by twisted) and synchronous versions \
    * Full server control context (device information, counters, etc) \
    * A number of backing contexts (database, redis, a slave device)
Name: pymodbus
Version: 3.15.0
Release:        1%{?dist}
Summary:        A Modbus Protocol Stack in Python
License: BSD-3-Clause
URL: https://github.com/pymodbus-dev/pymodbus/
Source0:        https://github.com/pymodbus-dev/pymodbus/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: 0001-Solve-ModbusDeviceContext-bug.-2653.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68.2.2
Requires:       python3-pymodbus = %{version}-%{release}
# /oreon:deps
%package -n       python3-pymodbus+serial
Summary:        Metapackage for python3-pymodbus serial extras
Requires:       python3-pymodbus = %{version}-%{release}
Requires:       python3dist(pyserial) >= 3.5
Provides:       python3dist(pymodbus[serial]) = %{version}-%{release}

%description -n python3-pymodbus+serial
Metapackage for python3-pymodbus serial extras.

%package -n       python3-pymodbus+simulator
Summary:        Metapackage for python3-pymodbus simulator extras
Requires:       python3-pymodbus = %{version}-%{release}
Requires:       python3dist(aiohttp) >= 3.8.6
Requires:       python3dist(aiohttp) >= 3.14.1
Provides:       python3dist(pymodbus[simulator]) = %{version}-%{release}

%description -n python3-pymodbus+simulator
Metapackage for python3-pymodbus simulator extras.

%package -n       python3-pymodbus+documentation
Summary:        Metapackage for python3-pymodbus documentation extras
Requires:       python3-pymodbus = %{version}-%{release}
Requires:       python3dist(recommonmark) >= 0.7.1
Requires:       python3dist(sphinx) >= 7.3.7
Requires:       python3dist(sphinx) >= 9.1.0
Requires:       python3dist(sphinx-rtd-theme) >= 3.1.0
Provides:       python3dist(pymodbus[documentation]) = %{version}-%{release}

%description -n python3-pymodbus+documentation
Metapackage for python3-pymodbus documentation extras.

%package -n       python3-pymodbus+development
Summary:        Metapackage for python3-pymodbus development extras
Requires:       python3-pymodbus = %{version}-%{release}
Requires:       python3dist(build) >= 1.5.0
Requires:       python3dist(codespell) >= 2.4.2
Requires:       python3dist(coverage) >= 7.14.3
Requires:       python3dist(pylint) >= 4.0.6
Requires:       python3dist(pytest) >= 9.1.1
Requires:       python3dist(pytest-asyncio) >= 1.4.0
Requires:       python3dist(pytest-cov) >= 7.1.0
Requires:       python3dist(pytest-profiling) >= 1.7.0
Requires:       python3dist(pytest-timeout) >= 2.3.1
Requires:       python3dist(pytest-xdist) >= 3.6.1
Requires:       python3dist(pytest-aiohttp) >= 1.1.1
Requires:       python3dist(ruff) >= 0.15.20
Requires:       python3dist(twine) >= 6.2.0
Requires:       python3dist(zuban) >= 0.9.0
Provides:       python3dist(pymodbus[development]) = %{version}-%{release}

%description -n python3-pymodbus+development
Metapackage for python3-pymodbus development extras.

%package -n       python3-pymodbus+all
Summary:        Metapackage for python3-pymodbus all extras
Requires:       python3-pymodbus = %{version}-%{release}
Provides:       python3dist(pymodbus[all]) = %{version}-%{release}

%description -n python3-pymodbus+all
Metapackage for python3-pymodbus all extras.

%description
%{desc}

%package -n python3-%{name}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{name}}
BuildRequires: python3-devel
Requires: python3-pyserial >= 2.6
%description -n python3-%{name}
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# lower the version requirements for setuptools
sed -i 's/setuptools>=[^"]*"/setuptools>=62.0.0"/' pyproject.toml
%build

%pyproject_wheel
%install
%pyproject_install
sed -i '/^#!\/usr\/bin\/env.*$/d' $RPM_BUILD_ROOT%{python3_sitelib}/pymodbus/server/simulator/main.py
rm -rf %{buildroot}%{python3_sitelib}/test
%oreon_autofiles main usr/lib/python3*/site-packages/pymodbus* usr/lib64/python3*/site-packages/pymodbus* usr/bin/*

%files
%files -n python3-pymodbus -f %{oreon_filedir}/python3-pymodbus.list

%changelog

%autochangelog
