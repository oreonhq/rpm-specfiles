%global source0_hash 96db3d8fad497924a7390ad108a3ef72432a1d62d2456cae5e1934057018814f
Name:           gnome-taquin
Version:        3.38.1
Release:        15%{?dist}
Summary:        Sliding-block puzzle game
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Taquin
Source0:        https://download.gnome.org/sources/gnome-taquin/3.38/gnome-taquin-%{version}.tar.xz
Patch1:         0001-Don-t-alter-or-try-to-write-GtkChild-fields.patch
Patch2:         0001-Reference-of-GtkChild-fields-is-handled-by-GtkBuilde.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala
# /oreon:deps
%description
Taquin is a computer version of the 15-puzzle and other sliding puzzles.
The object of Taquin is to move tiles so that they reach their places, 
either indicated with numbers, or with parts of a great image.

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

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Taquin.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
