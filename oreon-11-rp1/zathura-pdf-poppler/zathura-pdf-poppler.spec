%global source0_hash 605d3f2c2e90efbc0434bb7206f013dc8ff99d8b679c6b519e13543777635bf1
Name:             zathura-pdf-poppler
Version:          2026.07.18
Release:        1%{?dist}
Summary:        PDF support for zathura via poppler
License:          Zlib
URL:              http://pwmt.org/projects/%{name}
Source0:        http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
Requires:         zathura >= 0.5.3
Conflicts:        zathura-pdf-mupdf < 2026.07.18
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  girara-devel
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  poppler-glib-devel
BuildRequires:  zathura-devel
# /oreon:deps
%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%oreon_autofiles main

%pre

[ -L %{_libdir}/zathura/pdf.so ] || rm -f %{_libdir}/zathura/pdf.so
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
