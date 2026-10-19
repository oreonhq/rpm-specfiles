%global source0_hash e65c1b7867f836faad9f9ee04acf5c5a6cae2bbc784833fe093207e0cb590248
%define glib2_version 2.44.0
Name:           dconf
Version:        51.0
Release:        1%{?dist}
Summary:        A configuration system
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://wiki.gnome.org/Projects/dconf
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch1:         dconf-override.patch
Requires:       dbus
Requires:       glib2%{?_isa} >= %{glib2_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
dconf is a low-level configuration system. Its main purpose is to provide a
backend to the GSettings API in GLib.

%package devel
Summary: Header files and libraries for dconf development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
dconf development package. Contains files needed for doing software
development using dconf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true -Dsystemduserunitdir=%{_userunitdir}
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/profile
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/dconf/profile/user
user-db:user
system-db:local
system-db:site
system-db:distro
EOF
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/local.d/locks
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/site.d/locks
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dconf/db/distro.d/locks
%oreon_autofiles dconf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%posttrans

%{_bindir}/dconf update
%post

%systemd_user_post dconf.service
%preun

%systemd_user_preun dconf.service
%postun

%systemd_user_postun_with_restart dconf.service
%files -f %{oreon_filedir}/main.list
%files -n dconf-devel -f %{oreon_filedir}/dconf-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.49.0-1
- Import
