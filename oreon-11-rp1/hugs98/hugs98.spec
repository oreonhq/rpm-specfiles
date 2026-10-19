%global source0_hash aafaca9ca544572ebef70bbe86b5eb0abaa5d7c11c0b766d7db72a46b022bed5
%define hugs_ver plus-Sep2006
Name:		hugs98
Version:	2006.09
Release:        1%{?dist}
Summary:        Haskell Interpreter
License:	LicenseRef-Callaway-BSD
URL:		http://www.haskell.org/hugs
Source0:        http://cvs.haskell.org/Hugs/downloads/2%{build_type_safety_c}%{build_type_safety_c}6-%{build_type_safety_c}9/%{name}-%{hugs_ver}.tar.gz
Patch0:         hugs98-gnu.patch
Patch1:		hugs98-config.patch
Patch2: hugs98-machdep-bufsize.patch
%ifnarch aarch64 ppc64le x86_64
%endif
# oreon:deps
BuildRequires:  /usr/bin/execstack
BuildRequires:  docbook-utils
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  openal-soft-devel
BuildRequires:  readline-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Hugs 98 is a functional programming system based on Haskell 98,
the de facto standard for non-strict functional programming languages.
Hugs 98 provides an almost complete implementation of Haskell 98.

%package openal
Summary:	OpenAL package for Hugs98
Requires:	%{name} = %{version}-%{release}
%description openal
OpenAL package for Hugs98.

%package alut
Summary:	ALUT package for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-openal = %{version}-%{release}
%description alut
ALUT package for Hugs98.

%package x11
Summary:	X11 package for Hugs98
Requires:	%{name} = %{version}-%{release}
%description x11
X11 package for Hugs98.

%package opengl
Summary:	OpenGL package for Hugs98
Requires:	%{name} = %{version}-%{release}
%description opengl
OpenGL package for Hugs98.

%package glut
Summary:	GLUT package for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-opengl = %{version}-%{release}
%description glut
GLUT package for Hugs98.

%package hgl
Summary:	Haskell Graphics Library for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}
%description hgl
Haskell Graphics Library for Hugs98.

%package demos
Summary:	Demo files for Hugs98
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-glut = %{version}-%{release}
Requires:	%{name}-hgl = %{version}-%{release}
%description demos
Demo files for Hugs98.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{hugs_ver}
# add undefined struct
%patch -P0 -p1 -b .gnu
%patch -P1 -p1 -b .config
%patch -P 2 -p1
# use inline keyword
sed -i 's|extern inline|inline|' packages/base/include/HsBase.h packages/network/include/HsNet.h packages/unix/include/HsUnix.h hsc2hs/Main.hs
# libalut needs libopenal
sed -i 's|ALUT_LIBS="$ac_cv_search_alutExit"|ALUT_LIBS="$ac_cv_search_alutExit -lopenal"|' packages/ALUT/configure
# this is to avoid network lookup of the DTD
sed -i 's|\"http://www.oasis-open.org.*\"||' docs/users_guide/users_guide.xml
# Update config.guess/sub to fix builds on new architectures (aarch64/ppc64le)
cp /usr/lib/rpm/redhat/config.* .

%build

%global build_type_safety_c 0
export CC="gcc -fpermissive"
%define __global_ldflags ""
%configure --with-pthreads --enable-char-encoding=locale
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install_all_but_docs
make -C docs DESTDIR=%{buildroot} install_man
%ifnarch aarch64 ppc64le x86_64
execstack -s %{buildroot}%{_bindir}/{hugs,runhugs,ffihugs}
%endif
find %{buildroot} -name '*.so' -exec chmod 0755 '{}' ';'
rm %{buildroot}%{_libdir}/hugs/demos/Makefile.in
mv %{buildroot}%{_datadir}/hsc2hs-*/* %{buildroot}%{_libdir}/hugs/programs/hsc2hs
sed -i "s|^bindir.*|bindir=\"%{_bindir}\"|
        s|^libdir.*|libdir=\"%{_libdir}/hugs/programs/hsc2hs|
        s|^datadir.*|datadir=\"%{_libdir}/hugs/programs/hsc2hs\"|" \
    %{buildroot}%{_libdir}/hugs/programs/hsc2hs/Paths_hsc2hs.hs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hugs98-openal -f %{oreon_filedir}/hugs98-openal.list
%files -n hugs98-alut -f %{oreon_filedir}/hugs98-alut.list
%files -n hugs98-x11 -f %{oreon_filedir}/hugs98-x11.list
%files -n hugs98-opengl -f %{oreon_filedir}/hugs98-opengl.list
%files -n hugs98-glut -f %{oreon_filedir}/hugs98-glut.list
%files -n hugs98-hgl -f %{oreon_filedir}/hugs98-hgl.list
%files -n hugs98-demos -f %{oreon_filedir}/hugs98-demos.list

%changelog

%autochangelog
