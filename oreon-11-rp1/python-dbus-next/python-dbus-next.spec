%global source0_hash db19689b0de50edd8587e8b55fcc6c30fe5155d813b9972e152ee05790beef59
%global pypi_name dbus-next
%global srcname   dbus_next
%bcond_without  tests
Name:           python-%{pypi_name}
Version:        0.2.3
Release:        1%{?dist}
Summary:        Zero-dependency DBus library for Python with asyncio support
License:        MIT
URL:            https://github.com/altdesktop/python-dbus-next
Source0:        https://github.com/altdesktop/python-dbus-next/archive/refs/tags/v0.2.3.tar.gz#/python-dbus-next-0.2.3.tar.gz
Patch:          0001-glib-destroy-the-_AuthLineSource-explicitly.patch
Patch:          0002-Address-Python-3.15-and-3.16-deprecations.patch
Patch:          0003-Fix-compatibility-with-pytest-asyncio-1.x.patch
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dbus-next = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        Zero-dependency DBus library for Python with asyncio support
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n python-dbus-next-0.2.3
# Fix permissions for examples
chmod -x examples/*.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/dbus_next* usr/lib64/python3*/site-packages/dbus_next* usr/bin/*

%check

%pyproject_check_import
%if %{with tests}
%global __pytest  /usr/bin/dbus-run-session -- %{__pytest}
PYTHONPATH="${PWD}" %pytest -k 'not test_tcp_connection_with_forwarding'
%endif
%files
%files -n python3-dbus-next -f %{oreon_filedir}/python3-dbus-next.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.3-18
- Import
