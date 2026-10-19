%global source0_hash 101ca3d018e7fdb8a5ab4482debb7cb0d181743beea2d20f3998b18e107d84e1
%global meson_version 0.49.0
%global glib2_version 2.44.0
%global libvirt_version 3.1.0
%global libvirt_glib_version 0.0.7
%global system_user libvirtdbus
Name: libvirt-dbus
Version: 1.4.1
Release:        1%{?dist}
Summary:        libvirt D-Bus API binding
License: LGPL-2.1-or-later
URL: https://libvirt.org/
Source0:        https://libvirt.org/sources/dbus/%{name}-%{version}.tar.xz
Requires: dbus
Requires: glib2 >= %{glib2_version}
Requires: libvirt-libs >= %{libvirt_version}
Requires: libvirt-glib >= %{libvirt_glib_version}
Requires: polkit
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libvirt-devel
BuildRequires:  libvirt-glib-devel
BuildRequires:  meson
BuildRequires:  python3-docutils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package provides D-Bus API for libvirt

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libvirt-dbus-1.4.1

# Create a sysusers.d config file
cat >libvirt-dbus.sysusers.conf <<EOF
u libvirtdbus - 'Libvirt D-Bus bridge' - -
EOF

%build

%meson \
    -Dinit_script=systemd
%meson_build
%install
%meson_install
install -m0644 -D libvirt-dbus.sysusers.conf %{buildroot}%{_sysusersdir}/libvirt-dbus.conf
%oreon_autofiles main

%post

%systemd_post %{name}.service
%systemd_user_post %{name}.service
%preun

%systemd_preun %{name}.service
%systemd_user_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%systemd_user_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.1-9
- Import
