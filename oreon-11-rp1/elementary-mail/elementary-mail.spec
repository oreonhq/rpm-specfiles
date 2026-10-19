%global source0_hash 4c2e50f9958465911eb4d88a136eab8fa511d3870c4213a075c5bfe96ac51f8d
%global srcname mail
%global appname io.elementary.mail
%global __provides_exclude_from ^%{_libdir}/%{appname}/webkit2/.*\\.so$
Name:           elementary-mail
Summary:        Mail app designed for elementary
Version:        8.0.1
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.1-only
URL:            https://github.com/elementary/mail
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:          0001-libcamel-3.57.1.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk3)
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appname}
rm -r %{buildroot}/%{_sysconfdir}/apparmor.d
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
