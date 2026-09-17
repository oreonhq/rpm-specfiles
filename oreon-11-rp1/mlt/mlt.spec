%global source0_hash 0d2b956864ba2ff58bb4e2b2779aa36870bd2a3a835e2dbfda33faa5fc6f4d3a

%if 0%{?rhel} == 8
%bcond_with     ruby
%bcond_with     php
%bcond_with     opencv
%else
%bcond_without  ruby
%if 0%{?fedora} >= 41 && 0%{?fedora} <= 43
%ifarch %{ix86}
%bcond_with     php
%else
%bcond_without  php
%endif
%else
%bcond_without  php
%endif
%bcond_without  opencv
%endif

# Temporarily restore Qt5 support
%if 0%{?fedora} && 0%{?fedora} < 44
%bcond_without qt5
%else
%bcond_with qt5
%endif

# needs nonfree/ndi-sdk
%bcond_with  ndi

Name:           mlt
Version:        7.36.1
Release:        4%{?dist}
Summary:        Toolkit for broadcasters, video editors, media players, transcoders

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# but is not used in Linux
# Automatically converted from old format: GPLv3 and LGPLv2+ - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.mltframework.org/
Source0:        https://github.com/mltframework/mlt/releases/download/v%{version}/%{name}-%{version}.tar.gz

# Upstream backports (0~500)

# Proposed fixes (501~1000)

# Downstream only changes (1001~2000)

# Temporary fixes (2001+)
## Only for 7.36.x and for F43 and older
Patch2001:      mlt-7.36-restore-qt5-support.patch

%if 0%{?fedora} > 43
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sed
BuildRequires:  frei0r-devel
BuildRequires:  opencv-devel
%if %{with qt5}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Network)
%endif
BuildRequires:  cmake(Qt6CoreTools)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiTools)
BuildRequires:  cmake(Qt6DBusTools)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6WidgetsTools)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  SDL2-devel
#BuildRequires:  gtk2-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  libatomic
BuildRequires:  libogg-devel
#Deprecated dv and kino modules are not built.
#https://github.com/mltframework/mlt/commit/9d082192a4d79157e963fd7f491da0f8abab683f
#BuildRequires:  libdv-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  ladspa-devel
BuildRequires:  libxml2-devel
BuildRequires:  sox-devel
# verion 3.0.11 needed for php7 IIRC
BuildRequires:  swig >= 3.0.11
BuildRequires:  python3-devel
BuildRequires:  freetype-devel
BuildRequires:  libexif-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  vid.stab-devel
BuildRequires:  movit-devel
BuildRequires:  eigen3-devel
BuildRequires:  libebur128-devel
BuildRequires:  rubberband-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  xine-lib-devel
Provides:  mlt-freeworld = %{version}-%{release}
Obsoletes: mlt-freeworld < %{version}-%{release}

%if %{with ndi}
BuildRequires:  libndi-devel
BuildRequires:  ndi-sdk-devel
%endif
%if %{with opencv}
BuildRequires:  opencv-devel
%endif
BuildRequires:  pkgconfig(libarchive)

%if %{with ruby}
BuildRequires:  ruby-devel
BuildRequires:  ruby
%else
Obsoletes: mlt-ruby < %{version}-%{release}
%endif

%if %{with php}
BuildRequires: php-devel
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$
%endif

%if %{with qt5}
Requires:      (%{name}-qt5%{?_isa} = %{version}-%{release} if qt5-qtbase%{?_isa})
%else
Obsoletes:      mlt-qt5 < %{version}-%{release}
%endif

Requires:      (%{name}-qt6%{?_isa} = %{version}-%{release} if qt6-qtbase%{?_isa})

%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting.

It provides a toolkit for broadcasters, video editors,media players,
transcoders, web streamers and many more types of applications. The
functionality of the system is provided via an assortment of ready to use
tools, xml authoring components, and an extendible plug-in based API.

%if %{with qt5}
%package qt5
Summary:        Qt5 support for MLT
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description qt5
This packages includes Qt5 support modules to MLT.
%endif

%package qt6
Summary:        Qt6 support for MLT
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description qt6
This packages includes Qt6 support modules to MLT.

%if %{with ndi}
%package ndi
Summary:        NDI support for MLT
%description ndi
This package adds NDI support through the NDI SDK to MLT.
%endif

%package devel
Summary:        Libraries, includes to develop applications with %{name}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%package -n python3-mlt
%{?python_provide:%python_provide python3-mlt}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Python package to work with MLT

%description -n python3-mlt
This module allows to work with MLT using python 3.

%package ruby
Requires: %{name}%{_isa} = %{version}-%{release}
Summary: Ruby package to work with MLT

%description ruby
This module allows to work with MLT using ruby.

%package php
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: PHP package to work with MLT

%description php
This module allows to work with MLT using PHP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%autopatch -p1 -M 2000

%if %{with qt5}
%patch -p1 -P 2001
%endif

chmod 644 src/modules/qt/kdenlivetitle_wrapper.cpp
chmod 644 src/modules/kdenlive/filter_freeze.c
chmod -x demo/demo

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# be sure that aren't used
rm -r src/win32/

%conf
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON           \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON   \
       %{?with_php: -DSWIG_PHP:BOOL=ON}     \
       -DSWIG_PYTHON:BOOL=ON                \
       %{?with_ruby: -DSWIG_RUBY:BOOL=ON}   \
       %{?with_opencv: -DMOD_OPENCV:BOOL=ON}  \
       -DMOD_GLAXNIMATE:BOOL=%{?with_qt5:ON}%{!?with_qt5:OFF}  \
       -DMOD_GLAXNIMATE_QT6:BOOL=ON  \
       -DMOD_QT:BOOL=%{?with_qt5:ON}%{!?with_qt5:OFF} \
       -DMOD_QT6:BOOL=ON \
       %{?with_ndi: -DMOD_NDI:BOOL=ON -DNDI_SDK_INCLUDE_PATH=%{_includedir}/ndi-sdk -DNDI_SDK_LIBRARY_PATH=%{_libdir} -DNDI_INCLUDE_DIR=%{_includedir}/ndi-sdk -DNDI_LIBRARY_DIR=%{_libdir}}

%build
%cmake_build

%install
%cmake_install

%if %{with php}
install -d %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/mlt.ini << 'EOF'
; Enable mlt extension module
extension=mlt.so
EOF
%endif

# maintain binary /usr/bin/mlt-melt
mv %{buildroot}%{_bindir}/melt %{buildroot}%{_bindir}/mlt-melt

# Remove rpath file '/usr/bin/melt-7' contains an invalid rpath '/home/martin/rpmbuild/BUILD/mlt-7.0.1/x86_64-redhat-linux-gnu/out/lib' in [/home/martin/rpmbuild/BUILD/mlt-7.0.1/x86_64-redhat-linux-gnu/out/lib]
#chrpath --delete %{buildroot}%{_bindir}/melt-7

%check
# verify pkg-config version sanity
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion mlt-framework-7)" = "%{version}"
test "$(pkg-config --modversion mlt++-7)" = "%{version}"

%files
%doc AUTHORS NEWS README*
%doc demo/
%license COPYING GPL
%{_bindir}/mlt-melt
%{_bindir}/melt-7
%{_libdir}/mlt-7/
%{_libdir}/libmlt++-7.so.*
%{_libdir}/libmlt-7.so.*
%{_datadir}/mlt-7/
%{_mandir}/man1/melt-7.1*
%exclude %{_libdir}/mlt-7/libmltglaxnimate*.so
%exclude %{_libdir}/mlt-7/libmltqt*.so
%if %{with ndi}
%exclude %{_libdir}/mlt-7/libmltndi.so

%files ndi
%{_libdir}/mlt-7/libmltndi.so
%endif

%if %{with qt5}
%files qt5
%{_libdir}/mlt-7/libmltglaxnimate.so
%{_libdir}/mlt-7/libmltqt.so
%endif

%files qt6
%{_libdir}/mlt-7/libmltglaxnimate-qt6.so
%{_libdir}/mlt-7/libmltqt6.so

%files -n python3-mlt
%{python3_sitearch}/mlt7.py*
%{python3_sitearch}/_mlt7.so
%{python3_sitearch}/__pycache__/mlt7.*

%if %{with ruby}
%files ruby
%{ruby_vendorarchdir}/mlt.so
%endif

%if %{with php}
%files php
%config(noreplace) %{_sysconfdir}/php.d/mlt.ini
%{php_extdir}/mlt.so
%endif

%files devel
%{_libdir}/pkgconfig/mlt-framework-7.pc
%{_libdir}/pkgconfig/mlt++-7.pc
%{_libdir}/libmlt-7.so
%{_libdir}/libmlt++-7.so
%{_libdir}/cmake/Mlt7/Mlt7*.cmake
%{_includedir}/mlt-7/

%changelog
%autochangelog
