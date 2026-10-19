%global source0_hash 55051c6fead6b720fc93be1ed3c8bfdd8b1d20caea0c3261368555d7e3c47498
%global glib2_version 2.68.0
%global libgit2_glib_version 1.2.0
%global libpeas1_version 1.36.0-11
%global commit f7501bc827f1d4476336b0db0791335cf8a613c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20250512
%global git 1
Name:           gitg
Version:        45~%{gitdate}git%{shortcommit}
Release:        6%{?dist}
Summary:        GTK+ graphical interface for the git revision control system
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND MIT
URL:            https://wiki.gnome.org/Apps/Gitg
%if 0%{?git}
Source0:        https://gitlab.gnome.org/GNOME/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
Patch0:         gitg-norpath.patch
Patch1:         gitg-gir-2.0.patch
%else
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libpeas-gtk%{?_isa} >= %{libpeas1_version}
%global __provides_exclude_from ^%{_libdir}/gitg/plugins/.*\\.so$
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gettext
BuildRequires:  libpeas1-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  python3-devel
BuildRequires:  vala
# /oreon:deps
%description
gitg is the GNOME GUI client to view git repositories.

%package libs
Summary:        Backend Library for gitg
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}
%description libs
libgitg is a GObject based library that provides an easy access to git methods
through GObject based methods

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gitg-%{commit}

%build

%meson \
        -Dpython=true
%meson_build
%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{python3_sitelib}/gi/overrides/GitgExt.py
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.gitg.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/org.gnome.gitg.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n gitg-libs -f %{oreon_filedir}/gitg-libs.list
%files -n gitg-devel -f %{oreon_filedir}/gitg-devel.list

%changelog

%autochangelog
