# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 598b85cd1f5e94b97684b725cd45a65f6ab734c6edaa61d4aec98721f30e9401
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define min_rhel 9
%define min_fedora 43

%if (0%{?fedora} && 0%{?fedora} >= %{min_fedora}) || (0%{?rhel} && 0%{?rhel} >= %{min_rhel}) || 0%{?oreon}
    %define supported_platform 1
%else
    %define supported_platform 0
%endif

%define dist_name libvirt_python

Summary: The libvirt virtualization API python3 binding
Name: libvirt-python
Version: 12.9.0
Release: 1%{?dist}
Source0: https://libvirt.org/sources/python/%{dist_name}-%{version}.tar.gz
Url: https://libvirt.org
License: LGPL-2.1-or-later
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: libvirt-devel ==
BuildRequires: %{version}
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-lxml
%{?filter_provides_in: %filter_provides_in %{python3_sitearch}/.*\.so}
%{?filter_setup}

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n python3-libvirt
Summary: The libvirt virtualization API python3 binding
Url: http://libvirt.org
%{?python_provide:%python_provide python3-libvirt}
Provides: libvirt-python3 = %{version}-%{release}
Obsoletes: libvirt-python3 <= 3.6.0-1%{?dist}

%description -n python3-libvirt
The python3-libvirt package contains a module that permits applications
written in the Python 3.x programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%oreon_sha256
%setup -q -n %{dist_name}-%{version}

find examples -type f -exec chmod 0644 \{\} \;

%generate_buildrequires
%pyproject_buildrequires

%build
%if ! %{supported_platform}
echo "This RPM requires either Fedora >= %{min_fedora} or RHEL >= %{min_rhel}"
exit 1
%endif

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files libvirt libvirt_lxc libvirt_qemu libvirtaio 'libvirtmod*'

%check
%pyproject_check_import
%pytest

%files -n python3-libvirt -f %{pyproject_files}
%doc ChangeLog AUTHORS README COPYING examples/

%changelog
%autochangelog
