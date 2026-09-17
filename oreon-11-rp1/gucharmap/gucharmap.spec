%global source0_hash d5aa79bee703846af9ba477803e0fd8c8f63d9c7c522a48e64ebf304bfbfe324

%define glib2_version 2.32.0
# this is already higher than the minimum supported upstream
%define gtk3_version 3.15.9

Name:           gucharmap
Version:        17.0.2
Release:        1%{?dist}
Summary:        Unicode character picker and font browser

# semver X, Y and Y+1
%global ver_major       %(echo %{version} | cut -d. -f1)
%global ver_minor       %(echo %{version} | cut -d. -f2)
%global ver_minor_next  %(echo $((%{ver_minor}+1)))

License:        GPL-3.0-or-later AND GFDL-1.3-or-later AND Unicode-DFS-2016
# GPL for the source code, GFDL for the docs, MIT for Unicode data
URL:            https://wiki.gnome.org/Apps/Gucharmap
Source:         https://gitlab.gnome.org/GNOME/gucharmap/-/archive/%{version}/gucharmap-%{version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  gobject-introspection-devel
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  perl(Env)
BuildRequires:  (unicode-ucd >= %{ver_major}.%{ver_minor} with unicode-ucd < %{ver_major}.%{ver_minor_next})
BuildRequires:  (unicode-ucd-unihan >= %{ver_major}.%{ver_minor} with unicode-ucd-unihan < %{ver_major}.%{ver_minor_next})
BuildRequires:  vala

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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

%autosetup

%build
%meson -Ducd_path=/usr/share/unicode/ucd -Ddocs=true

%meson_build

%install
%meson_install

%find_lang gucharmap --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files -f gucharmap.lang
%license COPYING COPYING.GFDL COPYING.UNICODE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.gschema.xml
%{_metainfodir}/%{name}.metainfo.xml

%files libs
%license COPYING
%{_libdir}/libgucharmap_2_90.so.*
%{_libdir}/girepository-1.0/

%files devel
%{_includedir}/gucharmap-2.90
%{_libdir}/libgucharmap_2_90.so
%{_libdir}/pkgconfig/gucharmap-2.90.pc
%{_datadir}/gir-1.0
%{_datadir}/gtk-doc/html/gucharmap-2.90/
%{_datadir}/vala/vapi/gucharmap-2.90.deps
%{_datadir}/vala/vapi/gucharmap-2.90.vapi

%changelog
%autochangelog
