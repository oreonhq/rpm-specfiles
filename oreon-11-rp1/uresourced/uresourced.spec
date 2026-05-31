%global source0_hash 4c3b586bcd51f4221c80790c23c6560a3c48ff7b11fe0f2a5c98f33b9da615a3

Name:           uresourced
Version:        0.5.4
Release:        %autorelease
Summary:        Dynamically allocate resources to the active user

License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/benzea/uresourced
Source0:        https://gitlab.freedesktop.org/benzea/uresourced/-/archive/v0.5.4/uresourced-v0.5.4.tar.bz2

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%description
This daemon dynamically assigns a resource allocation to the active
graphical user. If the user has an active graphical session managed
using systemd (e.g. GNOME), then the memory allocation will be used
to protect the sessions core processes (session.slice).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-v%{version} -p1

%build
%meson -Dappmanagement=true
%meson_build

%install
%meson_install

%post
%systemd_post uresourced.service
%systemd_user_post uresourced.service

%preun
%systemd_preun uresourced.service
%systemd_user_preun uresourced.service

%postun
%systemd_postun uresourced.service
%systemd_user_postun uresourced.service

%files
%license COPYING
%doc README
%doc NEWS.md
%config(noreplace) %{_sysconfdir}/uresourced.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UResourced.conf
%{_libexecdir}/uresourced
%{_libexecdir}/cgroupify
%{_unitdir}/*
%{_userunitdir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.4-1
- Prepare for Oreon 11 (RP1)
