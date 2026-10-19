%global source0_hash bc8e7946ca091fdeeeebeb64db4e95d33a3ffb879048137f8d8a41ecd76caa3f
Name:           granite-7
Version:        7.8.1
Release:        1%{?dist}
Summary:        Extend GTK with common widgets and utilities
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/elementary/granite
Source0:        https://github.com/elementary/granite/archive/%{version}/%{name}.8.1.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(shumate-1.0)
BuildRequires:  sassc
BuildRequires:  vala
# /oreon:deps
%description

%package        devel
Summary:        Granite Toolkit (development headers)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
%description    devel

This package contains the development headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir granite-%{version}
%oreon_prep
%build

%meson -D gtk-stylesheets=true
%meson_build
%install
%meson_install
%find_lang granite-7
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/granite-7.metainfo.xml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite-7.demo.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n granite-7-devel -f %{oreon_filedir}/granite-7-devel.list

%changelog

%autochangelog
