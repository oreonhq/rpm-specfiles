%global source1_hash 5dd899640cb1eb19cc8dacb2f4246da3e0890d3e0602f1098f6a77db66a88814
%global source0_hash 0f77f5ef3a6ea3a6b95e3305eab6ff4c407244cec490ede88150a1b029be127e
%global         gsspver 1.1.4
%global         __cmake_in_source_build 1
%if 0%{?fedora} < 42 && 0%{?rhel} < 10 && 0%{?oreon} < 11
%global         kio4 1
%endif
%ifnarch %{ix86} s390x
%global         qtweb 1
%endif
%global         chm 1
Summary:        Desktop full text search tool with Qt GUI
Name:           recoll
Version:        1.44.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://www.recoll.org
Source0:        https://www.recoll.org/recoll-%{version}.tar.gz
Source1:        https://www.recoll.org/downloads/src/gssp-recoll-%{gsspver}.tar.gz
Source10:       qmake-qt6.sh
Patch:          recoll-1.42.1-cmake4.patch
%{?chm:BuildRequires:  chmlib-devel}
%{?kio4:BuildRequires:  kdelibs4-devel}
%{?qtweb:BuildRequires:  qt6-qtwebengine-devel}
Requires:       xdg-utils
Recommends:     (recoll-krunner if kf6-krunner)
Recommends:     (recoll-gssp if gnome-shell)
Recommends:     %{name}-helpers = %{version}-%{release}
# oreon:deps
BuildRequires:  aspell-devel
BuildRequires:  bison
BuildRequires:  chmlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  file-devel
BuildRequires:  gcc-c++
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
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xapian-core-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
install -m755 -D %{SOURCE10} qmake-qt6.sh
export QMAKE=$(pwd)/qmake-qt6.sh
%meson -Drecollq=true -Dsystemd=true %{?qtweb:-Dwebengine=true} -Dwebkit=false
%meson_build
pushd gssp
%configure
popd
%install
%meson_install
desktop-file-install --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/%{name}-searchgui.desktop
rm -f %{buildroot}/usr/share/recoll/filters/xdg-open
rm -f %{buildroot}%{_libdir}/recoll/librecoll.la
export RECOLL_LIB_DIR=%{_builddir}/%{name}-%{version}/redhat-linux-build/
pushd kde/kioslave/kio_recoll
cp CMakeLists-KF6.txt CMakeLists.txt
%cmake -DRECOLL_PUBLIC_LIB=1 -DQT_MAJOR_VERSION=6
%cmake_build
%cmake_install
popd
%if 0%{?kio4}
export QMAKE=qmake-qt4
pushd kde/kioslave/kio_recoll-kde4
%cmake_kde4 -DRECOLL_PUBLIC_LIB=1 -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%cmake_install
popd
%endif
pushd kde/krunner
cp CMakeLists-KF6.txt CMakeLists.txt
%cmake -DRECOLL_PUBLIC_LIB=1 -DQT_MAJOR_VERSION=6
%cmake_build
%cmake_install
popd
pushd gssp
make install DESTDIR=%{buildroot}
popd
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/recoll" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/recoll-%{_arch}.conf
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/filters/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{oreon_filedir}/main.list
%files -n recoll-libs -f %{oreon_filedir}/recoll-libs.list
%files -n recoll-devel -f %{oreon_filedir}/recoll-devel.list
%files -n recoll-helpers -f %{oreon_filedir}/recoll-helpers.list
%files -n recoll-kio -f %{oreon_filedir}/recoll-kio.list
%files -n recoll-krunner -f %{oreon_filedir}/recoll-krunner.list
%files -n recoll-gssp -f %{oreon_filedir}/recoll-gssp.list

%changelog

%autochangelog
