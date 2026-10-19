%global source0_hash 451ac83ff99bbcf1e8231abbace77b65793f4ff2bb06e70df053410d454d36a5
Name:             zathura-djvu
Version:          2026.07.18
Release:        1%{?dist}
Summary:        DjVu support for zathura
License:          Zlib
URL:              http://pwmt.org/projects/%{name}
Source0:        http://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
Requires:         zathura >= 0.3.8
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  gcc
BuildRequires:  girara-devel
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  zathura-devel
# /oreon:deps
%description
The zathura-djvu plugin adds DjVu support to zathura by
using the djvulibre library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
