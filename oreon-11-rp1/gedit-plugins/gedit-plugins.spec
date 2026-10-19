%global source0_hash ef9d0c2a50b6b7f90aa2342d64c9fed5fcea43388ffaf2e514d9ab0e6f88dc1d
%global __provides_exclude_from ^%{_libdir}/gedit/plugins/
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           gedit-plugins
Version:        50.0
Release:        1%{?dist}
Summary:        Plugins for gedit
License:        GPL-2.0-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Requires:       gedit-plugin-bookmarks
Requires:       gedit-plugin-drawspaces
Requires:       gedit-plugin-smartspaces
Requires:       gedit-plugin-wordcompletion
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gedit)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  yelp-tools
# /oreon:deps
%description
A collection of plugins for gedit.

%package data
Summary:        Common data required by plugins
Requires:       gedit
%description data
Common files required by all plugins.

%package -n     gedit-plugin-bookmarks
Summary:        gedit bookmarks plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n     gedit-plugin-drawspaces
Summary:        gedit drawspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%package -n     gedit-plugin-smartspaces
Summary:        gedit smartspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin.

%package -n     gedit-plugin-wordcompletion
Summary:        gedit wordcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang gedit --with-gnome
%oreon_autofiles gedit-plugin-bookmarks usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gedit-plugin-drawspaces usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gedit-plugin-smartspaces usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gedit-plugin-wordcompletion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gedit-plugins-data -f %{oreon_filedir}/gedit-plugins-data.list
%files -n gedit-plugin-bookmarks -f %{oreon_filedir}/gedit-plugin-bookmarks.list
%files -n gedit-plugin-drawspaces -f %{oreon_filedir}/gedit-plugin-drawspaces.list
%files -n gedit-plugin-smartspaces -f %{oreon_filedir}/gedit-plugin-smartspaces.list
%files -n gedit-plugin-wordcompletion -f %{oreon_filedir}/gedit-plugin-wordcompletion.list

%changelog

%autochangelog
