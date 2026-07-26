%global source0_hash b0ba4537258d2b848fd07dedb1044dab132de3fb3f1976d240da40a7dee1b8cf

%if 0%{?fedora}
%global with_seccomp 1
%global with_static_init 1
%endif

%if 0%{?rhel} >= 7
%ifarch %{ix86} x86_64 %{arm} aarch64
%global with_seccomp 1
%endif
%endif

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           lxc
Version:        6.0.6
Release:        1%{?dist}
Summary:        Linux Resource Containers
# Automatically converted from old format: LGPLv2+ and GPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-only
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        lxc-net
Patch0:         lxc-2.0.7-fix-init.patch
Patch1:         lxc-4.0.1-fix-lxc-net.patch

BuildRequires:  cmake
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibc-headers
BuildRequires:  kernel-headers
BuildRequires:  libcap
BuildRequires:  libcap-devel
%if 0%{?with_seccomp}
BuildRequires:  pkgconfig(libseccomp)
%endif
BuildRequires:  libselinux-devel
BuildRequires:  meson >= 0.61
BuildRequires:  openssl-devel
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(dbus-1)
%if 0%{?with_static_init}
BuildRequires:  libcap-static
BuildRequires:  glibc-static
%endif
# lxc-extra subpackage not needed anymore, lxc-ls has been rewriten in
# C and does not depend on the Python3 binding anymore
Provides:       lxc-extra = %{version}-%{release}
Obsoletes:      lxc-extra < 1.1.5-3

# https://bugzilla.redhat.com/show_bug.cgi?id=2274215
Requires: lxc-libs%{?_isa} = %{version}-%{release}
Requires: lxcfs
Requires: openssl
Requires: rsync
# Requires: dnsmasq
# Requires: bridge-utils
# Needed to create openSUSE containers using template.
# Recommends: build
# Recommends: criu >= 2.0

%description
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

%package           libs
Summary:           Runtime library files for %{name}
# rsync is called in bdev.c, e.g. by lxc-clone
Requires:          rsync
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Requires(post):    /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description    libs
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-libs package contains libraries for running %{name} applications.

%package        templates
Summary:        Templates for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# Note: Not all requirements for the template scripts (busybox, dpkg,
# debootstrap, rsync, openssh-server, dhclient, apt, pacman, zypper,
# ubuntu-cloudimg-query etc...) are explicitly mentioned here: their
# presence varies wildly on supported Fedora/EPEL releases and archs,
# and they are in most cases needed for a single template only. Also,
# the templates normally fail graciously when such a tool is
# missing. Moving each template to its own subpackage on the other
# hand would be overkill.
#
# Add wget, used by the 'download' template (see also #1828032)
Requires:       wget

%description    templates
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-templates package contains templates for creating containers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
        -D examples=true \
        -D man=true \
        -D tools=true \
        -D commands=true \
        -D capabilities=true \
        -D openssl=true \
        -D selinux=true \
%if 0%{?with_seccomp}
        -D seccomp=true \
%endif
        -D memfd-rexec=true \
        -D thread-safety=true \
        -D dbus=true \
        -D tests=false \
        -D init-script=systemd \
        -D systemd-unitdir=%{_unitdir} \
        -D distrosysconfdir=sysconfig \
        -D pam-cgroup=true \
        -D runtime-path=%{_rundir} \
        %{nil}
%meson_build

cd doc/api/ && doxygen

%install
%meson_install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

# docs
mkdir -p %{buildroot}%{_pkgdocdir}/api
cp -a AUTHORS README.md %{buildroot}%{_pkgdocdir}
cp -a doc/api/html/* %{buildroot}%{_pkgdocdir}/api/

# cache dir
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}

# remove libtool .a file
rm -r %{buildroot}%{_libdir}/liblxc.a

# lxc-net config file
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}-net

%post libs
%systemd_post %{name}-net.service
%systemd_post %{name}.service
%systemd_post lxc-monitord.service

%preun libs
%systemd_preun %{name}-net.service
%systemd_preun %{name}.service
%systemd_preun lxc-monitord.service

%postun libs
%systemd_postun %{name}-net.service
%systemd_postun %{name}.service
%systemd_postun lxc-monitord.service

%files
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
# in lxc-libs:
%exclude %{_bindir}/%{name}-autostart
%exclude %{_mandir}/man1/%{name}-autostart*
%exclude %{_mandir}/*/man1/%{name}-autostart*
%exclude %{_mandir}/man1/%{name}-user-nic*
%exclude %{_mandir}/*/man1/%{name}-user-nic*
%{_datadir}/%{name}/%{name}.functions
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/_%{name}
%{_datadir}/bash-completion/completions/%{name}-*

%files libs
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/templates
%dir %{_datadir}/%{name}/config
%{_datadir}/%{name}/hooks
%{_datadir}/%{name}/%{name}-patch.py*
%{_datadir}/%{name}/selinux
%{_libdir}/liblxc.so.*
%{_libdir}/%{name}
%{_libexecdir}/%{name}
# fixme: should be in libexecdir?
%{_sbindir}/init.%{name}
%if 0%{?with_static_init}
%{_sbindir}/init.%{name}.static
%endif
%{_bindir}/%{name}-autostart
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}-net
%{_mandir}/man1/%{name}-autostart*
%{_mandir}/*/man1/%{name}-autostart*
%{_mandir}/man1/%{name}-user-nic*
%{_mandir}/*/man1/%{name}-user-nic*
%{_mandir}/man5/%{name}*
%{_mandir}/man7/%{name}*
%{_mandir}/*/man5/%{name}*
%{_mandir}/*/man7/%{name}*
%{_mandir}/man8/pam_cgfs*
%{_mandir}/*/man8/pam_cgfs*
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README.md
%{_pkgdocdir}/examples
%license COPYING
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-net.service
%{_unitdir}/%{name}-monitord.service
%dir %{_localstatedir}/cache/%{name}
%{_libdir}/security/pam_cgfs.so

%files templates
%{_datadir}/%{name}/templates/lxc-*
%{_datadir}/%{name}/config/*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lxc
%{_libdir}/liblxc.so

%files doc
%dir %{_pkgdocdir}
# README, AUTHORS and COPYING intentionally duplicated because -doc
# can be installed on its own.
%{_pkgdocdir}/*
%license COPYING

%changelog
%autochangelog
