%global source0_hash 73f4b76480644b2840415859a51d20cd7487b0619714f8defcd38212c3ddcffe
%global glib2_version 2.80
%global gtk4_version 4.14
%global vte291_version 0.77
%global json_glib_version 1.6
%global libadwaita_version 1.6
%global libportal_gtk4_version 0.7.1
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:		ptyxis
Version:	50.1
Release:        1%{?dist}
Summary:        A container oriented terminal for GNOME
License:	GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.0-or-later AND CC0-1.0
URL:		https://gitlab.gnome.org/chergert/ptyxis
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Source1:	org.gnome.Ptyxis.fedora.gschema.override
Requires:	hicolor-icon-theme
ExcludeArch:	%{ix86}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
# /oreon:deps
%description
Ptyxis is a container oriented terminal that provides transparent support for
container systems like Podman, Distrobox, and Toolbx. It also has robust
support for user profiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dgeneric=terminal
%meson_build
%install
%meson_install
install -p %{SOURCE1} %{buildroot}%{_datadir}/glib-2.0/schemas
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Ptyxis.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Ptyxis.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.1-1
- Prepare for Oreon 11 (RP1)
