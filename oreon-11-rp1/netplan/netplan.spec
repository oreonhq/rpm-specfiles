%global source0_hash 9fc5fba9e8247b9d4ec8fc132d37a60ebe49dc5bdd653645c6719886890a746c
%global ubuntu_name netplan.io
%{?!_systemdgeneratordir:%global _systemdgeneratordir /usr/lib/systemd/system-generators}
%global libsomajor 1
%bcond_without networkd_support
%bcond_with tests
Name:           netplan
Version:        1.2.2
Release:        1%{?dist}
Summary:        Network configuration tool using YAML
License:        GPL-3.0-only
URL:            http://netplan.io/
Source0:        https://github.com/canonical/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1001:      netplan-fallback-renderer.patch
Patch1002:      status_fail_cleanly.patch
%if %{with tests}
%endif
Requires:       python3dist(netifaces)
Requires:       python3dist(pyyaml)
Requires:       %{_sbindir}/ip
Requires:       dbus-common
Requires:       %{name}-default-backend
Suggests:       %{name}-default-backend-NetworkManager
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Provides:       %{ubuntu_name} = %{version}-%{release}
Provides:       %{ubuntu_name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  //bin/ip
BuildRequires:  //bin/pandoc
BuildRequires:  gcc
BuildRequires:  libcmocka-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(pyflakes)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

Currently supported backends are NetworkManager and systemd-networkd.

%package libs
Summary:        Network configuration tool using YAML (core library)
%description libs
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package provides Netplan's core libraries.

%package devel
Summary:        Network configuration tool using YAML (development files)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package provides development headers and libraries for building applications using Netplan.

%package default-backend-NetworkManager
Summary:        Network configuration tool using YAML (NetworkManager backend)
Requires:       %{name} = %{version}-%{release}
Requires:       NetworkManager
Requires:       NetworkManager-config-server
Recommends:     (NetworkManager-wifi if linux-firmware-whence)
Suggests:       NetworkManager-wifi
Conflicts:      %{name}-default-backend
Provides:       %{name}-default-backend
BuildArch:      noarch
%description default-backend-NetworkManager
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package configures Netplan to use NetworkManager as its backend.

%package -n python3-%{name}
Summary:        Python bindings for lib%{name}
Requires:       python3-cffi
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
Declarative network configuration Python bindings
Netplan reads YAML network configuration files which are written
by administrators, installers, cloud image instantiations, or other OS
deployments. During early boot it then generates backend specific
configuration files in /run to hand off control of devices to a particular
networking daemon.

Currently supported backends are networkd and NetworkManager.

This package provides a CFFI based Python bindings to libnetplan.

%package default-backend-networkd
Summary:        Network configuration tool using YAML (systemd-networkd backend)
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-networkd
Recommends:     (wpa_supplicant if linux-firmware-whence)
Suggests:       wpa_supplicant
Conflicts:      %{name}-default-backend
Provides:       %{name}-default-backend
BuildArch:      noarch
%description default-backend-networkd
netplan reads network configuration from /etc/netplan/*.yaml which are written by administrators,
installers, cloud image instantiations, or other OS deployments. During early boot, it generates
backend specific configuration files in /run to hand off control of devices to a particular
networking daemon.

This package configures Netplan to use systemd-networkd as its backend.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# these tests all fail in containers, or are linting/codestyle which we don't care about
sed -i -e "/    test('legacy-tests',/,+3d" \
	-e "/    test('codestyle',/,+3d" \
	-e "/    test('linting',/,+3d" \
	-e "/    test('unit-tests',/,+4d" \
	meson.build

%build

%if %{with tests}
%meson
%else
%meson -Dtesting=false
%endif
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
mv -n %{buildroot}/%{python3_sitelib}/%{name}/* %{buildroot}/%{python3_sitearch}/%{name}/
rm -f %{python3_sitelib}/%{name}/
cat > %{buildroot}%{_prefix}/lib/%{name}/00-network-manager-all.yaml <<EOF
network:
  version: 2
  renderer: NetworkManager
EOF
%if %{with networkd_support}
cat > %{buildroot}%{_prefix}/lib/%{name}/00-netplan-default-renderer-networkd.yaml <<EOF
network:
  version: 2
  renderer: networkd
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with tests}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n netplan-libs -f %{oreon_filedir}/netplan-libs.list
%files -n netplan-devel -f %{oreon_filedir}/netplan-devel.list
%files -n netplan-default-backend-NetworkManager -f %{oreon_filedir}/netplan-default-backend-NetworkManager.list
%files -n python3-netplan -f %{oreon_filedir}/python3-netplan.list
%files -n netplan-default-backend-networkd -f %{oreon_filedir}/netplan-default-backend-networkd.list

%changelog

%autochangelog
