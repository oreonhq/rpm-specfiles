%global source0_hash 96cadbda7367304233e90084da544f546ade397a8b4464fe99882e7ad00a06b1
Name:     phosh-tour
Version:  0.57.0
Release:        1%{?dist}
Summary:        Simple introduction to Phosh
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/phosh-tour
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch:    Require-appstreamcli-to-validate-appstream-file.patch
ExcludeArch:  %{ix86}
Requires:  hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Simple introduction to Phosh shell.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version_no_tilde _}

%build

%meson -Dvendor="Fedora Remix Mobility"
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/mobi.phosh.PhoshTour.desktop
%meson_test
%post

%systemd_user_post mobi.phosh.PhoshTour-first-login.service
%preun

%systemd_user_preun mobi.phosh.PhoshTour-first-login.service
%postun

%systemd_user_postun_with_restart mobi.phosh.PhoshTour-first-login.service
%systemd_user_postun_with_reload mobi.phosh.PhoshTour-first-login.service
%systemd_user_postun mobi.phosh.PhoshTour-first-login.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
