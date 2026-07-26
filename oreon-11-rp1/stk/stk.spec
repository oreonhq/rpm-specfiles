%global source0_hash d9817f9d6c709e3451fea9d0e80bee0c2334a68a5c609089185c6b57226e2066

Name:           stk
Version:        4.6.1
Release:        12%{?dist}
Summary:        Synthesis ToolKit in C++
License:        MIT
URL:            https://ccrma.stanford.edu/software/stk/
Source0:        %{name}-%{version}.stripped.tar.gz
# Original tarfile can be found at %%{url}/release/%%{name}-%%{version}.tar.gz
# We remove legeally questionable files as well as accidentally packed
# object files.
Source1:        README.fedora
Patch0:         stk-4.6.1-header.patch
Patch1:         stk-4.6.1-cflags-lib.patch
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  symlinks
BuildRequires:  autoconf

%description
The Synthesis ToolKit in C++ (STK) is a set of open source audio
signal processing and algorithmic synthesis classes written in the C++
programming language. STK was designed to facilitate rapid development
of music synthesis and audio processing software, with an emphasis on
cross-platform functionality, realtime control, ease of use, and
educational example code. The Synthesis ToolKit is extremely portable
(it's mostly platform-independent C and C++ code), and it's completely
user-extensible (all source included, no unusual libraries, and no
hidden drivers). We like to think that this increases the chances that
our programs will still work in another 5-10 years. In fact, the
ToolKit has been working continuously for about 10 years now. STK
currently runs with realtime support (audio and MIDI) on Linux,
Macintosh OS X, and Windows computer platforms. Generic, non-realtime
support has been tested under NeXTStep, Sun, and other platforms and
should work with any standard C++ compiler.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package demo
Summary:        Demo applications for %{name}
Requires:       tk
Requires:       %{name} = %{version}-%{release}

%description demo
The %{name}-demo package contains the demo applications for the
C++ Sound Synthesis ToolKit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# we patched configure.ac
autoconf

cp -a %{SOURCE1} README.fedora

# remove backup and other extra files
find . -name '*~' -exec rm {} \;
find . -name '._*' -exec rm {} \;

%build
%configure --with-jack --with-alsa \
  --disable-static --enable-shared \
  RAWWAVE_PATH=%{_datadir}/stk/rawwaves/
%make_build
%make_build -C projects/demo libMd2Skini

%install
mkdir -p \
  %{buildroot}%{_includedir}/stk \
  %{buildroot}%{_libdir} \
  %{buildroot}%{_bindir} \
  %{buildroot}%{_datadir}/stk/rawwaves \
  %{buildroot}%{_datadir}/stk/demo \
  %{buildroot}%{_datadir}/stk/examples \
  %{buildroot}%{_datadir}/stk/effects \
  %{buildroot}%{_datadir}/stk/ragamatic \
  %{buildroot}%{_datadir}/stk/eguitar

cp -p include/* %{buildroot}%{_includedir}/stk
cp -pd src/libstk*.so %{buildroot}%{_libdir}
cp -p rawwaves/*.raw %{buildroot}%{_datadir}/stk/rawwaves

cp -pr projects/demo/tcl %{buildroot}%{_datadir}/stk/demo
cp -pr projects/demo/scores %{buildroot}%{_datadir}/stk/demo
cp -p projects/demo/stk-demo %{buildroot}%{_bindir}/stk-demo
cp -p projects/demo/Md2Skini %{buildroot}%{_bindir}/Md2Skini
for f in Banded Drums Modal Physical Shakers StkDemo Voice ; do
  chmod +x projects/demo/$f
  sed -e '1i#! /bin/sh' -i projects/demo/$f
  cp -p projects/demo/$f %{buildroot}%{_datadir}/stk/demo
done

cp -pr projects/examples/midifiles %{buildroot}%{_datadir}/stk/examples
cp -pr projects/examples/rawwaves %{buildroot}%{_datadir}/stk/examples
cp -pr projects/examples/scores %{buildroot}%{_datadir}/stk/examples
for f in sine sineosc foursine audioprobe midiprobe duplex play \
    record inetIn inetOut rtsine crtsine bethree controlbee \
    threebees playsmf grains ; do
  cp -p projects/examples/$f %{buildroot}%{_bindir}/stk-$f
  # absolute links, will be shortened later
  ln -s %{buildroot}%{_bindir}/stk-$f %{buildroot}%{_datadir}/stk/examples/$f
done

cp -pr projects/effects/tcl %{buildroot}%{_datadir}/stk/effects
cp -p projects/effects/effects %{buildroot}%{_bindir}/stk-effects
sed -e 's,\./effects,%{_bindir}/stk-effects,' -e '1i#! /bin/sh' \
  -i projects/effects/StkEffects
cp -p projects/effects/StkEffects %{buildroot}%{_datadir}/stk/effects

cp -pr projects/ragamatic/tcl %{buildroot}%{_datadir}/stk/ragamatic
cp -pr projects/ragamatic/rawwaves %{buildroot}%{_datadir}/stk/ragamatic
cp -p projects/ragamatic/ragamat %{buildroot}%{_bindir}/stk-ragamat
sed -e 's,\./ragamat,%{_bindir}/stk-ragamat,' -e '1i#! /bin/sh' \
  -i projects/ragamatic/Raga
cp -p projects/ragamatic/Raga %{buildroot}%{_datadir}/stk/ragamatic

cp -pr projects/eguitar/tcl %{buildroot}%{_datadir}/stk/eguitar
cp -pr projects/eguitar/scores %{buildroot}%{_datadir}/stk/eguitar
cp -p projects/eguitar/eguitar %{buildroot}%{_bindir}/stk-eguitar
sed -e 's,\./eguitar,%{_bindir}/stk-eguitar,' -e '1i#! /bin/sh' \
  -i projects/eguitar/ElectricGuitar
cp -p projects/eguitar/ElectricGuitar %{buildroot}%{_datadir}/stk/eguitar

# fix encoding
iconv -f iso-8859-1 -t utf-8 doc/doxygen/index.txt \
  -o doc/doxygen/index.txt.tmp
mv doc/doxygen/index.txt.tmp doc/doxygen/index.txt

# fix symlinks
symlinks -crv %{buildroot}

# fix permissions
find %{buildroot} \( -name '*.h' -o -name '*.raw' -o -name '*.tcl' \
     -o -name '*.xbm' -o -name '*.bmp' -o -name 'README' \) -a -exec chmod -x {} \;
find doc README.md README.fedora -type f -exec chmod -x {} \;
chmod -R u=rwX,go=rX %{buildroot}

%ldconfig_scriptlets

%files
%doc README.md
%{_libdir}/libstk-*.so
%dir %{_datadir}/stk
%{_datadir}/stk/rawwaves

%files devel
%doc README.md doc/* README.fedora
%{_libdir}/libstk.so
%{_includedir}/*

%files demo
%doc README.md README.fedora
%{_bindir}/stk-*
%{_bindir}/Md2Skini
%{_datadir}/stk/demo
%{_datadir}/stk/examples
%{_datadir}/stk/effects
%{_datadir}/stk/ragamatic
%{_datadir}/stk/eguitar

%changelog
%autochangelog
