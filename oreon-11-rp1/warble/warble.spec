%global source0_hash a68fb46315114f6ed613560d6d43b4a8f7cc31a298a32e43084bc9277e10afe7

%global appname com.github.avojak.warble

Name:		warble
Version:	2.0.1
Release:	2%{?dist}
Summary:	The word-guessing game

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/avojak/warble
Source:		%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(granite-7)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	vala
BuildRequires:	/usr/bin/appstream-util
BuildRequires:	/usr/bin/desktop-file-validate

%description
Native Linux word-guessing game built in Vala and Gtk.
Warble is inspired by the recently popular online game Wordle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appname}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/%{appname}
%{_datadir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%changelog
%autochangelog
