%global source1_hash da3680bd38314546a915df5ea265f8c963a42ff5ddc7d69dc1b339775f05dbd6
%global source0_hash a7ce55ef49653996bd6c29add801f9120ff14534941794f61f89dabe067d06b0
%global gvdb_commit 4758f6fb7f889e074e13df3f914328f3eecb1fd3
Name:     cellbroadcastd
Version:  0.0.3
Release:        1%{?dist}
Summary:        DBus service for cellular broadcast messages
License:  GPL-3.0-or-later AND LGPL-2.1-or-later
URL:      https://gitlab.freedesktop.org/devrtz/%{name}
Source0:        https://gitlab.freedesktop.org/devrtz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:  https://gitlab.gnome.org/GNOME/gvdb/-/archive/%{gvdb_commit}/gvdb-%{gvdb_commit}.tar.gz
ExcludeArch:  %{ix86}
Requires:  hicolor-icon-theme
Requires:  libcellbroadcast%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
cellbroadcastd provides DBus daemon that manages cell broadcast messages via
ModemManager. It provides a storage for them and allows configuring channels
for the modem to watch out for.

%package -n libcellbroadcast
Summary:   Library to ease usage from applications
%description -n libcellbroadcast
Library to ease usage from applications.

%package -n libcellbroadcast-devel
Summary:   Development headers for libcellbroadcastd
Requires:  libcellbroadcast%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libcellbroadcast-devel
Development headers for libcellbroadcast.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}
mkdir subprojects/gvdb
tar -xf %{S:1} -C subprojects/gvdb --strip-components 1

%conf
%meson -Dsystemd_user_unit_dir="%{_userunitdir}"

%build

%meson_build
%install
%meson_install
rm %{buildroot}%{_libdir}/libcellbroadcast-0.0.a
%oreon_autofiles libcellbroadcast usr/*/lib*.so.*
%oreon_autofiles libcellbroadcast-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.freedesktop.cbd.desktop
dbus-run-session sh <<'SH'
%meson_test
SH
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%postun

%systemd_user_postun_with_restart %{name}.service
%systemd_user_postun_with_reload %{name}.service
%systemd_user_postun %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n libcellbroadcast -f %{oreon_filedir}/libcellbroadcast.list
%files -n libcellbroadcast-devel -f %{oreon_filedir}/libcellbroadcast-devel.list

%changelog

%autochangelog
