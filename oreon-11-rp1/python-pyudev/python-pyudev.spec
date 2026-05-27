%global source0_hash e788bb983700b1a84efc2e88862b0a51af2a995d5b86bc9997546505cf7b36bc

%global srcname pyudev
%if 0%{?rhel} > 9
%bcond_with qt
%else
%bcond_without qt
%endif

Name:             python-%{srcname}
Version:          0.24.4
Release:          %autorelease
Summary:          A libudev binding

License:          LGPL-2.1-or-later
URL:              http://pypi.python.org/pypi/pyudev
Source0:          https://pypi.io/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:        noarch

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.
The binding supports CPython 3 and PyPy.

%package -n python3-%{srcname}
Summary:          A libudev binding

BuildRequires:    python3-devel

# Needed for libudev, loaded through ctypes
Requires:         systemd-libs

%description -n python3-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.
The binding supports CPython 3 and PyPy.

%if %{with qt}
%package -n python3-%{srcname}-qt5
Summary:          Qt5 integration for pyudev

Requires:         python3-qt5
Requires:         python3-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}-qt5
Qt5 integration for pyudev.

This package provides a module pyudev.pyqt5 that contains classes for
integrating a pyudev monitor with the Qt5 main loop.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}.dist-info
%exclude %{python3_sitelib}/pyudev/glib.py
%exclude %{python3_sitelib}/pyudev/__pycache__/glib.*
%exclude %{python3_sitelib}/pyudev/pyqt4.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt4.*
%exclude %{python3_sitelib}/pyudev/pyqt5.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%exclude %{python3_sitelib}/pyudev/pyside.py
%exclude %{python3_sitelib}/pyudev/__pycache__/pyside.*
%exclude %{python3_sitelib}/pyudev/wx.py
%exclude %{python3_sitelib}/pyudev/__pycache__/wx.*

%if %{with qt}
%files -n python3-%{srcname}-qt5
%license COPYING
%{python3_sitelib}/pyudev/pyqt5.py
%{python3_sitelib}/pyudev/__pycache__/pyqt5.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24.4-1
- Prepare for Oreon 11 (RP1)
