%global source0_hash 9b18d267c55ec950beeea42d3291d2e77f8f7e351c31c6a48feb90dacb195fc5
%global systemd_unit gnome-ponytail-daemon.service
%global libname ponytail
Name:           gnome-ponytail-daemon
Version:        0.0.11
Release:        9%{?dist}
Summary:        Sort of a bridge for dogtail for GNOME on Wayland
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon
Source0:        https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon/-/archive/0.0.11/gnome-ponytail-daemon-0.0.11.tar.gz
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
GNOME Ponytail Daemon is a sort of bridge for dogtail for GNOME on Wayland.

%package        -n python3-%{name}
Summary:        Python module for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-dbus
Requires:       python3-gobject
BuildArch:      noarch
%description -n python3-%{name}
Python module for D-BUS interactions with gnome-ponytail-daemon interfaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_user_post %{systemd_unit}
%preun

%systemd_user_preun %{systemd_unit}
%postun

%systemd_user_postun_with_restart %{systemd_unit}
%systemd_user_postun_with_reload %{systemd_unit}
%systemd_user_postun %{systemd_unit}
%files -f %{oreon_filedir}/main.list
%files -n python3-gnome-ponytail-daemon -f %{oreon_filedir}/python3-gnome-ponytail-daemon.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.11-9
- Prepare for Oreon 11 (RP1)
