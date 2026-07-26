%global source0_hash 5673c6a8b7e195b91a1720b24091915b8145de34879db1158bc936b100eaf3e3

Summary:       DjVu viewer
Name:          djview4
Version:       4.12
Release:       16%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://djvu.sourceforge.net/djview4.html
Source0:       http://downloads.sourceforge.net/djvu/djview-%{version}.tar.gz
Source20:      qmake-qt5.sh
Patch1:        djview-4.8-include.patch
Patch2:        djview4-aarch64.patch
# don't strip -g flags even without --enable-debug
Patch3:        djview-4.12-debug.patch
Patch4:        djview4-disable-workaround-qt55.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: djvulibre-devel >= 3.5.19 
# For plugin, see #756950
BuildRequires: glib2-devel
BuildRequires: libtiff-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-devel

%description 
DjView4 is a DjVu document viewer with the following features:
 o continuous scrolling of pages
 o side-by-side display of pages
 o display thumbnails as a grid
 o display outlines
 o page names supported
 o metadata dialog

It is based on DjVuLibre and Qt5.

%package       plugin
Summary:       Browser plugin for DjVu viewer
Requires:      %{name} = %{version}-%{release}

%description   plugin
This package provides a browser plugin for the DjVu document viewer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS

# avoid possible FTBFS if qt3 is installed
QTDIR=

# force use of custom/local qmake, to inject proper build flags (above)
install -m755 -D %{SOURCE20} bin/qmake-qt5
PATH=`pwd`/bin:%{_qt5_bindir}:$PATH; export PATH

./autogen.sh
%configure \
  --enable-nsdejavu \
  QMAKE="`pwd`/bin/qmake-qt5"

make %{?_smp_mflags} V=1 \
  QMAKE="`pwd`/bin/qmake-qt5"

%install
make DESTDIR=%{buildroot} INSTALL="%{__install} -p" \
     install plugindir=%{_libdir}/mozilla/plugins

# djview is taken from djvulibre
mv %{buildroot}%{_bindir}/djview %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/djview.1* %{buildroot}%{_mandir}/man1/%{name}.1*

%files
%license COPYING
%doc COPYRIGHT NEWS README
%{_bindir}/%{name}
%dir %{_datadir}/djvu
%{_datadir}/djvu/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/djvulibre-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/mimetypes/djvulibre-%{name}.png
%{_datadir}/icons/hicolor/64x64/mimetypes/djvulibre-%{name}.png
%{_datadir}/icons/hicolor/scalable/mimetypes/djvulibre-%{name}.svgz

%files plugin
%{_libdir}/mozilla
%{_mandir}/man1/nsdejavu.1*

%changelog
%autochangelog
