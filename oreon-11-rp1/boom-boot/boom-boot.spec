%global source0_hash aa8980c9e33fa6130d678233bea71afa25f2d041186e19b6513f093de7d74a53
%global summary A set of libraries and tools for managing boot loader entries
%global sphinx_docs 1
Name:		boom-boot
Version:	1.6.8
Release:        4%{?dist}
Summary:        A set of libraries and tools for managing boot loader entries
License:	Apache-2.0
URL:		https://github.com/snapshotmanager/boom-boot
Source0:        https://github.com/snapshotmanager/boom-boot/archive/refs/tags/1.6.8.tar.gz#/boom-boot-1.6.8.tar.gz
BuildArch:	noarch
%if 0%{?sphinx_docs}
%endif
Requires: python3-boom = %{version}-%{release}
Requires: %{name}-conf = %{version}-%{release}
Requires: python3-dbus
Requires: systemd >= 254
Obsoletes: boom-boot-grub2 <= 1.3
Obsoletes: boom-grub2 <= 1.3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-boom-boot = %{version}-%{release}
# /oreon:deps
%package -n       python3-boom-boot+docs
Summary:        Metapackage for python3-boom-boot docs extras
Requires:       python3-boom-boot = %{version}-%{release}
Requires:       python3dist(Sphinx) >= 1.8
Provides:       python3dist(boom-boot[docs]) = %{version}-%{release}

%description -n python3-boom-boot+docs
Metapackage for python3-boom-boot docs extras.

%package -n python3-boom
Summary:        A set of libraries and tools for managing boot loader entries
%{?python_provide:%python_provide python3-boom}
Requires: %{__python3}
Recommends: (lvm2 or brtfs-progs)
Recommends: %{name}-conf = %{version}-%{release}
Conflicts: boom
%package conf
Summary: %{summary}
%description
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

%description -n python3-boom
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

This package provides python3 boom module.

%description conf
Boom is a boot manager for Linux systems using boot loaders that support
the BootLoader Specification for boot entry configuration.

Boom requires a BLS compatible boot loader to function: either the
systemd-boot project, or Grub2 with the BLS patch (Red Hat Grub2 builds
include this support in both Red Hat Enterprise Linux 7 and Fedora).

This package provides configuration files for boom.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%if 0%{?sphinx_docs}
make %{?_smp_mflags} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -r doc/_build
%endif
%pyproject_wheel
%install
%pyproject_install
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/profiles
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/hosts
install -d -m 700 ${RPM_BUILD_ROOT}/boot/loader/entries
install -d -m 700 ${RPM_BUILD_ROOT}/boot/boom/cache
install -m 644 examples/boom.conf ${RPM_BUILD_ROOT}/boot/boom
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man5
install -m 644 man/man8/boom.8 ${RPM_BUILD_ROOT}/%{_mandir}/man8
install -m 644 man/man5/boom.5 ${RPM_BUILD_ROOT}/%{_mandir}/man5
rm doc/Makefile
rm doc/conf.py
%oreon_autofiles python3-boom usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles boom-boot-conf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pytest-3 --log-level=debug -v
%files
%files -n python3-boom -f %{oreon_filedir}/python3-boom.list
%files -n boom-boot-conf -f %{oreon_filedir}/boom-boot-conf.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.8-4
- Prepare for Oreon 11 (RP1)
