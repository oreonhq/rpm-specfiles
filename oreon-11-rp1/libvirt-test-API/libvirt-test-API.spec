%global source0_hash 9a783195b3f44a7c178fce9441c368cc18730cb27411000bbf58bfcecd0f43d1
%global __brp_mangle_shebangs_exclude_from virtlab.py|jenkins.py
%global with_python2 1
%global with_python3 0
%global __python %{__python3}
Summary:        Python based regression tests for libvirt API
Name: libvirt-test-API
Version: 1.1
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://github.com/libvirt/libvirt-test-API
Source0:        https://github.com/libvirt/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: python3-six
Requires: python3-lxml
Requires: python3-libvirt
Requires: libvirt
Requires: qemu-kvm
Requires: qemu-img
Requires: virt-install
BuildArch: noarch
# oreon:deps
BuildRequires:  mock
BuildRequires:  python3-attrs
BuildRequires:  python3-devel
BuildRequires:  python3-libvirt
BuildRequires:  python3-lxml
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
# /oreon:deps
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
%oreon_autofiles main usr/*/lib*.so.*

%check

%{__python} setup.py test
%files -f %{oreon_filedir}/main.list
%files -n libvirt-test-API-doc -f %{oreon_filedir}/libvirt-test-API-doc.list

%changelog

%autochangelog
