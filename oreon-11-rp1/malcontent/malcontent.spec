%global source0_hash 951c2732106254b2f4d22c06061d1a813d8b6310a045afc638c1e1a0c97e4e69
%global source1_hash 32673cfe72e0527b086af92a288add310166f7363a118191f64059e22d45dd0a
%global source2_hash 14f082f122eb4e495e2ac96f235efb01525ae5d4a1f0fd98148b4f7c7f95ccd2
%global source3_hash 469de2d445bf54880f652f4b6dc95c7cdf6f5502c35524a45b2122d70d47ebc2
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           malcontent
Version:        0.14.0
Release:        1%{?dist}
Summary:        Parental controls implementation
License:        LGPL-2.1-only AND CC-BY-3.0
URL:            https://gitlab.freedesktop.org/pwithnall/malcontent/
Source0:        https://tecnocode.co.uk/downloads/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gitlab.gnome.org/pwithnall/libgsystemservice/-/archive/0.3.0/libgsystemservice-0.3.0.tar.bz2
Source2:        https://github.com/GNOME/gvdb/archive/c6f2359cc1d00f16e0a0e2527fa0bc1882b8b5ab.tar.gz
Source3:        http://www.corpit.ru/mjt/tinycdb/tinycdb-0.81.tar.gz
Provides:       bundled(gvdb)
Provides:       bundled(libgsystemservice)
Provides:       bundled(tinycdb)
Requires: polkit
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-testing-0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
# /oreon:deps
%description
libmalcontent implements parental controls support which can be used by
applications to filter or limit the access of child accounts to inappropriate
content.

%package control
Summary:        Parental Controls UI
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description control
Parental controls UI for malcontent.

%package pam
Summary:        Parental Controls PAM Module
%description pam
PAM module for malcontent time limits.

%package tools
Summary:        Parental Controls Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
CLI tools for malcontent.

%package ui-devel
Summary:        Development files for libmalcontent-ui
Requires:       %{name}-ui-libs%{?_isa} = %{version}-%{release}
%description ui-devel
Development files for libmalcontent-ui.

%package ui-libs
Summary:        Libraries for %{name}
%description ui-libs
libmalcontent-ui.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for libmalcontent.

%package libs
Summary:        Libraries for %{name}
%description libs
libmalcontent runtime library.

%package doc
Summary:        Documentation for %{name}
%description doc
Documentation for libmalcontent.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n malcontent-%{tarball_version} -S git
tar -xf %{SOURCE1} -C subprojects
mv subprojects/libgsystemservice-0.3.0 subprojects/libgsystemservice
mkdir -p subprojects/gvdb
tar -xf %{SOURCE2} -C subprojects/gvdb --strip-components=1
tar -xf %{SOURCE3} -C subprojects
cp subprojects/packagefiles/tinycdb/meson.build subprojects/tinycdb-0.81

%build

%meson -Dui=enabled -Dinstalled_tests=false
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.freedesktop.MalcontentControl.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n malcontent-control -f %{oreon_filedir}/malcontent-control.list
%files -n malcontent-pam -f %{oreon_filedir}/malcontent-pam.list
%files -n malcontent-tools -f %{oreon_filedir}/malcontent-tools.list
%files -n malcontent-ui-devel -f %{oreon_filedir}/malcontent-ui-devel.list
%files -n malcontent-ui-libs -f %{oreon_filedir}/malcontent-ui-libs.list
%files -n malcontent-devel -f %{oreon_filedir}/malcontent-devel.list
%files -n malcontent-libs -f %{oreon_filedir}/malcontent-libs.list
%files -n malcontent-doc -f %{oreon_filedir}/malcontent-doc.list

%changelog

* Tue Jun 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.0-1
- import for oreon 11 iso
