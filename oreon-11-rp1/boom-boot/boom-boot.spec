%global source0_hash aa8980c9e33fa6130d678233bea71afa25f2d041186e19b6513f093de7d74a53

%global summary A set of libraries and tools for managing boot loader entries
%global sphinx_docs 1

Name:		boom-boot
Version:	1.6.8
Release:	4%{?dist}
Summary:	%{summary}

License:	Apache-2.0
URL:		https://github.com/snapshotmanager/boom-boot
Source0:        https://github.com/snapshotmanager/boom-boot/archive/1.6.8/boom-boot-1.6.8.tar.gz

BuildArch:	noarch

BuildRequires:	make
BuildRequires:	python3-devel
%if 0%{?rhel} && 0%{?rhel} < 11
BuildRequires:	python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%endif
BuildRequires:  python3-pytest
%if 0%{?sphinx_docs}
BuildRequires:	python3-dbus
BuildRequires:	python3-sphinx
%endif
BuildRequires: make

Requires: python3-boom = %{version}-%{release}
Requires: %{name}-conf = %{version}-%{release}
Requires: python3-dbus
%if 0%{?rhel} == 9
Requires: systemd >= 252-18
%else
Requires: systemd >= 254
%endif

Obsoletes: boom-boot-grub2 <= 1.3
# boom-grub2 was not an official name of subpackage in fedora, but was used upstream:
Obsoletes: boom-grub2 <= 1.3

%package -n python3-boom
Summary: %{summary}
%{?python_provide:%python_provide python3-boom}
Requires: %{__python3}
Recommends: (lvm2 or brtfs-progs)
Recommends: %{name}-conf = %{version}-%{release}

# There used to be a boom package in fedora, and there is boom packaged in
# copr. How to tell which one is installed? We need python3-boom and no boom
# only.
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
%autosetup -p1 -n %{name}-%{version}

%if 0%{?fedora} || 0%{?rhel} >= 11
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?sphinx_docs}
make %{?_smp_mflags} -C doc html
rm doc/_build/html/.buildinfo
mv doc/_build/html doc/html
rm -r doc/_build
%endif

%if 0%{?rhel} && 0%{?rhel} < 11
%py3_build
%else
%pyproject_wheel
%endif

%install
%if 0%{?rhel} && 0%{?rhel} < 11
%py3_install
%else
%pyproject_install
%endif

# Make configuration directories
# mode 0700 - in line with /boot/grub2 directory:
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

%check
pytest-3 --log-level=debug -v

%files
%license LICENSE
%doc README.md
%{_bindir}/boom
%doc %{_mandir}/man*/boom.*

%files -n python3-boom
%license LICENSE
%doc README.md
%{python3_sitelib}/boom/*
%if 0%{?rhel} && 0%{?rhel} < 11
%{python3_sitelib}/boom*.egg-info/
%else
%{python3_sitelib}/boom*.dist-info/
%endif
%doc doc
%doc examples
%doc tests

%files conf
%license LICENSE
%doc README.md
%dir /boot/boom
%config(noreplace) /boot/boom/boom.conf
%dir /boot/boom/profiles
%dir /boot/boom/hosts
%dir /boot/boom/cache
%dir /boot/loader/entries


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.8-4
- Prepare for Oreon 11 (RP1)
