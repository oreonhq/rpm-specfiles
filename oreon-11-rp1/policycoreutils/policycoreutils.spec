%global source1_hash 42de7b2055fbf75452a30b6a306dd2940e23f1c0f330d3bcb886d037417d066d
%global source0_hash 6b6d47ab0f35fe1c09bda0c62821c8d97a0cbe7f6e9404b338df7bde0182c4f4
%global source2_key_fpr 63191CE94183098689CAB8DB7EF137EC935B0EAF
%global libauditver     4.0
%global libsepolver     3.11-1
%global libsemanagever  3.11-1
%global libselinuxver   3.11-1
%global generatorsdir %{_prefix}/lib/systemd/system-generators
%global _python_bytecompile_extra 0
Summary:        SELinux policy core utilities
Name:    policycoreutils
Version: 3.11
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-%{version}.tar.gz.asc
Source2:        bachradsusi.gpg
Source3: changelog
URL:     https://github.com/SELinuxProject/selinux
Source13: system-config-selinux.png
Source15: selinux-autorelabel
Source16: selinux-autorelabel.service
Source17: selinux-autorelabel-mark.service
Source18: selinux-autorelabel.target
Source19: selinux-autorelabel-generator.sh
Patch0001: 0001-Don-t-be-verbose-if-you-are-not-on-a-tty.patch
Patch0002: 0002-sepolicy-generate-Handle-more-reserved-port-types.patch
Patch0003: 0003-sandbox-Use-matchbox-window-manager-instead-of-openb.patch
Patch0004: 0004-Use-SHA-2-instead-of-SHA-1.patch
Patch0005: 0005-python-sepolicy-Fix-spec-file-dependencies.patch
Patch0006: 0006-sepolicy-Fix-detection-of-writeable-locations.patch
Obsoletes: policycoreutils < 2.0.61-2
Conflicts: filesystem < 3, selinux-policy-base < 3.13.1-138
Conflicts: initscripts < 9.66
Provides: /sbin/fixfiles
Provides: /sbin/restorecon
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/restorecon
Provides: /usr/sbin/fixfiles
Provides: /usr/sbin/setfiles
Provides: /usr/sbin/setsebool
Provides: /usr/sbin/semodule
%endif
Requires: util-linux grep gawk diffutils sed
Requires: libsepol >= %{libsepolver} coreutils libselinux-utils >=  %{libselinuxver}
Recommends: rpm
# oreon:deps
BuildRequires:  (python3-wheel if python3-setuptools < 71)
BuildRequires:  audit-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  libcap-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libsepol-static
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  systemd
BuildRequires:  systemd-units
# /oreon:deps
%description
Security-enhanced Linux is a feature of the Linux® kernel and a number
of utilities with enhanced security functionality designed to add
mandatory access controls to Linux.  The Security-enhanced Linux
kernel contains new architectural components originally developed to
improve the security of the Flask operating system. These
architectural components provide general support for the enforcement
of many kinds of mandatory access control policies, including those
based on the concepts of Type Enforcement®, Role-based Access
Control, and Multi-level Security.

policycoreutils contains the policy core utilities that are required
for basic operation of a SELinux system.  These utilities include
load_policy to load policies, setfiles to label filesystems, newrole
to switch roles.

%prep -p /usr/bin/bash

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 1 -n selinux-%{version}

cp %{SOURCE13} gui/

%build

%set_build_flags
export PYTHON=%{__python3}
make -C policycoreutils SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" SEMODULE_PATH="/usr/sbin" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C python SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C gui SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C sandbox SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C dbus SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C semodule-utils SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
make -C restorecond SBINDIR="%{_sbindir}" LSPP_PRIV=y LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a" all
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
%{__mkdir} -p %{buildroot}/%{_usr}/share/doc/%{name}/
%make_install -C policycoreutils LSPP_PRIV=y SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" SEMODULE_PATH="/usr/sbin" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C python PYTHON=%{__python3} PIP_NO_BUILD_ISOLATION=0 SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C gui PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C sandbox PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C dbus PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C semodule-utils PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
%make_install -C restorecond PYTHON=%{__python3} SBINDIR="%{_sbindir}" LIBDIR="%{_libdir}" LIBSEPOLA="%{_libdir}/libsepol.a"
chmod 0755 %{buildroot}%{_bindir}/newrole
rm -rf %{buildroot}/%{_sysconfdir}/rc.d/init.d/restorecond
rm -f %{buildroot}/usr/share/man/man8/open_init_pty.8
rm -f %{buildroot}%{_sbindir}/open_init_pty
rm -f %{buildroot}%{_sbindir}/run_init
rm -f %{buildroot}/usr/share/man/man8/run_init.8*
rm -f %{buildroot}/etc/pam.d/run_init*
mkdir   -m 755 -p %{buildroot}/%{generatorsdir}
install -m 644 -p %{SOURCE16} %{buildroot}/%{_unitdir}/
install -m 644 -p %{SOURCE17} %{buildroot}/%{_unitdir}/
install -m 644 -p %{SOURCE18} %{buildroot}/%{_unitdir}/
install -m 755 -p %{SOURCE19} %{buildroot}/%{generatorsdir}/
install -m 755 -p %{SOURCE15} %{buildroot}/%{_libexecdir}/selinux/
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/system-config-selinux
%find_lang policycoreutils
%find_lang selinux-python
%find_lang selinux-gui
%find_lang selinux-sandbox
install -m 644 -p %{SOURCE3} %{buildroot}/%{_docdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package python-utils
Summary:    SELinux policy core python utilities
Requires:   python3-policycoreutils = %{version}-%{release}
Obsoletes:  policycoreutils-python <= 2.4-4
BuildArch:  noarch
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/semanage
%endif
%description python-utils
The policycoreutils-python-utils package contains the management tools use to manage
an SELinux environment.

%package dbus
Summary:    SELinux policy core DBUS api
Requires:   python3-policycoreutils = %{version}-%{release}
Requires:   python3-gobject-base
Requires:   polkit
BuildArch:  noarch
%description dbus
The policycoreutils-dbus package contains the management DBUS API use to manage
an SELinux environment.

%package -n python3-policycoreutils
%{?python_provide:%python_provide python3-policycoreutils}
Provides: %{name}-python3 = %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Summary: SELinux policy core python3 interfaces
Requires:policycoreutils = %{version}-%{release}
Requires:python3-libsemanage >= %{libsemanagever} python3-libselinux
Requires:audit-libs-python3 >=  %{libauditver}
Requires: checkpolicy
Requires: python3-setools >= 4.4.0
Requires: python3-distro
BuildArch: noarch
%description -n python3-policycoreutils
The python3-policycoreutils package contains the interfaces that can be used
by python 3 in an SELinux environment.

%package devel
Summary: SELinux policy core policy devel utilities
Requires: policycoreutils-python-utils = %{version}-%{release}
Requires: /usr/bin/make
Requires: python3-dnf
Requires: (selinux-policy-devel if selinux-policy)
%description devel
The policycoreutils-devel package contains the management tools use to develop policy in an SELinux environment.

%package sandbox
Summary: SELinux sandbox utilities
Requires: python3-policycoreutils = %{version}-%{release}
Requires: rsync
BuildRequires: libcap-ng-devel
%description sandbox
The policycoreutils-sandbox package contains the scripts to create graphical
sandboxes

%package newrole
Summary: The newrole application for RBAC/MLS
Requires: policycoreutils = %{version}-%{release}
%description newrole
RBAC/MLS policy machines require newrole as a way of changing the role
or level of a logged in user.

%package gui
Summary: SELinux configuration GUI
Requires: policycoreutils-devel = %{version}-%{release}, python3-policycoreutils = %{version}-%{release}
Requires: policycoreutils-dbus = %{version}-%{release}
Requires: gtk3, python3-gobject
BuildRequires: desktop-file-utils
BuildArch: noarch
%description gui
system-config-selinux is a utility for managing the SELinux environment

%package restorecond
Summary: SELinux restorecond utilities
BuildRequires: systemd-units
%description restorecond
The policycoreutils-restorecond package contains the restorecond service.

%post

%systemd_post selinux-autorelabel-mark.service
%preun

%systemd_preun selinux-autorelabel-mark.service
%post restorecond

%systemd_post restorecond.service
%preun restorecond

%systemd_preun restorecond.service
%postun restorecond

%systemd_postun_with_restart restorecond.service
%files -f %{oreon_filedir}/main.list
%files -n policycoreutils-python-utils -f %{oreon_filedir}/policycoreutils-python-utils.list
%files -n policycoreutils-dbus -f %{oreon_filedir}/policycoreutils-dbus.list
%files -n python3-policycoreutils -f %{oreon_filedir}/python3-policycoreutils.list
%files -n policycoreutils-devel -f %{oreon_filedir}/policycoreutils-devel.list
%files -n policycoreutils-sandbox -f %{oreon_filedir}/policycoreutils-sandbox.list
%files -n policycoreutils-newrole -f %{oreon_filedir}/policycoreutils-newrole.list
%files -n policycoreutils-gui -f %{oreon_filedir}/policycoreutils-gui.list
%files -n policycoreutils-restorecond -f %{oreon_filedir}/policycoreutils-restorecond.list

%changelog

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-4
- Remove sepolicy-icons and Weblate zip sources (unused in %%prep 3.10 tree already ships icons)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-3
- Drop unused gen_changelog macros load so rpmspec works without SOURCES macros file

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10-2
- Prepare for Oreon 11 (RP1)
