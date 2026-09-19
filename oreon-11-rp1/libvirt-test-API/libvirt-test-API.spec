%global source0_hash 71fafcec5c533486371cb2e1e154b6e173e13f643a9c82735e62abdac6428f79

# Disable the shebangs checks on scripts that currently don't
# define a Python version. The point here is that these scripts
# will be copied to guest VM instances, which may be running
# operating systems that can have either Python 2 or Python 3,
# but it's impossible to know for sure at packaging time.
%global __brp_mangle_shebangs_exclude_from virtlab.py|jenkins.py

%global with_python2 1
%if 0%{?fedora} > 30 || 0%{?rhel} > 7
%global with_python2 0
%endif

%global with_python3 0
%if 0%{?fedora} > 30 || 0%{?rhel} > 7
%global with_python3 1
%endif

%if %{with_python3}
%global __python %{__python3}
%else
%global __python %{__python2}
%endif

Summary: Python based regression tests for libvirt API
Name: libvirt-test-API
Version: 1.1
Release: 22%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/libvirt/libvirt-test-API
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: mock

%if %{with_python3}
BuildRequires: python3-devel
BuildRequires: python3-lxml
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-six
BuildRequires: python3-attrs
BuildRequires: python3-libvirt
BuildRequires: python3-pexpect

Requires: python3-six
Requires: python3-lxml
Requires: python3-libvirt

%else
BuildRequires: python2-devel
BuildRequires: python2-pytest
BuildRequires: python2-setuptools
BuildRequires: python2-attrs
BuildRequires: python-six
BuildRequires: python2-pexpect

Requires: python-six
Requires: python-lxml
%endif

Requires: libvirt
Requires: qemu-kvm
Requires: qemu-img
Requires: virt-install

%if 0%{?rhel} && 0%{?rhel} < 8
Requires: libvirt-python
%endif

BuildArch: noarch

%description
Libvirt-test-API is designed to test the functionality of libvirt
through Python bindings of libvirt API. It supports writing cases
by using the Python language. It supports testing for KVM and
Xen either paravirt (for which only Fedora and Red Hat Enterprise
Linux guests are currently supported) as well as fully virtualized guests.

%package        doc
Summary:        Documentation files for libvirt-test-API
BuildArch:      noarch

%description    doc
This package installs the detailed documentation of libvirt-test-API

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%py_build

%install
%py_install

%check
%{__python} setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python_sitelib}/libvirt_test_API*
%{python_sitelib}/libvirttestapi*
%{_datadir}/libvirt-test-API*

%files doc
%license LICENSE
%doc docs/

%changelog
%autochangelog
