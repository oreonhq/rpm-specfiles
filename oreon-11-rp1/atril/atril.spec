%global source0_hash 74c4f42979f3ead52def23767448d06ad7f715421e03c9b509404b096de8193e
Name:          atril
Version:       1.28.7
Release:        1%{?dist}
Summary:        Document viewer
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:           http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       mate-desktop-libs
Requires:       mathjax
# oreon:deps
BuildRequires:  cairo-gobject-devel
BuildRequires:  caja-devel
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libXt-devel
BuildRequires:  libarchive-devel
BuildRequires:  libgxps-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libsecret-devel
BuildRequires:  libspectre-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  texlive-lib-devel
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  yelp-tools
# /oreon:deps
%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU, epub and XPS files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.

%package libs
Summary: Libraries for the mate-document-viewer
%description libs
This package contains shared libraries needed for mate-document-viewer.

%package devel
Summary: Support for developing back-ends for the mate-document-viewer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.

%package caja
Summary: Mate-document-viewer extension for caja
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: caja
%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package thumbnailer
Summary: Atril thumbnailer extension for caja
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: caja
%description thumbnailer
This package contains the atril extension for the
caja file manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-introspection \
        --enable-comics \
        --enable-dvi=yes \
        --enable-djvu=yes \
        --enable-t1lib=no \
        --enable-pixbuf \
        --enable-xps \
        --enable-epub \
        --enable-synctex
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags} V=1
%install
%{make_install}
%find_lang %{name} --with-gnome --all-name
find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/atril.desktop
%files -f %{oreon_filedir}/main.list
%files -n atril-libs -f %{oreon_filedir}/atril-libs.list
%files -n atril-devel -f %{oreon_filedir}/atril-devel.list
%files -n atril-caja -f %{oreon_filedir}/atril-caja.list
%files -n atril-thumbnailer -f %{oreon_filedir}/atril-thumbnailer.list

%changelog

%autochangelog
