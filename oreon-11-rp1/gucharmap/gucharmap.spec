%global source0_hash 564aca0ed8a25e4880ed5298de033889dfbc11bd49af1d7ee2959a5f46eb8f1d
%define glib2_version 2.32.0
%define gtk3_version 3.15.9
Name:           gucharmap
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode character picker and font browser
%global ver_major       %(echo %{version} | cut -d. -f1)
%global ver_minor       %(echo %{version} | cut -d. -f2)
%global ver_minor_next  %(echo $((%{ver_minor}+1)))
License:        GPL-3.0-or-later AND GFDL-1.3-or-later AND Unicode-DFS-2016
URL:            https://wiki.gnome.org/Apps/Gucharmap
Source0:        https://gitlab.gnome.org/GNOME/gucharmap/-/archive/%{version}/gucharmap-%{version}.tar.bz2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  (unicode-ucd >= 18.0 with unicode-ucd < 18.1)
BuildRequires:  (unicode-ucd-unihan >= 18.0 with unicode-ucd-unihan < 18.1)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  perl(Env)
BuildRequires:  vala
# /oreon:deps
%description
This program allows you to browse through all the available Unicode
characters and categories for the installed fonts, and to examine their
detailed properties. It is an easy way to find the character you might
only know by its Unicode name or code point.

%package libs
Summary: libgucharmap library
%description libs
The %{name}-libs package contains the libgucharmap library.

%package devel
Summary: Libraries and headers for libgucharmap
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The gucharmap-devel package contains header files and other resources
needed to use the libgucharmap library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ducd_path=/usr/share/unicode/ucd -Ddocs=true
%meson_build
%install
%meson_install
%find_lang gucharmap --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n gucharmap-libs -f %{oreon_filedir}/gucharmap-libs.list
%files -n gucharmap-devel -f %{oreon_filedir}/gucharmap-devel.list

%changelog

%autochangelog
