%global source0_hash 956664cff547757a64127395a47f7e30b0c764b8265eeef253ede4ca47a7be88
Name:           deja-dup
Version:        50.2
Release:        1%{?dist}
Summary:        Simple backup tool and frontend for duplicity
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/deja-dup
Source0:        https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/deja-dup-%{version}.tar.bz2
%if %{undefined flatpak}
%endif
Requires:       duplicity >= 0.6.23
Requires:       python3-gobject-base
Requires:       rclone
Requires:       fuse
Recommends:     gvfs-fuse
Recommends:     restic
# oreon:deps
BuildRequires:  PackageKit-glib-devel
BuildRequires:  blueprint-compiler
BuildRequires:  cairo-devel
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  gtk4-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  json-glib-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  libgpg-error-devel
BuildRequires:  libhandy1-devel
BuildRequires:  libnotify-devel
BuildRequires:  libpeas-devel
BuildRequires:  libsecret-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libtool
BuildRequires:  libvala-devel
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
%description
Déjà Dup is a simple backup tool. It hides the complexity of doing backups the
'right way' (encrypted, off-site, and regular) and uses duplicity as the
backend.

Features: 
 • Support for local, remote, or consumer cloud backup locations (Google Drive, etc)
 • Securely encrypts and compresses your data
 • Incrementally backs up, letting you restore from any particular backup
 • Schedules regular backups
 • Integrates well into your GNOME desktop

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Denable_restic=true %{?flatpak:-Dpackagekit=disabled}
%meson_build
%install
%meson_install
rm -f %{buildroot}/%{_libdir}/deja-dup/*.la
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.DejaDup.desktop
desktop-file-validate %{buildroot}/%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
%find_lang %{name} --with-gnome
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
