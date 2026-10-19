%global source0_hash 885e29ce005b64cfe8ae04e3db75e2b2a29c023883111716271ebaa48c286313
%global app_id  app.drey.MultiplicationPuzzle
Name:           gmult
Version:        16.0
Release:        1%{?dist}
Summary:        Multiplication Puzzle
License:        GPL-3.0-or-later AND CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/mterry/gmult
Source0:        https://gitlab.gnome.org/mterry/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Requires:       hicolor-icon-theme
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
Multiplication Puzzle is a simple game inspired by the multiplication game 
inside the popular editor emacs. You are presented with a long multiplication 
problem where a 3-digit number is multiplied by a 2-digit number, yielding two 
intermediate 4-digit number and a final 5-digit answer.  However, all the 
digits are replaced by letters.  Your job is to discover which letters are 
which digits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
