%global source0_hash 0449622187d80442c012ed5d38b5c04439afc6399ee1a2b53ab33e315827d33c
%global majorrel 6.7
%global commit b3254b11e9e340b08eb5b38ccc1a34785693261e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20240420
%ifarch %{java_arches}
%bcond_without java
%endif
%bcond_with plugin
Name:		freewrl
Version:	%{majorrel}
Release:        1%{?dist}
Summary:        X3D / VRML visualization program
License:	LGPL-3.0-or-later
URL:		http://freewrl.sourceforge.net
Source0:        %{name}-%{version}-%{commitdate}git%{shortcommit}.tar.bz2
Source1:	README.FreeWRL.java
Patch3:		freewrl-3.0.0-20170208git621ae4e-cparse-stl-fix.patch
Patch4:		freewrl-4.3.0-use-memcpy-instead-of-strncpy.patch
Patch5:		freewrl-4.3.0-missing-functions.patch
Patch6:		freewrl-6.7-fix-indent-issues.patch
Patch7:		freewrl-6.7-sign-fixes.patch
Patch8:		freewrl-6.7-c99.patch
Patch9:		freewrl-6.7-fix-cast.patch
Patch10:	freewrl-6.7-fix-function-references.patch
Patch11:	freewrl-6.7-fix-headers.patch
Patch12:	freewrl-6.7-fix-makefile.patch
Patch13:	freewrl-6.7-c23.patch
Patch14:	freewrl-6.7-no-pointproperties_pointmethod.patch
Patch15:	freewrl-6.7-fix-stubs.patch
Patch16:	freewrl-6.7-fix-peek_audio_context.patch
Patch17:	freewrl-6.7-fix-missing-types.patch
Patch18:	freewrl-6.7-fix-midi-symbols.patch
Patch19:	freewrl-6.7-fix-sound-stubs.patch
Patch20:	freewrl-6.7-fix-win32-only.patch
Patch21:	freewrl-6.7-fix-lookup_brotoDefname.patch
%if %{with java}
%endif
%if %{with plugin}
%ifnarch armv7hl s390x i686
%endif
%endif
Requires:	sox, unzip, wget, ImageMagick
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freealut-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  imlib2-devel
BuildRequires:  java-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  nspr-devel
BuildRequires:  ode-devel
BuildRequires:  openal-soft-devel
BuildRequires:  sox
BuildRequires:  unzip
BuildRequires:  wget
BuildRequires:  zlib-devel
# /oreon:deps
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
chrpath --delete %{buildroot}%{_libdir}/libFreeWRLEAI.so.*
%ldconfig_scriptlets
%ldconfig_scriptlets -n libEAI
%oreon_autofiles libEAI usr/*/lib*.so.*
%oreon_autofiles libEAI-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n freewrl-devel -f %{oreon_filedir}/freewrl-devel.list
%files -n freewrl-java -f %{oreon_filedir}/freewrl-java.list
%files -n libEAI -f %{oreon_filedir}/libEAI.list
%files -n libEAI-devel -f %{oreon_filedir}/libEAI-devel.list

%changelog

%autochangelog
