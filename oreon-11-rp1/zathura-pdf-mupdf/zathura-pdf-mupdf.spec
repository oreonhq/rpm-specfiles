%global source0_hash 82f302bc786616d2d7dd98c1cb0559f08f7620e4b01044e6ec6aba10e3d5c36a
Name:             zathura-pdf-mupdf
Version:          2026.07.18
Release:        1%{?dist}
Summary:        PDF support for zathura via mupdf
License:          Zlib
URL:              https://pwmt.org/projects/%{name}/
Source0:        https://pwmt.org/projects/%{name}//download/%{name}-%{version}.tar.xz
Patch1:           0001-Update-Debian-build-branch-recent-packaging-changes-.patch
Patch2:           0001-configure-for-shared-mupdf-build.patch
Requires:         zathura >= 0.3.9
Conflicts:        zathura-pdf-poppler < 0.2.9
# oreon:deps
BuildRequires:  binutils
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  girara-devel
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  meson
BuildRequires:  mupdf-devel
BuildRequires:  zathura-devel
# /oreon:deps
%description
This plugin adds PDF support to zathura using the mupdf rendering engine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%oreon_autofiles main

%pre

[ -L %{_libdir}/zathura/pdf.so ] && rm -f %{_libdir}/zathura/pdf.so || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
