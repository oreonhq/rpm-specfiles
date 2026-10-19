%global source0_hash 73f827924663c7c6b451a74c8385304d99feaa13c81f4e0a171da597c6843574
Name:           meld
Version:        3.24.0
Release:        1%{?dist}
Summary:        Visual diff and merge tool
License:        GPL-2.0-or-later
URL:            https://meldmerge.org/
Source0:        https://download.gnome.org/sources/meld/3.23/meld-%{version}.tar.xz
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
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  python3-devel
# /oreon:deps
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
appstream-util replace-screenshots %{buildroot}%{_datadir}/metainfo/org.gnome.Meld.metainfo.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/meld/b.png
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Meld.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Meld.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
