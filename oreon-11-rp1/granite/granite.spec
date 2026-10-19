%global source0_hash bc8e7946ca091fdeeeebeb64db4e95d33a3ffb879048137f8d8a41ecd76caa3f
%global common_description %{expand:
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.}
Name:           granite
Summary:        elementary companion library for GTK+ and GLib
Version:        7.8.1
Release:        1%{?dist}
License:        LGPL-3.0-or-later
URL:            https://github.com/elementary/granite
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       gsettings-desktop-schemas
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  vala
# /oreon:deps
%description %{common_description}

%package        devel
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel %{common_description}

This package contains the development headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir granite-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang granite
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/io.elementary.granite.demo.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/granite.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n granite-devel -f %{oreon_filedir}/granite-devel.list

%changelog

%autochangelog
