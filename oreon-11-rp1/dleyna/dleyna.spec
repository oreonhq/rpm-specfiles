%global source0_hash aeda5ed5148eb27a3587b9ee8a552731cfd8e236fe68db587c0dd52ee8e627e1
Name:    dleyna
Version: 0.8.5
Release:        1%{?dist}
Summary:        Services and D-Bus APIs for UPnP access
License: LGPL-2.1-or-later
URL:     https://gitlab.gnome.org/World/dLeyna
Source0:        https://gitlab.gnome.org/World/dLeyna/-/archive/v%{version}/dLeyna-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gssdp-1.6)
BuildRequires:  pkgconfig(gupnp-1.6)
BuildRequires:  pkgconfig(gupnp-av-1.0)
BuildRequires:  pkgconfig(gupnp-dlna-2.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
dLeyna is a set of services and D-Bus APIs that aim to simplify access to UPnP
and DLNA media devices in a network.

%package  connector-dbus
Summary:  D-Bus connector for dLeyna services
Requires: %{name}%{?_isa} = %{version}-%{release}
%description connector-dbus
D-Bus connector for dLeyna services.

%package  renderer
Summary:  Service for interacting with Digital Media Renderers
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-connector-dbus%{?_isa} = %{version}-%{release}
%description renderer
D-Bus service for clients to discover and manipulate DLNA Digital Media
Renderers (DMRs).

%package  server
Summary:  Service for interacting with Digital Media Servers
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-connector-dbus%{?_isa} = %{version}-%{release}
%description server
D-Bus service for clients to discover and manipulate DLNA Digital Media
Servers (DMSes).

%package  devel
Summary:  Development files for the dLeyna components
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
dLeyna is a set of services and D-Bus APIs that aim to simplify access to UPnP
and DLNA media devices in a network. This package contains files used for
development with dleyna.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dLeyna-v%{version}
%oreon_prep
%build

%meson -Ddocs=false
%meson_build
%install
%meson_install
rm -rf %{buildroot}/%{python3_sitelib}
rm -rf %{buildroot}/%{_libdir}/dleyna/libdleyna-renderer-1.0.so \
       %{buildroot}/%{_libdir}/pkgconfig/dleyna-renderer-service-1.0.pc \
       %{buildroot}/%{_libdir}/dleyna-server/libdleyna-server-1.0.so \
       %{buildroot}/%{_libdir}/pkgconfig/dleyna-server-service-1.0.pc \
       %{_includedir}/dleyna-1.0/renderer \
       %{_includedir}/dleyna-1.0/server
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dleyna-connector-dbus -f %{oreon_filedir}/dleyna-connector-dbus.list
%files -n dleyna-renderer -f %{oreon_filedir}/dleyna-renderer.list
%files -n dleyna-server -f %{oreon_filedir}/dleyna-server.list
%files -n dleyna-devel -f %{oreon_filedir}/dleyna-devel.list

%changelog

%autochangelog
