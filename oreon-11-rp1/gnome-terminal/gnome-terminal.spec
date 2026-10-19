%global source0_hash b8daf3f08545172c4d2885733f720361ab0349ea669b99245eed4ad16ed3de28
%define gettext_package gnome-terminal
%global gettext_version 0.19.8
%define glib2_version 2.52.0
%define gtk3_version 3.24.0
%define libhandy_version 1.6.0
%define vte_version 0.79.90
%define desktop_file_utils_version 0.2.90
Name:    gnome-terminal
Version: 3.60.0
Release:        1%{?dist}
Summary:        Terminal emulator for GNOME
License: GPL-3.0-or-later AND GFDL-1.3-only
URL:     https://wiki.gnome.org/Apps/Terminal
Source0:        https://download.gnome.org/sources/%{name}/3.60/%{name}-%{version}.tar.xz
Source1:        org.gnome.Terminal.gschema.override
Requires: dbus
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libhandy%{?_isa} >= %{libhandy_version}
Requires: vte291%{?_isa} >= %{vte_version}
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-shell
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  systemd-rpm-macros
BuildRequires:  yelp-tools
# /oreon:deps
%description
gnome-terminal is a terminal emulator for GNOME. It features the ability to use
multiple terminals in a single window (tabs) and profiles support.

%package nautilus
Summary: GNOME Terminal extension for Nautilus
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: nautilus-open-terminal = %{version}-%{release}
Obsoletes: nautilus-open-terminal < 0.20-8
%description nautilus
This package provides a Nautilus extension that adds the 'Open in Terminal'
option to the right-click context menu in Nautilus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Ddebug=true \
    -Ddocs=true \
    -Dnautilus_extension=true \
    -Dsearch_provider=true
%meson_build
%install
%meson_install
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas
%find_lang %{gettext_package} --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Terminal*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Terminal.desktop
%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gnome-terminal-nautilus -f %{oreon_filedir}/gnome-terminal-nautilus.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.60.0-1
- Import
