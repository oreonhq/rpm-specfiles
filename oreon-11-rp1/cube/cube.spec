%global source0_hash c2e43089bb24bf27bb07eb1a3b4114df8040372e4ba247788d99bc872d23d8ea

# The different tarballs have been at different versions
%define shortv %(echo %version|awk -F. '{print $1 "." $2}')
# Has been different from cubelib/cube
%define cubew_vers %version
%define shortwv %(echo %cubew_vers|awk -F. '{print $1 "." $2}')
%{!?bash_completion_dir:%global bash_completion_dir /usr/share/bash-completion/completions}

Name:           cube
Version:        4.9.1
Release:        3%{?dist}
Summary:        CUBE Uniform Behavioral Encoding generic presentation component
License:        BSD-3-Clause
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortv/dist/cubegui-%{version}.tar.gz
Source1:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortwv/dist/cubew-%{cubew_vers}.tar.gz
Source2:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortv/dist/cubelib-%{version}.tar.gz
BuildRequires:  dbus-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires: 	make
BuildRequires:  gcc-c++
%ifarch %qt5_qtwebengine_arches
# Not in ppc64le el9, for instance
BuildRequires:  qt5-qtwebengine-devel
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global ver %version

%description
CUBE (CUBE Uniform Behavioral Encoding) is a generic presentation component
suitable for displaying a wide variety of performance metrics for parallel
programs including MPI and OpenMP applications. CUBE allows interactive
exploration of a multidimensional performance space in a scalable fashion.
Scalability is achieved in two ways: hierarchical decomposition of individual
dimensions and aggregation across different dimensions. All performance
metrics are uniformly accommodated in the same display and thus provide the
ability to easily compare the effects of different kinds of performance
behavior.

%package        libs
Summary:        Non-GUI libraries for %{name}

%description    libs
Non-GUI libraries required by %{name}

%package  	libs-devel
Summary:	Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	libs-devel
Development files for %{name}-libs.

%package        guilib
Summary:        GUI library for %{name}

%description    guilib
GUI library for %{name}.

%package  	guilib-devel
Summary:	Development files for %{name}-guilib
Requires:       %{name}-guilib%{?_isa} = %{version}-%{release}

%description	guilib-devel
Development files for %{name}-guilib.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs-devel = %{version}-%{release}
Requires:	%{name}-guilib-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}, including GUI applications.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
tar fx %SOURCE0
tar fx %SOURCE1
tar fx %SOURCE2
# In v4.7 these files define compiler flags overriding the supplied
# ones in configure, which actually breaks the test for working CC due
# to -fPIE inconsistency.
# for d in cubew-* cubelib-%ver cubegui-*; do
#   printf 'CC=gcc\nCXX=g++\n' >$d/build-config/common/platforms/platform-backend-linux
# done

%build
# This may not be the best way to eliminate rpath from the -config binaries.
# rpmlint still complains, apparently about a string which doesn't
# affect --ldflags or show up in chrpath -l.
%global unhardcode \
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \\\
         -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/"
cd cubelib-%ver
%configure --enable-shared --disable-static --disable-silent-rules \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-frontend/config.status
%make_build
make install DESTDIR=$(pwd)/inst
cd ..
# Interface version (used by fake cubelib-config in build)
intver=$(awk -F \" '/^#define LIBRARY_INTERFACE_VERSION/ {print $2}' cubelib-%version/src/cubelib-config-frontend.h)
# Fiddle for cubelib not being installed when building cubegui by
# making a dummy -config script which prints what we want.  Ideally
# the package should be split into components now, but presumably that
# means a new revview
cat <<+ >cubelib-config
#!/bin/sh
case \$1 in
--cppflags|--cflags) printf '%s\n' -I$(pwd)/cubelib-%ver/inst%_includedir/cubelib ;;
--ldflags)  printf '%s\n' -L$(pwd)/cubelib-%ver/inst%_libdir ;;
--ltldflags)  printf '%s\n' -L$(pwd)/cubelib-%ver/inst%_libdir ;;
--libs) printf '%s\n' '-lcube4 -lz' ;;
--interface-version) printf '%s\n' $intver ;;
--include) printf '%s\n' $(pwd)/cubelib-%ver/inst%_includedir ;;
esac
+
chmod +x cubelib-config
cd cubew-%cubew_vers
# The configure configuration now ignores $CFLAGS etc. in the
# environment and actually fails for want of -fPIC, sigh, but not if
# they're given as args.
%configure --enable-shared --disable-static --disable-silent-rules \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-backend/config.status
%make_build
# Collect it for use by cubegui
make install DESTDIR=$(pwd)/inst
# Wrong paths in .la cause trouble
#rm inst%_libdir/*.la
cd ../cubegui-%ver
# Kludge: For some reason the Qt dependencies are found as .so paths
# in Fedora (only), and libtool re-orders them with libcube4gui after what it
# should link against, and linking fails.
%{?fedora:export LIBS="$LIBS -lQt5PrintSupport -lQt5Widgets -lQt5Gui -lQt5Network -lQt5Concurrent -lQt5Core"}
%configure --disable-static \
  --disable-silent-rules \
  --with-platform=linux \
  --with-cubelib=$(pwd)/.. \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-frontend/config.status
%make_build

%install
%make_install -C cubew-%cubew_vers
%make_install -C cubelib-%ver
%make_install -C cubegui-%ver
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Don't duplicate large files
ln -sf ../../cubelib/example/{trace,summary}.cubex %buildroot%_docdir/cubegui/example

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/CUBE.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright (c) 2014 Forschungszentrum Juelich GmbH, Germany -->

<application>
 <id type="desktop">CUBE.desktop</id>
 <metadata_license>CC0-1.0</metadata_license>
 <project_license>BSD-3-Clause</project_license>
 <name>Cube</name>
 <summary>A presentation component suitable for displaying
performance data for parallel programs</summary>
 <description>
  <p>
    "Cube" (CUBE Uniform Behavioral Encoding) is a presentation
    component suitable for displaying a wide variety of performance
    data for parallel programs including MPI and OpenMP applications.
  </p>
  <p>
    Program performance is represented in a multi-dimensional space including various program and
    system resources. The tool allows the interactive exploration of this
    space in a scalable fashion and browsing the different kinds of
    performance behavior with ease.  All metrics are uniformly accommodated in the 
    same display and thus provide the ability to easily compare the effects of 
    different kinds of program behavior.
  </p>
  <p>
    "Cube" also includes a library to
    read and write performance data as well as operators to compare,
    integrate, and summarize data from different experiments. 
  </p>
  <p>
    The Cube 4.x release series uses an incompatible API and
    file format compared to previous versions, however,
    existing files in CUBE3 format can still be processed
    for backwards-compatibility.    
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/topo1.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/topo2.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/box.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/flat.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/palette.png</screenshot>
 </screenshots>
 <url type="homepage">http://www.scalasca.org/software/cube-4.x/download.html</url>
 <updatecontact>scalasca_at_fz-juelich.de</updatecontact>
</application>
EOF

# Strip rpath
chrpath -d -k %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/{,cube-plugins/}*.so  || :

# Install desktop file
cat <<EOF >CUBE.desktop
[Desktop Entry]
Comment=Performance profile browser CUBE
Exec=%_bindir/cube
Icon=%_datadir/icons/cubegui/Cube.xpm
InitialPreference=3
MimeType=application/cube;
Name=Cube (scalasca.org)
Terminal=false
Type=Application
Categories=Science;ComputerScience;DataVisualization;
EOF
desktop-file-install --dir=%{buildroot}%{_datadir}/applications CUBE.desktop

# For abipkgdiff/taskotron; fixme: is there a conventional place to put it?
cat >%{buildroot}%{_libdir}/cube-plugins/plugins.abignore <<EOF
[suppress_file]
file_name_regexp = .*-plugin\\.so.*
EOF

mv %{buildroot}%{_prefix}/lib/cmake/CubeW %{buildroot}%{_libdir}/cmake/ || :
rmdir %{buildroot}%{_prefix}/lib/cmake || :

mkdir -p %{buildroot}%{bash_completion_dir}
mv %{buildroot}%{_bindir}/cubegui-autocompletion.sh %{buildroot}%{bash_completion_dir}/cube
# For MacOS?
rm %{buildroot}%{_bindir}/maccubegui.sh

%check
make -C cubelib-%ver check || { cat test/test*/*log && false; }
make -C cubew-%cubew_vers check || { cat test/test*/*log && false; }

%ldconfig_scriptlets libs
%ldconfig_scriptlets guilib

%files
%license cubegui-%ver/COPYING
%doc cubegui-%ver/AUTHORS
%doc cubegui-%ver/ChangeLog
%doc cubegui-%ver/OPEN_ISSUES
%doc cubegui-%ver/README
%{_bindir}/cube
%{_bindir}/cube3to4
%{_bindir}/cube4to3
%{_bindir}/cube_calltree
%{_bindir}/cube_canonize
%{_bindir}/cube_clean
%{_bindir}/cube_cmp
%{_bindir}/cube_commoncalltree
%{_bindir}/cube_cut
%{_bindir}/cube_derive
%{_bindir}/cube_diff
%{_bindir}/cube_dump
%{_bindir}/cube_exclusify
%{_bindir}/cube_inclusify
%{_bindir}/cube_info
%{_bindir}/cube_is_empty
%{_bindir}/cube_mean
%{_bindir}/cube_merge
%{_bindir}/cube_nodeview
%{_bindir}/cube_part
%{_bindir}/cube_pop_metrics
%{_bindir}/cube_rank
%{_bindir}/cube_regioninfo
%{_bindir}/cube_remap2
%{_bindir}/cube_sanity
%{_bindir}/cube_stat
%{_bindir}/cube_test
%{_bindir}/cube_topoassist
%{_bindir}/tau2cube
%{_libdir}/cube-plugins/
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/CUBE.desktop
%{_datadir}/icons/*
%{_datadir}/cubegui/
%{bash_completion_dir}/cube

%files devel

%files libs
%license cubegui-%ver/COPYING
%{_bindir}/cube_server
%exclude %{_libdir}/lib%{name}4gui*.so*
%{_libdir}/lib%{name}*.so.13*
%{_libdir}/libcube4w.so.12*
%{_datadir}/cubelib/
%{_datadir}/cubew/

%files libs-devel
%{_bindir}/cubelib-config
%{_bindir}/cubew-config
%{_includedir}/cubew
%{_includedir}/cubelib
%{_libdir}/lib%{name}*.so
%{_libdir}/cmake/CubeLib/CubeLibConfig.cmake
%{_libdir}/cmake/CubeW/CubeWConfig.cmake
%doc cubegui-%ver/examples

%files guilib
%license cubegui-%ver/COPYING
%{_libdir}/lib%{name}4gui.so.10*
%{_libdir}/libcube_graphwidgetcommon_plugin.so.10*

%files guilib-devel
%{_bindir}/cubegui-config
%{_includedir}/cubegui
%{_libdir}/lib%{name}4gui.so
%{_libdir}/cmake/CubeGui/CubeGuiConfig.cmake

%files doc
%license cubegui-%ver/COPYING
%doc %_docdir/cubew
%doc %_docdir/cubelib
%doc %_docdir/cubegui

%changelog
%autochangelog
