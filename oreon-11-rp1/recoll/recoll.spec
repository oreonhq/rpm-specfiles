%global source0_hash 5dd899640cb1eb19cc8dacb2f4246da3e0890d3e0602f1098f6a77db66a88814

%global         gsspver 1.1.4
%global         __cmake_in_source_build 1

%if 0%{?fedora} < 42 && 0%{?rhel} < 10
%global         kio4 1
%endif

%ifnarch %{ix86} s390x
%global         qtweb 1
%endif

%if 0%{?rhel} > 9
# pass
%else
%global         chm 1
%endif

Summary:        Desktop full text search tool with Qt GUI
Name:           recoll
Version:        1.43.13
Release:        1%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.recoll.org
Source0:        https://www.recoll.org/recoll-%{version}.tar.gz
Source1:        https://www.recoll.org/downloads/src/gssp-recoll-%{gsspver}.tar.gz
Source10:       qmake-qt6.sh
Patch:          recoll-1.42.1-cmake4.patch
BuildRequires:  aspell-devel
BuildRequires:  bison
%{?chm:BuildRequires:  chmlib-devel}
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  file-devel
BuildRequires:  gcc-c++
# kio
%{?kio4:BuildRequires:  kdelibs4-devel}
# krunner
BuildRequires:  jsoncpp-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-kpackage-devel
BuildRequires:  kf6-krunner-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
%{?qtweb:BuildRequires:  qt6-qtwebengine-devel}
BuildRequires:  systemd-rpm-macros
BuildRequires:  xapian-core-devel
BuildRequires:  zlib-devel
Requires:       xdg-utils
Recommends:     (recoll-krunner if kf6-krunner)
Recommends:     (recoll-gssp if gnome-shell)
Recommends:     %{name}-helpers = %{version}-%{release}
%description
Recoll is a personal full text search package for Linux, FreeBSD and
other Unix systems. It is based on a very strong back end (Xapian), for
which it provides an easy to use, feature-rich, easy administration
interface.

%package       libs
Summary:       Libraries for Recoll applications
%description   libs
Shared libraries required to run Recoll applications.

%package       devel
Summary:       Libraries and header files to develop Recoll enabled applications
Requires:      %{name}-libs = %{version}-%{release}
%description   devel
Libraries and header files required to develop Recoll enabled
applications.

%package       helpers
Summary:       External helpers to make recoll understand more document formats
Requires:      %{name} = %{version}-%{release}
Requires:      %{name} = %{version}-%{release}
Recommends:    antiword
Recommends:    djvulibre
Recommends:    ghostscript
Recommends:    info
Recommends:    libwpd-tools
Recommends:    perl-Image-ExifTool
Recommends:    poppler-utils
Recommends:    python-chardet
Recommends:    python-rarfile
Recommends:    python3-mutagen
Recommends:    unrtf
Recommends:    wv
Suggests:      chmlib
Suggests:      texlive-detex
%description   helpers
Package will bring in a set of external helpers to make recoll able to parse and extract
information from various data formats

%package       kio
Summary:       KIO support for recoll
Requires:      %{name} = %{version}-%{release}
Supplements:   (kf6-kio-core and recoll)

%description   kio
The recoll KIO slave allows performing a recoll search by entering an
appropriate URL in a KDE open dialog, or with an HTML-based interface
displayed in Konqueror.

%package       krunner
Summary:       KRunner support for recoll
Requires:      %{name} = %{version}-%{release}
Supplements:   (kf6-krunner and recoll)
%description   krunner
The recoll KRunner plugin adds Recoll search results to KRunner output.

%package       gssp
Summary:       Recoll GNOME Shell search provider
Requires:      %{name} = %{version}-%{release}
Requires:      gnome-shell
Requires:      python3-pydbus
Supplements:   (gnome-shell and recoll)
%description   gssp
This package contains the Recoll GNOME Shell search provider

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -D -a 1
sed -i -e '1{\,^#!/usr/bin/env,d}' python/recoll/recoll/rclconfig.py
ln -s gssp-recoll-%{gsspver} gssp

%build
CFLAGS="%{optflags}"; export CFLAGS
CXXFLAGS="%{optflags}"; export CXXFLAGS
LDFLAGS="%{?__global_ldflags}"; export LDFLAGS

# force use of custom/local qmake, to inject proper build flags (above)
install -m755 -D %{SOURCE10} qmake-qt6.sh
export QMAKE=$(pwd)/qmake-qt6.sh
%meson -Drecollq=true -Dsystemd=true %{?qtweb:-Dwebengine=true} -Dwebkit=false
%meson_build

# gssp
pushd gssp
%configure
popd

%install
%meson_install

desktop-file-install --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-searchgui.desktop

# use /usr/bin/xdg-open
rm -f %{buildroot}/usr/share/recoll/filters/xdg-open
rm -f %{buildroot}%{_libdir}/recoll/librecoll.la

export RECOLL_LIB_DIR=%{_builddir}/%{name}-%{version}/redhat-linux-build/

# kio_recoll -kde5
pushd kde/kioslave/kio_recoll
cp CMakeLists-KF6.txt CMakeLists.txt
%cmake -DRECOLL_PUBLIC_LIB=1 -DQT_MAJOR_VERSION=6
%cmake_build
%cmake_install
popd

%if 0%{?kio4}
# kio_recoll -kde4
export QMAKE=qmake-qt4
pushd kde/kioslave/kio_recoll-kde4
%cmake_kde4 -DRECOLL_PUBLIC_LIB=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%cmake_install
popd
%endif

# krunner_recoll
pushd kde/krunner
cp CMakeLists-KF6.txt CMakeLists.txt
%cmake -DRECOLL_PUBLIC_LIB=1 -DQT_MAJOR_VERSION=6
%cmake_build
%cmake_install
popd

# gssp
pushd gssp
make install DESTDIR=%{buildroot}
popd

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/recoll" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/recoll-%{_arch}.conf

%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/filters/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_sysconfdir}/ld.so.conf.d/recoll-%{_arch}.conf
%{_bindir}/recoll
%{_bindir}/recollindex
%{_bindir}/recollq
%{_datadir}/recoll
%{_datadir}/metainfo/org.recoll.recoll.appdata.xml
%{_datadir}/applications/recoll-searchgui.desktop
%{_datadir}/icons/hicolor/48x48/apps/recoll.png
%{_datadir}/icons/hicolor/scalable/apps/recoll.svg
%{_datadir}/pixmaps/recoll.png
%{python3_sitearch}/recoll
%{python3_sitearch}/recollchm
%{python3_sitearch}/recollaspell.cpython-*-linux-gnu*.so
%{_mandir}/man1/recoll.1*
%{_mandir}/man1/recollq.1*
%{_mandir}/man1/recollindex.1*
%{_mandir}/man5/recoll.conf.5*
%{_unitdir}/recollindex@.service
%{_userunitdir}/recollindex.service

%files libs
%{_libdir}/librecoll.so.*

%files devel
%{_libdir}/librecoll.so
%{_includedir}/recoll

%files helpers
%license COPYING

%files kio
%license COPYING
%{_libdir}/qt6/plugins/kf6/kio/kio_recoll.so
%if 0%{?kio4}
%{_libdir}/kde4/kio_recoll.so
%{_datadir}/kde4/apps/kio_recoll/
%{_datadir}/kde4/services/recoll.protocol
%{_datadir}/kde4/services/recollf.protocol
%endif
%{_datadir}/kio_recoll/help.html
%{_datadir}/kio_recoll/welcome.html

%files krunner
%{_libdir}/qt6/plugins/kf6/krunner/krunner_recoll.so

%files gssp
%license COPYING
%{_bindir}/gssp-recoll.py
%{_datadir}/dbus-1/services/org.recoll.Recoll.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/org.recoll.Recoll.search-provider.ini

%changelog
%autochangelog
