%global source0_hash e2e46a022c89392d193b81fdded1775b9bdb944b040696690b460f02e30025da

Name:           deja-dup
Version:        50.0
Release:        1%{?dist}
Summary:        Simple backup tool and frontend for duplicity

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/deja-dup
Source0:        https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/deja-dup-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext desktop-file-utils intltool
BuildRequires:  yelp-tools pango-devel cairo-devel
BuildRequires:  libvala-devel vala
BuildRequires:  libtool glib2-devel libnotify-devel
BuildRequires:  libpeas-devel
BuildRequires:  libsecret-devel
BuildRequires:  gtk4-devel > 4.5
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  gnome-online-accounts-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  dbus-daemon
BuildRequires:  json-glib-devel libsoup3-devel
BuildRequires:  libhandy1-devel
BuildRequires:  libadwaita-devel
%if %{undefined flatpak}
BuildRequires:  PackageKit-glib-devel
%endif
BuildRequires:  blueprint-compiler
Requires:       duplicity >= 0.6.23
Requires:       python3-gobject-base
Requires:       rclone
Requires:       fuse
Recommends:     gvfs-fuse
Recommends:     restic

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

%autosetup -p1

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

%files -f %{name}.lang
%license LICENSES/
%doc NEWS.md README.md
%{_bindir}/deja-dup
%{_mandir}/man1/deja-dup.1*
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
%{_libdir}/deja-dup/
%{_libexecdir}/deja-dup/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.DejaDup*
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service
%{_datadir}/metainfo/org.gnome.DejaDup.metainfo.xml
%{_datadir}/help/*

%changelog
%autochangelog
