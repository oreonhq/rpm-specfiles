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
Release: 1%{?dist}
Summary: %{sum}

License: BSD-3-Clause
URL: https://github.com/pymodbus-dev/pymodbus/
Source0: https://github.com/pymodbus-dev/pymodbus/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/pymodbus-dev/pymodbus/commit/eb84cfef92ddab8780652bd420479b9cb0a4a026
Patch0: 0001-Solve-ModbusDeviceContext-bug.-2653.patch

BuildArch: noarch
BuildRequires: python3-devel

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
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymodbus

# delete unnecessary shebang
sed -i '/^#!\/usr\/bin\/env.*$/d' $RPM_BUILD_ROOT%{python3_sitelib}/pymodbus/server/simulator/main.py

# remove test files
rm -rf %{buildroot}%{python3_sitelib}/test

%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc *.rst
%{_bindir}/pymodbus.simulator

%changelog
%autochangelog
