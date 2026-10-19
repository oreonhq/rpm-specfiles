%global source0_hash 17bfb9731ab8070e01235381f08e57b1231ffb5f49eb031873ebfa189cdaf47d
Summary:        DjVu viewer
Name:          djview4
Version:       4.12.3
Release:        1%{?dist}
License:       GPL-2.0-or-later
URL:           http://djvu.sourceforge.net/djview4.html
Source0:        http://downloads.sourceforge.net/djvu/djview-%{version}.tar.gz
Source20:      qmake-qt5.sh
Patch1:        djview-4.8-include.patch
Patch2:        djview4-aarch64.patch
Patch3:        djview-4.12-debug.patch
Patch4:        djview4-disable-workaround-qt55.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  glib2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
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
%oreon_prep
%build

CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS
QTDIR=
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
mv %{buildroot}%{_bindir}/djview %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/djview.1* %{buildroot}%{_mandir}/man1/%{name}.1*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n djview4-plugin -f %{oreon_filedir}/djview4-plugin.list

%changelog

%autochangelog
