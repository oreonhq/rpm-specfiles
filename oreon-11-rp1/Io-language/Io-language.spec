%global source0_hash 9ac5cd94bbca65c989cd254be58a3a716f4e4f16480f0dc81070457aa353c217
%filter_from_provides /libiovmall.so$/d
%filter_from_requires /libiovmall.so$/d
%filter_setup
%define _version 2017.09.06
Name:           Io-language
Version:        20170906
Release:        26%{?dist}
Summary:        Io is a small, prototype-based programming language
License:        BSD-3-Clause
URL:            https://iolanguage.org
Source0:        https://github.com/stevedekorte/io/archive/2017.09.06/%{name}-%{version}.tar.gz
Patch1:         Io-2007-10-10-gcc43.patch
Patch5:         io-disable-simd.patch
Patch6:         Io-language-freeglut.patch
Patch7:         io-nosysctl.patch
Patch8:         pcre.patch
Patch9:         c99.patch
Patch10:        libm-basekit.patch
Patch11:        pointer-types.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-gconv-extra
BuildRequires:  gmp-devel
BuildRequires:  libdbi-devel
BuildRequires:  libedit-devel
BuildRequires:  libevent-devel
BuildRequires:  libffi-devel
BuildRequires:  libgle-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libpq-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtiff-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  loudmouth-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  ode-devel
BuildRequires:  opensp-devel
BuildRequires:  portaudio-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  soundtouch-devel
BuildRequires:  sqlite-devel
BuildRequires:  taglib-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  yajl-devel
# /oreon:deps
%description
Io is a small, prototype-based programming language. The ideas in
Io are mostly inspired by Smalltalk (all values are objects), Self
(prototype-based), NewtonScript (differential inheritance), Act1
(actors and futures for concurrency), LISP (code is a runtime
inspectable/modifiable tree) and Lua (small, embeddable).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package graphics-and-sound
Summary:        Io graphics and sound support
Requires:       %{name} = %{version}-%{release}
%description graphics-and-sound
Io graphics and sound support, this package includes IO bindings needed to
write Io programs which want to display graphics and / or produce sound
(OpenGL, Image loading, PortAudio, etc.).

%package extras
Summary:        Io extra addons
Requires:       %{name} = %{version}-%{release}
%description extras
This package includes addons for Io which require additional libraries to be
installed. This includes the Python and Socket addons.

%package postgresql
Summary:        Io postgresql bindings
Requires:       %{name} = %{version}-%{release}
%description postgresql
Io postgresql bindings.

%package mysql
Summary:        Io mysql bindings
Requires:       %{name} = %{version}-%{release}
%description mysql
Io mysql bindings

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn io-%{_version}
%patch -P 1 -p1 -b .gcc43
%patch -P 5 -p0
%patch -P 6 -p0
%patch -P 7 -p0
%patch -P 8 -p0
%patch -P 9 -p1
%patch -P 10 -p0
%patch -P 11 -p0
sed -i 's|/lib/io/addons|/%{_lib}/io/addons|g' libs/iovm/io/AddonLoader.io
# building Io while Io-language-devel is installed results in binaries getting
# linked against the installed version, instead of the just build one <sigh>
if [ -f /usr/include/io/IoVM.h ]; then
  echo "Error building Io while Io-language-devel is installed does not work!"
  exit 1
fi
# libstdc++.so is searched and not found ...
#sed -i -e 's|dependsOnLib("stdc++")||g' addons/SoundTouch/build.io
# remove add-ons which we do not want to build ever
rm -fr addons/AVCodec
rm -rf addons/ODE
rm -rf addons/Regex
sed -i /ODE/d addons/CMakeLists.txt
# for %doc
#mv addons/OpenGL/docs OpenGL
iconv -f MACINTOSH -t UTF8 libs/basekit/license/bsd_license.txt > license.txt
sed -i 's/\r//g' license.txt `find OpenGL -type f`
# for debuginfo
chmod -x addons/NullAddon/source/IoNullAddon.?

sed -i "s|-g -O0|$RPM_OPT_FLAGS|" CMakeLists.txt
%ifnarch %{ix86} x86_64
sed -i /sse/d CMakeLists.txt
%endif

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
cmake . -DOpenGL_GL_PREFERENCE=GLVND -DCMAKE_SKIP_RPATH:BOOL=YES -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES
make INSTALL_PREFIX=%{_prefix} OPTIMIZE="$RPM_OPT_FLAGS" \
  DLL_COMMAND='-shared -Wl,-soname="libiovmall.so.2"'
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons
install -m 755 _build/binaries/io $RPM_BUILD_ROOT%{_bindir}
install -m 755 _build/binaries/io_static $RPM_BUILD_ROOT%{_bindir}
install -m 755 _build/dll/libiovmall.so \
  $RPM_BUILD_ROOT%{_libdir}/libiovmall.so.2
ln -s libiovmall.so.2 $RPM_BUILD_ROOT%{_libdir}/libiovmall.so
install -m 755 _build/dll/libbasekit.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libcoroutine.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libgarbagecollector.so $RPM_BUILD_ROOT%{_libdir}/
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a _build/headers $RPM_BUILD_ROOT%{_includedir}/io
rm -rf addons/Clutter
rm -rf addons/Font
rm -rf addons/GLFW
rm -rf addons/MySQL
rm -rf addons/QDBM
rm -rf addons/SecureSocket
rm -rf addons/AppleSensors
rm -rf addons/Regex
for i in addons/*; do
  if [ -d $i/_build ]; then
    ADDON=`basename $i`
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -m 755 $i/_build/dll/libIo$ADDON.so \
      $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -p -m 644 $i/depends $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON
    touch $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/build.io
  fi
done
%ldconfig_scriptlets
%oreon_autofiles Io-language-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Io-language-graphics-and-sound usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Io-language-extras usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Io-language-postgresql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles Io-language-mysql usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n Io-language-devel -f %{oreon_filedir}/Io-language-devel.list
%files -n Io-language-graphics-and-sound -f %{oreon_filedir}/Io-language-graphics-and-sound.list
%files -n Io-language-extras -f %{oreon_filedir}/Io-language-extras.list
%files -n Io-language-postgresql -f %{oreon_filedir}/Io-language-postgresql.list
%files -n Io-language-mysql -f %{oreon_filedir}/Io-language-mysql.list

%changelog

%autochangelog
