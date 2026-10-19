%global source0_hash e1377439533d55464340e81dbaac274eba32b29ec60ed568c7026294d5b15478
%global __provides_exclude_from ^%{_libdir}/%{name}/plugins/*/.*\\.so$
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnote
Version:        50.2
Release:        1%{?dist}
Summary:        Note-taking application
License:        GPL-3.0-or-later AND GFDL-1.1-only AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Gnote
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(giomm-2.68)
BuildRequires:  pkgconfig(glibmm-2.68)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++ 
and consumes fewer resources.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Gnote.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Gnote.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
