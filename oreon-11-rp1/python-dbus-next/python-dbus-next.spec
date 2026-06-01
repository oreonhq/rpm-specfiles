%global source0_hash db19689b0de50edd8587e8b55fcc6c30fe5155d813b9972e152ee05790beef59

%global pypi_name dbus-next
%global srcname   dbus_next

%bcond_without  tests

Name:           python-%{pypi_name}
Version:        0.2.3
Release:        18%{?dist}
Summary:        Zero-dependency DBus library for Python with asyncio support

License:        MIT
URL:            https://github.com/altdesktop/python-dbus-next
# pypi_source archive does not include test data
Source:        https://github.com/altdesktop/python-dbus-next/archive/v0.2.3/python-dbus-next-0.2.3.tar.gz
Patch:          0001-glib-destroy-the-_AuthLineSource-explicitly.patch
Patch:          0002-Address-Python-3.15-and-3.16-deprecations.patch
Patch:          0003-Fix-compatibility-with-pytest-asyncio-1.x.patch

BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  /usr/bin/dbus-run-session
%endif

%global _description %{expand:
python-dbus-next is a Python library for DBus that aims to be a fully
featured high level library primarily geared towards integration of
applications into Linux desktop and mobile environments.

Desktop application developers can use this library for integrating their
applications into desktop environments by implementing common DBus
standard interfaces or creating custom plugin interfaces.

Desktop users can use this library to create their own scripts and
utilities to interact with those interfaces for customization of their
desktop environment.

python-dbus-next plans to improve over other DBus libraries for Python in
the following ways:

 -  Zero dependencies and pure Python 3.
 -  Support for multiple IO backends including asyncio and the GLib main
    loop.
 -  Nonblocking IO suitable for GUI development.
 -  Target the latest language features of Python for beautiful services
    and clients.
 -  Complete implementation of the DBus type system without ever guessing
    types.
 -  Integration tests for all features of the library.
 -  Completely documented public API.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n python-dbus-next-0.2.3
# Fix permissions for examples
chmod -x examples/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
%if %{with tests}
# tests require dbus daemon to be running
%global __pytest  /usr/bin/dbus-run-session -- %{__pytest}
# test_tcp_connection_with_forwarding is broken by dbus 1.14.4
# altdesktop/python-dbus-next#135
PYTHONPATH="${PWD}" %pytest -k 'not test_tcp_connection_with_forwarding'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md examples/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.3-18
- Import
