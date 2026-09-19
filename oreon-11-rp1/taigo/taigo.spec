%global source0_hash 59efa2f7eb601af5c2c69d99d118c602c4f3eced759d3da16d9fbb4e04894c11

%global uuid    me.appadeia.Taigo

Name:           taigo
Version:        0.3
Release:        16%{?dist}
Summary:        Virtual pet for your desktop built with GTK+, Vala, and love

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/Appadeia/taigo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: taigo-c99.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  vala
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/*.xml

%changelog
%autochangelog
