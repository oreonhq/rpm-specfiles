%global source0_hash 5265f110f1d94e6719fa5e57f0f63ce490cc7eb66132fe75e30ffb653a597184

# === GLOBAL MACROS ===========================================================

# According to Fedora Package Guidelines, it is advised that packages that can
# process untrusted input are build with position-idenpendent code (PIC).
#
# Koji should override the compilation flags and add the -fPIC or -fPIE flags by
# default. This is here just in case this wouldn't happen for some reason.
# For more info: https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%global _hardened_build 1

%global shared_requirements \
Requires:         bash                       \
Requires:         filesystem          >= 3   \
Requires:         coreutils                  \
Requires:         gawk                       \

# =============================================================================

Name:             initscripts
Summary:          Basic support for legacy System V init scripts
Version:          10.27
Release:          2%{?dist}

License:          GPL-2.0-only

URL:              https://github.com/fedora-sysv/initscripts
Source:        https://github.com/fedora-sysv/initscripts/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%shared_requirements

Requires:         findutils
Requires:         grep
Requires:         procps-ng
Requires:         setup
Requires:         systemd
Requires:         util-linux
Requires:         chkconfig
Requires:         initscripts-service
Requires:         initscripts-rename-device

Requires(pre):    shadow-utils
Requires(post):   coreutils

BuildRequires:    filesystem          >= 3
BuildRequires:    gcc
BuildRequires:    git
BuildRequires:    gettext
BuildRequires:    glib2-devel
BuildRequires:    pkgconfig
BuildRequires:    popt-devel
BuildRequires:    setup
BuildRequires:    make

%{?systemd_requires}
BuildRequires:    systemd

Obsoletes:        %{name}            < 10.16-1
Obsoletes:        network-scripts    < 10.25-1

# === PATCHES =================================================================

# NOTE: 'autosetup' macro (below) uses 'git' for applying the patches:
#       ->> All the patches should be provided in 'git format-patch' format.
#       ->> Auxiliary repository will be created during 'fedpkg prep', you
#           can see all the applied patches there via 'git log'.

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last rebase that are necessary for any reason:
#Patch000: example000.patch


# Downstream patches -- these should be always included when doing rebase:
# ------------------
#Patch100: example100.patch


# Downstream patches for RHEL -- patches that we keep only in RHEL for various
# ---------------------------    reasons, but are not enabled in Fedora:
%if %{defined rhel} || %{defined centos}
#Patch200: example200.patch
%endif


# Patches to be removed -- deprecated functionality which shall be removed at
# ---------------------    some point in the future:


%description
This package provides basic support for legacy System V init scripts, and some
other legacy tools & utilities.

# === SUBPACKAGES =============================================================

%package -n initscripts-rename-device
Summary:          Udev helper utility that provides network interface naming

%shared_requirements

%description -n initscripts-rename-device
Udev helper utility that provides network interface naming

# ---------------

%package -n initscripts-service
Summary:          Support for service command
BuildArch:        noarch

%shared_requirements

Requires:         systemd

Provides:         /sbin/service

%description -n initscripts-service
This package provides service command.

# ---------------

%package -n netconsole-service
Summary:          Service for initializing of network console logging
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%shared_requirements

Requires:         glibc-common
Requires:         iproute
Requires:         iputils
Requires:         kmod
Requires:         sed
Requires:         util-linux

Obsoletes:        %{name}            < 9.82-2

%description -n netconsole-service
This packages provides a 'netconsole' service for loading of netconsole kernel
module with the configured parameters. The netconsole kernel module itself then
allows logging of kernel messages over the network.

# ---------------

%package -n readonly-root
Summary:          Service for configuring read-only root support
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%shared_requirements

Requires:         cpio
Requires:         findutils
Requires:         hostname
Requires:         iproute
Requires:         ipcalc
Requires:         util-linux

Obsoletes:        %{name}            < 9.82-2

%description -n readonly-root
This package provides script & configuration file for setting up read-only root
support. Additional configuration is required after installation.

Please note that readonly-root package is considered deprecated with limited support.
Please use systemd-volatile-root functionality instead, if possible.

# === BUILD INSTRUCTIONS ======================================================

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

# ---------------

%build
%make_build PYTHON=%{__python3}

# ---------------

%install
%make_install NO_NETWORK_SCRIPTS=true

# This installs the NLS language files:
%find_lang %{name}

%if "%{_sbindir}" == "%{_bindir}"
# Some files get installed wrong, but if $(sbindir) is overriden, the build fails :(
mv -v %{buildroot}/usr/sbin/* %{buildroot}%{_bindir}/
%endif

# =============================================================================

%post
%systemd_post import-state.service loadmodules.service

%preun
%systemd_preun import-state.service loadmodules.service

%postun
%systemd_postun import-state.service loadmodules.service

# ---------------

%post -n netconsole-service
%systemd_post netconsole.service

%preun -n netconsole-service
%systemd_preun netconsole.service

%postun -n netconsole-service
%systemd_postun netconsole.service

# ---------------

%post -n readonly-root
%systemd_post readonly-root.service

%preun -n readonly-root
%systemd_preun readonly-root.service

%postun -n readonly-root
%systemd_postun readonly-root.service

# === PACKAGING INSTRUCTIONS ==================================================

%files -f %{name}.lang
%license COPYING
%doc doc/sysconfig.txt

# NOTE: /etc/profile.d/ is owned by setup package.
#       /etc/sysconfig/ is owned by filesystem package.
%dir %{_sysconfdir}/rc.d
%dir %{_sysconfdir}/rc.d/init.d
%dir %{_sysconfdir}/rc.d/rc[0-6].d
%dir %{_sysconfdir}/sysconfig/console
%dir %{_sysconfdir}/sysconfig/modules
%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/legacy-actions

# ---------------

%{_sysconfdir}/rc.d/init.d/functions

# RC symlinks:
%{_sysconfdir}/rc[0-6].d

%{_sysconfdir}/init.d

# ---------------

%{_bindir}/usleep
%{_sbindir}/consoletype
%{_sbindir}/genhostid

%{_libexecdir}/import-state
%{_libexecdir}/loadmodules

%{_prefix}/lib/systemd/system/import-state.service
%{_prefix}/lib/systemd/system/loadmodules.service

%{_mandir}/man1/*

# =============================================================================

%files -n initscripts-rename-device
%license COPYING

%{_prefix}/lib/udev/rename_device

%{_udevrulesdir}/*

# ---------------

%files -n initscripts-service
%license COPYING

%dir %{_libexecdir}/%{name}
%dir %{_libexecdir}/%{name}/legacy-actions

%{_sbindir}/service

%{_mandir}/man8/service.*

# ---------------

%files -n netconsole-service
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/netconsole

%{_libexecdir}/netconsole
%{_prefix}/lib/systemd/system/netconsole.service

# ---------------

%files -n readonly-root
%license COPYING

%dir %{_sharedstatedir}/stateless
%dir %{_sharedstatedir}/stateless/state
%dir %{_sharedstatedir}/stateless/writable

%config(noreplace) %{_sysconfdir}/rwtab
%config(noreplace) %{_sysconfdir}/statetab
%config(noreplace) %{_sysconfdir}/sysconfig/readonly-root

%{_libexecdir}/readonly-root
%{_prefix}/lib/systemd/system/readonly-root.service

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.27-2
- Prepare for Oreon 11 (RP1)
