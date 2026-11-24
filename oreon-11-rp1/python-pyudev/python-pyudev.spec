# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4e7faaec419b81a902d057568101819f448972c0cf448bb9c22203e4fc6a8eb9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname pyudev
%if 0%{?rhel} > 9 || 0%{?oreon}
%bcond_with qt
%else
%bcond_without qt
%endif

Name:             python-%{srcname}
Version:          0.24.5
Release:        %{autorelease}
Summary:          A libudev binding

License:          LGPL-2.1-or-later
URL:              http://pypi.python.org/pypi/pyudev
Source0:          https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

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

BuildRequires: oreon-rpm-macros
BuildRequires:    python3-devel

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
%oreon_sha256
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
%autochangelog
