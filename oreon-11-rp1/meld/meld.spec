%global source0_hash 73f827924663c7c6b451a74c8385304d99feaa13c81f4e0a171da597c6843574

Name:           meld
Version:        3.23.1
Release:        2%{?dist}
Summary:        Visual diff and merge tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://meldmerge.org/
Source0:        https://download.gnome.org/sources/meld/3.23/meld-%{version}.tar.xz

BuildRequires:  meson >= 1.2.0
BuildRequires:  python3-devel
# glib-complie-schemas
BuildRequires:  glib2-devel
BuildRequires:  gettext
BuildRequires:  gtk-update-icon-cache
BuildRequires:  itstool

BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstream-util

Requires:       gtk3 >= 3.22
Requires:       glib2 >= 2.48
Requires:       gtksourceview4 >= 4.0
Requires:       python3-gobject >= 3.30
Requires:       python3-gobject-base >= 3.30
Requires:       python3-cairo >= 1.15
Recommends:     patch

BuildArch:      noarch

Provides:       mergetool
Provides:       difftool

%description
Meld is a visual diff and merge tool targeted at developers. It helps you
compare files, directories, and version controlled projects. It provides two-
and three-way comparison of both files and directories, and the tabbed interface
allows you to open many diffs at once.
Meld has has support for many popular version control systems including Git,
Mercurial, Bazaar, SVN and CVS. The diff viewer lets you edit files in place
(diffs update dynamically), and a middle column shows detailed changes and
allows merges. The margins show location of changes for easy navigation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# There is no reason to check bunch of runtime dependencies in buildtime
sed -i -e "/^dependency(/d" meson.build

%build
%meson
%meson_build

%install
%meson_install
# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/org.gnome.Meld.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/b.png
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Meld.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Meld.metainfo.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/meld
%{_mandir}/man1/meld.1*
%{_datadir}/meld/
%{_datadir}/glib-2.0/schemas/org.gnome.Meld.gschema.xml
%{_datadir}/applications/org.gnome.Meld.desktop
%{_datadir}/mime/packages/org.gnome.Meld.xml
%{_datadir}/metainfo/org.gnome.Meld.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Meld*
%{python3_sitelib}/meld/

%changelog
%autochangelog
