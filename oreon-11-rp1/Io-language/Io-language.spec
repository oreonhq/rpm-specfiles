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
Source0:        https://github.com/stevedekorte/io/archive/%{_version}/%{name}-%{version}.tar.gz
Patch1:         Io-2007-10-10-gcc43.patch
Patch5:         io-disable-simd.patch
Patch6:         Io-language-freeglut.patch
Patch7:         io-nosysctl.patch
Patch8:         pcre.patch
# https://github.com/IoLanguage/io/commit/ad58e1c661874e779f3638bb19090d633badb715
# https://github.com/IoLanguage/io/commit/05ca313f6cf1b5728631fe5ec923eb5078733684
# https://github.com/IoLanguage/io/commit/e707943b623c9bf680ac6a5bd54646ce1b5a61bd
# https://github.com/IoLanguage/io/commit/8cd5b5ad09a7707c859a7bdea342ae7ff2466e3c
# https://github.com/IoLanguage/io/commit/92fe8304c55b84a17b0624613a7006e85a0128a2
Patch9:         c99.patch
Patch10:        libm-basekit.patch
Patch11:        pointer-types.patch
BuildRequires:  make gcc gcc-c++
BuildRequires:  e2fsprogs-devel freeglut-devel gmp-devel
BuildRequires:  libedit-devel libevent-devel libjpeg-devel libpng-devel
BuildRequires:  libsamplerate-devel libsndfile-devel libtiff-devel
BuildRequires:  libxml2-devel ode-devel opensp-devel
BuildRequires:  portaudio-devel libpq-devel python3-devel soundtouch-devel
BuildRequires:  sqlite-devel taglib-devel ncurses-devel cairo-devel
BuildRequires:  libuuid-devel readline-devel cmake libogg-devel
BuildRequires:  mesa-libGLU-devel libffi-devel libdbi-devel loudmouth-devel
BuildRequires:  libmemcached-devel libgle-devel libtheora-devel
BuildRequires:  tokyocabinet-devel libvorbis-devel glibc-gconv-extra
BuildRequires:  yajl-devel >= 2
# Put back freetype-devel, clutter-devel, mysql-devel, qdbm-devel,
# openssl-devel when these extensions build

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
# not using smp_flags, parallel build is broken.

%install
rm -rf $RPM_BUILD_ROOT
# upstreams make install installs lots of unwanted parts of the addons, so DIY
#make install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons
install -m 755 _build/binaries/io $RPM_BUILD_ROOT%{_bindir}
install -m 755 _build/binaries/io_static $RPM_BUILD_ROOT%{_bindir}

#rm $RPM_BUILD_ROOT%{_libdir}/libiovmall.so
install -m 755 _build/dll/libiovmall.so \
  $RPM_BUILD_ROOT%{_libdir}/libiovmall.so.2
ln -s libiovmall.so.2 $RPM_BUILD_ROOT%{_libdir}/libiovmall.so

install -m 755 _build/dll/libbasekit.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libcoroutine.so $RPM_BUILD_ROOT%{_libdir}/
install -m 755 _build/dll/libgarbagecollector.so $RPM_BUILD_ROOT%{_libdir}/

mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a _build/headers $RPM_BUILD_ROOT%{_includedir}/io

# Clean out addons that don't build.
rm -rf addons/Clutter
rm -rf addons/Font
rm -rf addons/GLFW
rm -rf addons/MySQL
rm -rf addons/QDBM
rm -rf addons/SecureSocket
rm -rf addons/AppleSensors
rm -rf addons/Regex

# install the addons
for i in addons/*; do
  # skip unbuild addons
  if [ -d $i/_build ]; then
    ADDON=`basename $i`
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -m 755 $i/_build/dll/libIo$ADDON.so \
      $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -p -m 644 $i/depends $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON
    # Io doesn't find the addon if this file isn't present
    touch $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/build.io
  fi
done

%ldconfig_scriptlets

%files
%doc license.txt
%{_bindir}/io
%{_bindir}/io_static
%{_libdir}/libiovmall.so.2
%{_libdir}/libbasekit.so
%{_libdir}/libcoroutine.so
%{_libdir}/libgarbagecollector.so

%dir %{_libdir}/io
%dir %{_libdir}/io/addons
%{_libdir}/io/addons/AsyncRequest
%{_libdir}/io/addons/BigNum
%{_libdir}/io/addons/Bitly
%{_libdir}/io/addons/Blowfish
%{_libdir}/io/addons/Box
%{_libdir}/io/addons/Cairo
#%%{_libdir}/io/addons/CFFI
%{_libdir}/io/addons/CGI
%{_libdir}/io/addons/ContinuedFraction
%{_libdir}/io/addons/Curses
%{_libdir}/io/addons/DBI
%{_libdir}/io/addons/DistributedObjects
%{_libdir}/io/addons/EditLine
%{_libdir}/io/addons/Facebook
%{_libdir}/io/addons/Flux
%{_libdir}/io/addons/Fnmatch
%{_libdir}/io/addons/GoogleSearch
%{_libdir}/io/addons/HttpClient
%{_libdir}/io/addons/LZO
%{_libdir}/io/addons/Libxml2
%{_libdir}/io/addons/Loki
%{_libdir}/io/addons/Loudmouth
%{_libdir}/io/addons/MD5
#%%{_libdir}/io/addons/Memcached
#%%{_libdir}/io/addons/NetworkAdapter
%{_libdir}/io/addons/NotificationCenter
#%%{_libdir}/io/addons/NullAddon
%{_libdir}/io/addons/Obsidian
%{_libdir}/io/addons/Random
%{_libdir}/io/addons/Range
%{_libdir}/io/addons/Rational
%{_libdir}/io/addons/ReadLine
#%%{_libdir}/io/addons/Regex
%{_libdir}/io/addons/SGML
%{_libdir}/io/addons/SHA1
%{_libdir}/io/addons/SQLite3
%{_libdir}/io/addons/SqlDatabase
%{_libdir}/io/addons/Syslog
%{_libdir}/io/addons/SystemCall
%{_libdir}/io/addons/Thread
%{_libdir}/io/addons/TokyoCabinet
%{_libdir}/io/addons/Twitter
%{_libdir}/io/addons/UUID
%{_libdir}/io/addons/User
%{_libdir}/io/addons/VertexDB
%{_libdir}/io/addons/Volcano
%{_libdir}/io/addons/Yajl
%{_libdir}/io/addons/Zlib

%files devel
%doc docs/*
%{_libdir}/libiovmall.so
%{_includedir}/io

%files graphics-and-sound
#%%{_libdir}/io/addons/Font
%{_libdir}/io/addons/Image
%{_libdir}/io/addons/LibSndFile
%{_libdir}/io/addons/Ogg
%{_libdir}/io/addons/OpenGL
#%%{_libdir}/io/addons/PortAudio
#%%{_libdir}/io/addons/TagLib
%{_libdir}/io/addons/Theora
%{_libdir}/io/addons/Vorbis

%files extras
%{_libdir}/io/addons/Python
#%%{_libdir}/io/addons/SampleRateConverter
%{_libdir}/io/addons/Socket
#%%{_libdir}/io/addons/SoundTouch

%files postgresql
%{_libdir}/io/addons/Postgre*

%files mysql
#%%{_libdir}/io/addons/MySQL

%changelog
%autochangelog
