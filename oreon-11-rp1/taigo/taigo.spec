%global source0_hash 59efa2f7eb601af5c2c69d99d118c602c4f3eced759d3da16d9fbb4e04894c11
%global uuid    me.appadeia.Taigo
Name:           taigo
Version:        0.3
Release:        1%{?dist}
Summary:        Virtual pet for your desktop built with GTK+, Vala, and love
License:        GPL-3.0-or-later
URL:            https://github.com/Appadeia/taigo
Source0:        https://github.com/Appadeia/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: taigo-c99.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
