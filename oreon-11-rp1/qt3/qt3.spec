%define _default_patch_fuzz 2

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

%global source0_hash 1b7a1ff62ec5a9cb7a388e2ba28fda6f960b27f27999482ebeceeadb72ac9f6e

Name: qt3
Summary: The shared library for the Qt 3 GUI toolkit
Version: 3.3.8b
Release: 103%{?dist}
# Automatically converted from old format: QPL or GPLv2 or GPLv3 - review is highly recommended.
License: QPL-1.0 OR GPL-2.0-only OR GPL-3.0-only
Url: http://www.troll.no
Source0: https://ftp2.osuosl.org/pub/blfs/conglomeration/qt3/qt-x11-free-%{version}.tar.gz
Source2: qt.sh
Source3: qt.csh
Source4: designer3.desktop
Source5: assistant3.desktop
Source6: linguist3.desktop
Source7: qtconfig3.desktop

Patch1: qt-3.3.4-print-CJK.patch
Patch2: qt-3.0.5-nodebug.patch
Patch3: qt-3.1.0-makefile.patch
Patch4: qt-x11-free-3.3.7-umask.patch
Patch5: qt-x11-free-3.3.6-strip.patch
Patch7: qt-x11-free-3.3.2-quiet.patch
Patch8: qt-x11-free-3.3.3-qembed.patch
Patch12: qt-uic-nostdlib.patch
Patch13: qt-x11-free-3.3.6-qfontdatabase_x11.patch
Patch14: qt-x11-free-3.3.3-gl.patch
Patch19: qt-3.3.3-gtkstyle.patch
# hardcode the compiler version in the build key once and for all
Patch20: qt-x11-free-3.3.8b-hardcode-buildkey.patch
Patch24: qt-x11-free-3.3.5-uic.patch
Patch25: qt-x11-free-3.3.8b-uic-multilib.patch
Patch27: qt-3.3.6-fontrendering-ml_IN-209097.patch
Patch29: qt-3.3.8-fontrendering-as_IN-209972.patch
Patch31: qt-3.3.6-fontrendering-te_IN-211259.patch
Patch32: qt-3.3.6-fontrendering-214371.patch
Patch33: qt-3.3.8-fontrendering-#214570.patch
Patch34: qt-3.3.6-fontrendering-ml_IN-209974.patch
Patch35: qt-3.3.6-fontrendering-ml_IN-217657.patch
Patch37: qt-3.3.6-fontrendering-gu-228452.patch
Patch38: qt-x11-free-3.3.8-odbc.patch
Patch39: qt-x11-free-3.3.7-arm.patch
# See http://bugzilla.redhat.com/549820
# Try to set some sane defaults, for style, fonts, plugin path
# FIXME: style doesn't work.  use kde3 plastik, if available
Patch40: qt-x11-free-3.3.8b-sane_defaults.patch
# and/or just use qtrc to do the same thing
Source10: qtrc
# add missing #include <cstdef> to make gcc-4.6 happier
Patch41: qt-x11-free-3.3.8b-cstddef.patch
# fix aliasing issue in qlocale.cpp
Patch42: qt-x11-free-3.3.8b-qlocale-aliasing.patch
# use the system SQLite 2 (Debian's 91_system_sqlite.diff)
Patch43: qt-x11-free-3.3.8b-system-sqlite2.patch
# silence compiler warning in qimage.h by adding parentheses
Patch44: qt-x11-free-3.3.8b-qimage-parentheses.patch
# fix the include path for zlib.h in qcstring.cpp to pick up the system version
Patch45: qt-x11-free-3.3.8b-system-zlib-header.patch
# fix FTBFS with libpng 1.5 (patch from NetBSD)
Patch46: qt-3.3.8-libpng15.patch
# work around -Werror=format-security false positives (#1037297)
Patch47: qt-x11-free-3.3.8b-#1037297.patch
# search for FreeType using pkg-config, fixes FTBFS with freetype >= 2.5.1
Patch48: qt-x11-free-3.3.8b-freetype251.patch
# rename the struct Param in qsqlextension_p.h that conflicts with PostgreSQL 11
Patch49: qt-x11-free-3.3.8b-postgresql11.patch

# immodule patches
Patch50: qt-x11-immodule-unified-qt3.3.8-20071116.diff.bz2
Patch51: qt-x11-immodule-unified-qt3.3.5-20051012-quiet.patch
Patch52: qt-x11-free-3.3.8b-fix-key-release-event-with-imm.diff
Patch53: qt-x11-free-3.3.6-qt-x11-immodule-unified-qt3.3.5-20060318-resetinputcontext.patch

# mariadb support
Patch60: qt-x11-free-3.3.8b-mariadb.patch

# compile with PostgreSQL 12
Patch70: qt-x11-free-3.3.8b-PostgreSQL12.patch

# qt-copy patches
Patch100: 0038-dragobject-dont-prefer-unknown.patch
Patch101: 0047-fix-kmenu-width.diff
Patch102: 0048-qclipboard_hack_80072.patch
Patch103: 0056-khotkeys_input_84434.patch
Patch105: 0073-xinerama-aware-qpopup.patch
Patch107: 0079-compositing-types.patch
Patch108: 0080-net-wm-sync-request-2.patch
Patch110: 0084-compositing-properties.patch

# upstream patches
Patch200: qt-x11-free-3.3.4-fullscreen.patch
Patch201: qt-x11-free-3.3.8b-gcc43.patch

# security patches
# fix for CVE-2013-4549 backported from Qt 4
Patch300: qt-x11-free-3.3.8b-CVE-2013-4549.patch
# fix for CVE-2014-0190 (QTBUG-38367) backported from Qt 4
Patch301: qt-x11-free-3.3.8b-CVE-2014-0190.patch
# fix for CVE-2015-0295 backported from Qt 4
Patch302: qt-x11-free-3.3.8b-CVE-2015-0295.patch
# fix for CVE-2015-1860 backported from Qt 4
Patch303: qt-x11-free-3.3.8b-CVE-2015-1860.patch

%define qt_dirname qt-3.3
%define qtdir %{_libdir}/%{qt_dirname}
%define qt_docdir %{_docdir}/qt-devel-%{version}

%define smp 1
%define immodule 1
%define debug 0

# MySQL plugins
%define plugin_mysql -plugin-sql-mysql
%define mysql_include_dir %{_includedir}/mysql
%define mysql_lib_dir %{_libdir}/mysql

# Postgres plugins
%define plugin_psql -plugin-sql-psql

# ODBC plugins
%define plugin_odbc -plugin-sql-odbc

# sqlite plugins
%if 0%{?rhel} && 0%{?rhel} < 7
%define plugin_sqlite -plugin-sql-sqlite
%else
%define plugin_sqlite %{nil}
%endif

%define plugins_style -qt-style-cde -qt-style-motifplus -qt-style-platinum -qt-style-sgi -qt-style-windows -qt-style-compact -qt-imgfmt-png -qt-imgfmt-jpeg -qt-imgfmt-mng
%define plugins %{plugin_mysql} %{plugin_psql} %{plugin_odbc} %{plugin_sqlite} %{plugins_style}

# not sure what this is for anymore? -- rex
Requires: coreutils

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: libmng-devel
BuildRequires: glibc-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: giflib-devel
BuildRequires: perl-interpreter
BuildRequires: sed
BuildRequires: findutils
BuildRequires: cups-devel
BuildRequires: tar
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libXrender-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXt-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: desktop-file-utils
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
BuildRequires: mariadb-connector-c-devel
%else
BuildRequires: mysql-devel
%endif
BuildRequires: postgresql-server-devel
BuildRequires: unixODBC-devel
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: sqlite2-devel
%endif

%package config
Summary: Graphical configuration tool for programs using Qt 3
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}


%package devel
Summary: Development files for the Qt 3 GUI toolkit
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libXrender-devel
Requires: libXrandr-devel
Requires: libXcursor-devel
Requires: libXinerama-devel
Requires: libXft-devel
Requires: libXext-devel
Requires: libX11-devel
Requires: libSM-devel
Requires: libICE-devel
Requires: libXt-devel
Requires: xorg-x11-proto-devel
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel

%package devel-docs
Summary: Documentation for the Qt 3 GUI toolkit
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%package ODBC
Summary: ODBC drivers for Qt 3's SQL classes
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%package MySQL
Summary: MySQL drivers for Qt 3's SQL classes
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%package PostgreSQL
Summary: PostgreSQL drivers for Qt 3's SQL classes
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%package sqlite
Summary: sqlite drivers for Qt 3's SQL classes
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%package designer
Summary: Interface designer (IDE) for the Qt 3 toolkit
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt 3
applications, as well as the README files for Qt 3.


%description config
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains a graphical configuration tool for programs using Qt 3.


%description devel
The %{name}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

Install %{name}-devel if you want to develop GUI applications using the Qt 3
toolkit.


%description devel-docs
The %{name}-devel-docs package contains the man pages, the HTML documentation and
example programs for Qt 3.


%description ODBC
ODBC driver for Qt 3's SQL classes (QSQL)


%description MySQL
MySQL driver for Qt 3's SQL classes (QSQL)


%description PostgreSQL
PostgreSQL driver for Qt 3's SQL classes (QSQL)


%description sqlite
sqlite driver for Qt 3's SQL classes (QSQL)


%description designer
The %{name}-designer package contains an User Interface designer tool
for the Qt 3 toolkit.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n qt-x11-free-%{version}
%patch -P1 -p1 -b .cjk
%patch -P2 -p1 -b .ndebug
%patch -P3 -p1 -b .makefile
%patch -P4 -p1 -b .umask
%patch -P5 -p1 -b .strip
# drop backup file(s), else they get installed too, http://bugzilla.redhat.com/639459
rm -fv mkspecs/linux-g++*/qmake.conf.strip
%patch -P7 -p1 -b .quiet
%patch -P8 -p1 -b .qembed
%patch -P12 -p1 -b .nostdlib
%patch -P13 -p1 -b .fonts
%patch -P14 -p1 -b .gl
%patch -P19 -p1 -b .gtk
gcc -dumpversion ||:
%patch -P20 -p1 -b .hardcode-buildkey
%patch -P24 -p1 -b .uic
%patch -P25 -p1 -b .uic-multilib
%patch -P27 -p1 -b .fontrendering-ml_IN-bz#209097
%patch -P29 -p1 -b .fontrendering-as_IN-bz#209972
%patch -P31 -p1 -b .fontrendering-te_IN-bz#211259
%patch -P32 -p1 -b .fontrendering-bz#214371
%patch -P33 -p1 -b .fontrendering-#214570
%patch -P34 -p1 -b .fontrendering-#209974
%patch -P35 -p1 -b .fontrendering-ml_IN-217657
%patch -P37 -p1 -b .fontrendering-gu-228452
%patch -P38 -p1 -b .odbc
# it's not 100% clear to me if this is safe for all archs -- Rex
%ifarch %{arm} 
%patch -P39 -p1 -b .arm
%endif
%patch -P40 -p1 -b .sane_defaults
sed -i.KDE3_PLUGIN_PATH \
  -e "s|@@KDE3_PLUGIN_PATH@@|%{_libdir}/kde3/plugins|" \
  src/kernel/qapplication.cpp
%patch -P41 -p1 -b .cstddef
%patch -P42 -p1 -b .qlocale-aliasing
%patch -P43 -p1 -b .system-sqlite2
%patch -P44 -p1 -b .qimage-parentheses
%patch -P45 -p1 -b .system-zlib-header
# libpng >= 1.5 made png_info/png_struct opaque
%patch -P46 -p0 -b .libpng15
%patch -P47 -p1 -b .#1037297
%patch -P48 -p1 -b .freetype251
%patch -P49 -p1 -b .postgresql11

# immodule patches
%if %{immodule}
%patch -P50 -p1
%patch -P51 -p1 -b .quiet
%patch -P52 -p1 -b .fix-key-release-event-with-imm
%patch -P53 -p1 -b .resetinputcontext
%endif

# mariadb
%patch -P60 -p1 -b .mariadb

# PostgreSQL 12
%patch -P70 -p1 -b .PostgreSQL12

# qt-copy patches
%patch -P100 -p0 -b .0038-dragobject-dont-prefer-unknown
%patch -P101 -p0 -b .0047-fix-kmenu-width
%patch -P102 -p0 -b .0048-qclipboard_hack_80072
%patch -P103 -p0 -b .0056-khotkeys_input_84434
%patch -P105 -p0 -b .0073-xinerama-aware-qpopup
%patch -P107 -p0 -b .0079-compositing-types
%patch -P108 -p0 -b .0080-net-wm-sync-request
%patch -P110 -p0 -b .0084-compositing-properties

# upstream patches
%patch -P200 -p1 -b .fullscreen
%patch -P201 -p1 -b .gcc34

# security patches
%patch -P300 -p1 -b .CVE-2013-4549
%patch -P301 -p1 -b .CVE-2014-0190
%patch -P302 -p1 -b .CVE-2015-0295
%patch -P303 -p1 -b .CVE-2015-1860

# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 < doc/man/man3/qdial.3qt > doc/man/man3/qdial.3qt_
mv doc/man/man3/qdial.3qt_ doc/man/man3/qdial.3qt

# get rid of bundled libraries to ensure they won't be used
rm -rf src/3rdparty/{lib*,sqlite,zlib}

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

%if %{smp}
   export SMP_MFLAGS="%{?_smp_mflags}"
%endif

%if %{immodule}
   sh ./make-symlinks.sh
%endif

# set correct X11 prefix
perl -pi -e "s,QMAKE_LIBDIR_X11.*,QMAKE_LIBDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_X11.*,QMAKE_INCDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_OPENGL.*,QMAKE_INCDIR_OPENGL\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_LIBDIR_OPENGL.*,QMAKE_LIBDIR_OPENGL\t=," mkspecs/*/qmake.conf

# don't use rpath
perl -pi -e "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf

perl -pi -e "s|-O2|$INCLUDES %{optflags} -fno-strict-aliasing|g" mkspecs/*/qmake.conf

# set correct lib path
if [ "%{_lib}" == "lib64" ] ; then
  perl -pi -e "s,/usr/lib /lib,/usr/%{_lib} /%{_lib},g" config.tests/{unix,x11}/*.test
  perl -pi -e "s,/lib /usr/lib,/%{_lib} /usr/%{_lib},g" config.tests/{unix,x11}/*.test
fi

# build shared, threaded (default) libraries
echo yes | ./configure \
  -prefix $QTDEST \
  -docdir %{qt_docdir} \
%if "%{_lib}" == "lib64"
  -platform linux-g++-64 \
%else
  -platform linux-g++ \
%endif
%if %{debug}
  -debug \
%else
  -release \
%endif
  -shared \
  -largefile \
  -qt-gif \
  -system-zlib \
  -system-libpng \
  -system-libmng \
  -system-libjpeg \
  -no-exceptions \
  -enable-styles \
  -enable-tools \
  -enable-kernel \
  -enable-widgets \
  -enable-dialogs \
  -enable-iconview \
  -enable-workspace \
  -enable-network \
  -enable-canvas \
  -enable-table \
  -enable-xml \
  -enable-opengl \
  -enable-sql \
  -qt-style-motif \
  %{plugins} \
  -stl \
  -thread \
  -cups \
  -sm \
  -xinerama \
  -xrender \
  -xkb \
  -ipv6 \
  -dlopen-opengl \
  -xft \
  -tablet

%make_build src-qmake

%if 0%{?rhel} && 0%{?rhel} < 7
# build sqlite plugin
pushd plugins/src/sqldrivers/sqlite
qmake -o Makefile sqlite.pro
popd
%endif

# build psql plugin
pushd plugins/src/sqldrivers/psql
qmake -o Makefile "INCLUDEPATH+=%{_includedir}/pgsql %{_includedir}/pgsql/server %{_includedir}/pgsql/internal" "LIBS+=-lpq" psql.pro
popd

# build mysql plugin
pushd plugins/src/sqldrivers/mysql
qmake -o Makefile "INCLUDEPATH+=%{mysql_include_dir}" "LIBS+=-L%{mysql_lib_dir} -lmysqlclient" mysql.pro
popd

# build odbc plugin
pushd plugins/src/sqldrivers/odbc
qmake -o Makefile "LIBS+=-lodbc" odbc.pro
popd

%make_build src-moc
%make_build sub-src
%make_build sub-tools UIC="$QTDIR/bin/uic -nostdlib -L $QTDIR/plugins"

%install
rm -rf %{buildroot}

export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

make install INSTALL_ROOT=%{buildroot}

install -m644 -D %{SOURCE10} %{buildroot}%{qtdir}/etc/settings/qtrc
sed -i \
  -e "s|@@QTDIR@@|%{qtdir}|" \
  -e "s|@@KDE3_PLUGIN_PATH@@|%{_libdir}/kde3/plugins|" \
   %{buildroot}%{qtdir}/etc/settings/qtrc

for i in findtr qt20fix qtrename140 lrelease lupdate ; do
   install bin/$i %{buildroot}%{qtdir}/bin/
done

# strip extraneous dirs/libraries, stop overlinking
sed -i -e 's|^Libs: -L${libdir} -lqt-mt.*|Libs: -L${libdir} -lqt-mt|g' %{buildroot}%{qtdir}/lib/pkgconfig/*.pc
sed -i -e "s|^QMAKE_PRL_LIBS =.*|QMAKE_PRL_LIBS = -L%{qtdir}/lib -lqt-mt|g" %{buildroot}%{qtdir}/lib/*.prl

# pkgconfig love
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}%{qtdir}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

# install man pages
mkdir -p %{buildroot}%{_mandir}
cp -fR doc/man/* %{buildroot}%{_mandir}/

# clean up
make -C tutorial clean
make -C examples clean

# Make sure the examples can be built outside the source tree.
# Our binaries fulfill all requirements, so...
perl -pi -e "s,^DEPENDPATH.*,,g;s,^REQUIRES.*,,g" `find examples -name "*.pro"`

# don't include Makefiles of qt examples/tutorials
find examples -name "Makefile" | xargs rm -f
find examples -name "*.obj" | xargs rm -rf
find examples -name "*.moc" | xargs rm -rf
find tutorial -name "Makefile" | xargs rm -f

for a in */*/Makefile ; do
  sed 's|^SYSCONF_MOC.*|SYSCONF_MOC		= %{qtdir}/bin/moc|' < $a > ${a}.2
  mv -v ${a}.2 $a
done

mkdir -p %{buildroot}/etc/profile.d
install -m 644 %{SOURCE2} %{SOURCE3} %{buildroot}/etc/profile.d/

# Add desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --vendor="qt" \
  %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

# Patch qmake to use qt-mt unconditionally
perl -pi -e "s,-lqt ,-lqt-mt ,g;s,-lqt$,-lqt-mt,g" %{buildroot}%{qtdir}/mkspecs/*/qmake.conf

# remove broken links
rm -f %{buildroot}%{qtdir}/mkspecs/default/linux-g++*
rm -f %{buildroot}%{qtdir}/lib/*.la

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{qtdir}/lib" > %{buildroot}/etc/ld.so.conf.d/qt-%{_arch}.conf

# install icons
mkdir %{buildroot}%{_datadir}/pixmaps
install -m 644 tools/assistant/images/qt.png %{buildroot}%{_datadir}/pixmaps/qtconfig3.png
install -m 644 tools/assistant/images/designer.png %{buildroot}%{_datadir}/pixmaps/designer3.png
install -m 644 tools/assistant/images/assistant.png %{buildroot}%{_datadir}/pixmaps/assistant3.png
install -m 644 tools/assistant/images/linguist.png %{buildroot}%{_datadir}/pixmaps/linguist3.png

# own style directory
mkdir -p %{buildroot}%{qtdir}/plugins/styles


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc FAQ LICENSE* README* changes*
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %{qtdir}/etc/
%dir %{qtdir}/etc/settings/
%dir %{qtdir}/lib
%dir %{qtdir}/plugins
%dir %{qtdir}/plugins/sqldrivers
%dir %{qtdir}/plugins/styles
%config %{qtdir}/etc/settings/qtrc
%{qtdir}/translations/
%{qtdir}/plugins/designer/
%if %{immodule}
%{qtdir}/plugins/inputmethods
%endif
%config /etc/profile.d/*
/etc/ld.so.conf.d/*
%{qtdir}/lib/libqui.so.*
%{qtdir}/lib/libqt*.so.*

%files config
%{qtdir}/bin/qtconfig
%{_datadir}/applications/*qtconfig*.desktop
%{_datadir}/pixmaps/qtconfig3.png

%files devel
%{qt_docdir}/
%{qtdir}/bin/moc
%{qtdir}/bin/uic
%{qtdir}/bin/findtr
%{qtdir}/bin/qt20fix
%{qtdir}/bin/qtrename140
%{qtdir}/bin/assistant
%{qtdir}/bin/qm2ts
%{qtdir}/bin/qmake
%{qtdir}/bin/qembed
%{qtdir}/bin/linguist
%{qtdir}/bin/lupdate
%{qtdir}/bin/lrelease
%{qtdir}/include
%{qtdir}/mkspecs
%{qtdir}/lib/libqt*.so
%{qtdir}/lib/libqui.so
%{qtdir}/lib/libeditor.a
%{qtdir}/lib/libdesigner*.a
%{qtdir}/lib/libqassistantclient.a
%{qtdir}/lib/*.prl
%{qtdir}/phrasebooks
%{_libdir}/pkgconfig/*
%{_datadir}/applications/*linguist*.desktop
%{_datadir}/applications/*assistant*.desktop
%{_datadir}/pixmaps/linguist3.png
%{_datadir}/pixmaps/assistant3.png

%files devel-docs
%doc examples
%doc tutorial
%{_mandir}/*/*

%if 0%{?rhel} && 0%{?rhel} < 7
%files sqlite
%{qtdir}/plugins/sqldrivers/libqsqlite.so
%endif

%files ODBC
%{qtdir}/plugins/sqldrivers/libqsqlodbc.so

%files PostgreSQL
%{qtdir}/plugins/sqldrivers/libqsqlpsql.so

%files MySQL
%{qtdir}/plugins/sqldrivers/libqsqlmysql.so

%files designer
%{qtdir}/templates
%{qtdir}/bin/designer
%{_datadir}/applications/*designer*.desktop
%{_datadir}/pixmaps/designer3.png


%changelog
%autochangelog
