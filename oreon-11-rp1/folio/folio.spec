%global source0_hash 16437fd0786562c3ae3f0041fabdbad20dee5b3b454d0e1c662458399a7fc4ff
%global app_id com.toolstack.Folio
Name:           folio
Version:        25.02
Release:        1%{?dist}
Summary:        A markdown note-taking app for GNOME
License:        GPL-3.0-or-later
URL:            https://github.com/toolstack/Folio
Source0:        https://github.com/toolstack/Folio/archive/refs/tags/%{version}.tar.gz
Patch0:         storage-location.patch
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Folio-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{app_id}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
