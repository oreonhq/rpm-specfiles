%global source0_hash 35a3cabc1617fa53b0def887d04ceef3c62a8bd15ddf6f011be0fe0e6fc60587
Name:             zathura-ps
Version:          2026.07.18
Release:        1%{?dist}
Summary:        PS support for zathura via libspectre
License:          Zlib
URL:              https://pwmt.org/projects/%{name}
Source0:        https://pwmt.org/projects/%{name}/download/%{name}-%{version}.tar.xz
Requires:         zathura >= 0.3.8
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  girara-devel
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libspectre-devel
BuildRequires:  meson
BuildRequires:  zathura-devel
# /oreon:deps
%description
The zathura-ps plugin adds PostScript support to zathura by
using the libspectre library.

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

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
