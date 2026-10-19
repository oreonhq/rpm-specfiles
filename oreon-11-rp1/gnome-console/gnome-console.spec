%global source0_hash e4950207f0547e6a6c0f18eebfcf6e1a10461eab0f2fae0aae512b1044c7ac6e
%global gtk4_version 4.19
%global libadwaita_version 1.8
%global vte_version 0.77.0
Name:           gnome-console
Version:        51.0
Release:        1%{?dist}
Summary:        Simple user-friendly terminal emulator for the GNOME desktop
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/console
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       vte291-gtk4%{?_isa} >= %{vte_version}
Obsoletes: gnome-console-nautilus < 43~beta
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}-%{version_no_tilde .}

%build

%meson
%meson_build
%install
%meson_install
%find_lang kgx
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Console.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Console.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
