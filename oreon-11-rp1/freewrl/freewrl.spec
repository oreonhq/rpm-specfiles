%global source0_hash 0449622187d80442c012ed5d38b5c04439afc6399ee1a2b53ab33e315827d33c

%global majorrel 6.7
%global commit b3254b11e9e340b08eb5b38ccc1a34785693261e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240420

%ifarch %{java_arches}
%bcond_without java
%endif

# probably never coming back. sorry.
%bcond_with plugin

Name:		freewrl
Version:	%{majorrel}
Release:	3.%{commitdate}git%{shortcommit}%{?dist}
Summary:	X3D / VRML visualization program
License:	LGPL-3.0-or-later
URL:		http://freewrl.sourceforge.net
# Source0:	http://sourceforge.net/projects/freewrl/files/freewrl-linux/3.0/%%{name}-%%{version}.tar.bz2
# git clone https://git.code.sf.net/p/freewrl/git freewrl-git
# cd freewrl-git
# git checkout develop
# cp -a freex3d/ ../freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
# cd ..
# tar --exclude-vcs -cjf %%{name}-%%{version}-%%{commitdate}git%%{shortcommit}.tar.bz2 freewrl-%%{version}-%%{commitdate}git%%{shortcommit}
Source0:	%{name}-%{version}-%{commitdate}git%{shortcommit}.tar.bz2
Source1:	README.FreeWRL.java
# gcc says:
# main/ProdCon.c:427:19: error: too few arguments to function 'cParse'
Patch3:		freewrl-3.0.0-20170208git621ae4e-cparse-stl-fix.patch
# warning: '__builtin_strncpy' output truncated before terminating nul copying 54 bytes from a string of the same length [-Wstringop-truncation]
Patch4:		freewrl-4.3.0-use-memcpy-instead-of-strncpy.patch
# main/ProdCon.c:414:29: warning: implicit declaration of function 'convertAsciiSTL' [-Wimplicit-function-declaration]
# main/ProdCon.c:424:29: warning: implicit declaration of function 'convertBinarySTL' [-Wimplicit-function-declaration]
Patch5:		freewrl-4.3.0-missing-functions.patch
# lots of indent issues caught by -Wmisleading-indentation
Patch6:		freewrl-6.7-fix-indent-issues.patch
# lots of signedness fixes like
# io_files.c:627:17: warning: pointer targets in passing argument 1 of 'stlDTFT' differ in signedness [-Wpointer-sign]
Patch7:		freewrl-6.7-sign-fixes.patch
Patch8:		freewrl-6.7-c99.patch
# Fix issue with incompatible pointer type
Patch9:		freewrl-6.7-fix-cast.patch
# C requires the existence of functions before they are called.
Patch10:	freewrl-6.7-fix-function-references.patch
# Add missing includes for std headers
Patch11:	freewrl-6.7-fix-headers.patch
# Fix makefile
Patch12:	freewrl-6.7-fix-makefile.patch
# Fixes for C23
Patch13:	freewrl-6.7-c23.patch
# Do not use pointproperties_pointmethod (we don't actually use the enum, just the defines and it gets its symbol EVERYWHERE)
Patch14:	freewrl-6.7-no-pointproperties_pointmethod.patch
# Fix stubs to not duplicate function symbols
Patch15:	freewrl-6.7-fix-stubs.patch
# Gotta define before you use
Patch16:	freewrl-6.7-fix-peek_audio_context.patch
# Fix missing types
Patch17:	freewrl-6.7-fix-missing-types.patch
# Fix MIDI symbols
Patch18:	freewrl-6.7-fix-midi-symbols.patch
# Fix Sound stubs (symbols in lib)
Patch19:	freewrl-6.7-fix-sound-stubs.patch
# updateCursorStyle0 is win32 only
Patch20:	freewrl-6.7-fix-win32-only.patch
# move C function into C code, extern is causing naming mismatch
Patch21:	freewrl-6.7-fix-lookup_brotoDefname.patch

BuildRequires:	gcc-c++
BuildRequires:	zlib-devel, freetype-devel, fontconfig-devel
BuildRequires:	imlib2-devel, nspr-devel
BuildRequires:	expat-devel, libXxf86vm-devel, libX11-devel, libXext-devel
BuildRequires:	mesa-libGL-devel, mesa-libGLU-devel, glew-devel, libxml2-devel
BuildRequires:	libjpeg-devel, libpng-devel, unzip, wget
BuildRequires:	ImageMagick, desktop-file-utils, chrpath
BuildRequires:	libXaw-devel, libXmu-devel, freealut-devel
BuildRequires:	liblo-devel, libcurl-devel, openal-soft-devel
%if %{with java}
BuildRequires:	java-devel
%endif
%if %{with plugin}
%ifnarch armv7hl s390x i686
BuildRequires:	firefox
%endif
%endif
BuildRequires:	sox, doxygen
BuildRequires:	ode-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires:	make

Requires:	sox, unzip, wget, ImageMagick

%description
FreeWRL is an X3D / VRML visualization program. This package contains the
standalone commandline tool.

%package devel
Summary:	Development files for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development libraries and headers for FreeWRL.

%if %{with java}
%package java
Summary:	Java support for FreeWRL
Requires:	java-headless
Requires:	freewrl%{?_isa} = %{version}-%{release}

%description java
Java support for FreeWRL.
%endif

%package -n libEAI
Summary:	FreeWRL EAI C support library

%description -n libEAI
FreeWRL EAI C support library.

%package -n libEAI-devel
Summary:	Development files for libEAI
Requires:	libEAI%{?_isa} = %{version}-%{release}

%description -n libEAI-devel
Development libraries and headers for libEAI.

%if %{with plugin}
%ifnarch armv7hl s390x
%package plugin
Summary:	Browser plugin for FreeWRL
Requires:	freewrl%{?_isa} = %{version}-%{release}
Requires:	firefox

%description plugin
FreeWRL is an X3D / VRML visualization program. This package contains the
browser plugin for Firefox (and other xulrunner compatible browsers).
%endif
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{majorrel}-%{commitdate}git%{shortcommit}
%if %{with java}
cp %{SOURCE1} .
%endif
# Don't need it.
rm -rf appleOSX/
%patch -P3 -p1 -b .cparsestlfix
%patch -P4 -p1 -b .memcpy
%patch -P5 -p1 -b .missing-functions
%patch -P6 -p1 -b .fixindent
%patch -P7 -p1 -b .signfix
%patch -P8 -p1 -b .c99
%patch -P9 -p1 -b .fix-cast
%patch -P10 -p1 -b .fix-function-references
%patch -P11 -p1 -b .fix-headers
%patch -P12 -p1 -b .fix-makefile
%patch -P13 -p1 -b .c23
%patch -P14 -p1 -b .no-pointproperties_pointmethod
%patch -P15 -p1 -b .fix-stubs
%patch -P16 -p1 -b .fix-peek_audio_context
%patch -P17 -p1 -b .fix-missing-types
%patch -P18 -p1 -b .fix-midi
%patch -P19 -p1 -b .fix-sound-stubs
%patch -P20 -p1 -b .fix-win32-only
%patch -P21 -p1 -b .fix-lookup_brotoDefname

# no snapshot testing
sed -i 's|AC_DEFINE(USE_SNAPSHOT_TESTING|#AC_DEFINE(USE_SNAPSHOT_TESTING|g' configure.ac

autoreconf --force --install

# hardcoding /usr/local/lib is a no-no
sed -i 's|libpath = "/usr/local/lib"|libpath = "%{_libdir}"|g' src/bin/main.c

%build
%global optflags %{optflags} -Wno-comment -Wno-unused-variable -std=gnu17 -Wno-error=incompatible-pointer-types
export LDFLAGS="-Wl,--as-needed"
%configure --with-target=x11 \
	   --enable-fontconfig \
	   %{?with_java:--enable-java} \
	   --enable-libeai \
	   --disable-osc \
	   --enable-libcurl \
	   --enable-rbp \
	   --enable-twodee \
	   --enable-STL \
	   --disable-static \
	   --with-javadir=/usr/lib/jvm/java-openjdk/jre/lib/ext \
	   --with-javascript=duk \
	   --with-statusbar=hud
make %{?_smp_mflags} V=1
pushd doc
make html/index.html
popd

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}/
%if %{with java}
install -p src/java/java.policy %{buildroot}%{_datadir}/%{name}/
%endif

%if %{with plugin}
# no firefox on armv7hl | s390x | i686
%ifarch armv7hl s390x i686
rm -rf %{buildroot}%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif
%endif

rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/mozilla/plugins/*.la

desktop-file-validate %{buildroot}%{_datadir}/applications/freewrl.desktop
chmod -x %{buildroot}%{_datadir}/applications/freewrl.desktop
%if %{with java}
chmod -x %{buildroot}%{_datadir}/%{name}/java.policy
%endif

chrpath --delete %{buildroot}%{_bindir}/freewrl
# chrpath --delete %%{buildroot}%%{_bindir}/freewrl_snd
chrpath --delete %{buildroot}%{_libdir}/libFreeWRLEAI.so.*

%ldconfig_scriptlets

%ldconfig_scriptlets -n libEAI

%files
%doc AUTHORS README TODO
%license COPYING COPYING.LESSER
%{_bindir}/%{name}
%{_bindir}/%{name}_msg
# %%{_bindir}/%%{name}_snd
%{_libdir}/libFreeWRL.so.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}*

%files devel
%doc doc/html
%{_includedir}/libFreeWRL.h
%{_libdir}/libFreeWRL.so
%{_libdir}/pkgconfig/libFreeWRL.pc

%if %{with java}
%files java
%doc README.FreeWRL.java
%{_datadir}/%{name}/
/usr/lib/jvm/java-openjdk/jre/lib/ext/vrml.jar
%endif

%files -n libEAI
%license COPYING COPYING.LESSER
%{_libdir}/libFreeWRLEAI.so.*

%files -n libEAI-devel
%{_includedir}/FreeWRLEAI/
%{_libdir}/libFreeWRLEAI.so
%{_libdir}/pkgconfig/libFreeWRLEAI.pc

# Plugin is dead and gone, thanks to Mozilla.
%if %{with plugin}
%ifnarch armv7hl s390x i686
%files plugin
%{_libdir}/mozilla/plugins/libFreeWRLplugin.so
%endif
%endif

%changelog
%autochangelog
