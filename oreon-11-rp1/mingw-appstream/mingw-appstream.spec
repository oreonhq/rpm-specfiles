%global source0_hash db4439db6a33de3ca1041473501610844ddf1b72ae23016c05242c681c380b4d
%{?mingw_package_header}
Summary:        Utilities to generate, maintain and access the AppStream database
Name:    mingw-appstream
Version: 1.0.6
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://github.com/ximion/appstream
Source0:        https://www.freedesktop.org/software/appstream/releases/AppStream-%{version}.tar.xz
Patch0002: 0001-Lower-native-appstream-requirement-for-now.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  appstream-devel
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-librsvg2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-libxmlb
BuildRequires:  mingw32-libyaml
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-librsvg2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-libxmlb
BuildRequires:  mingw64-libyaml
BuildRequires:  mingw64-pango
BuildRequires:  xmlto
# /oreon:deps
%description
MinGW Windows appstream library.

%package -n mingw32-appstream
Summary: MinGW utilities to generate, maintain and access the AppStream database
BuildArch: noarch
%description -n mingw32-appstream
%{summary}.

%package -n mingw64-appstream
Summary: MinGW utilities to generate, maintain and access the AppStream database
BuildArch: noarch
%description -n mingw64-appstream
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir AppStream-%{version}
%oreon_prep
%build

%mingw_meson \
 -Dsystemd=false \
 -Dgir=false \
 -Dstemming=false \
 -Dapidocs=false \
 -Dinstall-docs=false \
 -Ddocs=false \
 -Dqt=false
%mingw_ninja
%install
%mingw_ninja_install
%mingw_find_lang %{name} --all-name
%oreon_autofiles mingw32-appstream usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-appstream usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-appstream -f %{oreon_filedir}/mingw32-appstream.list
%files -n mingw64-appstream -f %{oreon_filedir}/mingw64-appstream.list

%changelog

%autochangelog
