%global source0_hash 5265f110f1d94e6719fa5e57f0f63ce490cc7eb66132fe75e30ffb653a597184
%global _hardened_build 1
%global shared_requirements \
Requires:         bash                       \
Requires:         filesystem          >= 3   \
Requires:         coreutils                  \
Requires:         gawk                       \
Name:             initscripts
Summary:        Basic support for legacy System V init scripts
Version:          10.27
Release:        1%{?dist}
License:          GPL-2.0-only
URL:              https://github.com/fedora-sysv/initscripts
Source0:        https://github.com/fedora-sysv/initscripts/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
%{?systemd_requires}
Obsoletes:        %{name}            < 10.16-1
Obsoletes:        network-scripts    < 10.25-1
# oreon:deps
BuildRequires:  filesystem
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  setup
BuildRequires:  systemd
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build PYTHON=%{__python3}
%install
%make_install NO_NETWORK_SCRIPTS=true
%find_lang %{name}
%if "%{_sbindir}" == "%{_bindir}"
mv -v %{buildroot}/usr/sbin/* %{buildroot}%{_bindir}/
%oreon_autofiles initscripts-rename-device usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles initscripts-service usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles netconsole-service usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles readonly-root usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%post

%systemd_post import-state.service loadmodules.service
%preun

%systemd_preun import-state.service loadmodules.service
%postun

%systemd_postun import-state.service loadmodules.service
%post -n netconsole-service

%systemd_post netconsole.service
%preun -n netconsole-service

%systemd_preun netconsole.service
%postun -n netconsole-service

%systemd_postun netconsole.service
%post -n readonly-root

%systemd_post readonly-root.service
%preun -n readonly-root

%systemd_preun readonly-root.service
%postun -n readonly-root

%systemd_postun readonly-root.service
%files -f %{oreon_filedir}/main.list
%files -n initscripts-rename-device -f %{oreon_filedir}/initscripts-rename-device.list
%files -n initscripts-service -f %{oreon_filedir}/initscripts-service.list
%files -n netconsole-service -f %{oreon_filedir}/netconsole-service.list
%files -n readonly-root -f %{oreon_filedir}/readonly-root.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.27-2
- Prepare for Oreon 11 (RP1)
