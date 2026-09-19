%global source0_hash 0fabd8c4ac04998e825a1d0b4691bc9a0022c2bd925fec5f5ed33341b2cda21f

%global commit  eaf6872f6ad490a4355c5c46279ddb81a9a15f92
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global commitdate 20130718

%global soname 0.7.0

Name:           libqxt-qt5
Version:        0.7.0
Release:        0.41.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Extended version of the original Qt extension library
# Automatically converted from old format: BSD and (CPL or LGPLv2) - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND (CPL-1.0 OR LicenseRef-Callaway-LGPLv2)
URL:            https://bitbucket.org/libqxt/libqxt/wiki/Home
Source0:        https://bitbucket.org/libqxt/libqxt/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
# Fix DSO linking
Patch0:         libqxt-linking.patch
# Fix build with GCC 6
Patch1:         libqxt-gcc6.patch
Patch2:         libqxt-header-fix.patch
#Debian patches
Patch3:         libqxt-use-system-qdoc3.patch
Patch4:         libqxt-fix-compiler-flags.patch
Patch5:         libqxt-qt5-libname.patch
Patch6:         libqxt-qt5-moc-pre-processing-order.patch

BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  libdb-devel
BuildRequires:  pkgconfig(xrandr)
# match what openssl version qt5-qtbase uses
%if 0%{?fedora} == 26
BuildRequires:  compat-openssl10-devel
%else
BuildRequires:  openssl-devel
%endif
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: make

%description
LibQxt, an extension library for Qt5, provides a suite of cross-platform
utility classes to add functionality not readily available in the Qt toolkit.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig(avahi-compat-libdns_sd)
Requires:       pkgconfig(avahi-core)
Requires:       libdb-devel

%description    devel
This package contains qt5 libraries and header files for developing applications
that use LibQxt.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc -n libqxt-libqxt-%{shortcommit}

mv libqxt-libqxt-%{shortcommit} qt5
pushd qt5
%patch -P0 -p1 -b .linking
%patch -P1 -p1 -b .gcc6
%patch -P2 -p1 -b .header-fix
%patch -P3 -p1 -b .use-system-qdoc3
%patch -P4 -p1 -b .fix-compiler-flags
%patch -P5 -p1 -b .libname
%patch -P6 -p1 -b .moc-pre-processing-order

# Remove bundled lib
rm -rf src/3rdparty/libssh2

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' examples/qxtsnapshot/{README,qxtsnapshotpreview.h,qxtsnapshot.h,qxtsnapshottooltip.h}

mkdir config.tests/qt5/
cp config.tests/qt4/qt4.pro config.tests/qt5/qt5.pro
cp config.tests/qt4/main.cpp config.tests/qt5/main.cpp
sed -i -e 's|configtest qt4 QT|configtest qt5 QT|' configure
sed -i -e 's|TARGET = qt4|TARGET = qt5|' config.tests/qt5/qt5.pro 
sed -i -e 's|qt4|qt5|' config.tests/qt5/main.cpp 
sed -i -e 's|qdoc3|qdoc|' doc/doc.pri
sed -i -e 's| -DQXT_DOXYGEN_RUN||' doc/doc.pri

# We don't want rpath
sed -i '/RPATH/d' src/qxtlibs.pri
popd

%build
############### QT5 ######################
pushd qt5
./configure -verbose                      \
 -I $(pkg-config --variable=includedir avahi-compat-libdns_sd) \
 -L $(pkg-config --variable=libdir avahi-compat-libdns_sd) \
 -qmake-bin %{_qt5_qmake}                 \
 -prefix %{_prefix}                       \
 -libdir %{_libdir}                       \
 -headerdir %{_qt5_headerdir}             \
 -docdir %{_datadir}/doc/libqxt-qt5-doc/html \
 -debug
# manually running qmake here may end up being fragile, if so,
# introducing a qmake wrapper is the next best thing -- rex
%{qmake_qt5} -r %{_qt5_qmake_flags} \
 QMAKE_LFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed"
%make_build
%make_build docs
popd

%install
############### QT5 ######################
pushd qt5

# We are installing these to the proper location
rm -fr %{buildroot}%{_prefix}/doc/

# Fix pkgconfig includedir qt5 path
sed -i -e 's|includedir=${prefix}/include/QxtNetwork|includedir=${prefix}/include/qt5/QxtNetwork|' lib/pkgconfig/QxtNetwork-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtSql|includedir=${prefix}/include/qt5/QxtSql|' lib/pkgconfig/QxtSql-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtWeb|includedir=${prefix}/include/qt5/QxtWeb|' lib/pkgconfig/QxtWeb-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtCore|includedir=${prefix}/include/qt5/QxtCore|' lib/pkgconfig/QxtCore-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtZeroconf|includedir=${prefix}/include/qt5/QxtZeroconf|' lib/pkgconfig/QxtZeroconf-qt5.pc
sed -i -e 's|includedir=${prefix}/include/QxtWidgets|includedir=${prefix}/include/qt5/QxtWidgets|' lib/pkgconfig/QxtWidgets-qt5.pc

# Fix pkgconfig files install dependencies
sed -i -e 's|Requires: QtCore|Requires: Qt5Core|' lib/pkgconfig/QxtCore-qt5.pc
sed -i -e 's|Requires: QxtCore QtNetwork|Requires: QxtCore-qt5 Qt5Network|' lib/pkgconfig/QxtNetwork-qt5.pc
sed -i -e 's|Requires: QxtCore QtSql|Requires: QxtCore-qt5 Qt5Sql|' lib/pkgconfig/QxtSql-qt5.pc
sed -i -e 's|Requires: QxtCore QxtNetwork|Requires: QxtCore-qt5 QxtNetwork-qt5|' lib/pkgconfig/QxtWeb-qt5.pc
sed -i -e 's|Requires: QtCore QxtCore QtGui|Requires: Qt5Core QxtCore-qt5 Qt5Gui|' lib/pkgconfig/QxtWidgets-qt5.pc
sed -i -e 's|Requires: QxtCore QxtNetwork|Requires: QxtCore-qt5 QxtNetwork-qt5|' lib/pkgconfig/QxtZeroconf-qt5.pc

make install --ignore-errors INSTALL_ROOT=%{buildroot}

 %if 0%{?flatpak}
 # qtbase is part of runtime in /usr, this is built in /app
 mv %{buildroot}/usr/%{_lib}/qt5 %{buildroot}%{_libdir}
 %endif
%ldconfig_scriptlets

%files
%doc qt5/AUTHORS qt5/CHANGES qt5/README
%license qt5/COPYING qt5/*.txt
%{_bindir}/qxtjsonrpc
%{_qt5_libdir}/*.so.*

%files devel
%{_qt5_headerdir}/QxtCore/
%{_qt5_headerdir}/QxtNetwork/
%{_qt5_headerdir}/QxtSql/
%{_qt5_headerdir}/QxtWeb/
%{_qt5_headerdir}/QxtWidgets/
%{_qt5_headerdir}/QxtZeroconf/
%{_qt5_libdir}/*.so
%{_qt5_plugindir}/designer/*.so
%{_qt5_libdir}/libQxt*.prl
%{_qt5_libdir}/pkgconfig/*.pc
%{_qt5_libdir}/qt5/mkspecs/features/qxt*.prf
%dir %{_qt5_libdir}/qt5/plugins/designer/pkgconfig
%{_qt5_libdir}/qt5/plugins/designer/pkgconfig/QxtDesignerPlugins-qt5.pc

%files doc
%doc qt5/examples/ qt5/doc/html/
%{_datadir}/doc/libqxt-qt5-doc/html/

%changelog
%autochangelog
