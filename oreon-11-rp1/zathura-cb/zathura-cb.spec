%global source0_hash 072660fd32ce56ce512655caf8c190ffbf6c3f36ff09b3f740d65150f99ddc13
Name:             zathura-cb
Version:          2026.07.18
Release:        1%{?dist}
Summary:        Comic book support for zathura
License:          Zlib
URL:              https://pwmt.org/projects/%{name}
Source0:        https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
Requires:         zathura >= 0.3.8
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  girara-devel
BuildRequires:  libappstream-glib
BuildRequires:  libarchive-devel
BuildRequires:  meson
BuildRequires:  zathura-devel
# /oreon:deps
%description
The zathura-cb plugin adds comic book archive support to zathura.

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
