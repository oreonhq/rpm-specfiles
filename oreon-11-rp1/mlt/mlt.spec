%global source0_hash f11c30e21670f62a3dfc56a31306ac02f3feea00908a2821a4a0bf3e989d3d6a
%bcond_without  ruby
%bcond_without  php
%bcond_without  opencv
%bcond_with qt5
%bcond_with  ndi
Name:           mlt
Version:        7.40.0
Release:        1%{?dist}
Summary:        Toolkit for broadcasters, video editors, media players, transcoders
License:        GPL-3.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.mltframework.org/
Source0:        https://github.com/mltframework/mlt/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch2001:      mlt-7.36-restore-qt5-support.patch
%if %{with qt5}
%endif
Provides:  mlt-freeworld = %{version}-%{release}
Obsoletes: mlt-freeworld < %{version}-%{release}
%if %{with ndi}
%endif
%if %{with opencv}
%endif
%if %{with ruby}
%else
Obsoletes: mlt-ruby < %{version}-%{release}
%endif
%if %{with php}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$
%endif
%if %{with qt5}
Requires:      (%{name}-qt5%{?_isa} = %{version}-%{release} if qt5-qtbase%{?_isa})
%else
Obsoletes:      mlt-qt5 < %{version}-%{release}
%endif
Requires:      (%{name}-qt6%{?_isa} = %{version}-%{release} if qt6-qtbase%{?_isa})
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6CoreTools)
BuildRequires:  cmake(Qt6DBusTools)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6WidgetsTools)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  eigen3-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fftw-devel
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  ladspa-devel
BuildRequires:  libatomic
BuildRequires:  libebur128-devel
BuildRequires:  libexif-devel
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  movit-devel
BuildRequires:  opencv-devel
BuildRequires:  php-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  rubberband-devel
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  sed
BuildRequires:  sox-devel
BuildRequires:  swig
BuildRequires:  vid.stab-devel
BuildRequires:  xine-lib-devel
# /oreon:deps
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
mv %{buildroot}%{_bindir}/melt %{buildroot}%{_bindir}/mlt-melt
%oreon_autofiles python3-mlt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion mlt-framework-7)" = "%{version}"
test "$(pkg-config --modversion mlt++-7)" = "%{version}"
%files -f %{oreon_filedir}/main.list
%files -n mlt-qt6 -f %{oreon_filedir}/mlt-qt6.list
%files -n mlt-devel -f %{oreon_filedir}/mlt-devel.list
%files -n python3-mlt -f %{oreon_filedir}/python3-mlt.list
%files -n mlt-ruby -f %{oreon_filedir}/mlt-ruby.list
%files -n mlt-php -f %{oreon_filedir}/mlt-php.list

%changelog

%autochangelog
