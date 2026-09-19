%global source0_hash 3ce1eed6efda27d650ff3f830af1512cef43b1827100be98e389a59118ddef41

%global newname gfeeds
%global uuid org.gabmus.%{newname}

Name: gnome-feeds
Version: 2.2.0
Release: %autorelease
Summary: RSS/Atom feed reader for GNOME

BuildArch: noarch

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://gabmus.gitlab.io/gnome-feeds
Source0: https://gitlab.com/gabmus/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: blueprint-compiler08.patch

BuildRequires: blueprint-compiler >= 0.8
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: meson >= 0.58.0
BuildRequires: python3-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(webkitgtk-6.0)

Requires: dbus-common
Requires: glib2
Requires: gtk4
Requires: hicolor-icon-theme
Requires: libadwaita
Requires: python3-beautifulsoup4
Requires: python3-dateutil
Requires: python3-humanize
Requires: python3-lxml
# not compatible with python3-file-magic from file
Requires: python3dist(python-magic)
Requires: python3-pillow
Requires: python3-pygments
Requires: python3-pytz
Requires: python3-readability-lxml
Requires: python3-requests
Requires: python3-syndom
Requires: webkitgtk6.0

%description
GNOME Feeds is a minimal RSS/Atom feed reader built with speed and simplicity
in mind.

It offers a simple user interface that only shows the latest news from your
subscriptions.

Articles are shown in a web view by default, with javascript disabled for a
faster and less intrusive user experience. There's also a reader mode
included, built from the one GNOME Web/Epiphany uses.

Feeds can be imported and exported via OPML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{newname} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{newname}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{newname}
%{_datadir}/%{newname}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{newname}/

%changelog
%autochangelog
