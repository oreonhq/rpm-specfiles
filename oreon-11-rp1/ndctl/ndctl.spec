%global source0_hash 69039ee12c75c44f67b5fa3f1abb61d1c38ff9303021e50cec0b45801cc93b2e
Name:		ndctl
Version:	85
Release:        1%{?dist}
Summary:        Manage "libnvdimm" subsystem devices (Non-volatile Memory)
License:	GPL-2.0-only AND LGPL-2.1-only AND CC0-1.0 AND MIT
Url:		https://github.com/pmem/ndctl
Source0:        https://github.com/pmem/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	ndctl-libs%{?_isa} = %{version}-%{release}
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}
Requires:	cxl-libs%{?_isa} = %{version}-%{release}
%define asciidoctor -Dasciidoctor=enabled
%define libtracefs -Dlibtracefs=enabled
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  iniparser-devel
BuildRequires:  keyutils-libs-devel
BuildRequires:  libtool
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  rubygem-asciidoctor
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
# /oreon:deps
%description
Utility library for managing the "libnvdimm" subsystem.  The "libnvdimm"
subsystem defines a kernel device model and control message interface for
platform NVDIMM resources like those defined by the ACPI 6+ NFIT (NVDIMM
Firmware Interface Table).

%if 0%{?flatpak}
%global _udevrulesdir %{_prefix}/lib/udev/rules.d
%endif

%package -n ndctl-devel
Summary:	Development files for libndctl
License:	LGPL-2.1-only
Requires:	ndctl-libs%{?_isa} = %{version}-%{release}
%description -n ndctl-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n daxctl
Summary:	Manage Device-DAX instances
License:	GPL-2.0-only
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}
%description -n daxctl
The daxctl utility provides enumeration and provisioning commands for
the Linux kernel Device-DAX facility. This facility enables DAX mappings
of performance / feature differentiated memory without need of a
filesystem.

%package -n cxl-cli
Summary:	Manage CXL devices
License:	GPL-2.0-only
Requires:	cxl-libs%{?_isa} = %{version}-%{release}
%description -n cxl-cli
The cxl utility provides enumeration and provisioning commands for
the Linux kernel CXL devices.

%package -n cxl-devel
Summary:	Development files for libcxl
License:	LGPL-2.1-only
Requires:	cxl-libs%{?_isa} = %{version}-%{release}
%description -n cxl-devel
This package contains libraries and header files for developing applications
that use libcxl, a library for enumerating and communicating with CXL devices.

%package -n daxctl-devel
Summary:	Development files for libdaxctl
License:	LGPL-2.1-only
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}
%description -n daxctl-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}, a library for enumerating
"Device DAX" devices.  Device DAX is a facility for establishing DAX
mappings of performance / feature-differentiated memory.

%package -n ndctl-libs
Summary:	Management library for "libnvdimm" subsystem devices (Non-volatile Memory)
License:	LGPL-2.1-only AND CC0-1.0 AND MIT
Requires:	daxctl-libs%{?_isa} = %{version}-%{release}
%description -n ndctl-libs
Libraries for %{name}.

%package -n daxctl-libs
Summary:	Management library for "Device DAX" devices
License:	LGPL-2.1-only AND CC0-1.0 AND MIT
%description -n daxctl-libs
Device DAX is a facility for establishing DAX mappings of performance /
feature-differentiated memory. daxctl-libs provides an enumeration /
control API for these devices.

%package -n cxl-libs
Summary:	Management library for CXL devices
License:	LGPL-2.1-only AND CC0-1.0 AND MIT
%description -n cxl-libs
libcxl is a library for enumerating and communicating with CXL devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q ndctl-%{version}

%build

%meson %{?asciidoctor} %{?libtracefs} -Dversion-tag=%{version}
%meson_build
%install
%meson_install
%oreon_autofiles ndctl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles daxctl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cxl-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cxl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles daxctl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ndctl-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles daxctl-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cxl-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%ldconfig_scriptlets -n ndctl-libs
%ldconfig_scriptlets -n daxctl-libs
%ldconfig_scriptlets -n cxl-libs
%define bashcompdir %(pkg-config --variable=completionsdir bash-completion)
%pre

if [ -f %{_sysconfdir}/ndctl/monitor.conf ] ; then
  if ! [ -f %{_sysconfdir}/ndctl.conf.d/monitor.conf ] ; then
    cp -a %{_sysconfdir}/ndctl/monitor.conf /var/run/ndctl-monitor.conf-migration
  fi
fi
%post

if [ -f /var/run/ndctl-monitor.conf-migration ] ; then
  config_found=false
  while read line ; do
    [ -n "$line" ] || continue
    case "$line" in
      \#*) continue ;;
    esac
    config_found=true
    break
  done < /var/run/ndctl-monitor.conf-migration
  if $config_found ; then
    echo "[monitor]" > %{_sysconfdir}/ndctl.conf.d/monitor.conf
    cat /var/run/ndctl-monitor.conf-migration >> %{_sysconfdir}/ndctl.conf.d/monitor.conf
  fi
  rm /var/run/ndctl-monitor.conf-migration
fi
%files -f %{oreon_filedir}/main.list
%files -n ndctl-devel -f %{oreon_filedir}/ndctl-devel.list
%files -n daxctl -f %{oreon_filedir}/daxctl.list
%files -n cxl-cli -f %{oreon_filedir}/cxl-cli.list
%files -n cxl-devel -f %{oreon_filedir}/cxl-devel.list
%files -n daxctl-devel -f %{oreon_filedir}/daxctl-devel.list
%files -n ndctl-libs -f %{oreon_filedir}/ndctl-libs.list
%files -n daxctl-libs -f %{oreon_filedir}/daxctl-libs.list
%files -n cxl-libs -f %{oreon_filedir}/cxl-libs.list

%changelog

%autochangelog
