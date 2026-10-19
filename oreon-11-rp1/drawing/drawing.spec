%global source0_hash 539e7e28fe4db96cfedd4477e217d5d48b9422ad8c98f33d8ae46120b2d5738b
%global uuid com.github.maoschanz.%{name}
Name: drawing
Version: 1.0.2
Release:        1%{?dist}
Summary:        Simple image editor for Linux
BuildArch: noarch
License: GPL-3.0-or-later
URL: https://github.com/maoschanz/drawing
Source0:        https://github.com/maoschanz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires: gtk3
Requires: hicolor-icon-theme
Requires: python3-cairo
Requires: python3-gobject
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  python3-cairo
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
# /oreon:deps
%description
This simple image editor, similar to Microsoft Paint, is aiming at the GNOME
desktop.

PNG, JPEG and BMP files are supported.

Besides GNOME, the app is well integrated in traditional-looking desktops, as
well as elementaryOS.

It should also be compatible with the Pinephone and Librem 5 smartphones.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
