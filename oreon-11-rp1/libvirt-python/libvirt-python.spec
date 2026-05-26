# -*- rpm-spec -*-

# This spec file assumes you are building on a Fedora or RHEL version
# that's still supported by the vendor. It may work on other distros
# or versions, but no effort will be made to ensure that going forward
%define min_rhel 8
%define min_fedora 33

%if (0%{?fedora} && 0%{?fedora} >= %{min_fedora}) || (0%{?rhel} && 0%{?rhel} >= %{min_rhel}) || 0%{?oreon}
    %define supported_platform 1
%else
    %define supported_platform 0
%endif

%define dist_name libvirt_python

Summary: The libvirt virtualization API python3 binding
Name: libvirt-python
Version: 12.0.0
Release: 1%{?dist}
Source0: https://libvirt.org/sources/python/%{dist_name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 7b4de7d2dde2bc380cf4e108d1eeb8aad50beb3ae351ab9265a7fedc587742bc
%global source0_file libvirt_python-12.0.0.tar.gz
# oreon url source checksums end
Url: https://libvirt.org
License: LGPL-2.1-or-later
BuildRequires: libvirt-devel == %{version}
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-lxml
BuildRequires: python3-setuptools
BuildRequires: gcc

# Don't want provides for python shared objects
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libvirt_python-12.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7b4de7d2dde2bc380cf4e108d1eeb8aad50beb3ae351ab9265a7fedc587742bc" || { echo "oreon: Source0 SHA256 mismatch for libvirt_python-12.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{dist_name}-%{version}

# Unset execute bit for example scripts; it can introduce spurious
# RPM dependencies, like /usr/bin/python3
# for the -python3 package
find examples -type f -exec chmod 0644 \{\} \;

%build
%if ! %{supported_platform}
echo "This RPM requires either Fedora >= %{min_fedora} or RHEL >= %{min_rhel}"
exit 1
%endif

%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-libvirt
%doc ChangeLog AUTHORS README COPYING examples/
%{python3_sitearch}/libvirt.py*
%{python3_sitearch}/libvirtaio.py*
%{python3_sitearch}/libvirt_qemu.py*
%{python3_sitearch}/libvirt_lxc.py*
%{python3_sitearch}/__pycache__/libvirt.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirt_qemu.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirt_lxc.cpython-*.py*
%{python3_sitearch}/__pycache__/libvirtaio.cpython-*.py*
%{python3_sitearch}/libvirtmod*
%{python3_sitearch}/*egg-info


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.0.0-1
- Import
