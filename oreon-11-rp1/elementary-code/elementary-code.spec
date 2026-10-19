%global source0_hash b0b523547e2fe785651c37e9a0cd9338eedbbc34f4fa52c085ad172bd7245d6e
%global srcname code
%global appname io.elementary.code
%global __provides_exclude_from ^%{_libdir}/%{appname}/.*\\.so$
Name:           elementary-code
Summary:        Code editor from elementary
Version:        8.4.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/elementary/%{srcname}
Source0:        https://github.com/elementary/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Requires:       polkit
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libvala-0.56)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  polkit-devel
BuildRequires:  vala
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        The text editor that works (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

This package contains the development headers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{appname}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n elementary-code-devel -f %{oreon_filedir}/elementary-code-devel.list

%changelog

%autochangelog
